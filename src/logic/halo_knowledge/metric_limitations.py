"""
halo_knowledge/metric_limitations.py
--------------------------------------
指標の既知の限界。

AIが断定を避けるべき制約を列挙する。
analysis_contract の claim_rules と合わせて参照する。
"""

from __future__ import annotations
from typing import Any

METRIC_LIMITATIONS: dict[str, Any] = {
    "pw_control_rate": (
        "Shock Rifle によるキルは PowerWeaponKills に反映されない可能性があり、"
        "pw_control_rate は過小評価になる（スナイパー・ロケット系のみ反映）。"
    ),
    "equipment": (
        "装備（Repulsor・Thruster 等）の取得/使用ログがないため、"
        "装備の使い方は直接評価できない。"
    ),
    "positioning": (
        "位置情報がないため、アンカー・スポーン制御・射線管理は"
        "代理指標でしか見られない。"
    ),
    "communication": (
        "VC や味方とのコミュニケーションは観測できない。"
    ),
    "objective_detail": (
        "旗ルート・ボール投棄・ヒル周辺ポジションなどの細かい判断は"
        "直接観測できない。"
    ),
    "small_sample": (
        "サンプル数が少ないマップ/ルール組み合わせは断定しない。"
        "claim_rules の閾値を参照すること。"
    ),
    "zone_kills_scope": (
        "zone_def_kills / zone_off_kills はエリア周辺での判定であり、"
        "移動経路上の遠距離キルは含まれないため過小評価になりうる。"
    ),
}
