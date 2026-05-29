"""
halo_knowledge/ranked_rotations.py
------------------------------------
ランクローテーション情報。

Ranked Arena / Ranked Slayer のマップ・ルール構成。
as_of と source を必ず持つ（頻繁に変わるため）。

DB実績（2026/04/20以降）を正とする。
公式ページの記載と差異がある項目はコメントで補足。
"""

from __future__ import annotations
from typing import Any

RANKED_ROTATIONS: dict[str, Any] = {
    "ranked_arena": {
        "label_ja": "ランクアリーナ",
        "as_of": "2026-04-20",
        "source": "DB実績データ（2026/04/20以降の生データを正とする）",
        "loadout": "Bandit Evo loadout",
        "loadout_label_ja": "初期武器: Bandit Evo",
        "motion_tracker": "disabled",
        "motion_tracker_label_ja": "モーショントラッカー無効",
        "map_mode_pairs": {
            # CTF のみ
            "Aquarius":  ["CTF"],
            "Empyrean":  ["CTF"],
            "Fortress":  ["CTF"],
            "Origin":    ["CTF", "Slayer"],
            # KOTH / Oddball
            "Lattice":   ["King of the Hill", "Oddball"],
            # フルセット
            "Live Fire": ["King of the Hill", "Oddball", "Slayer", "Strongholds"],
            "Recharge":  ["King of the Hill", "Oddball", "Slayer", "Strongholds"],
            "Streets":   ["King of the Hill", "Oddball", "Slayer", "Strongholds"],
            # KOTH / Slayer
            "Solitude":  ["King of the Hill", "Slayer"],
            "Vacancy":   ["King of the Hill", "Oddball", "Slayer"],
        },
    },
    "ranked_slayer": {
        "label_ja": "ランクスレイヤー",
        "as_of": "2026-04-20",
        "source": "DB実績データ（2026/04/20以降の生データを正とする）",
        "loadout": "Bandit Evo loadout",
        "loadout_label_ja": "初期武器: Bandit Evo",
        "motion_tracker": "disabled",
        "motion_tracker_label_ja": "モーショントラッカー無効",
        "map_mode_pairs": {
            "Aquarius":     ["Slayer"],
            "Empyrean":     ["Slayer"],
            "Interference": ["Slayer"],
            "Lattice":      ["Slayer"],
            "Live Fire":    ["Slayer"],
            "Origin":       ["Slayer"],
            "Recharge":     ["Slayer"],
            "Serenity":     ["Slayer"],
            "Solitude":     ["Slayer"],
            "Streets":      ["Slayer"],
            "Vacancy":      ["Slayer"],
        },
    },
}
