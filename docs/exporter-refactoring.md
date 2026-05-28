# exporter.py リファクタリング設計書

作成日: 2026-05-28  
ステータス: Phase A 実装中

---

## 目的

`src/logic/exporter.py` のAI相談用JSONを、単なる集計データではなく  
「Halo Infiniteの競技文脈を踏まえたコーチング用データ」にする。

現状は `GAME_CONTEXT` に良い知識が入り始めているが、  
文章量が大きく、マップ・ルール・装備・メタ変更・診断ルールが混在している。  
AIの精度を上げるには、知識を増やすだけでなく「AIが迷わない形に構造化する」必要がある。

---

## 基本方針

- 公式情報、コミュニティ由来のセオリー、プレイヤーのデータを分けて扱う
- AIには対象データに関係ある文脈だけ渡す
- セオリーは文章ではなく「文脈 + データシグナル + 反証条件」にする
- サンプル数が少ない項目は断定させない
- DBから観測できない位置取り・VC・心理・意図は仮説として扱わせる

---

## 最終JSONの構造

```json
{
  "meta":              {},
  "analysis_contract": {},
  "context":           {},
  "features":          {},
  "summary":           {},
  "matches":           {}
}
```

### キー一覧

| キー | 日本語ラベル | 内容 |
|---|---|---|
| `meta` | メタ情報 | 生成日時・対象プレイヤー・対象期間・フィルター条件 |
| `analysis_contract` | 分析ルール | AIが守るべき分析・出力ルール |
| `context` | 分析文脈 | ルール仕様・マップ情報・装備・指標の限界など |
| `features` | AI向け特徴量 | 勝敗差分・直近比較・ロール傾向などの要約 |
| `summary` | 集計サマリー | 全体・マップ別・ルール別・パーティ別などの集計 |
| `matches` | 試合サンプル | 直近試合・ベスト/ワースト試合など |

---

## analysis_contract（分析ルール）

AIに分析ルールを明示するセクション。

```json
{
  "do_not_infer": [
    "心理状態",
    "VCの有無",
    "正確な位置取り",
    "味方の意図",
    "敵の意図"
  ],
  "claim_rules": {
    "min_games_for_hint": 3,
    "min_games_for_claim": 5,
    "min_games_for_strong_claim": 10
  },
  "coaching_style": [
    "根拠指標を必ず添える",
    "改善提案は最大3つ",
    "断定できないものは仮説として書く",
    "ルール別・マップ別・共通習慣に分けて考える",
    "ユーザー向けの出力は日本語で書く"
  ]
}
```

| キー | 日本語ラベル |
|---|---|
| `do_not_infer` | 推測禁止項目 |
| `claim_rules` | 断定ルール |
| `min_games_for_hint` | ヒント扱いに必要な最低試合数 |
| `min_games_for_claim` | 通常の主張に必要な最低試合数 |
| `min_games_for_strong_claim` | 強い主張に必要な最低試合数 |
| `coaching_style` | コーチング出力スタイル |

---

## context（分析文脈）の構造

現在の `GAME_CONTEXT` を以下の粒度に分割する。

```python
GAME_CONTEXT = {
    "fundamentals":        {},  # 共通基礎
    "modes":               {},  # ルール / モード
    "maps":                {},  # マップ
    "map_mode_pairs":      {},  # マップ×ルール
    "equipment":           {},  # 装備 / アビリティ
    "power_items":         {},  # パワーウェポン / パワーアップ
    "sandbox_versions":    {},  # サンドボックス変更履歴
    "ranked_rotations":    {},  # ランクローテーション
    "metric_limitations":  {},  # 指標の限界
    "community_heuristics":{},  # コミュニティ由来の仮説
}
```

英語キーはコード上で統一。AIに渡すJSONとドキュメントでは  
`label_ja` / `description_ja` を持たせて日本語ラベルを補足する。

### ranked_rotations（ランクローテーション）スナップショット

2026-05-19更新の公式Halo Supportページより。  
ソース: https://support.halowaypoint.com/hc/en-us/articles/17920041655188

