"""
logic/exporter.py
-----------------
AI相談用データエクスポート。

フィルター済みDataFrameを受け取り、
特徴量 + 集計サマリー + 生データ(直近20+ベスト/ワースト5) +
用語集 + ゲームコンテキスト + プロンプト雛形を
1つのJSONファイルとして出力する。
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd

from src.utils.display import PLAYLIST_DISPLAY, RESULT_DISPLAY

# ==================================================
# matchesに含めるカラム
# 生データは直近20試合 + ベスト/ワースト5試合に絞る
# ==================================================

EXPORT_COLUMNS = [
    "match_id", "played_at", "playlist", "map_name", "rule_name",
    "result", "kills", "deaths", "assists",
    "kd_ratio", "kda", "accuracy",
    "damage_dealt", "damage_taken", "damage_diff",
    "k_rpi", "d_rpi", "lgai", "impact_score",
    "csr_pre", "csr_post", "csr_delta",
    "pw_control_rate", "engagement_density",
    "emmr_v2", "party_type",
    "session_id", "session_seq",
]

# ==================================================
# ゲームコンテキスト（固定・バージョン管理）
# ==================================================

GAME_CONTEXT: dict[str, Any] = {
    "version": "2026-05",
    "game": "Halo Infinite - Ranked Arena",
    "loadout": "全プレイヤーBandit Evo統一スタート。初期武器の差はない。",
    "power_weapons": {
        "description": "マップ上に配置されるパワーウェポン（PW）の確保が勝敗を大きく左右する。",
        "types": ["スナイパーライフル", "ロケットランチャー", "ショックライフル"],
        "shock_rifle_note": (
            "ショックライフルは3発同時射出・全弾ヘッドショット判定で一撃キル可能だが癖が強く、"
            "スナイパー的な運用が多い。APIの仕様上、ショックライフルによるキルはPWキルとして"
            "カウントされないため、pw_control_rateはスナイパー・ロケット系のみを反映した"
            "過小評価になる点に注意。"
        ),
        "spawn_cycle": (
            "PWのスポーンは試合開始時刻からの経過時間で固定（例：2分毎・3分毎）。"
            "取得タイミングに関わらず一定間隔で出現するため、20秒前からのポジショニングが重要。"
        ),
    },
    "kd_baseline": (
        "K/D=1.0が理論的均衡点。ただしアシスト・オブジェクト貢献が勝敗に与える影響が大きく、"
        "K/D単体での評価には限界がある。"
    ),
    "party_note": (
        "ソロとパーティでは難易度が異なる。主な要因はコールアウト（味方への位置情報共有）"
        "による情報量の差。パーティにはMMRペナルティが課されるとも言われる。"
    ),
    "rule_theory": {
        "slayer": {
            "objective": "先に規定キル数に到達する。",
            "core": "味方を死なせないために守り合うゲーム。キルを取るゲームに見えるが、不利な交戦を断る判断の積み重ねが勝敗を分ける。",
            "keys": [
                "味方を助けるキルを優先（味方を助けるキルは2点分の価値）",
                "有利状況を作ってから撃ち合う（グレネードで削る・ハイグラウンド・2v1を作る）",
                "不利交戦を断る（負けたファイトの再チャレンジをしない・シールドが割れたら即離脱）",
                "スポーンと陣地をコントロールする（有利エリアで戦い続けたチームが勝つ）",
            ],
        },
        "koth": {
            "objective": "ヒル時間を独占する。",
            "core": "ヒルを踏むことより、敵が戻れない状態を作ることが核心。",
            "keys": [
                "ヒル近くにアンカーを取る（死んでも近くに沸ける状態を維持）",
                "ヒル周辺をクリアして敵を遠くに追い出す",
                "敵の戻りルートを遮断する（移動経路のオフアングルで待つ）",
                "上記が揃ってからヒルを踏む",
            ],
            "obj_stats": {
                "zone_occupation_sec": "ヒルを占領していた合計時間（秒）。味方と同時に占領していた時間も含まれる。",
                "zone_scoring_ticks":  "ヒルのスコアティック数。",
                "zone_def_kills":      "ヒル内・ヒル周辺での防御キル数。多くて負けている場合はプッシュ圧が足りない可能性がある。ただしエリアから遠い移動経路を叩く立ち回りはこの判定に含まれないため過小評価になりうる。",
                "zone_off_kills":      "ヒル内・ヒル周辺での攻撃キル数。多くて負けている場合は防衛ができていない可能性がある。ただしエリアから遠い移動経路を叩く立ち回りはこの判定に含まれないため過小評価になりうる。",
                "notes": "キル数とヒル関連キル数のバランスを見ると、ヒル内での戦闘が多いか、スポーンをコントロールして移動経路を攻撃しているかなどがわかる。",
            },
        },
        "ctf": {
            "objective": "旗を奪って帰還する／敵に帰還させない。",
            "core": "取るより帰す方が難しい。",
            "keys": [
                "ウェーブを合わせる（キャリーが旗を拾う前に帰り道をクリア）",
                "敵陣到達後にもう1ウェーブスレイし、リスポーン空白時間を作ってから旗を運ぶ",
                "帰り道の護衛（キャリーが動いている間は自分の位置を動線上に寄せる）",
                "自陣フラッグ管理（敵キャリーが動いたら自陣を意識）",
            ],
            "note": "敵陣でのスレイは旗の近く・帰り道の途中で取れていないと空白時間を使いきれない。",
            "obj_stats": {
                "flag_captures":         "旗のキャプチャ数。旗を最後までキャプチャした回数。",
                "flag_grabs":            "旗をグラブした回数。ドリブル技術（旗を持って前方に投げてスプリント）を使うと1キャプチャあたりのグラブ数が多くなる傾向がある。グラブ数が多いのにキャプチャ数が少ない場合、ドリブルで何度もトライしている場合のほか、スポーンを読めずルートを誤った場合や敵の抵抗で旗が入らなかった場合など複数の可能性がある。",
                "flag_returns":          "自陣の旗をリターンした回数。最後までリターンをした本人のみカウント。味方と同時でもカウントされる。",
                "flag_secures":          "旗の近くでキルをして旗をセキュアした回数。",
                "flag_steals":           "敵陣の旗をグラブした回数。キル数が少ない場合、無理に敵陣の旗をスティールしに行っている可能性がある。",
                "flag_carrier_time_sec": "旗を保持していた合計時間（秒）。ドリブルをしていると1キャプチャあたりの保持時間が短くなる傾向がある。",
                "flag_carriers_killed":  "敵の旗キャリアをキルした回数。敵がドリブル中で旗を持っていないタイミングのキルはカウントされない。",
                "notes": "生存時間が長いのに旗関連スタッツが少ない場合はプッシュが弱い可能性がある。生存時間が短いのに旗関連スタッツが多い場合は無理なスティールを繰り返している可能性がある。",
            },
        },
        "oddball": {
            "objective": "ボールを保持し続けて時間を稼ぐ。",
            "core": "ボールファーストで状況を確認してから動く。生存よりボール持ちを守るためのキルを優先する場面がある。",
            "keys": [
                "ボールの位置を常に把握する（試合中の判断の主語がボールになる）",
                "キャリーの外側から守る（密着ではなく外側に立つ）",
                "護衛を崩してボールを奪う（保持者より周囲の護衛を先に倒す）",
                "死んでも交換する判断を持つ（キャリーが削られているときに引いてはいけない場面がある）",
            ],
            "stat_note": "D-RPIが高くK-RPIが低い状態は守りすぎのサイン。",
            "obj_stats": {
                "oddball_skull_time_sec": "ボールを保持していた合計時間（秒）。保持時間が長いプレイヤーは射撃できないためキルが少なくなりがち。保持時間が長いのにグラブ数が少ない場合、不利な状況（3v4・2v4など）でもOB（アウトオブバウンズ）や開けた場所への投棄をせず持ち続けてしまっている可能性がある。",
                "oddball_scoring_ticks":  "ボールのスコアティック数。",
                "oddball_skull_grabs":    "ボールをグラブした回数。ドリブルをしていると多くなる傾向がある。",
                "oddball_carrier_kills":  "ボールを保持している間にキルした回数。ボールでの近接攻撃はフルシールド相手には2回必要で味方のアシストがないと難しく、アリーナではあまり発生しない。",
                "oddball_skulls_denied":  "敵のボールキャリアをキルした回数。",
                "notes": "ボール持ちのプレイヤーはスタッツが少なくなりがち。生存時間が短いプレイヤーは敵にボールを持たれているときにまっすぐボールに向かいすぎの可能性がある。不利な状況（3v4・2v4など）ではボールをOBや開けた場所に投棄して味方のスポーンを待って仕切り直すことが推奨される。OBの優先度の目安: 持ち続ける→✕ / OBしてデス→△ / OBして生き残る→○ / OBして生き残りキルする→◎。",
            },
        },
        "strongholds": {
            "objective": "3点のうち2点以上を継続保持する。",
            "core": "2点を安定させることが3点を取りに行くより強い。",
            "keys": [
                "2点キープを最優先（3点目を取りに行くと敵が自陣目の前にスポーンする逆効果）",
                "脅かされやすいポイント近くにアンカーを取る",
                "敵のポイント間移動を遮断する",
                "ポイントが取れているなら押さない（敵が来る場所で待って交換する）",
            ],
            "note": "3点目を狙うのは敵が全落ちかつ自分たちが有利ポジションにいるときだけ。",
            "obj_stats": {
                "zone_occupation_sec": "ポイントを占領していた合計時間（秒）。",
                "zone_scoring_ticks":  "ポイントのスコアティック数。",
                "zone_captures":       "ポイントキャプチャ数。最後までキャプチャした回数。味方と同時でもカウントされる。敵に2点・3点取られた場合のリテイク（奪還）も含まれるため、負けている状況でもカウントが増えることに留意。",
                "zone_def_kills":      "ポイント周辺での防御キル数。",
                "zone_off_kills":      "ポイント周辺での攻撃キル数。",
                "zone_secures":        "ポイントのセキュア数。敵がキャプチャしているポイントをリセットした回数。",
                "notes": "攻撃キルが多く防御キルが少ない場合、攻めすぎて敵が自分のポイントにスポーンしてしまっている可能性がある。ポイントキャプチャ数が多いのに負けている場合、取得したポイントを維持できていない可能性がある。ゾーン関連スタッツが低くてもチーム全体でローテーションできていれば問題ない。",
            },
        },
        "common_frame": {
            "description": "全ルール共通の動きのフレーム",
            "steps": [
                "① アンカーを取る（どこに沸くかをコントロール）",
                "② エリアをクリアする（敵を遠くに追い出す）",
                "③ 敵の戻りを遮断する（移動経路・オフアングル）",
                "④ 目標に絡む（最後）",
            ],
            "note": "目標に絡むのは常に最後。①②③が崩れた状態で無理に動くと被ダメが増える。",
        },
    },
    "maps": {
        "Aquarius": {
            "size": "large", "symmetry": "symmetric",
            "power_weapons": [], "pw_count": 0,
            "notes": "3レーン構造。マップ中央にカモフラージュが配置されている。ベースとベースの距離はBandit Evoではエイムアシストがかからないが、BRではかかる距離。初期から存在するマップ。",
        },
        "Empyrean": {
            "size": "large", "symmetry": "symmetric",
            "power_weapons": ["rocket", "sniper"], "pw_count": 3,
            "notes": "3レーン構造。マップ中央にロケットランチャー、両サイドのスナイパータワー1階にスナイパーライフルが配置されている。Halo 3のThe Pitのリメイクマップ。2022-12-06追加。",
        },
        "Fortress": {
            "size": "small", "symmetry": "symmetric",
            "power_weapons": ["sniper"], "pw_count": 2,
            "notes": "3レーン構造。マップ中央にオーバーシールド、両ベースにスナイパーライフルが配置されている。中央には太い塔があり、内側と外側に螺旋階段がある。2024-10-30追加。",
        },
        "Interference": {
            "size": "medium", "symmetry": "asymmetric",
            "power_weapons": ["sniper"], "pw_count": 1,
            "notes": "マップ中央にオーバーシールドが配置されている。遠距離での戦闘が発生しやすい。ランクアリーナには存在しない。Halo 5のThe Rigのリメイクマップ。2024-04-23追加。",
        },
        "Lattice": {
            "size": "large", "symmetry": "asymmetric",
            "power_weapons": ["sniper"], "pw_count": 1,
            "notes": "横方向の3レーン構造。中央レーンが開けていて低い。両サイドに建物内の2レーンがある。エリアを管理できていないとマップの横断がしづらい。2025-08-05追加。",
        },
        "Live Fire": {
            "size": "medium", "symmetry": "asymmetric",
            "power_weapons": ["sniper"], "pw_count": 1,
            "notes": "3レーン構造。開けたレーン、スナイパーライフルが配置されている狭いレーン、カモフラージュが配置されている開けたレーンがある。初期から存在するマップ。",
        },
        "Origin": {
            "size": "large", "symmetry": "symmetric",
            "power_weapons": ["sniper", "rocket"], "pw_count": 2,
            "notes": "3レーン構造。スナイパーライフルの配置された建造物に囲まれたレーン、中央の低いレーン、ロケットランチャーの配置された開けた高いレーンがある。Halo 5のColliseumのリメイクマップ。2025-02-04追加。",
        },
        "Recharge": {
            "size": "medium", "symmetry": "asymmetric",
            "power_weapons": ["shock"], "pw_count": 1,
            "notes": "2階建ての外周部に囲まれたマップ。中央部は開けており、低い場所にカモフラージュが配置されている。ショックライフルはAPIでPWキルとしてカウントされない点に注意。初期から存在するマップ。",
        },
        "Serenity": {
            "size": "medium", "symmetry": "symmetric",
            "power_weapons": ["sniper", "rocket"], "pw_count": 3,
            "notes": "3レーン構造。両ベースにスナイパーライフル、マップ中央にロケットランチャーが配置されている。中央は3階建てのリング構造。ランクアリーナには存在しない。Halo 2のSanctuaryのリメイクマップ。2025-08-05追加。",
        },
        "Solitude": {
            "size": "large", "symmetry": "asymmetric",
            "power_weapons": ["shock"], "pw_count": 1,
            "notes": "高低差が激しい。中央の開けた高台にカモフラージュが配置されている。外周部は建物で囲まれている。ショックライフルはAPIでPWキルとしてカウントされない点に注意。Halo 5のPlazaのリメイクマップ。2023-06-27追加。",
        },
        "Streets": {
            "size": "medium", "symmetry": "asymmetric",
            "power_weapons": [], "pw_count": 0,
            "notes": "3レーン構造。レーン間が狭く隣のレーンに移動しやすい。入り組んでおり近距離での戦闘が発生しやすい。中央の開けた場所にカモフラージュが配置されている。2021-12-08追加。",
        },
        "Vacancy": {
            "size": "medium", "symmetry": "asymmetric",
            "power_weapons": ["shock"], "pw_count": 1,
            "notes": "地下と地上の二層構造。地下はマップ中央に位置し各所へアクセスしやすい。地上部は3レーン構造。地下を通った裏取りが起きやすい。ショックライフルはAPIでPWキルとしてカウントされない点に注意。2025-11-18追加。",
        },
    },
}

# ==================================================
# 用語集
# ==================================================

GLOSSARY: dict[str, str] = {
    "kd_ratio":           "K/D。キル数 / デス数。デス=0のときはキル数をそのまま使う",
    "kda":                "キル - デス + アシスト/3。試合の総合貢献度",
    "accuracy":           "命中率。命中数 / 発射数（0〜1の小数）",
    "damage_diff":        "与ダメージ - 被ダメージ。プラスが望ましい",
    "k_rpi":              "K-RPI（キル相対パフォーマンス指数）。TrueSkill2が予測した期待キル数に対する実績比率。1.0=期待通り、>1.0=期待超え、<1.0=期待以下",
    "d_rpi":              "D-RPI（デス相対パフォーマンス指数）。TrueSkill2が予測した期待デス数に対して実際に少なく死んだ比率。>1.0=期待より死ななかった（生存力が高い）",
    "lgai":               "LGAI（ロビー格差補正インパクト）。敵チームMMR - 自チームCSR。正=格上相手、負=格下相手",
    "impact_score":       "インパクトスコア。(K-RPI + D-RPI) / 2。TrueSkill2基準の総合パフォーマンス指標。1.0=平均",
    "emmr_v2":            "eMMR v2（推定MMR）。カルマンフィルタで平滑化した独自推定MMR。ノイズを除いたスキルトレンドを表す",
    "csr_delta":          "CSR増減。1試合でのCSR変動量",
    "party_type":         "パーティタイプ。ソロ/デュオ/トリオ/フルパ",
    "session_seq":        "セッション内試合番号。同一セッション（2時間以内の連続プレイ）内での何試合目か",
    "pw_control_rate":    "PWコントロール率。自チームPWキル / (自チーム + 敵チームPWキル)。0.5が均衡。ショックライフルが未計上のため過小評価になる点に注意",
    "engagement_density": "(キル + デス + アシスト) / 試合時間(分)。試合への関与の濃さ。ルール間比較に有用",
    "tsi":                "TSI（チームシュート依存度）。アシスト / (キル + アシスト)。高いほど連携キルが多い",
    "dtr":                "DTR（ダメージトレード比）。与ダメージ / 被ダメージ。1.0が均衡。差分より比率なのでルール間比較に強い",
    "dpm":                "DPM（分間ダメージ）。与ダメージ / 試合時間(分)。キルに繋がらなくとも前線への圧力を測る",
    "survival_index":     "生存指数（推定）。試合時間(秒) / (デス + 1)。1デスあたりの平均生存時間の近似",
    "k_rpi_std":          "K-RPIの標準偏差。小さいほど安定したキル貢献、大きいほど試合ごとの波がある",
}

# ==================================================
# プロンプト雛形
# ==================================================

SUGGESTED_PROMPT = """\
このデータはHalo Infinite専用のローカル分析ツール「Flood-Lab」によって生成されたエクスポートファイルです。

