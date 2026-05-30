"""
halo_knowledge/equipment.py
----------------------------
装備/アビリティ と パワーアイテムのコーチング用コンテキスト。

data_limit: 取得・使用ログがないため直接評価は不可。
coaching_use はあくまでコーチング上の参考として渡す。
"""

from __future__ import annotations
from typing import Any

EQUIPMENT: dict[str, Any] = {
    "Repulsor": {
        "label_ja": "リパルサー",
        "type": "defensive_utility",
        "type_label_ja": "防御/拒否系ユーティリティ",
        "coaching_use": [
            "グレネード・ロケット・近接を拒否する",
            "狭所の押し返しに使う",
            "ジャンプや位置取りの補助にもなる",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
    "Thruster": {
        "label_ja": "スラスター",
        "type": "duel_escape",
        "type_label_ja": "撃ち合い補助/離脱",
        "coaching_use": [
            "先撃ちされた時の離脱",
            "角待ちや射線切り",
            "短時間のピーク変更",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
    "Threat Seeker": {
        "label_ja": "スレットシーカー",
        "type": "information",
        "type_label_ja": "索敵/情報取得",
        "coaching_use": [
            "セットアップ崩し",
            "OddballやStrongholdsの敵位置確認",
            "味方プッシュ前の情報取り",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
    "Threat Sensor": {
        "label_ja": "スレットセンサー",
        "type": "information",
        "type_label_ja": "索敵/情報取得",
        "coaching_use": [
            "旗/ボール/ヒル周辺の敵位置を継続的に把握する",
            "狭所の入口に置いてアプローチを検知する",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
    "Drop Wall": {
        "label_ja": "ドロップウォール",
        "type": "defensive_cover",
        "type_label_ja": "防御/遮蔽",
        "coaching_use": [
            "開けた場所での一時的な遮蔽",
            "旗/ボールキャリアの護衛",
            "不利な射線を切るための時間稼ぎ",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
    "Shroud Screen": {
        "label_ja": "シュラウドスクリーン",
        "type": "concealment",
        "type_label_ja": "視界遮断",
        "coaching_use": [
            "スナイパーやロングレンジの射線を切る",
            "撤退・位置変更の煙幕として使う",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
    "Grappleshot": {
        "label_ja": "グラップルショット",
        "type": "mobility",
        "type_label_ja": "機動力",
        "coaching_use": [
            "高台や遮蔽物への素早いアクセス",
            "敵への近接起動",
            "離脱・位置転換",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
}

POWER_ITEMS: dict[str, Any] = {
    "Active Camouflage": {
        "label_ja": "アクティブカモフラージュ（Camo）",
        "type": "powerup",
        "type_label_ja": "パワーアップ",
        "coaching_use": [
            "接近・旗奪取・ボール奪取の起点として使う",
            "敵の視界を外して位置リセットする",
            "ショットを撃つと効果が弱まる点に注意",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
    "Overshield": {
        "label_ja": "オーバーシールド",
        "type": "powerup",
        "type_label_ja": "パワーアップ",
        "coaching_use": [
            "正面突破や旗キャリーの護衛に使う",
            "ヒル/拠点の維持コストを下げる",
            "取得タイミングが重要（敵に取られると大きく不利）",
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可。",
    },
}