```python
{
  "as_of": "2026-05-19",
  "loadout": "Bandit Evo",
  "motion_tracker": "disabled",
  "modes": [
    "Capture the Flag (3 Captures)",
    "Capture the Flag (5 Captures)",
    "King of the Hill",
    "Oddball",
    "Assault: Neutral Bomb",
    "Slayer",
    "Strongholds"
  ],
  "map_mode_pairs": {
    "Aquarius":  ["Assault: Neutral Bomb", "Capture the Flag (5 Captures)", "Slayer"],
    "Empyrean":  ["Capture the Flag (3 Captures)"],
    "Forbidden": ["Capture the Flag (3 Captures)"],
    "Fortress":  ["Assault: Neutral Bomb", "Capture the Flag (3 Captures)"],
    "Lattice":   ["King of the Hill", "Oddball", "Strongholds"],
    "Live Fire": ["King of the Hill", "Oddball", "Slayer", "Strongholds"],
    "Origin":    ["Capture the Flag (3 Captures)", "Slayer"],
    "Recharge":  ["King of the Hill", "Oddball", "Slayer", "Strongholds"],
    "Serenity":  ["Assault: Neutral Bomb", "Capture the Flag (3 Captures)"],
    "Solitude":  ["King of the Hill", "Slayer"],
    "Streets":   ["Slayer"],
    "Vacancy":   ["King of the Hill", "Oddball", "Slayer"]
  }
}
```

> **注意**: 現状のRanked Arenaのプレイリストと差異がある可能性あり。  
> 生データと突き合わせるか手動で修正が必要。

| キー | 日本語ラベル |
|---|---|
| `as_of` | 情報確認日 |
| `loadout` | 初期装備 |
| `motion_tracker` | モーショントラッカー |
| `modes` | 採用ルール |
| `map_mode_pairs` | マップ×ルール組み合わせ |
| `historical_changes` | 過去の変更履歴 |
| `current_playlist_snapshot` | 現行プレイリスト情報 |

### マップコンテキストのフィールド構造

`notes` に混在していた情報を独立フィールドに分離する。

```python
"Lattice": {
    "label_ja": "Lattice",
    "introduced_at": "2025-08-05",
    "ranked_added_at": "2025-08-05",
    "current_ranked_status": "active",
    "current_hcs_status": "unknown",
    "layout": {
        "size": "large",
        "symmetry": "asymmetric",
        "lanes": 3,
        "verticality": "medium",
        "long_sightlines": True
    },
    "items": {
        "power_weapons": ["sniper"],
        "powerups": [],
        "equipment": []
    },
    "common_diagnoses": [
        "中央横断で被弾しやすい",
        "建物側レーン管理が弱いと分断されやすい"
    ],
    "sources": [
        {"type": "official_or_user_defined", "url": ""}
    ]
}
```

### metric_limitations（指標の限界）

```python
{
  "global": [
    "Shock Rifle は PowerWeaponKills に反映されないため pw_control_rate は過小評価になる",
    "装備の取得/使用ログがないため Repulsor や Thruster の使い方は直接評価できない",
    "位置情報がないためアンカー・スポーン制御・射線管理は代理指標でしか見られない",
    "VCや味方とのコミュニケーションは観測できない",
    "サンプル数が少ないマップ/ルールは断定しない"
  ],
  "by_mode": {
    "CTF": [
      "旗をどのルートで運んだかは分からない",
      "自軍旗が取られていたかどうかの時系列は分からない",
      "旗キャリアへの護衛距離は分からない"
    ],
    "KOTH": [
      "ヒル内に複数人いたかは分からない",
      "ヒル外の戻りルートを抑えていたかは直接分からない"
    ],
    "Strongholds": [
      "拠点キャプチャに何人で入ったかは分からない",
      "3点取りでスポーンを荒らしたかは直接分からない"
    ],
    "Oddball": [
      "ボールを意図的に捨てたかは分からない",
      "ボール周辺の味方配置は分からない"
    ]
  }
}
```

---

## features（AI向け特徴量）の追加項目

### win_loss_delta（勝敗差分）

勝ち試合平均と負け試合平均の差。  
勝敗に効いていそうな指標をAIに明示する。

```json
{
  "kda": {"win": 1.23, "loss": -0.45, "diff": 1.68},
  "k_rpi": {"win": 1.15, "loss": 0.87, "diff": 0.28}
}
```

> 因果の方向性に注意。「勝ったからその指標が高い」場合もある。

### recent_vs_baseline（直近比較）

直近20戦 vs それ以前の比較。最近の調子の変化をAIが見やすくする。

```json
{
  "kda": {"recent": 0.82, "baseline": 1.14, "diff": -0.32}
}
```

### map_mode_matrix（マップ×ルール表）

