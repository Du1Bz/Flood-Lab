"""
components/calendar_heatmap.py
------------------------------
GitHub草風カレンダーヒートマップを3列で表示する Streamlit コンポーネント。

プレイ回数 / K/D / 勝率 の3指標を横並びで表示する。
"""

from __future__ import annotations

import json
from datetime import date, timedelta

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


def _build_daily_data(df: pd.DataFrame) -> dict[str, dict]:
    """
    DataFrame から日付ごとの集計データを作る。
    除外フラグのないものだけ対象。
    """
    stat = df[df["exclude_flag"] == ""].copy()
    if stat.empty:
        return {}

    stat["date_str"] = (
        stat["played_at"]
        .dt.tz_convert("Asia/Tokyo")
        .dt.strftime("%Y-%m-%d")
    )

    daily = (
        stat.groupby("date_str")
        .agg(
            games=("result_flag", "count"),
            wins=("result_flag", "sum"),
            kd=("kd_ratio", "mean"),
        )
        .reset_index()
    )
    daily["winrate"] = (daily["wins"] / daily["games"] * 100).round(1)
    daily["kd"]      = daily["kd"].round(2)

    return {
        row["date_str"]: {
            "games":   int(row["games"]),
            "kd":      float(row["kd"]),
            "winrate": float(row["winrate"]),
        }
        for _, row in daily.iterrows()
    }