あなたはHalo Infinite HCSの真剣なデータアナリストです。
以下のデータを分析し、このプレイヤーへのコーチングフィードバックを行ってください。

データ構成:
- game_context: ゲームルールと各ルールの競技セオリー（分析の文脈として参照してください）
- glossary: 各指標の定義
- summary: 集計済みサマリー（全体・マップ別・ルール別・パーティ別・セッション疲労・直近20試合）
- features: 事前に計算した特徴量（プレイスタイル・傾向の要約）
- matches.recent_20: 直近20試合の生データ
- matches.best_5 / worst_5: KDA上位・下位5試合

以下の構成を参考に分析してください。
各セクションの中身はあなたの判断で自由に構成してください。

① 総合評価
   期間・試合数・全体的な立ち位置を簡潔に。

② プレイスタイル診断
   ヒント: TSI・K-RPI・D-RPIからプレイスタイルの傾向を読み取ることができます。
   ヒント: パーフェクト率・DTR・DPMから精度と前線への圧力を評価できます。

③ ルール別適性分析
   ヒント: game_contextのrule_theoryのセオリーと照らし合わせることで、
   何ができていて何が足りないかを評価できます。
   ヒント: Oddballではd_rpiが高くk_rpiが低い場合に守りすぎのサインが読み取れることがあります。

