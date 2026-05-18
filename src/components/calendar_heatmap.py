"""
components/calendar_heatmap.py
------------------------------
GitHub草風カレンダーヒートマップを3列で表示。
直近8週・月曜始まり・過去が左/現在が右。
"""

from __future__ import annotations
import json
import pandas as pd
import streamlit.components.v1 as components


def _build_daily_data(df: pd.DataFrame) -> dict[str, dict]:
    stat = df[df["exclude_flag"] == ""].copy()
    if stat.empty:
        return {}
    stat["date_str"] = (
        stat["played_at"].dt.tz_convert("Asia/Tokyo").dt.strftime("%Y-%m-%d")
    )
    daily = (
        stat.groupby("date_str")
        .agg(games=("result_flag","count"), wins=("result_flag","sum"), kd=("kd_ratio","mean"))
        .reset_index()
    )
    daily["winrate"] = (daily["wins"] / daily["games"] * 100).round(1)
    daily["kd"]      = daily["kd"].round(2)
    return {
        row["date_str"]: {"games": int(row["games"]), "kd": float(row["kd"]), "winrate": float(row["winrate"])}
        for _, row in daily.iterrows()
    }


def render_calendar_heatmaps(df: pd.DataFrame, weeks: int = 8) -> None:
    daily_data = _build_daily_data(df)
    data_json  = json.dumps(daily_data)

    # セルサイズ・ギャップ
    CELL = 13
    GAP  = 3
    # 8列（週）× (CELL+GAP) + GAP = グリッド幅
    GRID_W = weeks * (CELL + GAP) - GAP  # 8*16-3=125px
    CARD_W = GRID_W + 26 * 2             # padding 26px両側
    TOTAL_W = CARD_W * 3 + 14 * 2       # 3カード + gap*2
    GRID_H = 7 * (CELL + GAP) - GAP     # 7*16-3=109px
    CARD_H = GRID_H + 11 + 16 + 9 + 6 + CELL  # title+grid+footer+padding
    HEIGHT  = CARD_H + 16               # wrap padding

    html = f"""
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:transparent}}
.hm-wrap{{
  display:grid;
  grid-template-columns:repeat(3,{CARD_W}px);
  gap:14px;
  width:{TOTAL_W}px;
}}
.hm-card{{
  background:var(--background-color,#1e1e2e);
  border:0.5px solid rgba(255,255,255,.08);
  border-radius:10px;
  padding:11px 26px 9px;
  width:{CARD_W}px;
}}
.hm-title{{
  font-family:sans-serif;
  font-size:10px;
  font-weight:500;
  color:rgba(255,255,255,.4);
  margin-bottom:7px;
  letter-spacing:.06em;
  text-transform:uppercase;
}}
.hm-grid{{display:flex;gap:{GAP}px}}
.hm-col{{display:flex;flex-direction:column;gap:{GAP}px}}
.hm-cell{{
  width:{CELL}px;
  height:{CELL}px;
  border-radius:2px;
  flex-shrink:0;
  cursor:default;
}}
.hm-footer{{
  display:flex;
  justify-content:flex-end;
  align-items:center;
  gap:3px;
  margin-top:6px;
}}
.hm-ll{{font-family:sans-serif;font-size:9px;color:rgba(255,255,255,.3)}}
#hm-tip{{
  position:fixed;
  background:#1a1a2e;
  border:0.5px solid rgba(255,255,255,.15);
  border-radius:6px;
  padding:6px 10px;
  font-family:sans-serif;
  font-size:12px;
  color:rgba(255,255,255,.85);
  pointer-events:none;
  z-index:9999;
  white-space:nowrap;
  display:none;
  line-height:1.6;
}}
</style>
<div class="hm-wrap" id="hm-root"></div>
<div id="hm-tip"></div>
<script>
(function(){{
  const DATA={data_json}, WEEKS={weeks};

  // 赤→緑 7段階（空セル含む）
  // dark mode 想定
  const EMPTY = '#1a1a1a';

  // プレイカウント: グレー系→teal
  const G_GAMES = [EMPTY,'#1a3328','#177a54','#1D9E75','#5DCAA5'];
  // KD & 勝率: 赤→黄→緑
  const G_RYG = [
    EMPTY,
    '#5c1a10',  // 深赤
    '#993C1D',  // 赤
    '#D85A30',  // 橙赤
    '#BA7517',  // 黄
    '#3a6614',  // 黄緑
    '#1D9E75',  // 緑
    '#085041',  // 深緑
  ];

  const SCHEMES={{
    games:{{
      title:'PLAY COUNT',
      getColor(v){{
        if(!v) return EMPTY;
        if(v<3)  return G_GAMES[1];
        if(v<8)  return G_GAMES[2];
        if(v<18) return G_GAMES[3];
        return G_GAMES[4];
      }},
      legend:[G_GAMES[1],G_GAMES[2],G_GAMES[3],G_GAMES[4]],
    }},
    kd:{{
      title:'K / D',
      getColor(v){{
        if(v===null||v===undefined) return EMPTY;
        if(v<0.6)  return G_RYG[1];
        if(v<0.8)  return G_RYG[2];
        if(v<1.0)  return G_RYG[3];
        if(v<1.05) return G_RYG[4];  // 1.0付近=黄
        if(v<1.3)  return G_RYG[5];
        if(v<1.6)  return G_RYG[6];
        return G_RYG[7];
      }},
      legend:[G_RYG[1],G_RYG[3],G_RYG[4],G_RYG[6],G_RYG[7]],
    }},
    winrate:{{
      title:'WIN RATE',
      getColor(v){{
        if(v===null||v===undefined) return EMPTY;
        if(v<35)   return G_RYG[1];
        if(v<45)   return G_RYG[2];
        if(v<50)   return G_RYG[3];
        if(v<55)   return G_RYG[4];  // 50%付近=黄
        if(v<62)   return G_RYG[5];
        if(v<72)   return G_RYG[6];
        return G_RYG[7];
      }},
      legend:[G_RYG[1],G_RYG[3],G_RYG[4],G_RYG[6],G_RYG[7]],
    }},
  }};

  function buildWeeks(){{
    const today=new Date(); today.setHours(0,0,0,0);
    const dow=today.getDay();
    const daysSinceMonday=(dow+6)%7;
    const thisMonday=new Date(today);
    thisMonday.setDate(today.getDate()-daysSinceMonday);
    const startMonday=new Date(thisMonday);
    startMonday.setDate(thisMonday.getDate()-(WEEKS-1)*7);
    const cols=[];
    let cur=new Date(startMonday);
    for(let w=0;w<WEEKS;w++){{
      const col=[];
      for(let d=0;d<7;d++){{
        col.push(new Date(cur));
        cur.setDate(cur.getDate()+1);
      }}
      cols.push(col);
    }}
    return cols;
  }}

  function dateKey(d){{
    return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
  }}

  const tip=document.getElementById('hm-tip');
  const today=new Date(); today.setHours(0,0,0,0);

  function buildCard(key,cols){{
    const scheme=SCHEMES[key];
    const card=document.createElement('div');
    card.className='hm-card';

    const title=document.createElement('div');
    title.className='hm-title';
    title.textContent=scheme.title;
    card.appendChild(title);

    const grid=document.createElement('div');
    grid.className='hm-grid';
    cols.forEach(col=>{{
      const colEl=document.createElement('div');
      colEl.className='hm-col';
      col.forEach(day=>{{
        const cell=document.createElement('div');
        cell.className='hm-cell';
        const isFuture=day>today;
        if(isFuture){{
          cell.style.background='transparent';
        }}else{{
          const k=dateKey(day);
          const entry=DATA[k]||null;
          const val=entry?entry[key]:null;
          cell.style.background=scheme.getColor(val);
          cell.addEventListener('mousemove',e=>{{
            tip.style.display='block';
            tip.style.left=(e.clientX+14)+'px';
            tip.style.top=(e.clientY-10)+'px';
            if(entry){{
              tip.innerHTML='<span style="opacity:.5;font-size:11px">'+k+'</span><br>'+
                entry.games+'試合 · K/D '+entry.kd.toFixed(2)+' · 勝率 '+entry.winrate.toFixed(1)+'%';
            }}else{{
              tip.innerHTML='<span style="opacity:.5;font-size:11px">'+k+'</span><br>'+
                '<span style="opacity:.4">プレイなし</span>';
            }}
          }});
          cell.addEventListener('mouseleave',()=>tip.style.display='none');
        }}
        colEl.appendChild(cell);
      }});
      grid.appendChild(colEl);
    }});
    card.appendChild(grid);

    const footer=document.createElement('div');
    footer.className='hm-footer';
    const l1=document.createElement('span'); l1.className='hm-ll'; l1.textContent='少';
    footer.appendChild(l1);
    scheme.legend.forEach(c=>{{
      const sq=document.createElement('div');
      sq.className='hm-cell';
      sq.style.background=c;
      footer.appendChild(sq);
    }});
    const l2=document.createElement('span'); l2.className='hm-ll'; l2.textContent='多';
    footer.appendChild(l2);
    card.appendChild(footer);
    return card;
  }}

  const cols=buildWeeks();
  const root=document.getElementById('hm-root');
  ['games','kd','winrate'].forEach(k=>root.appendChild(buildCard(k,cols)));
}})();
</script>
"""
    components.html(html, height=171, scrolling=False)