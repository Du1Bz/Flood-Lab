"""
halo_knowledge/modes.py
-----------------------
ルール仕様・セオリーコンテキスト。

C-1: FUNDAMENTALS（共通基礎）
C-2: RULE_THEORY に common_mistakes / data_signals / counter_evidence を追加
C-4: 公式情報とコミュニティ由来の仮説をソース付きで分離
"""

from __future__ import annotations
from typing import Any

# ==================================================
# C-1. FUNDAMENTALS（共通基礎）
# 全ルール共通の考え方。
# 公式情報と community_heuristic を分けて持つ。
# ==================================================

FUNDAMENTALS: dict[str, Any] = {
    "label_ja": "共通基礎",
    "description_ja": "全ルールに共通する考え方。ルール別セオリーの前提として参照する。",

    # C-4: 公式情報ベースの原則
    "official_principles": {
        "source": "Halo Infinite ゲームデザイン・公式ガイド",
        "items": [
            "Bandit Evo スタートで全プレイヤーの初期武器は統一されている。有利不利は位置取りと判断で生まれる。",
            "モーショントラッカーは Ranked では無効。音・視界・コールアウトが主な情報源になる。",
            "パワーウェポンのスポーンは試合開始時刻からの経過時間で固定。取得タイミングに関わらず一定間隔で出現する。",
            "シールドは自動回復する。不利交戦から離脱してシールドを回復してから再交戦するのが基本。",
            (
                "オブジェクティブルール（CTF / KOTH / Oddball / Strongholds）はSlayerより命が重い。"
                "リスポーン待機時間が長い（10秒 vs 8秒）うえ、前線や行くべきポジションが明確に存在するため、"
                "遠い場所にリスポーンすると移動時間も加わり、味方がより長く数的不利の状況に置かれる。"
                "味方のダウン数によっては積極的なプレイを辞め、ステイアライブとアンカーとしての役割に徹することが重要。"
            ),
        ],
    },

    # C-4: コミュニティ由来の原則
    "community_principles": {
        "confidence": "community_heuristic",
        "sources": [
            "https://www.reddit.com/r/CompetitiveHalo/comments/rzq9zo",
            "https://www.reddit.com/r/CompetitiveHalo/comments/r9x927",
            "https://www.reddit.com/r/CompetitiveHalo/comments/rjmk8b",
        ],
        "items": [
            "味方の位置を見て敵スポーンを推測する。",
            "先撃ちされたら無理に撃ち返さず、シールド回復を優先する。",
            "高台・遮蔽物・逃げ道を持って撃ち合う。",
            "単独キルより、味方の射線に合わせてダメージを出す（チームショット）。",
            "パワーウェポン・パワーアップ・重要ポジションを中心に動く。",
            "マップの約2/3を取って敵スポーンを狭める。",
        ],
    },

    # 共通フレーム（全ルール）
    "common_frame": {
        "description_ja": "全ルール共通の動きのフレーム",
        "steps": [
            "① アンカーを取る（どこに沸くかをコントロール）",
            "② エリアをクリアする（敵を遠くに追い出す）",
            "③ 敵の戻りを遮断する（移動経路・オフアングル）",
            "④ 目標に絡む（最後）",
        ],
        "note": "目標に絡むのは常に最後。①②③が崩れた状態で無理に動くと被ダメが増える。",
    },
}

# ==================================================
# ゲームベース情報
# ==================================================

