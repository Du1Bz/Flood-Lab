"""
halo_knowledge/roles.py
------------------------
E-1. ROLES: ロール/役割コンテキスト。

Halo Infiniteには固定職業ロールはない。
「この期間のデータから見た傾向」として扱う。
AIは断定せず、caution を必ず参照すること。
"""

from __future__ import annotations
from typing import Any

ROLES: dict[str, Any] = {
    "caution": (
        "ロールは固定職ではなく、この期間のデータから見た傾向。"
        "チーム構成・味方の役割・VC・位置情報は観測できないため、"
        "傾向として提示し断定しないこと。"
    ),

    "slayer": {
        "label_ja": "スレイヤー寄り",
        "description_ja": "キルを取り人数有利を作る役割",
        "positive_signals": [
            "k_rpi_mean >= 1.0",
            "kpm 上位（同ルール内比較）",
            "damage_dealt_per_min 高",
            "impact_score 高",
        ],
        "risk_signals": [
            "d_rpi_mean < 1.0（デスも多い）",
            "engagement_density 高 かつ d_rpi 低（無理な交戦継続）",
        ],
        "coaching_notes": [
            "キルを取りに行く役割ほど、デスで敵に点やスペースを渡すリスクも高い。",
            "キル数だけでなく、交換の質と生存も評価する。",
            "k_rpi 高 かつ d_rpi 低の場合は ego_challenge_risk が高い可能性がある。",
        ],
        # E-5: coaching_hints（role_profileのprimary_tendencyがslayerの場合に参照）
        "coaching_hints": [
            "撃ち負けた交戦の再チャレンジを減らすだけで d_rpi が改善しやすい。",
            "味方が削っている敵にダメージを合わせる（チームショット）意識を持つと impact_score が安定する。",
            "リードしている試合の後半は無理なキル狙いよりポジション維持を優先する。",
        ],
    },

    "support": {
        "label_ja": "サポート寄り",
        "description_ja": "味方の撃ち合いを補助し、ダメージとアシストで盤面を作る役割",
        "positive_signals": [
            "assist_ratio 高（assists / (kills + assists)）",
            "damage_dealt_per_min 高",
            "d_rpi 安定（1.0前後）",
        ],
        "risk_signals": [
            "k_rpi 低 かつ engagement_density 低（消極性の可能性）",
            "damage_dealt_per_min 低 かつ d_rpi 高（守りすぎ）",
        ],
        "coaching_notes": [
            "サポート寄りでもダメージ圧が低い場合は単なる消極性の可能性がある。",
            "アシストと与ダメージが高い場合、K/Dだけで低評価しない。",
        ],
        "coaching_hints": [
            "assist_ratio が高く damage_dealt_per_min も高ければサポートとして機能している。",
            "engagement_density が低い場合は前線への関与タイミングを早める。",
            "damage_dealt_per_min が低い場合はダメージを出す距離・角度の見直しを検討する。",
        ],
    },

    "objective_player": {
        "label_ja": "オブジェクト役寄り",
        "description_ja": "旗・ボール・ヒル・拠点など目標に直接絡む役割",
        "positive_signals": [
            "ルール別オブジェクトスタッツ 高（flag_grabs / zone_occupation_sec / oddball_skull_time_sec等）",
            "engagement_density 高（目標周辺での交戦が多い）",
        ],
        "risk_signals": [
            "k_rpi 低（オブジェクト負荷でキルが少ない場合は自然）",
            "objective スタッツ 高 かつ win_rate 低（目標に絡めているが得点変換できていない）",
        ],
        "coaching_notes": [
            "オブジェクト役はK-RPIやK/Dが低く出ることがある。ルール別スタッツとセットで評価する。",
            "オブジェクト関与が得点や勝率に変換されているかを確認する。",
        ],
        "coaching_hints": [
            "flag_grabs 高 かつ flag_captures 低の場合はウェーブを合わせてから旗を抜く意識を持つ。",
            "zone_occupation_sec 高 かつ win_rate 低の場合は周辺制圧が先に必要な可能性がある。",
            "オブジェクト負荷が高い場合、命の重さ（リスポーン10秒＋移動時間）を意識して生存を優先する局面を判断する。",
        ],
    },

    "anchor": {
        "label_ja": "アンカー寄り",
        "description_ja": "味方のスポーンや有利エリアを安定させる役割",
        "positive_signals": [
            "d_rpi 高（生存力が高い）",
            "deaths 少ない",
            "damage_diff 安定（プラス維持）",
        ],
        "risk_signals": [
            "engagement_density 低 かつ damage_dealt_per_min 低（低デスが消極性の可能性）",
        ],
        "limitations": [
            "位置情報がないため直接推定は難しい。",
            "スポーン制御は代理指標でしか見られない。",
        ],
        "coaching_notes": [
            "生存が高くても、味方の湧きやエリア維持に貢献しているかは直接見えない。",
            "低デスと低関与（消極性）を混同しない。",
        ],
        "coaching_hints": [
            "d_rpi 高 かつ engagement_density も高い場合は真のアンカー機能を果たしている可能性が高い。",
            "d_rpi 高 かつ engagement_density 低の場合は前線への関与を増やすことで impact_score が改善しやすい。",
            "damage_diff がマイナスの試合が多い場合は有利ポジションからの撃ち合いを意識する。",
        ],
    },

    "entry": {
        "label_ja": "エントリー寄り",
        "description_ja": "最初に接触して敵の位置を割り、味方が詰めるきっかけを作る役割",
        "positive_signals": [
            "engagement_density 高",
            "damage_taken_per_min 高（先に当たっている）",
            "assist_ratio 中程度（起点作りが味方のキルに繋がっている）",
        ],
        "risk_signals": [
            "d_rpi 低 かつ k_rpi 低（無謀な突入になっている可能性）",
            "damage_taken_per_min 高 かつ damage_diff マイナス（打開できていない）",
        ],
        "limitations": [
            "最初の接敵タイミングはDBから直接見えない。",
        ],
        "coaching_notes": [
            "エントリー傾向は有効な起点作りと無謀な突入の区別が重要。",
            "高い被ダメージが味方のキルに繋がっているかを見る。",
        ],
        "coaching_hints": [
            "damage_taken_per_min 高 かつ assists 高なら起点作りとして機能している。",
            "damage_taken_per_min 高 かつ d_rpi 低の場合は先撃ちされた交戦の継続をやめる意識を持つ。",
            "engagement_density 高 かつ impact_score 低の場合は交戦の質（タイミング・人数状況）を見直す。",
        ],
    },

    "power_item_controller": {
        "label_ja": "パワーアイテム管理寄り",
        "description_ja": "パワーウェポン/パワーアップ周辺の管理・取得・活用を担う役割",
        "positive_signals": [
            "pw_control_rate 高（0.6以上）",
            "pw_control_win_corr 高（PW確保と勝率の相関が強い）",
        ],
        "risk_signals": [
            "pw_control_rate 低（マップにPWがある場合）",
        ],
        "limitations": [
            "ショックライフルはPowerWeaponKillsに反映されないため pw_control_rate は過小評価になる。",
            "Camo / Overshield の取得・活用は直接見えない。",
        ],
        "coaching_notes": [
            "PWが強いマップとPWが薄いマップを同列に評価しない。",
            "PWキルだけでなく、PWを取らせない動きも重要だが直接観測しづらい。",
        ],
        "coaching_hints": [
            "pw_control_rate が低く pw_control_win_corr が高いマップでは、PW確保の優先度を上げる。",
            "PWスポーンは時間固定のため、スポーン20秒前からポジションを寄せる習慣を持つ。",
            "ショックライフル運用マップでは pw_control_rate の低さは仕様上の過小評価として扱う。",
        ],
    },
}