def render_calendar_heatmaps(df: pd.DataFrame, weeks: int = 53) -> None:
    """
    3つのカレンダーヒートマップを横並びで表示する。

    Args:
        df:    分析用 DataFrame（processor.build_match_df の戻り値）
        weeks: 表示する週数（デフォルト53週 = 約1年）
    """
    daily_data = _build_daily_data(df)
    data_json  = json.dumps(daily_data)

    html = f"""
<style>
  .hm-wrap {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    padding: 4px 0 12px;
  }}
  .hm-card {{
    background: var(--color-background-secondary, #f8f8f6);
    border: 0.5px solid var(--color-border-tertiary, rgba(0,0,0,.12));
    border-radius: 10px;
    padding: 12px 14px 10px;
    min-width: 0;
  }}
  .hm-title {{
    font-size: 12px;
    font-weight: 500;
    color: var(--color-text-secondary, #666);
    margin: 0 0 8px;
    letter-spacing: .03em;
  }}
  .hm-grid {{
    display: flex;
    gap: 2px;
  }}
  .hm-col {{
    display: flex;
    flex-direction: column;
    gap: 2px;
  }}
  .hm-cell {{
    width: 10px;
    height: 10px;
    border-radius: 2px;
    cursor: default;
    transition: opacity .1s;
  }}
  .hm-cell:hover {{ opacity: .75; }}
  .hm-tooltip {{
    position: fixed;
    background: var(--color-background-primary, #fff);
    border: 0.5px solid var(--color-border-secondary, rgba(0,0,0,.2));
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 12px;
    color: var(--color-text-primary, #111);
    pointer-events: none;
    z-index: 9999;
    white-space: nowrap;
    display: none;
    line-height: 1.6;
  }}
  .hm-footer {{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 3px;
    margin-top: 6px;
  }}
  .hm-legend-label {{
    font-size: 10px;
    color: var(--color-text-tertiary, #999);
  }}
</style>

<div class="hm-wrap" id="hm-root"></div>
<div class="hm-tooltip" id="hm-tip"></div>

<script>
(function() {{
  const DATA  = {data_json};
  const WEEKS = {weeks};

  const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  const SCHEMES = {{
    games: {{
      title: 'プレイ回数',
      empty:  isDark ? '#2a2a28' : '#eeecea',
      levels: isDark
        ? ['#1a3a2a','#1D9E75','#0F6E56','#085041']
        : ['#d5f0e6','#5DCAA5','#1D9E75','#085041'],
      thresholds: [1, 5, 15, 25],
      fmt: v => v + '試合',
    }},
    kd: {{
      title: 'K/D',
      empty:  isDark ? '#2a2a28' : '#eeecea',
      levels: isDark
        ? ['#2a2033','#7F77DD','#534AB7','#3C3489']
        : ['#e8e6fe','#AFA9EC','#7F77DD','#3C3489'],
      thresholds: [0, 0.8, 1.0, 1.5],
      fmt: v => 'K/D ' + v.toFixed(2),
    }},
    winrate: {{
      title: '勝率',
      empty:  isDark ? '#2a2a28' : '#eeecea',
      levels: isDark
        ? ['#2d1f1a','#F0997B','#D85A30','#993C1D']
        : ['#fce8e0','#F0997B','#D85A30','#712B13'],
      thresholds: [0, 40, 55, 70],
      fmt: v => '勝率 ' + v.toFixed(1) + '%',
    }},
  }};

  function getColor(scheme, val) {{
    if (val === null) return scheme.empty;
    const th = scheme.thresholds;
    const lv = scheme.levels;
    for (let i = th.length - 1; i >= 0; i--) {{
      if (val >= th[i]) return lv[i];
    }}
    return scheme.empty;
  }}

  function buildWeeks() {{
    const today = new Date();
    today.setHours(0,0,0,0);
    const startDow = today.getDay();
    const end = new Date(today);
    const start = new Date(today);
    start.setDate(start.getDate() - (WEEKS * 7 - 1));

    const cols = [];
    let cur = new Date(start);
    while (cur <= end) {{
      const col = [];
      for (let d = 0; d < 7; d++) {{
        if (cur > end) {{ col.push(null); }}
        else {{ col.push(new Date(cur)); }}
        cur.setDate(cur.getDate() + 1);
      }}
      cols.push(col);
    }}
    return cols;
  }}

  function dateKey(d) {{
    if (!d) return null;
    return d.getFullYear() + '-' +
      String(d.getMonth()+1).padStart(2,'0') + '-' +
      String(d.getDate()).padStart(2,'0');
  }}

  const tip = document.getElementById('hm-tip');

  function buildCard(metricKey, cols) {{
    const scheme = SCHEMES[metricKey];
    const card = document.createElement('div');
    card.className = 'hm-card';

    const title = document.createElement('div');
    title.className = 'hm-title';
    title.textContent = scheme.title;
    card.appendChild(title);

    const grid = document.createElement('div');
    grid.className = 'hm-grid';

    cols.forEach(col => {{
      const colEl = document.createElement('div');
      colEl.className = 'hm-col';
      col.forEach(day => {{
        const cell = document.createElement('div');
        cell.className = 'hm-cell';
        if (!day) {{
          cell.style.opacity = '0';
        }} else {{
          const key = dateKey(day);
          const entry = DATA[key] || null;
          const val = entry ? entry[metricKey] : null;
          cell.style.background = getColor(scheme, val);

          cell.addEventListener('mousemove', e => {{
            tip.style.display = 'block';
            tip.style.left = (e.clientX + 12) + 'px';
            tip.style.top  = (e.clientY - 8) + 'px';
            if (entry) {{
              tip.innerHTML =
                '<span style="color:var(--color-text-secondary,#888);font-size:11px">' + key + '</span><br>' +
                entry.games + '試合 &nbsp; K/D ' + entry.kd.toFixed(2) +
                ' &nbsp; 勝率 ' + entry.winrate.toFixed(1) + '%';
            }} else {{
              tip.innerHTML =
                '<span style="color:var(--color-text-secondary,#888);font-size:11px">' + key + '</span><br>' +
                '<span style="color:var(--color-text-tertiary,#aaa)">プレイなし</span>';
            }}
          }});
          cell.addEventListener('mouseleave', () => {{ tip.style.display = 'none'; }});
        }}
        colEl.appendChild(cell);
      }});
      grid.appendChild(colEl);
    }});

    card.appendChild(grid);

    // 凡例
    const footer = document.createElement('div');
    footer.className = 'hm-footer';
    const lbl1 = document.createElement('span');
    lbl1.className = 'hm-legend-label';
    lbl1.textContent = '少';
    footer.appendChild(lbl1);
    scheme.levels.forEach(c => {{
      const sq = document.createElement('div');
      sq.className = 'hm-cell';
      sq.style.background = c;
      sq.style.cursor = 'default';
      footer.appendChild(sq);
    }});
    const lbl2 = document.createElement('span');
    lbl2.className = 'hm-legend-label';
    lbl2.textContent = '多';
    footer.appendChild(lbl2);
    card.appendChild(footer);

    return card;
  }}

  const cols = buildWeeks();
  const root = document.getElementById('hm-root');
  ['games','kd','winrate'].forEach(k => {{
    root.appendChild(buildCard(k, cols));
  }});
}})();
</script>
"""

    components.html(html, height=200, scrolling=False)
