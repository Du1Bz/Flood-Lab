# 指標ヘルプ文サンプル

## 1. `display.py` に追加する `METRIC_HELP` 辞書（抜粋）

```python
METRIC_HELP: dict[str, str] = {
    # === 基礎スタッツ ===
    "kills": "**キル**\n\n敵を倒した回数。最終的に止めを刺したキルのみカウント。",
    "deaths": "**デス**\n\n自分が倒された回数。デスが多いほどポジションや立ち回りに問題がある可能性。",
    "assists": "**アシスト**\n\n敵へのキルに貢献した回数。ダメージを与えた後にチームメイトが止めを刺した場合にカウント。",
    "shots_fired": "**発射数**\n\n試合中に発射した弾の総数。無駄撃ちが多いほど値が大きくなる。",
    "shots_hit": "**命中数**\n\n敵に当たった弾の数。発射数との組み合わせで命中率が算出される。",
    "damage_dealt": "**与ダメージ**\n\n敵に与えたダメージの合計。キルだけでは測れないプレッシャーのかけ具合を表す。",
    "damage_taken": "**被ダメージ**\n\n敵から受けたダメージの合計。高いほど狙われている/ポジションが悪い可能性。",
    "score": "**個人スコア**\n\nキル・アシスト・オブジェクトプレイなどで獲得したゲーム内スコア。",
    "power_kills": "**重火器キル**\n\nパワーウェポン（ロケットランチャー・スナイパーライフル等）を使用して倒したキル数。マップコントロールの指標。",
    "perfect_kills": "**パーフェクトキル**\n\nヘッドショットフィニッシュ等のパーフェクトキル数。高いほど精密射撃が得意。",
    "team_rank": "**チーム内順位**\n\n自チーム内での順位。1が最良。低いほどチーム内でのパフォーマンスが良い。",
    "duration_sec": "**試合時間（秒）**\n\n試合の総経過時間。モードによって標準時間が異なる。",

    # === レート系 ===
    "kd_ratio": "**K/D**\n\nキル ÷ デス。1.0を超えるとキルよりデスが少ない=貢献できている。デス0の場合はキル数がそのまま表示される。",
    "kda": "**KDA**\n\nキル - デス + (アシスト ÷ 3)。アシスト3回をキル1回相当とみなす総合指標。プラスが望ましい。",
    "accuracy": "**命中率**\n\n命中数 ÷ 発射数。高いほど精密なエイム。50%以上で優秀。0除算防止のため発射数0の場合は表示なし。",
    "damage_diff": "**ダメージ差**\n\n与ダメージ - 被ダメージ。プラスならダメージレートで優位に立っている。",
    "kill_efficiency": "**キル効率**\n\n与ダメージ ÷ (キル + アシスト÷3)。1キル相当あたりの与ダメージ。低いほどクリーンキルが多い。",
    "death_efficiency": "**デス効率**\n\n被ダメージ ÷ デス。1デスあたりの被ダメージ。高いほど粘れている=デスするまでに多くのダメージを吸収している。",

    # === 時間正規化 ===
    "kpm": "**KPM (Kills Per Minute)**\n\n1分あたりの平均キル数。試合時間が異なるモード間の比較に使用。高いほど効率的にキルしている。",
    "dpm": "**DPM (Deaths Per Minute)**\n\n1分あたりの平均デス数。低いほど生存力が高い。",

    # === CSR ===
    "csr_pre": "**試合前CSR**\n\n試合開始時のCSR（競技スキルレーティング）。0の場合は未ランクまたはカジュアル/カスタム。",
    "csr_post": "**試合後CSR**\n\n試合終了時のCSR。勝てば上がり、負ければ下がる。",
    "csr_delta": "**CSR増減**\n\n試合後CSR - 試合前CSR。プラスならCSRが上昇したことを示す。",

    # === TrueSkill2 ===
    "expected_kills": "**期待キル**\n\nTrueSkill2が試合前に予測した期待キル数。MMRベースで算出される。",
    "expected_deaths": "**期待デス**\n\nTrueSkill2が試合前に予測した期待デス数。MMRベースで算出される。",
    "k_rpi": "**K-RPI (Relative Performance Index)**\n\nキル ÷ 期待キル。1.0=期待通り、1.0超=期待以上のキル（ポップオフ）、1.0未満=期待以下のキル（アグレッション不足やポジション問題）。",
    "d_rpi": "**D-RPI (Relative Performance Index)**\n\n期待デス ÷ デス。1.0=期待通り、1.0超=期待より死ななかった（生存力高い）、1.0未満=期待より多く死んでいる（立ち回り問題）。",
    "lgai": "**LGAI (Lobby Gap Adjusted Impact)**\n\n敵チームMMR - 試合前CSR。正=格上相手のロビー、負=格下相手のロビー、0付近=均衡マッチ。",
    "impact_score": "**インパクトスコア**\n\n(K-RPI + D-RPI) ÷ 2。TrueSkill2基準の総合パフォーマンス指標。1.0が平均。",
    "survival_contribution": "**生存貢献度**\n\n(期待デス - デス) × (敵チームMMR ÷ 試合前CSR)。格上相手にどれだけ死なずに戦えたかを測る。正の値が望ましい。",

    # === eMMR ===
    "emmr_pre": "**eMMR（試合前）**\n\nFlood-Lab独自の推定MMR（試合前）。前試合の試合後eMMRを引き継ぐ。",
    "emmr_post": "**eMMR（試合後）**\n\nFlood-Lab独自の推定MMR（試合後）。AvgCSR20 + 200×ln(K比率) - パーティペナルティで算出。",
    "emmr_delta": "**eMMR増減**\n\n試合後eMMR - 試合前eMMR。プラスなら推定MMRが上昇。",
    "emmr_v2": "**eMMR v2**\n\nカルマンフィルタで平滑化した推定MMR。ノイズを除いたトレンドを表す。",
    "emmr_v2_sigma": "**eMMR v2 不確実性**\n\neMMR v2のカルマン分散の平方根。試合数が少ないほど値が大きい（信頼性が低い）。",

    # === パーティ ===
    "party_size": "**パーティ人数**\n\n一緒にプレイしているフレンドの人数。1=ソロ、2=デュオ、3=トリオ、4=フルパ。前後2試合の同チーム出現頻度から推定。",
    "party_type": "**パーティタイプ**\n\nソロ/デュオ/トリオ/フルパの区分。party_sizeから自動判定。",
    "is_solo": "**ソロ**\n\nパーティを組まずに1人でプレイしているかどうか。",
    "is_party": "**パーティ**\n\nフレンドとパーティを組んでプレイしているかどうか。",

    # === その他 ===
    "playlist": "**区分**\n\nプレイリストの種別。ランクアリーナ/ランクスレイヤー/カジュアル/BTB/カスタムゲーム等。PublicNameから自動分類。",
    "map_name": "**マップ**\n\n試合が行われたマップの名前。PlaylistMapModePairのPublicNameから抽出。",
    "rule_name": "**ルール**\n\n試合のルール（Slayer/CTF/Oddball/Strongholds/KOTH等）。",
    "result": "**勝敗**\n\n試合結果。勝ち/負け/引き分け/途中抜けの4種類。",
    "result_flag": "**勝敗フラグ**\n\n勝ち=1、負け/引き分け/途中抜け=0の二値フラグ。集計用。",
    "exclude_flag": "**除外フラグ**\n\n統計対象から除外する理由。空文字=対象、short_match(1分未満)/incomplete(途中参加・抜け)/bot_match(BOT含む)/low_shots(発射数30以下)/custom_non_ranked。",
    "team_score": "**自チームスコア**\n\n自チームの総合スコア。モードによって計算基準が異なる。",
    "enemy_score": "**敵チームスコア**\n\n敵チームの総合スコア。",
    "team_mmr": "**自チームMMR**\n\n自チームの平均MMR。TrueSkill2のチーム評価値。",
    "enemy_mmr": "**敵チームMMR**\n\n敵チームの平均MMR。ロビーの強度判断に使用。",
}
```

