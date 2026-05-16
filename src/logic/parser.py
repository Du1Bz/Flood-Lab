"""
logic/parser.py
---------------
パーティ検出・セッション分割・party_type/is_solo などのフラグ追加。
database.py が作った raw DataFrame を受け取り、列を追加して返す。
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

import pandas as pd

from src.utils.helpers import safe_get
from src.utils.display import PARTY_TYPE_DISPLAY

# セッション分割の閾値（秒）: 2時間
SESSION_GAP_SEC = 2 * 60 * 60


# ==================================================
# パーティ検出
# ==================================================

def build_party_map(
    df: pd.DataFrame,
    db_path: Path,
    my_xuid: str,
) -> dict[str, int]:
    """
    全試合を時系列で走査し、各 match_id に対してパーティ人数を返す辞書を構築する。

    判定ルール:
    - カスタムゲーム (playlist="custom"): 4人固定
    - ランク等: 前後2試合を含むウィンドウで同チームに3回以上登場した味方 = パーティメンバー
    - 条件を満たさない = ソロ (1人)

    DB を直接読んで Players を取得する（database.py の load_matches では
    全プレイヤーを展開しないため）。
    """
    # MatchStats から Players を読む
    uri = f"file:{Path(db_path).resolve()}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    try:
        rows = conn.execute("SELECT ResponseBody FROM MatchStats").fetchall()
    finally:
        conn.close()

    # (played_at, allies_frozenset, match_id, playlist) を時系列昇順で構築
    sessions: list[tuple[str, frozenset, str, str]] = []
    mid_to_playlist: dict[str, str] = {}

    # df から match_id → playlist のマップを作る
    if not df.empty and "playlist" in df.columns:
        mid_to_playlist = dict(zip(df["match_id"], df["playlist"]))

    for (rb,) in rows:
        try:
            match = json.loads(rb)
        except json.JSONDecodeError:
            continue

        match_id = match.get("MatchId")
        if not match_id:
            continue

        me = next(
            (p for p in match.get("Players", [])
             if p.get("PlayerId") == my_xuid
             and p.get("PlayerType") != 2),
            None,
        )
        if not me:
            continue

        my_team = me.get("LastTeamId")
        allies = frozenset(
            str(p.get("PlayerId", ""))
            for p in match.get("Players", [])
            if p.get("PlayerType") != 2
            and not str(p.get("PlayerId", "")).startswith("bid(")
            and p.get("LastTeamId") == my_team
            and p.get("PlayerId") != my_xuid
        )

        start_time = safe_get(match, "MatchInfo", "StartTime") or ""
        playlist   = mid_to_playlist.get(match_id, "other")
        sessions.append((start_time, allies, match_id, playlist))

    # 時系列昇順
    sessions.sort(key=lambda x: x[0])

    party_map: dict[str, int] = {}
    n = len(sessions)

    for i, (_, allies, mid, playlist) in enumerate(sessions):
        if playlist == "custom":
            party_map[mid] = 4
            continue
        if not allies:
            party_map[mid] = 1
            continue

        window = [sessions[j][1] for j in range(max(0, i - 2), min(n, i + 3))]
        party_members = {
            xuid for xuid in allies
            if sum(1 for w in window if xuid in w) >= 3
        }
        party_map[mid] = len(party_members) + 1

    return party_map


# ==================================================
# セッション分割
# ==================================================

def assign_sessions(df: pd.DataFrame) -> pd.DataFrame:
    """
    played_at の時系列ギャップ（2時間以上）でセッションを分割し、
    session_id と session_seq カラムを追加する。

    df は played_at 昇順でソート済みであることを前提とする。
    """
    if df.empty:
        df["session_id"]  = pd.Series(dtype="Int64")
        df["session_seq"] = pd.Series(dtype="Int64")
        return df

    df = df.copy()
    session_ids: list[int] = []
    session_seqs: list[int] = []

    current_session = 0
    current_seq     = 0
    prev_at         = None

    for _, row in df.iterrows():
        played_at = row["played_at"]

        if prev_at is None:
            current_session = 1
            current_seq     = 1
        else:
            gap = (played_at - prev_at).total_seconds()
            if gap >= SESSION_GAP_SEC:
                current_session += 1
                current_seq      = 1
            else:
                current_seq += 1

        session_ids.append(current_session)
        session_seqs.append(current_seq)
        prev_at = played_at

    df["session_id"]  = session_ids
    df["session_seq"] = session_seqs
    return df


# ==================================================
# フラグ・派生カラムの追加
# ==================================================

def add_flags(df: pd.DataFrame) -> pd.DataFrame:
    """
    party_size が追加済みの DataFrame に、派生カラムを追加する。
    - party_type: "ソロ" / "デュオ" / "トリオ" / "フルパ"
    - is_solo / is_party: bool
    """
    if df.empty:
        return df

    df = df.copy()
    df["party_type"] = df["party_size"].map(
        lambda s: PARTY_TYPE_DISPLAY.get(int(s), f"{s}人") if pd.notna(s) else "不明"
    )
    df["is_solo"]  = df["party_size"] == 1
    df["is_party"] = df["party_size"].fillna(1) > 1
    return df
