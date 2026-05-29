"""
halo_knowledge/community_heuristics.py
----------------------------------------
C-3. コミュニティ由来の仮説。

Reddit / CompetitiveHalo 系の改善スレで繰り返し出てくる考え方。
公式情報ではないため confidence = "community_heuristic" として扱う。
AIは断定ではなく「コミュニティで言われている傾向」として提示する。
"""

from __future__ import annotations
from typing import Any

COMMUNITY_HEURISTICS: dict[str, Any] = {
    "label_ja": "コミュニティ由来の仮説",
    "caution": (
        "以下はコミュニティ（Reddit等）由来の仮説であり、公式情報ではない。"
        "AIはこれらを断定せず、データシグナルと照合したうえで提示すること。"
    ),

    # ---- ソロキュー全般 ----------------------------------------
    "solo_queue": [
        {
            "name": "support_when_struggling",
            "label_ja": "撃ち負けが続く時はサポート優先",
            "idea": (
                "撃ち負けが続く時は単独キル狙いより"
                "味方の後ろからダメージとカバーを優先する方が勝率に繋がりやすい。"
            ),
            "data_signals": ["low_k_rpi", "high_deaths", "low_d_rpi"],
            "counter_evidence": ["assists high", "damage_dealt_per_min high"],
            "confidence": "community_heuristic",
            "sources": ["https://www.reddit.com/r/CompetitiveHalo/comments/rzq9zo"],
        },
        {
            "name": "avoid_ego_challenge",
            "label_ja": "先撃ちされた撃ち合いを継続しすぎない",
            "idea": (
                "先撃ちされた撃ち合いを継続しすぎると"
                "デス効率が悪化しチームの人数不利が続く。"
                "シールドが割れた段階で離脱して回復を優先する。"
            ),
            "data_signals": ["high_damage_taken_per_min", "low_d_rpi", "high_dpm"],
            "counter_evidence": ["k_rpi high", "damage_diff positive"],
            "confidence": "community_heuristic",
            "sources": ["https://www.reddit.com/r/CompetitiveHalo/comments/r9x927"],
        },
        {
            "name": "team_shot_over_solo_kill",
            "label_ja": "単独キルよりチームショットを優先",
            "idea": (
                "単独でキルを狙うより、味方が撃っている敵に合わせてダメージを出す方が"
                "チームの有利状況を早く作れる。"
            ),
            "data_signals": ["low_tsi", "low_assist_ratio", "high_k_rpi"],
            "counter_evidence": ["high_impact_score", "win_rate high"],
            "confidence": "community_heuristic",
            "sources": ["https://www.reddit.com/r/CompetitiveHalo/comments/rjmk8b"],
        },
        {
            "name": "passivity_risk",
            "label_ja": "高生存・低関与は消極性のサイン",
            "idea": (
                "D-RPIが高くてもK-RPIとengagement_densityが低い場合、"
                "単なる消極性（戦闘回避）の可能性がある。"
                "サポート寄りと消極性を混同しないこと。"
            ),
            "data_signals": ["high_d_rpi", "low_k_rpi", "low_engagement_density", "low_damage_dealt_per_min"],
            "counter_evidence": ["assists high", "obj_stats high"],
            "confidence": "community_heuristic",
            "sources": [],
        },
    ],

    # ---- マップコントロール ----------------------------------------
    "map_control": [
        {
            "name": "two_thirds_control",
            "label_ja": "マップの2/3支配",
            "idea": (
                "マップの約2/3を取り、敵スポーンを残り1/3に寄せる。"
                "スポーン位置を制限することで敵が有利ポジションに戻るコストが上がる。"
            ),
            "observable_proxy": ["pw_control_rate", "zone_occupation_sec", "zone_def_kills"],
            "confidence": "community_heuristic",
            "sources": ["https://www.reddit.com/r/CompetitiveHalo/comments/r9x927"],
        },
        {
            "name": "power_item_timing",
            "label_ja": "パワーアイテム20秒前からのポジショニング",
            "idea": (
                "パワーウェポン・パワーアップのスポーン20秒前から"
                "取得ポジションに寄り始めることで確保率が上がる。"
                "スポーン時刻は試合開始からの経過時間で固定。"
            ),
            "observable_proxy": ["pw_control_rate", "power_kills"],
            "confidence": "community_heuristic",
            "sources": [],
        },
    ],

    # ---- ルール別 ----------------------------------------
    "by_rule": {
        "strongholds": [
            {
                "name": "two_cap_over_three_cap",
                "label_ja": "Strongholds: 2点維持 > 3点取り",
                "idea": (
                    "3点目を取りに行くと敵が自陣ポイント目の前にスポーンする逆効果になりやすい。"
                    "2点を安定維持する方がスコア効率が高い。"
                    "3点目を狙うのは敵が全落ちかつ大きくビハインドの時などに限定する。"
                ),
                "data_signals": ["zone_captures high", "zone_off_kills high", "win_rate low"],
                "counter_evidence": ["zone_occupation_sec high", "team_score close"],
                "confidence": "community_heuristic",
                "sources": ["https://www.reddit.com/r/CompetitiveHalo/comments/1ix5nf5"],
            },
        ],
        "oddball": [
            {
                "name": "ob_over_holding",
                "label_ja": "Oddball: 不利時はOBが優先",
                "idea": (
                    "不利な状況（3v4・2v4など）ではボールをOBや開けた場所に投棄して"
                    "味方のスポーンを待って仕切り直す方が時間効率が良い。"
                    "OBの優先度: 持ち続ける→✕ / OBしてデス→△ / OBして生き残る→○ / OBして生き残りキルする→◎"
                ),
                "data_signals": ["oddball_skull_time_sec high", "deaths high", "oddball_skull_grabs low"],
                "counter_evidence": ["oddball_scoring_ticks high"],
                "confidence": "community_heuristic",
                "sources": [],
            },
            {
                "name": "carrier_outside_protection",
                "label_ja": "Oddball: キャリア密着より外側カバー",
                "idea": (
                    "ボールキャリアに密着するより、外側の射線でカバーする方が"
                    "護衛の効果が高い。密着は敵のグレネードや近接で2人まとめて落とされるリスクがある。"
                ),
                "data_signals": ["d_rpi high", "k_rpi low", "engagement_density low"],
                "counter_evidence": ["oddball_skulls_denied high"],
                "confidence": "community_heuristic",
                "sources": [],
            },
        ],
        "ctf": [
            {
                "name": "wave_before_pull",
                "label_ja": "CTF: ウェーブを合わせてから旗を抜く",
                "idea": (
                    "敵陣に旗を抜きに行く前に、まず敵のウェーブを倒して"
                    "リスポーン空白時間を作ることが帰還成功率を高める。"
                    "旗を抜いてから倒そうとすると護衛が間に合わない。"
                ),
                "data_signals": ["flag_grabs high", "flag_captures low", "flag_carrier_time_sec high"],
                "counter_evidence": ["flag_carriers_killed high"],
                "confidence": "community_heuristic",
                "sources": [],
            },
        ],
        "koth": [
            {
                "name": "clear_before_entering_hill",
                "label_ja": "KOTH: ヒルを踏む前に周辺をクリア",
                "idea": (
                    "ヒル内に入る前にヒル周辺の敵をクリアし、"
                    "戻りルートを遮断してからヒルを踏む。"
                    "クリアせずにヒルに入ると連続デスで時間を失う。"
                ),
                "data_signals": ["zone_occupation_sec low", "zone_def_kills high", "deaths high"],
                "counter_evidence": ["zone_scoring_ticks high"],
                "confidence": "community_heuristic",
                "sources": [],
            },
        ],
    },
}
