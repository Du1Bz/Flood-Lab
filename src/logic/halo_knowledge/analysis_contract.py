"""
halo_knowledge/analysis_contract.py
-------------------------------------
AIが破ってはいけない制約（絶対ルール）。

推奨手順（SUGGESTED_PROMPT）とは分離する。
"""

from __future__ import annotations
from typing import Any

ANALYSIS_CONTRACT: dict[str, Any] = {
    "do_not_infer": [
        "心理状態",
        "VCの有無",
        "正確な位置取り",
        "味方の意図",
        "敵の意図",
    ],
    "claim_rules": {
        "min_games_for_hint":         3,
        "min_games_for_claim":        5,
        "min_games_for_strong_claim": 10,
    },
    "coaching_style": [
        "根拠指標を必ず添える",
        "改善提案は最大3つ",
        "断定できないものは仮説として書く",
        "ルール別・マップ別・共通習慣に分けて考える",
        "ユーザー向けの出力は日本語で書く",
    ],
}
