"""
core/database.py
----------------
OpenSpartan の SQLite DB からの読み取り専用アクセス。

設計方針:
- DB への書き込みは一切行わない（読み取り専用）
- URI モード ?mode=ro で書き込みを防止する
- 全フィールドを展開して DataFrame に持つ（理念: データは捨てない）
- 除外フラグを立てるだけで行は削除しない
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

import pandas as pd

from src.core.config import AppConfig
from src.utils.helpers import safe_get, parse_seconds, parse_dt_jst
from src.utils.display import OUTCOME_MAP, PLAYLIST_NAME_MAP, PLAYLIST_EXPERIENCE_MAP


# ==================================================
# 除外フラグ判定定数
# ==================================================

SHOTS_FIRED_MIN = 30   # 発射数がこれ以下は無効試合（AFK・マップラン等）


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
    """AssetId をキーにした辞書を返す。"""
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
# ランクマップマスタの構築
# ==================================================

def _build_ranked_map_master(
    cur: sqlite3.Cursor,
    pairs: dict[str, Any],
) -> set[str]:
    """
    PlaylistMapModePairs から実際にランクマッチで使われたマップ名（小文字）を収集する。
    3年のブランクで追加されたマップも自動的に拾える。
    """
    ranked_maps: set[str] = set()
    try:
        rows = cur.execute(
            "SELECT json_extract(ResponseBody,'$.MatchInfo.PlaylistMapModePair') "
            "FROM MatchStats "
            "WHERE json_extract(ResponseBody,'$.MatchInfo.LifecycleMode')=3"
        ).fetchall()
    except sqlite3.Error:
        return ranked_maps

    for (pair_json,) in rows:
        if not pair_json:
            continue
        try:
            pair_obj = json.loads(pair_json) if isinstance(pair_json, str) else pair_json
            pair_id  = pair_obj.get("AssetId","") if isinstance(pair_obj, dict) else ""
        except (json.JSONDecodeError, TypeError):
            continue
        if not pair_id or pair_id not in pairs:
            continue
        pub_name = pairs[pair_id].get("PublicName","")
        if " on " not in pub_name:
            continue
        _, map_part = pub_name.split(" on ", 1)
        map_name = map_part.replace(" - Ranked","").strip()
        if map_name and map_name.lower() != "other":
            ranked_maps.add(map_name.lower())

    return ranked_maps


# ==================================================
# PlayerMatchStats の読み込み
# ==================================================

def _load_player_match_stats(
    cur: sqlite3.Cursor,
    my_xuid: str,
    ms_rows: list[tuple[str]],
) -> dict[str, Any]:
    """MatchId → 自分のプレイヤーエントリ の辞書を返す。"""

    def get_my_entry(obj: dict[str, Any]) -> dict[str, Any] | None:
        for v in obj.get("Value") or []:
            if v.get("Id") == my_xuid:
                return v
        return None

    d: dict[str, Any] = {}
    try:
        rows = cur.execute("SELECT MatchId, ResponseBody FROM PlayerMatchStats").fetchall()
    except sqlite3.Error:
        rows = []

    for match_id, rb in rows:
        try:
            if not match_id:
                continue
            obj   = json.loads(rb)
            entry = get_my_entry(obj)
            if entry:
                d[match_id] = entry
        except (json.JSONDecodeError, KeyError):
            continue

    return d


# ==================================================
# プレイリスト分類
# ==================================================

def _classify_playlist(
    match_info: dict[str, Any],
    playlists: dict[str, Any],
) -> str:
    """
    LifecycleMode=1          → "custom"
    LifecycleMode=3          → プレイリスト PublicName で分類
    Playlist が DB にない    → "custom"
    """
    lifecycle = match_info.get("LifecycleMode")
    if lifecycle == 1:
        return "custom"

    playlist_obj = match_info.get("Playlist")
    if not playlist_obj:
        return "custom"
    playlist_asset = playlist_obj.get("AssetId","")
    if not playlist_asset or playlist_asset not in playlists:
        return "custom"

    pub_name = (playlists[playlist_asset].get("PublicName") or "").lower()

    for keyword, playlist_val in PLAYLIST_NAME_MAP:
        if keyword in pub_name:
            return playlist_val

    # フォールバック: PlaylistExperience
    exp = match_info.get("PlaylistExperience")
    return PLAYLIST_EXPERIENCE_MAP.get(exp, "casual")


# ==================================================
# マップ名・ルール名の解決
# ==================================================

def _normalize_rule(rule: str) -> str:
    """ルール名を正規化する。CTF 3 Captures / CTF 5 Captures → CTF にまとめる等。"""
    if rule.upper().startswith("CTF"):
        return "CTF"
    return rule


def _parse_pair_name(name: str | None) -> tuple[str, str]:
    """
    PlaylistMapModePair の PublicName から (rule_name, map_name) を返す。
    例: "Ranked:Slayer on Lattice - Ranked" → ("Slayer", "Lattice")
    """
    if not name or " on " not in name:
        return "Other", _clean_map(name)
    left, right = name.split(" on ", 1)
    rule = (
        left
        .replace("Ranked:","")
        .replace("Arena:","")
        .replace("BTB:","")
        .strip()
    )
    return _normalize_rule(rule or "Other"), _clean_map(right)


def _clean_map(name: str | None) -> str:
    return (name or "Other").replace(" - Ranked","").strip() or "Other"


def _parse_custom_rule(gv_name: str | None) -> str:
    """GameVariant.PublicName からルール名を返す。"""
    n = (gv_name or "").strip()
    if n.lower().startswith("ranked:"):
        n = n[7:].strip()
    return _normalize_rule(n) if n else "Other"


# ==================================================
# 除外フラグの判定
# ==================================================

def _get_exclude_flag(
    me: dict[str, Any],
    duration_sec: int | None,
    shots_fired: int,
    playlist: str,
    rule_name: str,
    map_name: str,
    ranked_map_master: set[str],
    has_bot: bool,
) -> str:
    """
    優先順位順に除外フラグを返す。空文字 = 除外しない。

    1. short_match    : 試合時間1分未満
    2. incomplete     : 途中参加・途中抜け
    3. bot_match      : BOT参加試合
    4. low_shots      : 発射数30以下（AFK・マップラン等）
    5. custom_non_ranked: カスタムゲームで非ランクルール or 非ランクマップ
    """
    # 1. 試合時間1分未満
    if duration_sec is not None and duration_sec < 60:
        return "short_match"

    # 2. 途中参加・途中抜け
    if safe_get(me, "ParticipationInfo", "JoinedInProgress"):
        return "incomplete"
    if me.get("Outcome") == 4:
        return "incomplete"
    if not safe_get(me, "ParticipationInfo", "PresentAtCompletion", default=True):
        return "incomplete"

    # 3. BOT参加試合
    if has_bot:
        return "bot_match"

    # 4. 発射数30以下
    if shots_fired <= SHOTS_FIRED_MIN:
        return "low_shots"

    # 5. カスタムゲームで非ランクルール or 非ランクマップ
    if playlist == "custom":
        rule_lower = rule_name.lower()
        map_lower  = map_name.lower()
        # ルールが Ranked: 系でない
        is_ranked_rule = (
            rule_lower.startswith("ranked:") or
            # _parse_custom_rule で "Ranked:" を除去した後の状態も考慮
            any(r in rule_lower for r in ["slayer","ctf","oddball","strongholds","king of the hill","koth","doubles slayer","ffa slayer"])
            and not any(x in rule_lower for x in ["octagon","brt","aimbot","bot","warmup","recover","回復","ふんわり","hcs:","arena:slayer"])
        )
        is_ranked_map = map_lower in ranked_map_master

        if not (is_ranked_rule and is_ranked_map):
            return "custom_non_ranked"

    return ""


# ==================================================
# パーフェクトキル集計
# ==================================================

PERFECT_KILL_NAME_ID = 1512363953


def _parse_obj_stats(me: dict[str, Any]) -> dict[str, Any]:
    """
    PlayerTeamStats から オブジェクトルール専用スタッツを取得して返す。
    存在しないフィールドはNone。
    """
    stats = safe_get(me, "PlayerTeamStats", 0, "Stats") or {}

    result: dict[str, Any] = {
        # Oddball
        "oddball_skull_time_sec":  None,
        "oddball_scoring_ticks":   None,
        "oddball_skull_grabs":     None,
        "oddball_carrier_kills":   None,
        "oddball_skulls_denied":   None,
        # Strongholds / KOTH（ZonesStatsを共有）
        "zone_occupation_sec":     None,
        "zone_scoring_ticks":      None,
        "zone_captures":           None,
        "zone_def_kills":          None,
        "zone_off_kills":          None,
        "zone_secures":            None,
        # CTF
        "flag_captures":           None,
        "flag_grabs":              None,
        "flag_returns":            None,
        "flag_secures":            None,
        "flag_steals":             None,
        "flag_carrier_time_sec":   None,
        "flag_carriers_killed":    None,
    }

    if ob := stats.get("OddballStats"):
        result["oddball_skull_time_sec"] = parse_seconds(ob.get("TimeAsSkullCarrier"))
        result["oddball_scoring_ticks"]  = ob.get("SkullScoringTicks")
        result["oddball_skull_grabs"]    = ob.get("SkullGrabs")
        result["oddball_carrier_kills"]  = ob.get("KillsAsSkullCarrier")
        result["oddball_skulls_denied"]  = ob.get("SkullCarriersKilled")

    if zs := stats.get("ZonesStats"):
        result["zone_occupation_sec"] = parse_seconds(zs.get("StrongholdOccupationTime"))
        result["zone_scoring_ticks"]  = zs.get("StrongholdScoringTicks")
        result["zone_captures"]       = zs.get("StrongholdCaptures")
        result["zone_def_kills"]      = zs.get("StrongholdDefensiveKills")
        result["zone_off_kills"]      = zs.get("StrongholdOffensiveKills")
        result["zone_secures"]        = zs.get("StrongholdSecures")

    if cf := stats.get("CaptureTheFlagStats"):
        result["flag_captures"]          = cf.get("FlagCaptures")
        result["flag_grabs"]             = cf.get("FlagGrabs")
        result["flag_returns"]           = cf.get("FlagReturns")
        result["flag_secures"]           = cf.get("FlagSecures")
        result["flag_steals"]            = cf.get("FlagSteals")
        result["flag_carrier_time_sec"]  = parse_seconds(cf.get("TimeAsFlagCarrier"))
        result["flag_carriers_killed"]   = cf.get("FlagCarriersKilled")

    return result



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


def _count_perfect_kills(player: dict[str, Any]) -> int:
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
                        if int(medal.get("NameId", 0)) == PERFECT_KILL_NAME_ID:
                            total += int(medal.get("Count", 0) or 0)
                    except (TypeError, ValueError):
                        pass
        for v in obj.values():
            total += _walk_medals(v)
    elif isinstance(obj, list):
        for item in obj:
            total += _walk_medals(item)
    return total


# ==================================================
# メインのデータ読み込み
# ==================================================

def load_matches(config: AppConfig) -> pd.DataFrame:
    """
    OpenSpartan DB から全試合データを読み込み DataFrame で返す。
    カラム名は COLUMN_NAMES.md の内部カラム名に準拠。
    """
    conn = open_db_readonly(config.db_path)
    try:
        cur = conn.cursor()
        maps          = _load_dict(cur, "Maps")
        playlists     = _load_dict(cur, "Playlists")
        pairs         = _load_dict(cur, "PlaylistMapModePairs")
        game_variants = _load_dict(cur, "GameVariants")

        # ランクマップマスタを自動構築
        ranked_map_master = _build_ranked_map_master(cur, pairs)

        try:
            ms_rows = cur.execute("SELECT ResponseBody FROM MatchStats").fetchall()
        except sqlite3.Error:
            ms_rows = []

        pms_map = _load_player_match_stats(cur, config.my_xuid, ms_rows)

    finally:
        conn.close()

    if not ms_rows:
        return pd.DataFrame()

    records: list[dict[str, Any]] = []

    for (rb,) in ms_rows:
        try:
            match = json.loads(rb)
        except json.JSONDecodeError:
            continue

        match_id = match.get("MatchId")
        if not match_id:
            continue

        match_info = match.get("MatchInfo", {})
        players    = match.get("Players", [])

        # BOT含み判定
        has_bot = any(p.get("PlayerType") == 2 for p in players)

        # 自分のプレイヤーエントリ
        me = next(
            (p for p in players
             if p.get("PlayerId") == config.my_xuid
             and p.get("PlayerType") != 2),
            None,
        )
        if not me:
            continue

        # 基礎情報
        duration_sec = parse_seconds(match_info.get("Duration"))
        played_at    = parse_dt_jst(match_info.get("StartTime"))
        playlist     = _classify_playlist(match_info, playlists)
        my_team_id   = me.get("LastTeamId", 0)

        # 個人スタッツ
        stats       = safe_get(me, "PlayerTeamStats", 0, "Stats", "CoreStats") or {}
        kills       = stats.get("Kills",   0)
        deaths      = stats.get("Deaths",  0)
        assists     = stats.get("Assists", 0)
        shots_fired = stats.get("ShotsFired", 0)

        # マップ・ルール名の解決
        if playlist == "custom":
            map_id   = safe_get(match_info, "MapVariant",    "AssetId")
            gv_id    = safe_get(match_info, "UgcGameVariant","AssetId")
            map_name  = _clean_map(maps.get(map_id,{}).get("PublicName","") if map_id else "")
            rule_name = _parse_custom_rule(game_variants.get(gv_id,{}).get("PublicName","") if gv_id else "")
        else:
            pair_obj  = match_info.get("PlaylistMapModePair")
            pair_id   = pair_obj.get("AssetId","") if pair_obj else ""
            pair_name = pairs.get(pair_id,{}).get("PublicName","") if pair_id else ""
            rule_name, map_name = _parse_pair_name(pair_name)

        # 除外フラグ
        exclude_flag = _get_exclude_flag(
            me, duration_sec, shots_fired,
            playlist, rule_name, map_name,
            ranked_map_master, has_bot,
        )

        # 勝敗
        result = OUTCOME_MAP.get(me.get("Outcome"), "unknown")

        # チームスコア
        team_score = enemy_score = None
        team_pw_kills = enemy_pw_kills = None
        for t in match.get("Teams", []):
            sc  = safe_get(t, "Stats", "CoreStats", "Score")
            pwk = safe_get(t, "Stats", "CoreStats", "PowerWeaponKills")
            if t.get("TeamId") == my_team_id:
                team_score    = sc
                team_pw_kills = pwk
            else:
                enemy_score    = sc
                enemy_pw_kills = pwk

        # PlayerMatchStats
        expected_kills = expected_deaths = None
        csr_pre = csr_post = None
        team_mmr = enemy_mmr = None

        if pms := pms_map.get(match_id):
            result_block = pms.get("Result", {})
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

            recap    = result_block.get("RankRecap", {})
            pre_val  = safe_get(recap, "PreMatchCsr",  "Value")
            post_val = safe_get(recap, "PostMatchCsr", "Value")
            csr_pre  = int(pre_val)  if pre_val  and pre_val  > 0 else None
            csr_post = int(post_val) if post_val and post_val > 0 else None

            team_mmrs = result_block.get("TeamMmrs", {}) or {}
            my_key    = str(my_team_id)
            enemy_key = "1" if my_team_id == 0 else "0"
            tm = team_mmrs.get(my_key)
            em = team_mmrs.get(enemy_key)
            team_mmr  = round(float(tm)) if tm is not None else None
            enemy_mmr = round(float(em)) if em is not None else None

        perfect_kills = _count_perfect_kills(me)
        obj_stats     = _parse_obj_stats(me)

        records.append({
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
            "shots_fired":   shots_fired,
            "damage_dealt":  stats.get("DamageDealt",      0),
            "damage_taken":  stats.get("DamageTaken",      0),
            "score":         stats.get("Score",            0),
            "power_kills":   stats.get("PowerWeaponKills", 0),
            "perfect_kills": perfect_kills,
            "team_rank":     me.get("Rank"),
            "team_score":    team_score,
            "enemy_score":   enemy_score,
            "team_pw_kills": team_pw_kills,
            "enemy_pw_kills": enemy_pw_kills,
            "team_mmr":      team_mmr,
            "enemy_mmr":     enemy_mmr,
            "duration_sec":  duration_sec,
            # CSR
            "csr_pre":       csr_pre,
            "csr_post":      csr_post,
            # TrueSkill2
            "expected_kills":  expected_kills,
            "expected_deaths": expected_deaths,
            # オブジェクトスタッツ
            **obj_stats,
            # パーティ（processor.py で追記）
            "party_size":    None,
        })

    if not records:
        return pd.DataFrame()

    df = pd.DataFrame(records)
    df["played_at"] = pd.to_datetime(df["played_at"], utc=True, errors="coerce")
    df = df.sort_values("played_at").reset_index(drop=True)
    return df