`map_name x rule_name` の勝率・KDA・試合数。  
苦手なマップ単体ではなく、苦手な「マップ/ルール組み合わせ」を見つける。

### confidence（信頼度）

各集計に `n`・`confidence_level`・`warning` を付けてAIの断定を防ぐ。

```json
{
  "n": 4,
  "confidence_level": "hint",
  "warning": "試合数が少ないため参考程度"
}
```

### ego_challenge_risk_proxy（無理な撃ち合いリスク）

| シグナル | 意味 |
|---|---|
| `high_damage_taken_per_min` | 被ダメージ/分が高い |
| `low_d_rpi` | D-RPIが低い |
| `high_dpm` | デス/分が高い |

### passivity_proxy（消極性の疑い）

| シグナル | 意味 |
|---|---|
| `high_d_rpi` | D-RPIが高い |
| `low_k_rpi` | K-RPIが低い |
| `low_engagement_density` | エンゲージメント密度が低い |
| `low_damage_dealt_per_min` | 与ダメージ/分が低い |

### lobby_bucket_summary（ロビー格差別サマリー）

LGAIを格下/同格/格上に分けて集計し、勝率だけで実力を誤診断しない。

---

## SUGGESTED_PROMPT の修正方針

追加する指示の優先順位:

1. まず `win_loss_delta` を見る
2. 次に `recent_vs_baseline` で最近の変化を見る
3. ルール別・マップ別に原因を分ける
4. `common_mistakes` と `data_signals` を照合する
5. `n` が少ない項目は仮説として扱う
6. `metric_limitations` の制約を必ず考慮する
7. 位置取り・VC・意図などDBにない情報は断定しない
8. 改善提案は最大3つに絞り、各提案に根拠指標を添える

---

## 実装フェーズ

### Phase A: JSON構造を整える（現在）

- [x] `win_loss_delta`（勝敗差分）を `features` に追加
- [ ] `analysis_contract`（分析ルール）を追加
- [ ] `recent_vs_baseline`（直近比較）を `features` に追加
- [ ] `map_mode_matrix`（マップ×ルール表）を `summary` に追加
- [ ] `metric_limitations`（指標の限界）を `context` に追加
- [ ] `confidence`（信頼度）を各集計に付与

### Phase B: コンテキスト分離

- [ ] `GAME_CONTEXT` を `halo_knowledge` 系モジュールに移動
- [ ] マップの `notes` から日付・アイテム・構造を独立フィールド化
- [ ] `equipment`（装備/アビリティ）と `power_items` を追加
- [ ] `build_relevant_context(stat_df)` を実装（対象データのマップ/ルールだけ渡す）

### Phase C: セオリー補強

- [ ] `fundamentals`（共通基礎）を追加
- [ ] モード別に `common_mistakes`・`data_signals`・`counter_evidence` を追加
- [ ] `community_heuristics`（コミュニティ由来の仮説）を追加
- [ ] 公式ソースとコミュニティソースを分離

### Phase D: ルール仕様の追加

- [ ] `mode_rules`（ルール仕様）を追加
- [ ] `game_terms`（ゲーム内用語）を追加
- [ ] `rule_diagnostics`（ルール別診断ルール）を追加
- [ ] `mode_metric_limitations`（ルール別のデータ限界）を追加

### Phase E: ロール推定の追加

- [ ] `roles`（ロール/役割）コンテキストを追加
- [ ] `features.role_profile`（ロール傾向）を追加
- [ ] ロール推定用の特徴量を追加

---

## 目指す診断出力のイメージ

```
直近20戦ではK-RPIがベースラインより下がっているが、D-RPIは維持できている。
特にOddballでengagement_densityが低く、ball_timeも高くないため、
単にボール役でキルが低いというより、仕掛けの遅さか外側カバー不足の可能性がある。
ただし位置情報はないため仮説。

改善提案:
1. Oddballではボールを持つ前に、敵の戻りルート側へ1枚分だけ押し上げる。
   根拠: OddballのK-RPI低下、engagement_density低下。
2. 先撃ちされた撃ち合いは離脱優先。
   根拠: damage_taken_per_min高、D-RPI低。
```

---

## 設計メモ

このリファクタリングの核心は「セオリーをたくさん書くこと」ではなく  
「AIが使える診断形式にすること」。

**良い形:**
```
文脈 + データシグナル + 反証条件 + 信頼度
```

**悪い形:**
```
長い一般論だけを渡す
```
