"""
components/calendar_heatmap.py
-------------------------------
GitHub草風カレンダーヒートマップを3列で表示。
直近8週・月曜始まり・過去が左/現在が右。

PythonでHTML（<div> + title属性）を生成し st.html() で表示。
JS不要・SVG不使用・ツールチップはブラウザ標準のtitle属性で動作。
"""

from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import streamlit as st


# ==================================================
# 定数
# ==================================================

CELL = 13
GAP  = 3
WEEKS = 8

LABEL_W = 28
TITLE_H = 18
FOOTER_H = 20
PAD_X = 12
PAD_Y = 8

GRID_W = WEEKS * (CELL + GAP) - GAP
GRID_H = 7 * (CELL + GAP) - GAP
CARD_W = LABEL_W + GRID_W + PAD_X * 2
CARD_H = TITLE_H + GRID_H + FOOTER_H + PAD_Y * 2
CARD_GAP = 14
TOTAL_W = CARD_W * 3 + CARD_GAP * 2

EMPTY = "#1a1a1a"

G_GAMES = [EMPTY, "#1a3328", "#177a54", "#1D9E75", "#5DCAA5"]
G_RYG   = [EMPTY, "#5c1a10", "#993C1D", "#D85A30", "#BA7517",
           "#3a6614", "#1D9E75", "#085041"]

DAY_LABELS = ["Mon", "", "Wed", "", "Fri", "", "Sun"]


# ==================================================
# データ集計
# ==================================================

def _build_daily_data(df: pd.DataFrame) -> dict[str, dict]:
    stat = df[df["exclude_flag"] == ""].copy()
    if stat.empty:
        return {}
    stat["date_str"] = (
        stat["played_at"].dt.tz_convert("Asia/Tokyo").dt.strftime("%Y-%m-%d")
    )
    daily = (
        stat.groupby("date_str")
        .agg(games=("result_flag", "count"), wins=("result_flag", "sum"),
             kd=("kd_ratio", "mean"))
        .reset_index()
    )
    daily["winrate"] = (daily["wins"] / daily["games"] * 100).round(1)
    daily["kd"] = daily["kd"].round(2)
    return {
        row["date_str"]: {
            "games":   int(row["games"]),
            "kd":      float(row["kd"]),
            "winrate": float(row["winrate"]),
        }
        for _, row in daily.iterrows()
    }


def _build_weeks() -> list[list[date]]:
    """月曜始まりで直近WEEKS週の日付一覧（外側=週, 内側=7日分）。"""
    today = date.today()
    this_monday = today - timedelta(days=today.weekday())
    start_monday = this_monday - timedelta(weeks=WEEKS - 1)
    return [
        [start_monday + timedelta(weeks=w, days=d) for d in range(7)]
        for w in range(WEEKS)
    ]


# ==================================================
# 色の決定
# ==================================================

def _color_games(v: int) -> str:
    if v < 3:  return G_GAMES[1]
    if v < 8:  return G_GAMES[2]
    if v < 18: return G_GAMES[3]
    return G_GAMES[4]


def _color_kd(v: float) -> str:
    if v < 0.6:  return G_RYG[1]
    if v < 0.8:  return G_RYG[2]
    if v < 1.0:  return G_RYG[3]
    if v < 1.05: return G_RYG[4]
    if v < 1.3:  return G_RYG[5]
    if v < 1.6:  return G_RYG[6]
    return G_RYG[7]


def _color_winrate(v: float) -> str:
    if v < 35: return G_RYG[1]
    if v < 45: return G_RYG[2]
    if v < 50: return G_RYG[3]
    if v < 55: return G_RYG[4]
    if v < 62: return G_RYG[5]
    if v < 72: return G_RYG[6]
    return G_RYG[7]


SCHEMES = [
    {"title": "PLAY COUNT", "key": "games", "color_fn": _color_games,
     "legend": G_GAMES[1:]},
    {"title": "K / D",     "key": "kd",    "color_fn": _color_kd,
     "legend": [G_RYG[1], G_RYG[3], G_RYG[4], G_RYG[6], G_RYG[7]]},
    {"title": "WIN RATE",  "key": "winrate","color_fn": _color_winrate,
     "legend": [G_RYG[1], G_RYG[3], G_RYG[4], G_RYG[6], G_RYG[7]]},
]


