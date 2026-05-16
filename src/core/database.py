"""
core/database.py
----------------
OpenSpartan の SQLite DB からの読み取り専用アクセス。

設計方針:
- DB への書き込みは一切行わない（読み取り専用）
- URI モード ?mode=ro で書き込みを防止する
- 全フィールドを展開して DataFrame に持つ（理念: データは捨てない）
- st.cache_data のデコレータは呼び出し側（Streamlit ページ）で付与する
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

import pandas as pd

from src.core.config import AppConfig
from src.utils.helpers import safe_get, parse_seconds, utc_to_jst, parse_dt_jst
from src.utils.display import OUTCOME_MAP, PLAYLIST_EXPERIENCE_MAP


# ==================================================
# DB 接続
# ==================================================

def open_db_readonly(db_path: str | Path) -> sqlite3.Connection:
    """OpenSpartan の SQLite DB を読み取り専用モードで開く。"""
    uri = f"file:{Path(db_path).resolve()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


# ==================================================
# マスタテーブルの読み込み
# ==================================================

def _load_dict(cur: sqlite3.Cursor, table: str) -> dict[str, Any]:
    """
    指定テーブルの全レコードを読み込み、AssetId をキーにした辞書を返す。
    対象: Maps / Playlists / PlaylistMapModePairs / GameVariants
    """
    d: dict[str, Any] = {}
    try:
        rows = cur.execute(f"SELECT ResponseBody FROM {table}").fetchall()
    except sqlite3.Error:
        return d
    for (rb,) in rows:
        try:
            obj = json.loads(rb)
            d[obj["AssetId"]] = obj
        except (json.JSONDecodeError, KeyError):
            continue
    return d


# ==================================================
# PlayerMatchStats の読み込み
# ==================================================

def _load_player_match_stats(
    cur: sqlite3.Cursor,
    my_xuid: str,
    ms_rows: list[tuple[int, str]],
) -> dict[str, Any]:
    """
    PlayerMatchStats を MatchId → プレイヤーエントリ の辞書で返す。
    新スキーマ（MatchId カラムあり）と旧スキーマ（rowid ベース）の両方に対応。
    """

    def get_my_entry(obj: dict[str, Any]) -> dict[str, Any] | None:
        for v in obj.get("Value") or []:
            if v.get("Id") == my_xuid:
                return v
        return None

    d: dict[str, Any] = {}

    # 新スキーマ
    try:
        rows = cur.execute("SELECT MatchId, ResponseBody FROM PlayerMatchStats").fetchall()
    except sqlite3.Error:
        rows = []

    if rows:
        for match_id, rb in rows:
            try:
                if not match_id:
                    continue
                obj = json.loads(rb)
                entry = get_my_entry(obj)
                if entry:
                    d[match_id] = entry
            except (json.JSONDecodeError, KeyError):
                continue
        if d:
            return d

    # 旧スキーマ（rowid ベース）
    rowid_to_mid: dict[int, str] = {}
    for rowid, rb in ms_rows:
        try:
            obj = json.loads(rb)
            rowid_to_mid[rowid] = obj["MatchId"]
        except (json.JSONDecodeError, KeyError):
            continue

    try:
        rows_by_rowid = cur.execute(
            "SELECT rowid, ResponseBody FROM PlayerMatchStats ORDER BY rowid"
        ).fetchall()
    except sqlite3.Error:
        return d

    for rowid, rb in rows_by_rowid:
        try:
            obj = json.loads(rb)
            entry = get_my_entry(obj)
            if entry:
                mid = rowid_to_mid.get(rowid)
                if mid:
                    d[mid] = entry
        except (json.JSONDecodeError, KeyError):
            continue

    return d


# ==================================================
# プレイリスト分類
# ==================================================

def _classify_playlist(match_info: dict[str, Any], playlists: dict[str, Any]) -> str:
    """
    MatchInfo から playlist 内部値を返す。

    LifecycleMode=1          → "custom"
    LifecycleMode=3          → PlaylistExperience で細分化
    Playlist が playlists にない → "custom"
    """
    lifecycle = match_info.get("LifecycleMode")
    if lifecycle == 1:
        return "custom"

    playlist_asset = safe_get(match_info, "Playlist", "AssetId")
    if not playlist_asset or playlist_asset not in playlists:
        return "custom"

    exp = match_info.get("PlaylistExperience")
    return PLAYLIST_EXPERIENCE_MAP.get(exp, "other")


# ==================================================
# マップ名・ルール名の解決
# ==================================================

def _parse_pair_name(name: str | None) -> tuple[str, str]:
    """
    PlaylistMapModePair の PublicName から (rule_name, map_name) を返す。
    例: "Ranked:Slayer on Lattice - Ranked" → ("Slayer", "Lattice")
    """
    if not name or " on " not in name:
        return "Other", _clean_map(name)

    left, right = name.split(" on ", 1)
    if "undefined" in left.lower() or "undefined" in right.lower():
        return "Other", "Other"
    if left.startswith(("Arena:", "BTB:")):
        return "Other", "Other"

    rule = left.replace("Ranked:", "").strip()
    for k, v in {
        "slayer":     "Slayer",
        "ctf":        "CTF",
        "oddball":    "Oddball",
        "king":       "KOTH",
        "stronghold": "Strongholds",
    }.items():
        if k in rule.lower():
            rule = v
            break

    return rule, _clean_map(right)


def _clean_map(name: str | None) -> str:
    return (name or "Other").replace(" - Ranked", "").strip() or "Other"


def _parse_custom_rule(gv_name: str | None) -> str:
    n = (gv_name or "").lower()
    for k, v in {
        "ffa slayer":  "FFA Slayer",
        "slayer":      "Slayer",
        "ctf":         "CTF",
        "oddball":     "Oddball",
        "stronghold":  "Strongholds",
        "king":        "KOTH",
    }.items():
        if k in n:
            return v
    return "Other"


# ==================================================
# 除外フラグの判定
# ==================================================

def _get_exclude_flag(
    match: dict[str, Any],
    me: dict[str, Any],
    duration_sec: int | None,
) -> str:
    """
    除外フラグを返す。
    除外しない場合は空文字列を返す。
    データは捨てない（除外フラグを立てるだけ）。
    """
    # 試合時間 1 分未満
    if duration_sec is not None and duration_sec < 60:
        return "short_match"

    # 途中参加
    if safe_get(me, "ParticipationInfo", "JoinedInProgress"):
        return "incomplete"

    # 本人が途中抜け（Outcome=4 または PresentAtEndOfMatch=False）
    if me.get("Outcome") == 4:
        return "incomplete"
    if not safe_get(me, "ParticipationInfo", "PresentAtCompletion", default=True):
        return "incomplete"

    return ""


# ==================================================
# メインのデータ読み込み
# ==================================================

def load_matches(config: AppConfig) -> pd.DataFrame:
    """
    OpenSpartan DB から全試合データを読み込み、DataFrame で返す。

    理念: 全フィールドを展開する。取捨選択はビューで行う。
    除外フラグを立てるが、データは捨てない。

    Returns:
        pd.DataFrame: 1行1試合。カラムは COLUMN_NAMES.md の内部カラム名に準拠。
    """
    conn = open_db_readonly(config.db_path)
    try:
        cur = conn.cursor()

        # マスタテーブルの読み込み
        maps          = _load_dict(cur, "Maps")
        playlists     = _load_dict(cur, "Playlists")
        pairs         = _load_dict(cur, "PlaylistMapModePairs")
        game_variants = _load_dict(cur, "GameVariants")

        # MatchStats の読み込み
        try:
            ms_rows: list[tuple[int, str]] = cur.execute(
                "SELECT rowid, ResponseBody FROM MatchStats"
            ).fetchall()
        except sqlite3.Error:
            ms_rows = []

        # PlayerMatchStats の読み込み
        pms_map = _load_player_match_stats(cur, config.my_xuid, ms_rows)

    finally:
        conn.close()

    if not ms_rows:
        return pd.DataFrame()

    records: list[dict[str, Any]] = []

    for _rowid, rb in ms_rows:
        try:
            match = json.loads(rb)
        except json.JSONDecodeError:
            continue

        match_id = match.get("MatchId")
        if not match_id:
            continue

        match_info = match.get("MatchInfo", {})

        # 自分のプレイヤーエントリを特定
        me = next(
            (p for p in match.get("Players", [])
             if p.get("PlayerId") == config.my_xuid
             and p.get("PlayerType") != 2),
            None,
        )
        if not me:
            continue

        # 試合時間
        duration_sec = parse_seconds(match_info.get("Duration"))

        # 除外フラグ
        exclude_flag = _get_exclude_flag(match, me, duration_sec)

        # 日時
        played_at = parse_dt_jst(match_info.get("StartTime"))

        # プレイリスト分類
        playlist = _classify_playlist(match_info, playlists)

        # マップ・ルール名の解決
        if playlist == "custom":
            map_asset = safe_get(match_info, "MapVariant", "AssetId")
            gv_asset  = safe_get(match_info, "UgcGameVariant", "AssetId")
            map_name  = _clean_map(
                maps.get(map_asset, {}).get("PublicName", "") if map_asset else ""
            )
            rule_name = _parse_custom_rule(
                game_variants.get(gv_asset, {}).get("PublicName", "") if gv_asset else ""
            )
        else:
            pair_asset = safe_get(match_info, "PlaylistMapModePair", "AssetId")
            pair_name  = pairs.get(pair_asset, {}).get("PublicName", "") if pair_asset else ""
            rule_name, map_name = _parse_pair_name(pair_name)

        # 勝敗
        outcome_raw = me.get("Outcome")
        result = OUTCOME_MAP.get(outcome_raw, "unknown")

        # 個人スタッツ
        my_team_id = me.get("LastTeamId", 0)
        stats = safe_get(me, "PlayerTeamStats", 0, "Stats", "CoreStats") or {}

        kills   = stats.get("Kills",   0)
        deaths  = stats.get("Deaths",  0)
        assists = stats.get("Assists", 0)

        # チームスコア
        team_score = enemy_score = None
        for t in match.get("Teams", []):
            sc = safe_get(t, "Stats", "CoreStats", "Score")
            if t.get("TeamId") == my_team_id:
                team_score = sc
            else:
                enemy_score = sc

        # PlayerMatchStats から取得
        expected_kills = expected_deaths = None
        csr_pre = csr_post = None
        team_mmr = enemy_mmr = None

        if pms := pms_map.get(match_id):
            result_block = pms.get("Result", {})

            # StatPerformances
            sp = result_block.get("StatPerformances", {})
            ek = safe_get(sp, "Kills",  "Expected")
            ed = safe_get(sp, "Deaths", "Expected")
            try:
                expected_kills  = float(ek) if ek is not None else None
            except (TypeError, ValueError):
                expected_kills  = None
            try:
                expected_deaths = float(ed) if ed is not None else None
            except (TypeError, ValueError):
                expected_deaths = None

            # CSR
            recap   = result_block.get("RankRecap", {})
            pre_val = safe_get(recap, "PreMatchCsr",  "Value")
            post_val= safe_get(recap, "PostMatchCsr", "Value")
            csr_pre  = pre_val  if pre_val  and pre_val  > 0 else None
            csr_post = post_val if post_val and post_val > 0 else None

            # MMR
            team_mmrs: dict = result_block.get("TeamMmrs", {}) or {}
            my_key    = str(my_team_id)
            enemy_key = "1" if my_team_id == 0 else "0"
            team_mmr  = team_mmrs.get(my_key)
            enemy_mmr = team_mmrs.get(enemy_key)

        # パーフェクトキル（メダル走査）
        perfect_kills = _count_perfect_kills(me)

        rec: dict[str, Any] = {
            # 識別・メタ
            "match_id":      match_id,
            "played_at":     played_at,
            "playlist":      playlist,
            "map_name":      map_name,
            "rule_name":     rule_name,
            "result":        result,
            "result_flag":   1 if result == "win" else 0,
            "exclude_flag":  exclude_flag,
            # 基礎スタッツ
            "kills":         kills,
            "deaths":        deaths,
            "assists":       assists,
            "shots_hit":     stats.get("ShotsHit",        0),
            "shots_fired":   stats.get("ShotsFired",       0),
            "damage_dealt":  stats.get("DamageDealt",      0),
            "damage_taken":  stats.get("DamageTaken",      0),
            "score":         stats.get("Score",            0),
            "power_kills":   stats.get("PowerWeaponKills", 0),
            "perfect_kills": perfect_kills,
            "team_rank":     me.get("Rank"),
            "team_score":    team_score,
            "enemy_score":   enemy_score,
            "team_mmr":      round(team_mmr)  if team_mmr  is not None else None,
            "enemy_mmr":     round(enemy_mmr) if enemy_mmr is not None else None,
            "duration_sec":  duration_sec,
            # CSR
            "csr_pre":       csr_pre,
            "csr_post":      csr_post,
            # TrueSkill2
            "expected_kills":  expected_kills,
            "expected_deaths": expected_deaths,
            # パーティ（processor.py で後から追記）
            "party_size":    None,
        }
        records.append(rec)

    if not records:
        return pd.DataFrame()

    df = pd.DataFrame(records)

    # played_at を datetime 型に
    df["played_at"] = pd.to_datetime(df["played_at"], utc=True, errors="coerce")

    # 時系列昇順でソート
    df = df.sort_values("played_at").reset_index(drop=True)

    return df


# ==================================================
# パーフェクトキル集計ヘルパー
# ==================================================

PERFECT_KILL_STACK_NAME_ID = 1512363953


def _count_perfect_kills(player: dict[str, Any]) -> int:
    """メダル配列を再帰走査してパーフェクトキル数を集計する。"""
    pts_list = player.get("PlayerTeamStats") or []
    want = player.get("LastTeamId")
    if want is not None:
        matched = [p for p in pts_list if p.get("TeamId") == want]
        if matched:
            pts_list = matched

    total = 0
    for pts in pts_list:
        total += _walk_medals(pts.get("Stats", {}))
    return total


def _walk_medals(obj: Any) -> int:
    total = 0
    if isinstance(obj, dict):
        medals = obj.get("Medals")
        if isinstance(medals, list):
            for medal in medals:
                if isinstance(medal, dict):
                    try:
                        if int(medal.get("NameId", 0)) == PERFECT_KILL_STACK_NAME_ID:
                            total += int(medal.get("Count", 0) or 0)
                    except (TypeError, ValueError):
                        pass
        for v in obj.values():
            total += _walk_medals(v)
    elif isinstance(obj, list):
        for item in obj:
            total += _walk_medals(item)
    return total