## 2. 各ビューでの使用例

### analysis.py のテーブル（st.dataframe + column_config）
```python
from src.utils.display import METRIC_HELP, display_name

# テーブル表示したいカラムを選ぶ
show_cols = ["played_at", "map_name", "rule_name", "result", "kd_ratio", "kda", "accuracy", "damage_diff"]

# column_config を動的生成
col_config = {}
for col in show_cols:
    if col in METRIC_HELP:
        col_config[col] = st.column_config.Column(
            display_name(col),
            help=METRIC_HELP[col],
        )

st.dataframe(
    df[show_cols],
    column_config=col_config,
    use_container_width=True,
)
```

### 実際の表示イメージ

| KDA ℹ️ | K/D ℹ️ | 命中率 ℹ️ |
|---------|---------|-----------|
| +1.25 | 1.50 | 52.3% |

ℹ️ にマウスオーバーすると：
> **KDA**  
> キル - デス + (アシスト ÷ 3)。アシスト3回をキル1回相当とみなす総合指標。プラスが望ましい。

### app_home.py の主要指標（st.metric + help）
```python
col1, col2, col3, col4 = st.columns(4)
col1.metric("K/D", f"{avg_kd:.2f}", help=METRIC_HELP.get("kd_ratio"))
col2.metric("KDA", f"{avg_kda:.2f}", help=METRIC_HELP.get("kda"))
col3.metric("命中率", f"{avg_acc:.1f}%", help=METRIC_HELP.get("accuracy"))
col4.metric("eMMR v2", f"{latest_emmr:.0f}", help=METRIC_HELP.get("emmr_v2"))
```

## 3. ヘルプ文のルール（設計方針）

| 項目 | 内容 |
|------|------|
| フォーマット | Markdown（`**` で指標名を太字、改行は `\n\n`） |
| 1行目 | `**表示名**` |
| 2行目以降 | 定義・計算式（簡潔に）＋解釈ガイド（1行） |
| 長さ | 50〜120文字程度を目安 |
| 言語 | 日本語 |
| 対象 | ゲームに詳しくない人でも理解できる平易な表現 |