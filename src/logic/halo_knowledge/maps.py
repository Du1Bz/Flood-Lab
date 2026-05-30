"""
halo_knowledge/maps.py
----------------------
マップコンテキスト。

layout / items / added_at を独立フィールド化。
notes は構造化しきれない補足用として残す。
"""

from __future__ import annotations
from typing import Any

MAPS: dict[str, Any] = {
    "Aquarius": {
        "added_at": "2021-11-15",
        "current_ranked_status": "active",
        "layout": {
            "size": "large",
            "symmetry": "symmetric",
            "lanes": 3,
            "verticality": "medium",
            "long_sightlines": "high",
        },
        "items": {
            "power_weapons": [],
            "powerups": ["camo"],
            "equipment": [],
        },
        "notes": (
            "3レーン構造。マップ中央にカモフラージュが配置されている。"
            "ベースとベースの距離はBandit Evoではエイムアシストがかからないが、BRではかかる距離。"
        ),
    },
    "Empyrean": {
        "added_at": "2022-12-06",
        "current_ranked_status": "active",
        "layout": {
            "size": "large",
            "symmetry": "symmetric",
            "lanes": 3,
            "verticality": "medium",
            "long_sightlines": "high",
        },
        "items": {
            "power_weapons": ["rocket", "sniper"],
            "powerups": [],
            "equipment": [],
        },
        "notes": (
            "3レーン構造。マップ中央にロケットランチャー、両サイドのスナイパータワー1階に"
            "スナイパーライフルが配置されている。Halo 3のThe Pitのリメイクマップ。"
        ),
    },
    "Fortress": {
        "added_at": "2024-10-30",
        "current_ranked_status": "active",
        "layout": {
            "size": "small",
            "symmetry": "symmetric",
            "lanes": 3,
            "verticality": "high",
            "long_sightlines": "medium",
        },
        "items": {
            "power_weapons": ["sniper"],
            "powerups": ["overshield"],
            "equipment": [],
        },
        "notes": (
            "3レーン構造。マップ中央にオーバーシールド、両ベースにスナイパーライフルが配置されている。"
            "中央には太い塔があり、内側と外側に螺旋階段がある。"
        ),
    },
    "Interference": {
        "added_at": "2024-04-23",
        "current_ranked_status": "active",    # ranked_slayer に存在（DB実績 2026/04/20以降）
        "layout": {
            "size": "medium",
            "symmetry": "asymmetric",
            "lanes": None,
            "verticality": "medium",
            "long_sightlines": "high",
        },
        "items": {
            "power_weapons": ["sniper"],
            "powerups": ["overshield"],
            "equipment": [],
        },
        "notes": (
            "マップ中央にオーバーシールドが配置されている。遠距離での戦闘が発生しやすい。"
            "Halo 5のThe Rigのリメイクマップ。"
        ),
    },
    "Lattice": {
        "added_at": "2025-08-05",
        "current_ranked_status": "active",
        "layout": {
            "size": "large",
            "symmetry": "asymmetric",
            "lanes": 3,
            "verticality": "medium",
            "long_sightlines": "high",
        },
        "items": {
            "power_weapons": ["sniper"],
            "powerups": [],
            "equipment": [],
        },
        "notes": (
            "横方向の3レーン構造。中央レーンが開けていて低い。両サイドに建物内の2レーンがある。"
            "エリアを管理できていないとマップの横断がしづらい。"
        ),
    },
    "Live Fire": {
        "added_at": "2021-11-15",
        "current_ranked_status": "active",
        "layout": {
            "size": "medium",
            "symmetry": "asymmetric",
            "lanes": 3,
            "verticality": "high",
            "long_sightlines": "medium",
        },
        "items": {
            "power_weapons": ["sniper"],
            "powerups": ["camo"],
            "equipment": [],
        },
        "notes": (
            "3レーン構造。開けたレーン、スナイパーライフルが配置されている狭いレーン、"
            "カモフラージュが配置されている開けたレーンがある。"
        ),
    },
    "Origin": {
        "added_at": "2025-02-04",
        "current_ranked_status": "active",
        "layout": {
            "size": "large",
            "symmetry": "symmetric",
            "lanes": 3,
            "verticality": "high",
            "long_sightlines": "high",
        },
        "items": {
            "power_weapons": ["sniper", "rocket"],
            "powerups": [],
            "equipment": [],
        },
        "notes": (
            "3レーン構造。スナイパーライフルの配置された建造物に囲まれたレーン、中央の低いレーン、"
            "ロケットランチャーの配置された開けた高いレーンがある。Halo 5のColliseumのリメイクマップ。"
        ),
    },
    "Recharge": {
        "added_at": "2021-11-15",
        "current_ranked_status": "active",
        "layout": {
            "size": "medium",
            "symmetry": "asymmetric",
            "lanes": None,
            "verticality": "medium",
            "long_sightlines": "high",
        },
        "items": {
            "power_weapons": ["shock"],
            "powerups": ["camo"],
            "equipment": [],
        },
        "notes": (
            "2階建ての外周部に囲まれたマップ。中央部は開けており、低い場所にカモフラージュが配置されている。"
            "ショックライフルはAPIでPWキルとしてカウントされない点に注意。"
        ),
    },
    "Serenity": {
        "added_at": "2025-08-05",
        "current_ranked_status": "active",    # ranked_slayer に存在（DB実績 2026/04/20以降）
        "layout": {
            "size": "medium",
            "symmetry": "symmetric",
            "lanes": 3,
            "verticality": "low",             # テンプレートの"small"はsize誤記と判断しlowに変換
            "long_sightlines": "medium",
        },
        "items": {
            "power_weapons": ["sniper", "rocket"],
            "powerups": [],
            "equipment": [],
        },
        "notes": (
            "3レーン構造。両ベースにスナイパーライフル、マップ中央にロケットランチャーが配置されている。"
            "中央は3階建てのリング構造。Halo 2のSanctuaryのリメイクマップ。"
        ),
    },
    "Solitude": {
        "added_at": "2023-06-27",
        "current_ranked_status": "active",
        "layout": {
            "size": "large",
            "symmetry": "asymmetric",
            "lanes": 3,
            "verticality": "high",
            "long_sightlines": "high",
        },
        "items": {
            "power_weapons": ["shock"],
            "powerups": ["camo"],
            "equipment": [],
        },
        "notes": (
            "高低差が激しい。中央の開けた高台にカモフラージュが配置されている。"
            "外周部は建物で囲まれている。"
            "ショックライフルはAPIでPWキルとしてカウントされない点に注意。"
            "Halo 5のPlazaのリメイクマップ。"
        ),
    },
    "Streets": {
        "added_at": "2021-12-08",
        "current_ranked_status": "active",
        "layout": {
            "size": "medium",
            "symmetry": "asymmetric",
            "lanes": 3,
            "verticality": "medium",
            "long_sightlines": "low",
        },
        "items": {
            "power_weapons": [],
            "powerups": ["camo"],
            "equipment": [],
        },
        "notes": (
            "3レーン構造。レーン間が狭く隣のレーンに移動しやすい。"
            "入り組んでおり近距離での戦闘が発生しやすい。"
            "中央の開けた場所にカモフラージュが配置されている。"
        ),
    },
    "Vacancy": {
        "added_at": "2025-11-18",
        "current_ranked_status": "active",
        "layout": {
            "size": "medium",
            "symmetry": "asymmetric",
            "lanes": 3,
            "verticality": "medium",
            "long_sightlines": "medium",
        },
        "items": {
            "power_weapons": ["shock"],
            "powerups": [],
            "equipment": [],
        },
        "notes": (
            "地下と地上の二層構造。地下はマップ中央に位置し各所へアクセスしやすい。"
            "地上部は3レーン構造。地下を通った裏取りが起きやすい。"
            "ショックライフルはAPIでPWキルとしてカウントされない点に注意。"
        ),
    },
}