④ マップ適性
   得意マップ・苦手マップの特定と、その推定理由。

⑤ パワーウェポンコントロール
   ヒント: pw_control_rateとpw_control_win_corrから傾向を読み取ることができます。
   ただしgame_contextのshock_rifle_noteにある通り、過小評価になる点を前置きしてください。

⑥ セッション・コンディション傾向
   ヒント: session_fatigueとソロ/パーティの勝率差から傾向を読み取ることができます。

⑦ 優先改善ポイント（最大3つ）
   「〇〇という状況で△△を試してください」レベルまで具体的に。
   game_contextのセオリーと数値の両方を根拠にしてください。

⑧ データから見えた意外な知見（自由記述）
   枠組みの外で気づいたこと・仮説があれば追記してください。

注意:
- 数値の引用はsummaryとfeaturesを主に使い、matchesは補足的に参照してください
- 根拠のない一般論は避け、データに基づいて述べてください
- 改善ポイントは「試合に勝つために何をすればよいか」に直結させてください
- 数値から行動や意図を読み取るには限界があります。分析結果はあくまで参考として、複数の可能性を検討しながら解釈してください\
"""

# ==================================================
# 集計サマリーの生成
# ==================================================

def _safe_round(val: Any, decimals: int = 3) -> Any:
    """NaN / inf を None に変換して丸める。"""
    if val is None:
        return None
    try:
        f = float(val)
        if not np.isfinite(f):
            return None
        return round(f, decimals)
    except (TypeError, ValueError):
        return None


def _agg_group(df: pd.DataFrame) -> dict[str, Any]:
    """DataFrameの集計サマリーを返す。"""
    n = len(df)
    if n == 0:
        return {}

    kills   = df["kills"].sum()
    deaths  = df["deaths"].sum()
    assists = df["assists"].sum()

    return {
        "matches":            n,
        "win_rate":           _safe_round(df["result_flag"].mean(), 3),
        "kd_ratio":           _safe_round(kills / deaths if deaths > 0 else kills, 2),
        "kda_mean":           _safe_round(df["kda"].mean(), 2),
        "accuracy_mean":      _safe_round(
            df["shots_hit"].sum() / df["shots_fired"].sum()
            if "shots_fired" in df.columns and df["shots_fired"].sum() > 0
            else df["accuracy"].mean(), 3
        ),
        "damage_diff_mean":   _safe_round(df["damage_diff"].mean(), 0),
        "k_rpi_mean":         _safe_round(df["k_rpi"].mean(), 3),
        "d_rpi_mean":         _safe_round(df["d_rpi"].mean(), 3),
        "impact_mean":        _safe_round(df["impact_score"].mean(), 3),
        "csr_delta_sum":      _safe_round(df["csr_delta"].sum(), 0),
        "pw_control_rate_mean": _safe_round(df["pw_control_rate"].mean(), 3)
            if "pw_control_rate" in df.columns else None,
        "engagement_density_mean": _safe_round(df["engagement_density"].mean(), 2)
            if "engagement_density" in df.columns else None,
    }


def _build_features(df: pd.DataFrame) -> dict[str, Any]:
    """
    AIに渡す事前計算済み特徴量。
    生データを渡す代わりにここで要約する。
    """
    if df.empty:
        return {}

    kills   = df["kills"]
    deaths  = df["deaths"]
    assists = df["assists"]

    # TSI（チームシュート依存度）
    total_ka = kills.sum() + assists.sum()
    tsi = _safe_round(assists.sum() / total_ka if total_ka > 0 else None, 3)

    # DTR（ダメージトレード比）
    dtr = _safe_round(
        df["damage_dealt"].sum() / df["damage_taken"].sum()
        if df["damage_taken"].sum() > 0 else None, 3
    )

    # DPM（分間ダメージ）
    dpm = _safe_round(df["damage_dealt_per_min"].mean(), 1) \
        if "damage_dealt_per_min" in df.columns else None

    # 生存指数（試合時間 / (デス+1) の平均）
    survival_index = _safe_round(
        (df["duration_sec"] / (deaths + 1)).mean(), 1
    ) if "duration_sec" in df.columns else None

    # K-RPI標準偏差（安定性）
    k_rpi_std = _safe_round(df["k_rpi"].std(), 3)

    # パーフェクト率
    perfect_rate_mean = _safe_round(df["perfect_rate"].mean(), 3) \
        if "perfect_rate" in df.columns else None

    # ルール別エンゲージメント密度
    eng_by_rule: dict[str, Any] = {}
    if "engagement_density" in df.columns:
        for rule, grp in df.groupby("rule_name"):
            eng_by_rule[str(rule)] = _safe_round(grp["engagement_density"].mean(), 2)

    # ソロ vs パーティ 勝率差
    solo_wr = party_wr = None
    if "is_solo" in df.columns:
        solo_df  = df[df["is_solo"] == True]
        party_df = df[df["is_solo"] == False]
        if len(solo_df) >= 3:
            solo_wr  = _safe_round(solo_df["result_flag"].mean(), 3)
        if len(party_df) >= 3:
            party_wr = _safe_round(party_df["result_flag"].mean(), 3)

    # PWコントロール率と勝敗の相関
    pw_win_corr = None
    if "pw_control_rate" in df.columns:
        pw_valid = df.dropna(subset=["pw_control_rate"])
        if len(pw_valid) >= 5:
            pw_win_corr = _safe_round(
                pw_valid["pw_control_rate"].corr(pw_valid["result_flag"]), 3
            )

    # K-RPI/D-RPIのスタイル分類
    k_rpi_mean = df["k_rpi"].mean()
    d_rpi_mean = df["d_rpi"].mean()
    if pd.notna(k_rpi_mean) and pd.notna(d_rpi_mean):
        if k_rpi_mean >= 1.0 and d_rpi_mean >= 1.0:
            style = "balanced_aggressive（キル・生存ともに期待以上）"
        elif k_rpi_mean >= 1.0 and d_rpi_mean < 1.0:
            style = "aggressive（キルは取れるが死も多い）"
        elif k_rpi_mean < 1.0 and d_rpi_mean >= 1.0:
            style = "survival_focused（生存重視だがキルが少ない。Oddballでは守りすぎの可能性）"
        else:
            style = "underperforming（キル・生存ともに期待以下）"
    else:
        style = None

    # 勝敗別比較
    WIN_LOSS_COLS = [
        "kda", "accuracy", "damage_diff", "k_rpi", "d_rpi",
        "pw_control_rate", "engagement_density", "tsi_per_match",
    ]
    win_df  = df[df["result_flag"] == 1]
    loss_df = df[df["result_flag"] == 0]

    # TSIは試合単位で計算
    def _tsi_mean(sub: pd.DataFrame) -> float | None:
        k = sub["kills"].sum(); a = sub["assists"].sum()
        return _safe_round(a / (k + a), 3) if (k + a) > 0 else None

    win_loss_cmp: dict[str, Any] = {}
    compare_cols = [
        ("kda",               "KDA"),
        ("accuracy",          "命中率"),
        ("damage_diff",       "ダメージ差"),
        ("k_rpi",             "K-RPI"),
        ("d_rpi",             "D-RPI"),
        ("pw_control_rate",   "PWコントロール率（ショックライフル未計上）"),
        ("engagement_density","エンゲージメント密度"),
    ]
    for col, label in compare_cols:
        if col not in df.columns:
            continue
        w = _safe_round(win_df[col].mean(),  3) if len(win_df)  > 0 else None
        l = _safe_round(loss_df[col].mean(), 3) if len(loss_df) > 0 else None
        d = _safe_round(w - l, 3) if (w is not None and l is not None) else None
        win_loss_cmp[col] = {"label": label, "win": w, "loss": l, "diff": d}

    # TSIは別途計算
    win_loss_cmp["tsi"] = {
        "label": "チームシュート依存度（TSI）",
        "win":  _tsi_mean(win_df),
        "loss": _tsi_mean(loss_df),
        "diff": _safe_round(
            (_tsi_mean(win_df) or 0) - (_tsi_mean(loss_df) or 0), 3
        ) if (_tsi_mean(win_df) is not None and _tsi_mean(loss_df) is not None) else None,
    }

    # ルール別オブジェクトスタッツの勝敗比較
    OBJ_FEATURE_COLS: dict[str, list[str]] = {
        "CTF":         ["flag_captures", "flag_grabs", "flag_carrier_time_sec", "flag_carriers_killed"],
        "Oddball":     ["oddball_skull_time_sec", "oddball_skull_grabs", "oddball_skulls_denied"],
        "KOTH":        ["zone_occupation_sec", "zone_def_kills", "zone_off_kills"],
        "Strongholds": ["zone_occupation_sec", "zone_captures", "zone_secures",
                        "zone_def_kills", "zone_off_kills"],
    }
    obj_by_rule: dict[str, Any] = {}
    for rule_key, cols in OBJ_FEATURE_COLS.items():
        grp = df[df["rule_name"] == rule_key]
        if len(grp) < 3:
            continue
        obj_entry: dict[str, Any] = {"matches": len(grp)}
        for col in cols:
            if col in grp.columns and grp[col].notna().any():
                obj_entry[col + "_mean"] = _safe_round(grp[col].mean(), 2)
        obj_by_rule[rule_key] = obj_entry

    return {
        "tsi":                  tsi,
        "dtr":                  dtr,
        "dpm":                  dpm,
        "survival_index_sec":   survival_index,
        "k_rpi_std":            k_rpi_std,
        "perfect_rate_mean":    perfect_rate_mean,
        "style_classification": style,
        "solo_win_rate":        solo_wr,
        "party_win_rate":       party_wr,
        "pw_control_win_corr":  pw_win_corr,
        "engagement_by_rule":   eng_by_rule,
        "obj_stats_by_rule":    obj_by_rule,
    }


def _build_summary(df: pd.DataFrame) -> dict[str, Any]:
    """集計サマリー全体を構築する。"""
    summary: dict[str, Any] = {}

    summary["overall"]     = _agg_group(df)

    # 区分別
    summary["by_playlist"] = {}
    for pl, grp in df.groupby("playlist"):
        label = PLAYLIST_DISPLAY.get(str(pl), str(pl))
        summary["by_playlist"][label] = _agg_group(grp)

    # マップ別（5試合以上）
    summary["by_map"] = {}
    for map_name, grp in df.groupby("map_name"):
        if len(grp) < 5:
            continue
        summary["by_map"][str(map_name)] = _agg_group(grp)

    # ルール別（3試合以上）+ オブジェクトスタッツ
    OBJ_COLS: dict[str, list[str]] = {
        "Slayer":      [],
        "CTF":         ["flag_captures", "flag_grabs", "flag_returns", "flag_secures",
                        "flag_steals", "flag_carrier_time_sec", "flag_carriers_killed"],
        "Oddball":     ["oddball_skull_time_sec", "oddball_scoring_ticks",
                        "oddball_skull_grabs", "oddball_carrier_kills", "oddball_skulls_denied"],
        "KOTH":        ["zone_occupation_sec", "zone_scoring_ticks",
                        "zone_def_kills", "zone_off_kills"],
        "Strongholds": ["zone_occupation_sec", "zone_scoring_ticks", "zone_captures",
                        "zone_def_kills", "zone_off_kills", "zone_secures"],
    }

    summary["by_rule"] = {}
    for rule_name, grp in df.groupby("rule_name"):
        if len(grp) < 3:
            continue
        rule_data = _agg_group(grp)

        # ルール名を正規化してOBJ_COLSを引く
        rule_key = str(rule_name)
        obj_cols = OBJ_COLS.get(rule_key, [])
        if obj_cols:
            obj_agg: dict[str, Any] = {}
            for col in obj_cols:
                if col in grp.columns and grp[col].notna().any():
                    obj_agg[col + "_mean"] = _safe_round(grp[col].mean(), 2)
            if obj_agg:
                rule_data["obj_stats"] = obj_agg

        summary["by_rule"][rule_key] = rule_data

    # パーティタイプ別
    summary["by_party"] = {}
    for pt, grp in df.groupby("party_type"):
        summary["by_party"][str(pt)] = _agg_group(grp)

    # セッション疲労（試合番号ごとの平均KDA）
    if "session_seq" in df.columns:
        fatigue = (
            df.dropna(subset=["kda", "session_seq"])
            .groupby("session_seq")["kda"]
            .agg(mean="mean", count="count")
            .reset_index()
            .query("count >= 3")
        )
        summary["session_fatigue"] = {
            int(row["session_seq"]): _safe_round(row["mean"], 2)
            for _, row in fatigue.iterrows()
        }

    # 直近20試合のトレンド
    summary["recent_20"] = _agg_group(df.tail(20))

    return summary


def _build_matches_sample(df: pd.DataFrame, stat_df: pd.DataFrame) -> dict[str, Any]:
    """
    直近20試合 + KDAベスト5 + ワースト5 を返す。
    生データは絞って渡す。
    """
    cols = [c for c in EXPORT_COLUMNS if c in stat_df.columns]

    def _to_records(sub: pd.DataFrame) -> list[dict]:
        sub = sub[cols].copy()
        if "played_at" in sub.columns:
            sub["played_at"] = (
                sub["played_at"].dt.tz_convert("Asia/Tokyo").dt.strftime("%Y-%m-%d %H:%M")
            )
        if "playlist" in sub.columns:
            sub["playlist"] = sub["playlist"].map(lambda x: PLAYLIST_DISPLAY.get(str(x), str(x)))
        if "result" in sub.columns:
            sub["result"] = sub["result"].map(lambda x: RESULT_DISPLAY.get(str(x), str(x)))
        return json.loads(sub.to_json(orient="records", force_ascii=False))

    recent_20 = stat_df.sort_values("played_at").tail(20)
    best_5    = stat_df.nlargest(5,  "kda")
    worst_5   = stat_df.nsmallest(5, "kda")

    return {
        "recent_20": _to_records(recent_20),
        "best_5":    _to_records(best_5),
        "worst_5":   _to_records(worst_5),
    }


# ==================================================
# メインエントリポイント
# ==================================================

def build_export(
    df_filtered: pd.DataFrame,
    filter_info: dict[str, str],
    my_xuid: str,
) -> str:
    """
    フィルター済みDataFrameからAI相談用JSONを生成して文字列で返す。
    """
    stat_df = df_filtered[df_filtered["exclude_flag"] == ""].copy()

    # メタ情報
    now_jst    = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_range = ""
    if not stat_df.empty and "played_at" in stat_df.columns:
        dates      = stat_df["played_at"].dt.tz_convert("Asia/Tokyo")
        date_range = f"{dates.min().strftime('%Y-%m-%d')} 〜 {dates.max().strftime('%Y-%m-%d')}"

    meta = {
        "generated_at":   now_jst,
        "player_xuid":    my_xuid,
        "export_matches": len(stat_df),
        "date_range":     date_range,
        "filter":         filter_info,
    }

    export = {
        "meta":             meta,
        "suggested_prompt": SUGGESTED_PROMPT,
        "game_context":     GAME_CONTEXT,
        "glossary":         GLOSSARY,
        "features":         _build_features(stat_df),
        "summary":          _build_summary(stat_df),
        "matches":          _build_matches_sample(df_filtered, stat_df),
    }

    return json.dumps(export, ensure_ascii=False, indent=2)