GAME_BASE: dict[str, Any] = {
    "version": "2026-05",
    "game": "Halo Infinite - Ranked Arena",
    "loadout": "全プレイヤーBandit Evo統一スタート。初期武器の差はない。",
    "power_weapons_general": {
        "description": "マップ上に配置されるパワーウェポン（PW）の確保が勝敗を大きく左右する。",
        "types": ["スナイパーライフル", "ロケットランチャー", "ショックライフル"],
        "shock_rifle_note": (
            "ショックライフルは3発同時射出・全弾ヘッドショット判定で一撃キル可能だが癖が強く、"
            "スナイパー的な運用が多い。APIの仕様上、ショックライフルによるキルはPWキルとして"
            "カウントされないため、pw_control_rate はスナイパー・ロケット系のみを反映した"
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
}

# ==================================================
# C-2. RULE_THEORY
# ルール別セオリー。
# 各ルールに以下を追加:
#   common_mistakes  : よくあるミス
#   data_signals     : データシグナル（状況→仮説のマッピング）
#   counter_evidence : 反証条件（仮説を否定しうる指標）
# ==================================================

RULE_THEORY: dict[str, Any] = {

    "slayer": {
        "label_ja": "スレイヤー",
        "objective": "先に規定キル数に到達する。",
        "core": (
            "味方を死なせないために守り合うゲーム。"
            "キルを取るゲームに見えるが、不利な交戦を断る判断の積み重ねが勝敗を分ける。"
        ),
        "keys": [
            "味方を助けるキルを優先（味方を助けるキルは2点分の価値）",
            "有利状況を作ってから撃ち合う（グレネードで削る・ハイグラウンド・2v1を作る）",
            "不利交戦を断る（負けたファイトの再チャレンジをしない・シールドが割れたら即離脱）",
            "スポーンと陣地をコントロールする（有利エリアで戦い続けたチームが勝つ）",
        ],
        # C-2
        "common_mistakes": [
            "人数不利で再チャレンジする",
            "味方から離れて単独で深追いする",
            "リード時に無理に攻めてデスを献上する",
            "シールドが割れた状態で次の交戦に入る",
        ],
        "data_signals": {
            "too_aggressive": {
                "condition": "high_kpm AND high_dpm AND low_d_rpi",
                "hypothesis": "キルは取れているが死も多く、不利交戦を継続しすぎている可能性",
            },
            "too_passive": {
                "condition": "low_engagement_density AND low_k_rpi AND high_d_rpi",
                "hypothesis": "生存はできているが、味方を助けるキルやダメージ参加が不足している可能性",
            },
            "win_diff_low_kda": {
                "condition": "win_rate high AND kda low",
                "hypothesis": "チームへの貢献がK/D以外の形（オブジェクト、ポジション維持）で出ている可能性",
            },
        },
        "counter_evidence": {
            "too_aggressive": ["damage_diff positive", "team_score close"],
            "too_passive":    ["assists high", "damage_dealt_per_min high"],
        },
    },

    "koth": {
        "label_ja": "キング・オブ・ザ・ヒル",
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
        # C-2
        "common_mistakes": [
            "ヒル周辺が制圧できていない状態でヒルに入る",
            "ヒル内で戦い続けて死に続ける",
            "敵の戻りルートを放置する",
            "ヒルが動いた後の次のヒルへの先回りが遅い",
            "味方が複数ダウンしている状態でも無理にヒルを踏みに行って死ぬ",
        ],
        "data_signals": {
            "high_occ_low_win": {
                "condition": "zone_occupation_sec high AND win_rate low",
                "hypothesis": "ヒルには入れているが周辺制圧や戻りルート遮断が足りない可能性",
            },
            "low_occ_high_kill": {
                "condition": "zone_occupation_sec low AND k_rpi high",
                "hypothesis": "キルは取れているがヒル時間への変換が弱い可能性",
            },
            "high_def_low_off": {
                "condition": "zone_def_kills high AND zone_off_kills low",
                "hypothesis": "守りに偏っており、ヒルを取りに行くプッシュが少ない可能性",
            },
        },
        "counter_evidence": {
            "high_occ_low_win": ["zone_def_kills high", "team_score close"],
            "low_occ_high_kill": ["zone_off_kills high"],
            "high_def_low_off":  ["zone_occupation_sec high"],
        },
    },

    "ctf": {
        "label_ja": "キャプチャー・ザ・フラッグ",
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
        # C-2
        "common_mistakes": [
            "スポーン空白時間を作れていない状態で旗を運び始める",
            "キャリーの護衛に寄れず単独で別動している",
            "自陣フラッグが出ている時に敵陣へ深く入りすぎる",
            "旗を持ったまま不利な正面突破を繰り返す",
            "味方が複数ダウンしている状態で旗を抜きに行って孤立する",
        ],
        "data_signals": {
            "high_steals_low_kills": {
                "condition": "flag_steals high AND k_rpi low",
                "hypothesis": (
                    "敵陣に旗を取りに行くチャレンジは多いがキルが取れていない可能性。"
                    "ウェーブを合わせる前にスティールに行って死んでいるパターンが疑われる。"
                    "flag_steals を無理な突入の主シグナルとして使う。"
                ),
            },
            "high_steals_low_captures": {
                "condition": "flag_steals high AND flag_captures low",
                "hypothesis": (
                    "旗を奪取しているが帰還できていない可能性。"
                    "ウェーブを合わせずに旗を触っている、またはルート・護衛に課題がある可能性。"
                ),
            },
            "low_steals_low_captures": {
                "condition": "flag_steals low AND flag_captures low",
                "hypothesis": (
                    "攻撃への参加が少ない可能性。"
                    "プッシュが遅い、またはプッシュ中にデスして攻め切れていない可能性。"
                ),
            },
            "high_returns_low_captures": {
                "condition": "flag_returns high AND flag_captures low",
                "hypothesis": "防衛貢献はあるが、攻撃のセットアップや旗キャリア護衛に課題がある可能性",
            },
        },
        "flag_grabs_note": (
            "flag_grabs はドリブル技術・ルート・妨害など複数要因が絡むため単体で推論に使わない。"
            "1本キャプチャでも安全ルートで邪魔されなければ grabs=9 になりうる（ドリブル仕様）。"
            "grabs 数の多少は「チャレンジ回数」ではなく「ドリブル技術やルート」の指標として扱う。"
        ),
        "counter_evidence": {
            "high_steals_low_kills":     ["flag_captures high"],
            "high_steals_low_captures":  ["flag_carrier_time_sec high", "flag_carriers_killed high"],
            "low_steals_low_captures":   ["flag_returns high", "damage_diff positive"],
            "high_returns_low_captures": ["team_score close", "damage_diff positive"],
        },
    },

    "oddball": {
        "label_ja": "オッドボール",
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
            "oddball_skull_time_sec": "ボールを保持していた合計時間（秒）。保持時間が長いプレイヤーは射撃できないためキルが少なくなりがち。",
            "oddball_scoring_ticks":  "ボールのスコアティック数。",
            "oddball_skull_grabs":    "ボールをグラブした回数。ドリブルをしていると多くなる傾向がある。",
            "oddball_carrier_kills":  "ボールを保持している間にキルした回数。アリーナではあまり発生しない。",
            "oddball_skulls_denied":  "敵のボールキャリアをキルした回数。",
            "notes": "ボール持ちのプレイヤーはスタッツが少なくなりがち。不利な状況ではボールをOBや開けた場所に投棄して仕切り直すことが推奨される。",
        },
        # C-2
        "common_mistakes": [
            "ボールを無理に持ち続けて不利な場所で死ぬ",
            "ボールキャリアに密着して護衛の外側ポジションを取れない",
            "ボールを持つ前に敵の戻りルートを潰せていない",
            "キャリアが削られているときに引いてしまう",
            "味方が複数ダウンしている状態でボールを持ったまま動いて孤立する",
        ],
        "data_signals": {
            "high_time_low_k": {
                "condition": "oddball_skull_time_sec high AND k_rpi low",
                "hypothesis": "ボール役として自然にキルが低く出ている可能性（役割上の特性）",
            },
            "high_time_low_grabs": {
                "condition": "oddball_skull_time_sec high AND oddball_skull_grabs low",
                "hypothesis": (
                    "保持時間は長いがグラブ数が少ない。"
                    "人数不利（3v4・2v4等）の状況でもボールをOB/オープンへ投棄せず"
                    "持ち続けてしまっている可能性がある。"
                    "不利状況では投棄して味方スポーンを待って仕切り直す判断が重要。"
                ),
            },
            "low_time_low_k_low_eng": {
                "condition": "oddball_skull_time_sec low AND k_rpi low AND engagement_density low",
                "hypothesis": "ボール保持にも周辺戦闘にも関与が薄い可能性",
            },
            "high_d_low_k": {
                "condition": "d_rpi high AND k_rpi low AND oddball_skull_time_sec low",
                "hypothesis": "守りすぎ・外側カバー不足・仕掛けの遅さの可能性",
            },
        },
        "counter_evidence": {
            "high_time_low_k":        ["oddball_scoring_ticks high"],
            "high_time_low_grabs":    ["oddball_skulls_denied high", "k_rpi high"],
            "low_time_low_k_low_eng": ["d_rpi high", "damage_diff positive"],
            "high_d_low_k":           ["oddball_skulls_denied high"],
        },
    },

    "strongholds": {
        "label_ja": "ストロングホールド",
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
            "zone_captures":       "ポイントキャプチャ数。最後までキャプチャした回数。味方と同時でもカウントされる。敵に2点・3点取られた場合のリテイク（奪還）も含まれるため、負けている状況でもカウントが増えることに留意。",
            "zone_def_kills":      "ポイント周辺での防御キル数。",
            "zone_off_kills":      "ポイント周辺での攻撃キル数。",
            "zone_secures":        "ポイントのセキュア数。敵がキャプチャしているポイントをリセットした回数。",
            "notes": "攻撃キルが多く防御キルが少ない場合、攻めすぎて敵が自分のポイントにスポーンしてしまっている可能性がある。",
        },
        # C-2
        "common_mistakes": [
            "リードしている状態で3点目を取りに行って敵スポーンを荒らす",
            "ポイントを取った後に前に出すぎて敵に沸かれる",
            "ポイントキャプチャに複数人入って他エリアの防衛が薄くなる",
            "敵のポイント間移動ルートを放置する",
            "味方が複数ダウンしている状態で拠点を踏みに行って死ぬ",
        ],
        "data_signals": {
            "high_captures_low_win": {
                "condition": "zone_captures high AND win_rate low",
                "hypothesis": "拠点は取れているが維持できていない、または3点取りでスポーンを荒らしている可能性",
            },
            "high_off_low_def": {
                "condition": "zone_off_kills high AND zone_def_kills low",
                "hypothesis": "攻めすぎて敵が自陣ポイントにスポーンしてしまっている可能性",
            },
            "low_captures_high_damage": {
                "condition": "zone_captures low AND damage_diff positive",
                "hypothesis": "撃ち合いでは勝てているが、拠点ローテーションや踏む判断が遅い可能性",
            },
        },
        "counter_evidence": {
            "high_captures_low_win":    ["zone_secures high", "team_score close"],
            "high_off_low_def":         ["zone_occupation_sec high"],
            "low_captures_high_damage": ["zone_def_kills high"],
        },
    },

    "common_frame": {
        "description_ja": "全ルール共通の動きのフレーム",
        "steps": [
            "① アンカーを取る（どこに沸くかをコントロール）",
            "② エリアをクリアする（敵を遠くに追い出す）",
            "③ 敵の戻りを遮断する（移動経路・オフアングル）",
            "④ 目標に絡む（最後）",
        ],
        "note": "目標に絡むのは常に最後。①②③が崩れた状態で無理に動くと被ダメが増える。",
    },
}