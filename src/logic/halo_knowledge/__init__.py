"""
halo_knowledge/__init__.py
---------------------------
halo_knowledge パッケージの公開インターフェース。

外部からは以下をインポートして使う:

    from src.logic.halo_knowledge import (
        build_game_context,
        build_relevant_context,
        ANALYSIS_CONTRACT,
        METRIC_LIMITATIONS,
    )

build_game_context()      : 全コンテキストをまとめた dict を返す（フィルタなし）
build_relevant_context()  : stat_df に登場するマップ/ルールだけに絞った dict を返す（B-4）
"""

from __future__ import annotations
from typing import Any

import pandas as pd

from .analysis_contract  import ANALYSIS_CONTRACT
from .metric_limitations import METRIC_LIMITATIONS
from .maps               import MAPS
from .modes              import GAME_BASE, RULE_THEORY
from .equipment          import EQUIPMENT, POWER_ITEMS
from .ranked_rotations   import RANKED_ROTATIONS


def build_game_context() -> dict[str, Any]:
    """全コンテキストをまとめた dict を返す（フィルタなし）。"""
    return {
        **GAME_BASE,
        "rule_theory":       RULE_THEORY,
        "maps":              MAPS,
        "equipment":         EQUIPMENT,
        "power_items":       POWER_ITEMS,
        "ranked_rotations":  RANKED_ROTATIONS,
    }


def build_relevant_context(stat_df: pd.DataFrame) -> dict[str, Any]:
    """
    B-4. 対象データ用の文脈抽出。

    stat_df に登場するマップ名・ルール名だけを絞り込んで返す。
    AIに渡すコンテキストのサイズを削減し、関係ない情報でノイズを増やさない。

    Parameters
    ----------
    stat_df : pd.DataFrame
        exporter.py で exclude_flag 処理済みの DataFrame。
        map_name / rule_name カラムを持つことを前提とする。

    Returns
    -------
    dict
        relevant_maps / relevant_rules / equipment / power_items /
        ranked_rotations / game_base を含む絞り込み済みコンテキスト。
    """
    # 対象データに登場するマップ・ルールを抽出
    active_maps: set[str] = set()
    active_rules: set[str] = set()

    if "map_name" in stat_df.columns:
        active_maps  = set(stat_df["map_name"].dropna().unique())
    if "rule_name" in stat_df.columns:
        active_rules = set(stat_df["rule_name"].dropna().unique())

    # マップコンテキストを絞り込む
    relevant_maps: dict[str, Any] = {
        name: data
        for name, data in MAPS.items()
        if name in active_maps
    }

    # ルールセオリーを絞り込む
    # rule_nameとRULE_THEORYキーのマッピング（大文字/スペース違いを吸収）
    _rule_key_map: dict[str, str] = {
        "slayer":      "slayer",
        "ctf":         "ctf",
        "koth":        "koth",
        "oddball":     "oddball",
        "strongholds": "strongholds",
    }
    relevant_rules: dict[str, Any] = {}
    for rule in active_rules:
        key = _rule_key_map.get(rule.lower())
        if key and key in RULE_THEORY:
            relevant_rules[rule] = RULE_THEORY[key]
    # common_frame は常に含める
    relevant_rules["common_frame"] = RULE_THEORY["common_frame"]

    # パワーアイテムは登場マップに絞る
    # マップの items.powerups に含まれるもののみ渡す
    active_powerups: set[str] = set()
    for map_data in relevant_maps.values():
        for pu in map_data.get("items", {}).get("powerups", []):
            # powerups の値（"camo", "overshield"）を POWER_ITEMS のキーに変換
            _pu_map = {
                "camo":        "Active Camouflage",
                "overshield":  "Overshield",
            }
            pi_key = _pu_map.get(pu)
            if pi_key:
                active_powerups.add(pi_key)

    relevant_power_items: dict[str, Any] = {
        k: v for k, v in POWER_ITEMS.items() if k in active_powerups
    }

    return {
        "game_base":         GAME_BASE,
        "relevant_maps":     relevant_maps,
        "relevant_rules":    relevant_rules,
        "equipment":         EQUIPMENT,
        "power_items":       relevant_power_items,
        "ranked_rotations":  RANKED_ROTATIONS,
    }


__all__ = [
    "ANALYSIS_CONTRACT",
    "METRIC_LIMITATIONS",
    "build_game_context",
    "build_relevant_context",
]