# ==================================================
# HTML 生成（<div> ベース + title属性でツールチップ）
# ==================================================

def _make_cell(day: date | None, today: date,
               daily_data: dict[str, dict], key: str,
               color_fn) -> str:
    """1セルのHTMLを返す。"""
    if day is None or day > today:
        return f'<div style="width:{CELL}px;height:{CELL}px;flex-shrink:0"></div>'

    date_str = day.strftime("%Y-%m-%d")
    entry = daily_data.get(date_str)
    if entry is None:
        color = EMPTY
        tip   = f"{date_str} | プレイなし"
    else:
        val   = entry[key]
        color = color_fn(val)
        tip   = (f"{date_str} | {entry['games']}試合 · "
                 f"K/D {entry['kd']:.2f} · "
                 f"勝率 {entry['winrate']:.1f}%")

    return (
        f'<div style="width:{CELL}px;height:{CELL}px;flex-shrink:0;'
        f'border-radius:2px;background:{color};cursor:default" '
        f'title="{tip}"></div>'
    )


def _make_card(scheme: dict, cols: list[list[date]],
               daily_data: dict[str, dict], today: date) -> str:
    """1指標分のカードHTMLを返す。"""
    key = scheme["key"]
    color_fn = scheme["color_fn"]

    # 曜日ラベル
    day_labels_html = ""
    for d, label in enumerate(DAY_LABELS):
        if not label:
            continue
        day_labels_html += (
            f'<div style="height:{CELL}px;display:flex;align-items:center;'
            f'justify-content:flex-end;padding-right:4px;font-size:8px;'
            f'color:rgba(255,255,255,0.25);font-family:sans-serif">'
            f'{label}</div>'
        )

    # セルグリッド
    grid_html = ""
    for col in cols:
        col_html = '<div style="display:flex;flex-direction:column;gap:{}px">'.format(GAP)
        for day in col:
            col_html += _make_cell(day, today, daily_data, key, color_fn)
        col_html += "</div>"
        grid_html += col_html

    # 凡例
    legend_html = ""
    for c in scheme["legend"]:
        legend_html += (
            f'<div style="width:{CELL}px;height:{CELL}px;flex-shrink:0;'
            f'border-radius:2px;background:{c}"></div>'
        )

    return f"""\
<div style="background:#1e1e2e;border:0.5px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:{PAD_Y}px {PAD_X}px">
  <div style="font-family:sans-serif;font-size:10px;font-weight:500;
              color:rgba(255,255,255,0.4);margin-bottom:6px;
              letter-spacing:0.06em;text-transform:uppercase;
              text-align:center">{scheme["title"]}</div>
  <div style="display:flex;gap:{GAP}px">
    <div style="display:flex;flex-direction:column;gap:{GAP}px;width:{LABEL_W}px;flex-shrink:0">
      {day_labels_html}
    </div>
    <div style="display:flex;gap:{GAP}px">{grid_html}</div>
  </div>
  <div style="display:flex;justify-content:flex-end;align-items:center;gap:3px;margin-top:6px">
    <span style="font-family:sans-serif;font-size:9px;color:rgba(255,255,255,0.3)">少</span>
    <div style="display:flex;gap:{GAP}px">{legend_html}</div>
    <span style="font-family:sans-serif;font-size:9px;color:rgba(255,255,255,0.3)">多</span>
  </div>
</div>"""


# ==================================================
# メインエントリポイント
# ==================================================

def render_calendar_heatmaps(df: pd.DataFrame, weeks: int = WEEKS) -> None:
    daily_data = _build_daily_data(df)
    today = date.today()
    cols = _build_weeks()

    cards_html = "".join(
        _make_card(scheme, cols, daily_data, today) for scheme in SCHEMES
    )

    html = (
        f'<div style="display:grid;grid-template-columns:repeat(3,{CARD_W}px);'
        f'gap:{CARD_GAP}px;width:{TOTAL_W}px;box-sizing:border-box">'
        f'{cards_html}'
        f'</div>'
    )

    st.html(html)