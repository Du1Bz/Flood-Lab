# exporter.py / AIコーチング用コンテキスト リファクタリング提案

作成日: 2026-05-28

## 目的

`src/logic/exporter.py` のAI相談用JSONを、単なる集計データではなく「Halo Infiniteの競技文脈を踏まえたコーチング用データ」にする。

現状は `GAME_CONTEXT` に良い知識が入り始めているが、文章量が大きく、マップ・ルール・装備・メタ変更・診断ルールが混ざっている。AIの精度を上げるには、知識を増やすだけでなく、AIが迷わない形に構造化する必要がある。

## 基本方針

- 公式情報、コミュニティ由来のセオリー、自分のデータを分けて扱う。
- AIには対象データに関係ある文脈だけ渡す。
- セオリーは文章ではなく「文脈 + データシグナル + 反証条件」にする。
- サンプル数が少ない項目は断定させない。
- DBから観測できない位置取り、VC、心理、意図は仮説として扱わせる。

## exporter.py の責務分割案

将来的に `exporter.py` はJSONの組み立てだけに薄くする。

```text
src/logic/exporter.py
  最終JSONの組み立て

src/logic/export_features.py
  AI向け特徴量の生成

src/logic/export_context.py
  対象データに応じた文脈の選別

src/logic/halo_knowledge/
  maps.py
  modes.py
  equipment.py
  sandbox_versions.py
  ranked_rotations.py
  community_heuristics.py
  metric_limitations.py
```

最終JSONのイメージ:

```json
{
  "meta": {},
  "analysis_contract": {},
  "context": {},
  "features": {},
  "summary": {},
  "matches": {}
}
```

主要JSONキー対応表:

| 英語キー | 日本語ラベル | 内容 |
|---|---|---|
| `meta` | メタ情報 | 生成日時、対象プレイヤー、対象期間、フィルター条件 |
| `analysis_contract` | 分析ルール | AIが守るべき分析・出力ルール |
| `context` | 分析文脈 | ルール仕様、マップ情報、装備、指標の限界など |
| `features` | AI向け特徴量 | 勝敗差分、直近比較、ロール傾向などの要約 |
| `summary` | 集計サマリー | 全体、マップ別、ルール別、パーティ別などの集計 |
| `matches` | 試合サンプル | 直近試合、ベスト/ワースト試合など |

## analysis_contract（分析ルール）の追加

AIに分析ルールを明示する。

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

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `do_not_infer` | 推測禁止項目 |
| `claim_rules` | 断定ルール |
| `min_games_for_hint` | ヒント扱いに必要な最低試合数 |
| `min_games_for_claim` | 通常の主張に必要な最低試合数 |
| `min_games_for_strong_claim` | 強い主張に必要な最低試合数 |
| `coaching_style` | コーチング出力スタイル |

## GAME_CONTEXT（AI文脈）の再構成

現在の `GAME_CONTEXT` は、以下の粒度に分けたい。

```python
GAME_CONTEXT = {
    "fundamentals": {},          # 共通基礎
    "modes": {},                 # ルール / モード
    "maps": {},                  # マップ
    "map_mode_pairs": {},        # マップ×ルール
    "equipment": {},             # 装備 / アビリティ
    "power_items": {},           # パワーウェポン / パワーアップ
    "sandbox_versions": {},      # サンドボックス変更履歴
    "ranked_rotations": {},      # ランクローテーション
    "metric_limitations": {},    # 指標の限界
    "community_heuristics": {},  # コミュニティ由来の仮説
}
```

正式ドキュメントやJSON内では、英語キーだけだと読みにくいので日本語ラベルも併記する。

例:

```json
{
  "fundamentals": {
    "label_ja": "共通基礎",
    "description_ja": "全ルールに共通する考え方"
  },
  "ranked_rotations": {
    "label_ja": "ランクローテーション",
    "description_ja": "現在のRanked Arenaに含まれるマップ/ルールの組み合わせ"
  }
}
```

コード上のキーは英語で統一してよいが、AIに渡すJSONとドキュメントでは `label_ja` / `description_ja` を持たせる。

## マップコンテキストの修正

現状の `maps` は `notes` に追加日、構造、武器、感想が混ざっている。AIが比較しやすいようにフィールド化する。

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

追加したいマップ項目:

- `introduced_at`: 初登場日
- `ranked_added_at`: ランク追加日
- `current_ranked_status`: 現在のランク採用状態
- `current_hcs_status`: 現在のHCS採用状態
- `layout.size`: マップサイズ
- `layout.symmetry`: 対称/非対称
- `layout.lanes`: レーン数
- `layout.verticality`: 高低差
- `layout.long_sightlines`: 長い射線の有無
- `items.power_weapons`: パワーウェポン
- `items.powerups`: パワーアップ
- `items.equipment`: 装備/アビリティ
- `common_diagnoses`: よくある診断仮説
- `sources`: 情報ソース

## 公式情報として保持したいもの

公式情報は事実として扱う。ただし Ranked / HCS / Rotational は頻繁に変わるため、必ず `as_of` と `source_url` を持つ。

特に重要:

- 「過去のHCS Roadmapで削除された/追加された」は履歴情報であり、現在のRanked Arenaローテーションとは別扱いにする。
- 現行の分析コンテキストでは、Halo Support の `Halo Infinite Multiplayer Playlists` のような現在更新されているページを優先する。
- HCS大会用マッププールとRanked Arenaマッチメイキングは同一視しない。

### 現行Ranked Arena（ランクアリーナ）スナップショット

※ユーザー追記：この項目は現状のRanked Arenaのプレイリストと差異がある。後で生データと突き合わせるか手動で修正が必要。追記終わり

2026-05-28時点で確認した公式Halo Supportページは `Updated: May 19, 2026`。このページの Ranked Arena には以下が含まれている。

```python
CURRENT_RANKED_ARENA_AS_OF_2026_05_19 = {
    "source_url": "https://support.halowaypoint.com/hc/en-us/articles/17920041655188-Halo-Infinite-Multiplayer-Playlists",
    "source_label_ja": "Halo Support: Halo Infinite Multiplayer Playlists",
    "as_of": "2026-05-19",
    "loadout": "Bandit Evo loadout",
    "loadout_label_ja": "初期武器: Bandit Evo",
    "motion_tracker": "disabled",
    "motion_tracker_label_ja": "モーショントラッカー無効",
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
        "Aquarius": ["Assault: Neutral Bomb", "Capture the Flag (5 Captures)", "Slayer"],
        "Empyrean": ["Capture the Flag (3 Captures)"],
        "Forbidden": ["Capture the Flag (3 Captures)"],
        "Fortress": ["Assault: Neutral Bomb", "Capture the Flag (3 Captures)"],
        "Lattice": ["King of the Hill", "Oddball", "Strongholds"],
        "Live Fire": ["King of the Hill", "Oddball", "Slayer", "Strongholds"],
        "Origin": ["Capture the Flag (3 Captures)", "Slayer"],
        "Recharge": ["King of the Hill", "Oddball", "Slayer", "Strongholds"],
        "Serenity": ["Assault: Neutral Bomb", "Capture the Flag (3 Captures)"],
        "Solitude": ["King of the Hill", "Slayer"],
        "Streets": ["Slayer"],
        "Vacancy": ["King of the Hill", "Oddball", "Slayer"]
    }
}
```

例: 以前のHCS 2025 Roadmap上では Empyrean CTF が削除対象として扱われていたが、2026-05-19更新の公式Ranked Arena一覧では `Empyrean: Capture the Flag (3 Captures)` が復活している。AIコンテキストではこのような変化を表現するため、`historical_changes` と `current_playlist_snapshot` を分離する。

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `source_url` | ソースURL |
| `as_of` | 情報確認日 |
| `loadout` | 初期装備 |
| `motion_tracker` | モーショントラッカー |
| `modes` | 採用ルール |
| `map_mode_pairs` | マップ×ルール組み合わせ |
| `historical_changes` | 過去の変更履歴 |
| `current_playlist_snapshot` | 現行プレイリスト情報 |

例:

- HCS 2025 Roadmap / 履歴情報
  - Origin Slayer / Origin CTF 追加
  - Aquarius Neutral Bomb Assault 追加
  - Fortress Neutral Bomb Assault 追加
  - Empyrean CTF 削除
  - Fortress Slayer 削除
- Spring Update 2025
  - Ranked Arena のマップ別アイテム配置更新
  - Aquarius: Camo が Overshield の代わりに Top Mid
  - Recharge: Shock Rifle が power weapon pad に配置
  - 一部マップに新ジャンプ
  - グレネードキャストタイム調整
  - ストレイフ加速度調整
  - Shock Rifle 等の調整
- Equipment in Halo Infinite
  - Multiplayerで使える装備の一覧

ソース:

- https://www.halowaypoint.com/news/2025roadmap
- https://www.halowaypoint.com/news/spring-update-2025-halo-infinite
- https://support.halowaypoint.com/hc/en-us/articles/26608497528596-Equipment-in-Halo-Infinite

## 装備・アビリティコンテキストの追加

Halo Infiniteでは装備が戦術判断に絡むため、AIコーチング用コンテキストに追加する。

```python
"equipment": {
    "Repulsor": {
        "label_ja": "リパルサー",
        "type": "defensive_utility",
        "type_label_ja": "防御/拒否系ユーティリティ",
        "coaching_use": [
            "グレネード、ロケット、近接を拒否する",
            "狭所の押し返しに使う",
            "ジャンプや位置取りの補助にもなる"
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可"
    },
    "Thruster": {
        "label_ja": "スラスター",
        "type": "duel_escape",
        "type_label_ja": "撃ち合い補助/離脱",
        "coaching_use": [
            "先撃ちされた時の離脱",
            "角待ちや射線切り",
            "短時間のピーク変更"
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可"
    },
    "Threat Seeker": {
        "label_ja": "スレットシーカー",
        "type": "information",
        "type_label_ja": "索敵/情報取得",
        "coaching_use": [
            "セットアップ崩し",
            "OddballやStrongholdsの敵位置確認",
            "味方プッシュ前の情報取り"
        ],
        "data_limit": "取得・使用ログがないため直接評価は不可"
    }
}
```

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `equipment` | 装備/アビリティ |
| `type` | 装備タイプ |
| `coaching_use` | コーチング上の使い道 |
| `data_limit` | データ上の限界 |

候補:

- Active Camouflage
- Overshield
- Repulsor
- Thruster
- Threat Seeker
- Threat Sensor
- Drop Wall
- Shroud Screen
- Grappleshot

## モード別セオリーの補強

現状の `rule_theory` は良い土台。追加するなら、AIが診断に使える形にする。

## ルール仕様コンテキストの追加

AIコーチング精度を上げるには、戦術セオリーだけでなく「そもそものルール仕様」を独立して持つ必要がある。

例:

- 勝利条件
- 得点条件
- 特殊仕様
- よく使う用語
- 仕様から導ける診断ルール
- DBから直接観測できないもの

公式情報の起点:

- https://support.halowaypoint.com/hc/en-us/articles/4407649063316-Guide-to-Halo-Infinite-Multiplayer-Game-Mode-Rules
- https://support.halowaypoint.com/hc/en-us/articles/17920041655188-Halo-Infinite-Multiplayer-Playlists

提案構造:

```python
"mode_rules": {
    "CTF": {
        "label_ja": "キャプチャー・ザ・フラッグ",
        "win_condition": "規定数の旗キャプチャで勝利",
        "scoring_rules": [],
        "special_rules": [],
        "key_terms": {},
        "data_signals": {},
        "limitations": []
    }
}
```

※ユーザー追記：時間制限がある。時間制限になったら、より得点したほうの勝利。タイだった場合、1本先取のオーバータイムに突入する。試合時間とかオーバータイムの時間とかは後で調べる。各ルールこの粒度の説明を調べる。規定時間もカラムとして持つ。追記終わり

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `mode_rules` | ルール仕様 |
| `win_condition` | 勝利条件 |
| `scoring_rules` | 得点条件 |
| `special_rules` | 特殊仕様 |
| `key_terms` | 用語 |
| `data_signals` | データシグナル |
| `limitations` | データ上の限界 |

### CTF 仕様コンテキスト

追加したい内容:

- 規定数の旗キャプチャで勝利。
- 敵フラッグを自陣のキャプチャ地点へ持ち帰ると得点。
- Arena系CTFでは、自チームのフラッグが自陣に戻っていないと得点できない。
- 自軍旗が取られている状態で敵旗を持ち帰っても、即得点にはならない。
- 旗を持つと通常の射撃ができないため、護衛、ルート選択、タイミングが重要。

用語:

```python
"CTF": {
    "label_ja": "キャプチャー・ザ・フラッグ",
    "key_terms": {
        "pull": "敵フラッグを抜くこと",
        "capture": "敵フラッグを自陣に持ち帰って得点すること",
        "return": "自陣フラッグを元の位置へ戻すこと",
        "reset": "落ちたフラッグが時間経過で初期位置へ戻ること",
        "escort": "旗持ちを護衛すること",
        "counter_pull": "自軍旗を取られている状態で敵旗を抜くこと",
        "flag_standoff": "両チームが相手旗を保持し、どちらも得点できない状態"
    }
}
```

診断ルール例:

```python
"CTF": [
    {
        "condition": "flag_grabs high + flag_captures low",
        "hypothesis": "旗を抜くタイミング、ルート、護衛、敵旗リターン判断に課題がある可能性",
        "counter_evidence": ["flag_carrier_time_sec high", "flag_carriers_killed high"]
    },
    {
        "condition": "flag_returns high + flag_captures low",
        "hypothesis": "防衛貢献はあるが、攻撃のセットアップや旗キャリア護衛に課題がある可能性",
        "counter_evidence": ["team_score close", "damage_diff positive"]
    }
]
```

※ユーザー追記：参考に、各マップでカスタムゲームで実際に旗をドリブルして保持時間、グラブ数などを確認してデータに組み込みたい。追記終わり

### Strongholds 仕様コンテキスト

追加したい内容:

- 3拠点のうち複数を保持して継続得点する。
- 敵が占有しているエリアに複数人で入ると、キャプチャ/奪取ゲージが速く進む。
- ただし複数人で入りすぎると、他エリアの防衛やスポーン制御が薄くなる。
- 3点取りは常に正解ではなく、2点維持が安定戦略になりやすい。

用語:

```python
"Strongholds": {
    "label_ja": "ストロングホールド",
    "key_terms": {
        "capture": "拠点を自チームのものにすること",
        "contest": "敵味方が同じ拠点内にいて進行を止めること",
        "rotate": "次に取る/守る拠点へ移動すること",
        "two_cap": "2拠点保持",
        "trip_cap": "3拠点保持",
        "spawn_flip": "拠点状況や位置取りにより敵味方の湧き位置が大きく変わること"
    }
}
```

診断ルール例:

```python
"Strongholds": [
    {
        "condition": "zone_captures high + win_rate low",
        "hypothesis": "拠点は取れているが維持できていない、または不要な3点取りでスポーンを荒らしている可能性",
        "counter_evidence": ["zone_secures high", "team_score close"]
    },
    {
        "condition": "zone_captures low + damage_diff positive",
        "hypothesis": "撃ち合いでは勝てているが、拠点ローテーションや踏む判断が遅い可能性",
        "counter_evidence": ["zone_def_kills high"]
    }
]
```

### KOTH 仕様コンテキスト

追加したい内容:

- 指定ヒルに入り、保持時間でスコアを進める。
- 複数人でヒルに入っても、スコア進行速度は基本的に1人の時と同じ扱いとしてコンテキスト化する。
- そのため、全員でヒル内に固まるより、周辺クリア、戻りルート遮断、外側カバーが重要。
- ヒル内で死に続けるより、ヒル周辺の有利位置から敵を削る方が有効な場面がある。

用語:

```python
"KOTH": {
    "label_ja": "キング・オブ・ザ・ヒル",
    "key_terms": {
        "hill": "得点対象のエリア",
        "hill_time": "ヒル内にいて得点を進めた時間",
        "setup": "ヒル周辺を制圧して敵の侵入を防ぐ配置",
        "break": "敵が固めたヒル周辺の布陣を崩すこと",
        "rotation": "次のヒルや周辺ポジションへ先回りすること"
    }
}
```

診断ルール例:

```python
"KOTH": [
    {
        "condition": "zone_occupation_sec high + loss",
        "hypothesis": "ヒルには入れているが、周辺制圧や戻りルート遮断が足りない可能性",
        "counter_evidence": ["zone_def_kills high", "team_score close"]
    },
    {
        "condition": "zone_occupation_sec low + k_rpi high",
        "hypothesis": "キルは取れているが、ヒル時間への変換が弱い可能性",
        "counter_evidence": ["zone_off_kills high"]
    }
]
```

### Oddball 仕様コンテキスト

追加したい内容:

- ボール保持中に得点する。
- ボール保持者は通常射撃できないため、保持時間が長いほどキルが低くなるのは自然。
- 不利状況ではボールを外へ捨てる、敵が取りづらい場所へ落とす、時間を稼ぐ判断がある。
- ボール密着ではなく、外側の射線でキャリアを守ることが重要。

用語:

```python
"Oddball": {
    "label_ja": "オッドボール",
    "key_terms": {
        "ball": "得点対象のスカル",
        "carrier": "ボール保持者",
        "play_ball": "敵に取られにくい場所へボールを捨てる判断",
        "setup": "ボール周辺を守る配置",
        "rotate_ball": "安全な場所や味方スポーン側へボールを移すこと"
    }
}
```

診断ルール例:

```python
"Oddball": [
    {
        "condition": "oddball_skull_time_sec high + k_rpi low",
        "hypothesis": "ボール役として自然にキルが低く出ている可能性",
        "counter_evidence": ["oddball_scoring_ticks low", "death_efficiency low"]
    },
    {
        "condition": "oddball_skull_time_sec low + k_rpi low + engagement_density low",
        "hypothesis": "ボール保持にも周辺戦闘にも関与が薄い可能性",
        "counter_evidence": ["d_rpi high", "damage_diff positive"]
    }
]
```

### Slayer 仕様コンテキスト

追加したい内容:

- 規定キル数到達、または時間切れ時のスコア優位で勝利。
- 1デスは敵に1点を渡すため、キル数だけでなくデス抑制が重要。
- リード時は無理な交戦を避ける。
- ビハインド時は単独特攻ではなく、人数有利やパワーアイテムから状況を作る。

用語:

```python
"Slayer": {
    "label_ja": "スレイヤー",
    "key_terms": {
        "trade": "味方が倒された直後に敵を倒し返すこと",
        "pick": "孤立した敵を倒して人数有利を作ること",
        "stagger": "味方と復帰タイミングがずれて人数不利が続くこと",
        "collapse": "複数人で同じ敵やエリアへ一気に詰めること"
    }
}
```

診断ルール例:

```python
"Slayer": [
    {
        "condition": "kills high + deaths high + loss",
        "hypothesis": "キルは取れているが、交換が悪く敵に点を渡しすぎている可能性",
        "counter_evidence": ["team_score close", "damage_diff positive"]
    },
    {
        "condition": "d_rpi high + k_rpi low + engagement_density low",
        "hypothesis": "生存はできているが、味方を助けるキルやダメージ参加が不足している可能性",
        "counter_evidence": ["assists high", "damage_dealt_per_min high"]
    }
]
```

## ゲーム内用語集の追加

現在の `GLOSSARY` は指標説明が中心。ゲーム内用語は `game_terms` として分ける。

```python
"game_terms": {
    "anchor": "味方のスポーン位置を安定させるための位置取り",
    "spawn_control": "敵味方の湧き位置を予測・制御すること",
    "team_shot": "複数人で同じ敵を撃つこと",
    "trade": "味方が倒された直後に敵を倒し返すこと",
    "overextend": "味方のカバーが届かない位置まで押しすぎること",
    "play_ball": "Oddballを敵に取られにくい場所へ捨てる判断",
    "counter_pull": "自軍旗を取られている状態で敵旗を抜くこと",
    "setup": "目標周辺や有利エリアを固めた配置",
    "break": "敵のセットアップを崩すこと",
    "rotate": "次の目標・有利位置へ移動すること"
}
```

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `game_terms` | ゲーム内用語 |
| `anchor` | アンカー |
| `spawn_control` | スポーン制御 |
| `team_shot` | チームショット |
| `trade` | トレード |
| `overextend` | 押しすぎ/伸びすぎ |
| `play_ball` | ボールを捨てる判断 |
| `counter_pull` | カウンタープル |
| `setup` | セットアップ |
| `break` | セットアップ崩し |
| `rotate` | ローテーション |

## ロール / 役割コンテキストの追加

Halo Infiniteには、LoLやOverwatchのような固定職業ロールはない。ただし、試合中の役割やプレイ傾向としてのロールは存在する。

AIコーチングでは、プレイヤーを固定ロールに断定するのではなく、データから見える「この期間の傾向」として扱う。

悪い表現:

```text
あなたはSlayerです。
```

良い表現:

```text
この期間のデータ上は support / objective 寄りの傾向が強いです。
ただし位置情報・味方構成・VCは見えないため、固定ロールではなくプレイ傾向として解釈してください。
```

### roles（ロール/役割）コンテキスト案

```python
"roles": {
    "slayer": {
        "label_ja": "スレイヤー寄り",
        "description": "キルを取り人数有利を作る役割",
        "positive_signals": [
            "high_k_rpi",
            "high_kpm",
            "high_damage_dealt_per_min",
            "high_impact_score"
        ],
        "risk_signals": [
            "high_deaths",
            "low_d_rpi",
            "overextend_risk"
        ],
        "coaching_notes": [
            "キルを取りに行く役割ほど、デスで敵に点やスペースを渡すリスクも高い",
            "キル数だけでなく、交換の質と生存も評価する"
        ]
    },
    "support": {
        "label_ja": "サポート寄り",
        "description": "味方の撃ち合いを補助し、ダメージとアシストで盤面を作る役割",
        "positive_signals": [
            "high_assist_ratio",
            "high_damage_dealt_per_min",
            "stable_d_rpi",
            "team_shot_profile"
        ],
        "risk_signals": [
            "low_k_rpi",
            "low_finishing_rate",
            "passivity_proxy"
        ],
        "coaching_notes": [
            "サポート寄りでもダメージ圧が低い場合は、単なる消極性の可能性がある",
            "アシストと与ダメージが高い場合、K/Dだけで低評価しない"
        ]
    },
    "objective_player": {
        "label_ja": "オブジェクト役寄り",
        "description": "旗・ボール・ヒル・拠点など目標に直接絡む役割",
        "positive_signals": [
            "high_objective_presence",
            "high_zone_time",
            "high_ball_time",
            "flag_actions"
        ],
        "risk_signals": [
            "low_k_rpi_due_to_objective_load",
            "high_deaths_on_objective"
        ],
        "coaching_notes": [
            "オブジェクト役はK-RPIやK/Dが低く出ることがある",
            "オブジェクト関与が得点や勝率に変換されているかを見る"
        ]
    },
    "anchor": {
        "label_ja": "アンカー寄り",
        "description": "味方のスポーンや有利エリアを安定させる役割",
        "positive_signals": [
            "high_d_rpi",
            "low_deaths",
            "stable_damage_diff",
            "consistent_presence"
        ],
        "risk_signals": [
            "low_engagement_density",
            "low_damage_pressure",
            "passivity_proxy"
        ],
        "limitations": [
            "位置情報がないため直接推定は難しい",
            "スポーン制御は代理指標でしか見られない"
        ],
        "coaching_notes": [
            "生存が高くても、味方の湧きやエリア維持に貢献しているかは直接見えない",
            "低デスと低関与を混同しない"
        ]
    },
    "entry": {
        "label_ja": "エントリー寄り",
        "description": "最初に接触して敵の位置を割り、味方が詰めるきっかけを作る役割",
        "positive_signals": [
            "high_engagement_density",
            "high_damage_taken_per_min",
            "assist_ratio",
            "opening_pressure_proxy"
        ],
        "risk_signals": [
            "low_d_rpi",
            "high_deaths",
            "ego_challenge_risk_proxy"
        ],
        "limitations": [
            "最初の接敵タイミングはDBから直接見えない"
        ],
        "coaching_notes": [
            "Entry傾向は有効な起点作りと無謀な突入の区別が重要",
            "高い被ダメージが味方のキルに繋がっているかを見る"
        ]
    },
    "power_item_controller": {
        "label_ja": "パワーアイテム管理寄り",
        "description": "Power Weapon / Power Up 周辺の管理、取得、活用を担う役割",
        "positive_signals": [
            "high_power_kills",
            "high_pw_control_rate",
            "power_item_map_context"
        ],
        "risk_signals": [
            "low_pw_control_rate_on_pw_maps",
            "high_deaths_on_power_item_timing"
        ],
        "limitations": [
            "Camo / Overshield の取得・活用は直接見えない",
            "Shock Rifle はPowerWeaponKillsに反映されない可能性がある"
        ],
        "coaching_notes": [
            "PWが強いマップとPWが薄いマップを同列に評価しない",
            "PWキルだけでなく、PWを取らせない動きも重要だが直接観測しづらい"
        ]
    }
}
```

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `roles` | ロール/役割 |
| `description` | 説明 |
| `positive_signals` | 良いシグナル |
| `risk_signals` | リスクシグナル |
| `limitations` | 推定上の限界 |
| `coaching_notes` | コーチング時の注意 |

### role_profile（ロール傾向）特徴量

`features` に `role_profile` を追加する。

```json
"role_profile": {
  "label_ja": "ロール傾向",
  "primary_tendency": "support_objective",
  "primary_tendency_label_ja": "サポート/オブジェクト寄り",
  "secondary_tendency": "anchor",
  "secondary_tendency_label_ja": "アンカー寄り",
  "scores": {
    "slayer": 0.42,
    "support": 0.71,
    "objective_player": 0.66,
    "anchor": 0.58,
    "entry": 0.39,
    "power_item_controller": 0.31
  },
  "evidence": {
    "support": [
      "assist_ratio high",
      "damage_dealt_per_min above baseline"
    ],
    "objective_player": [
      "zone_occupation_sec high"
    ]
  },
  "caution": "ロールは固定役職ではなく、この期間のデータから見た傾向"
}
```

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `role_profile` | ロール傾向 |
| `primary_tendency` | 第一傾向 |
| `secondary_tendency` | 第二傾向 |
| `scores` | ロール別スコア |
| `evidence` | 根拠 |
| `caution` | 注意書き |

### ロール推定用の追加特徴量

既存DataFrameから作れそうなもの:

- `assist_ratio = assists / (kills + assists)`
- `damage_pressure = damage_dealt_per_min`
- `finish_profile = kills / damage_dealt`
- `survival_profile = d_rpi, deaths, damage_taken_per_min`
- `objective_presence_by_mode`
- `power_item_profile = power_kills, pw_control_rate`
- `engagement_profile = engagement_density, kpm, dpm`
- `ego_challenge_risk_proxy`
- `passivity_proxy`

### ロール診断時の注意

- 固定ロールとして断定しない。
- チーム構成、味方の役割、VC、位置情報がないことを明示する。
- オブジェクト役はK/DやK-RPIが低く出ることがあるため、ルール別スタッツとセットで見る。
- Support傾向と消極性を混同しない。
- Entry傾向と無謀なデスを混同しない。
- Anchor傾向は位置情報なしでは特に推定が難しい。

## mode_metric_limitations（ルール別のデータ限界）の追加

ルールごとにDBから見えないものを明示する。

```python
"mode_metric_limitations": {
    "CTF": [
        "旗をどのルートで運んだかは分からない",
        "自軍旗が取られていたかどうかの時系列は分からない",
        "旗キャリアへの護衛距離は分からない"
    ],
    "KOTH": [
        "ヒル内に複数人いたかは分からない",
        "ヒル外の戻りルートを抑えていたかは分からない"
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
```

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `mode_metric_limitations` | ルール別のデータ限界 |
| `CTF` | キャプチャー・ザ・フラッグ |
| `KOTH` | キング・オブ・ザ・ヒル |
| `Strongholds` | ストロングホールド |
| `Oddball` | オッドボール |

このカテゴリを入れると、AIがルールの仕様を踏まえて「観測可能な事実」と「推測」を分けやすくなる。

### fundamentals（共通基礎）

Reddit / CompetitiveHalo系の改善スレで繰り返し出てくる考え方:

- 味方の位置を見て敵スポーンを推測する。
- 先撃ちされたら無理に撃ち返さず、生存を優先する。
- 高台、遮蔽物、逃げ道を持って撃ち合う。
- 単独キルより、味方の射線に合わせてダメージを出す。
- Power Weapon / Power Up / 重要ポジションを中心に動く。
- マップの約2/3を取って敵スポーンを狭める。

Reddit由来の情報は断定ではなく `community_heuristic` として扱う。

参考:

- https://www.reddit.com/r/CompetitiveHalo/comments/rzq9zo
- https://www.reddit.com/r/CompetitiveHalo/comments/r9x927
- https://www.reddit.com/r/CompetitiveHalo/comments/rjmk8b

### Slayer（スレイヤー）

```python
"slayer": {
    "primary_goal": "死なずに有利交換を積む",
    "common_mistakes": [
        "人数不利で再チャレンジする",
        "味方から離れて単独で深追いする",
        "リード時に無理に攻めてデスを献上する"
    ],
    "data_signals": {
        "too_aggressive": ["high_kpm", "high_dpm", "low_d_rpi"],
        "too_passive": ["low_engagement_density", "low_k_rpi", "high_d_rpi"]
    }
}
```

### CTF（キャプチャー・ザ・フラッグ）

追加したい観点:

- pull timing: 敵が2枚以上落ちた後に旗を触れているか。
- route discipline: 旗ルートを無意味に変えすぎていないか。
- escort vs overextend: キャリア護衛に寄れているか。
- return priority: 自陣旗が出ている時に敵陣へ行きすぎていないか。
- spawn control: 敵を片側に湧かせて反対側に旗を通せているか。

直接観測できないものが多いため、`flag_grabs`, `flag_captures`, `flag_carrier_time_sec`, `flag_returns`, `flag_carriers_killed`, `k_rpi`, `d_rpi` の代理指標で見る。

### Oddball（オッドボール）

追加したい観点:

- ball rotation: 味方スポーン側へ逃がす。
- play ball: 不利時に外へ捨てる/落とす判断。
- push past ball: ボールを持つ前に敵の戻りルートを潰す。
- carrier protection: ボール密着ではなく外側で射線を作る。

診断例:

```text
もし Oddball で D-RPI は高いが K-RPI と engagement_density が低いなら、
守りすぎ、ボール周辺の外側カバー不足、仕掛けの遅さを疑う。
ただし ball_time が高い場合は役割上キルが低い可能性を考慮する。
```

### Strongholds（ストロングホールド）

コミュニティでよく出る考え:

- 3点取りより2点安定。
- 3点目を取りに行って敵スポーンを荒らすと逆に不利になる。
- 3点目は敵が全落ち、または大きくビハインドの時などに限定する。
- 敵が湧きそうな1/3を予測し、2/3のマップ支配を維持する。

参考:

- https://www.reddit.com/r/CompetitiveHalo/comments/1ix5nf5

### KOTH（キング・オブ・ザ・ヒル）

追加したい観点:

- ヒルを踏む前に周辺をクリアする。
- ヒル周辺だけでなく、敵の戻りルートを塞ぐ。
- ヒル内で死に続けるより、周辺の有利位置から敵を削る。
- 防御キルと攻撃キルのバランスを見る。

## community_heuristics（コミュニティ由来の仮説）の設計

Redditやコミュニティ由来のセオリーは、ソースと信頼度を付けて短い仮説として保存する。

```python
"community_heuristics": {
    "label_ja": "コミュニティ由来の仮説",
    "solo_queue": [
        {
            "name": "support_when_struggling",
            "idea": "撃ち負けが続く時は単独キル狙いより味方の後ろからダメージとカバーを優先する",
            "data_signals": ["low_k_rpi", "high_deaths", "low_d_rpi"],
            "confidence": "community_heuristic",
            "source": "reddit"
        },
        {
            "name": "avoid_ego_challenge",
            "idea": "先撃ちされた撃ち合いを継続しすぎるとデス効率が悪化する",
            "data_signals": ["high_damage_taken_per_min", "low_d_rpi"]
        }
    ],
    "map_control": [
        {
            "name": "two_thirds_control",
            "idea": "マップの約2/3を取り、敵スポーンを残り1/3に寄せる",
            "observable_proxy": ["pw_control_rate", "team_score_diff", "objective_stats"]
        }
    ]
}
```

キーの日本語:

| 英語キー | 日本語ラベル |
|---|---|
| `community_heuristics` | コミュニティ由来の仮説 |
| `solo_queue` | ソロキュー |
| `map_control` | マップコントロール |
| `name` | 仮説名 |
| `idea` | 考え方 |
| `data_signals` | データシグナル |
| `confidence` | 信頼度 |
| `source` | ソース |
| `observable_proxy` | 観測できる代理指標 |

## 追加したい特徴量

まずは既存DataFrameから作れるものを優先する。

### recent_vs_baseline（直近比較）

直近20戦 vs それ以前、または選択期間 vs 全期間。

目的:

- 最近改善しているのか、崩れているのかをAIが見やすくする。

対象:

- `win_rate`: 勝率
- `kd_ratio`: K/D
- `kda`: KDA
- `accuracy`: 命中率
- `damage_diff`: ダメージ差
- `k_rpi`: K-RPI / 期待キルに対する達成率
- `d_rpi`: D-RPI / 期待デスに対する生存率
- `impact_score`: インパクトスコア
- `pw_control_rate`: パワーウェポンコントロール率
- `engagement_density`: エンゲージメント密度

### win_loss_delta（勝敗差分）

勝ち試合平均と負け試合平均の差。

目的:

- 勝敗に効いていそうな指標をAIに明示する。

### map_mode_matrix（マップ×ルール表）

`map_name x rule_name` の勝率、KDA、試合数。

目的:

- 苦手マップではなく、苦手なマップ/ルール組み合わせを見つける。

### confidence（信頼度）

各集計に `n`, `confidence_level`, `warning` を付ける。

目的:

- AIの断定を防ぐ。

### support_profile（サポート傾向）

アシスト、与ダメージ/分、K-RPIなどからサポート寄りかフィニッシュ寄りかを見る。

候補:

```text
assist_ratio = assists / (kills + assists)
damage_without_finish_proxy = high_damage_dealt_per_min + low_k_rpi
```

### ego_challenge_risk_proxy（無理な撃ち合いリスク）

無理な撃ち合いの疑い。

候補シグナル:

- `high_damage_taken_per_min`: 被ダメージ/分が高い
- `low_d_rpi`: D-RPIが低い
- `high_dpm`: デス/分が高い
- `low_death_efficiency`: デス効率が低い

### passivity_proxy（消極性の疑い）

生存はできているが圧が低い疑い。

候補シグナル:

- `high_d_rpi`: D-RPIが高い
- `low_k_rpi`: K-RPIが低い
- `low_engagement_density`: エンゲージメント密度が低い
- `low_damage_dealt_per_min`: 与ダメージ/分が低い

### objective_involvement_by_mode（ルール別オブジェクト関与）

CTF/Oddball/Strongholds/KOTHを別々にスコア化する。すべてを同じ「オブジェクト貢献」にしない。

### lobby_bucket_summary（ロビー格差別サマリー）

LGAIを格下/同格/格上に分けて集計する。

目的:

- 勝率だけで実力を誤診断しない。

## metric_limitations（指標の限界）に入れるべき内容

- Shock Rifle は `PowerWeaponKills` に反映されない可能性があり、`pw_control_rate` は過小評価になる。
- 装備の取得/使用ログがないため、RepulsorやThrusterの使い方は直接評価できない。
- 位置情報がないため、アンカー、スポーン制御、射線管理は代理指標でしか見られない。
- VCや味方とのコミュニケーションは観測できない。
- 旗ルート、ボール投棄、ヒル周辺ポジションなどの細かい判断は直接観測できない。
- サンプル数が少ないマップ/ルールは断定しない。

## SUGGESTED_PROMPT（AIへの指示文）の修正方針

追加したい指示:

```text
0. ユーザー向けのコーチング出力は日本語で書く。
   内部キーが英語でも、説明では日本語ラベルを優先する。
   ※ユーザー追記：将来の英語対応のために、ユーザーの使用言語を参照するとかにしといたほうが？追記終わり
1. まず勝敗差分を見る。
2. 次に最近の変化を見る。
3. その後、ルール別・マップ別に原因を分ける。
4. common_mistakes（よくあるミス）と data_signals（データシグナル）を照合する。
5. sample_size（サンプル数）が少ない項目は仮説として扱う。
6. metric_limitations（指標の限界）に書かれた制約を必ず考慮する。
7. 位置取り、VC、意図などDBにない情報は断定しない。
8. 改善提案は最大3つに絞り、各提案に根拠指標を添える。
```

## 実装優先順位

### Phase A: JSON構造を整える

1. `analysis_contract`（分析ルール）を追加する。
2. `features`（AI向け特徴量）に `win_loss_delta`（勝敗差分）を追加する。
3. `features`（AI向け特徴量）に `recent_vs_baseline`（直近比較）を追加する。
4. `summary`（集計サマリー）に `map_mode_matrix`（マップ×ルール表）を追加する。
5. `metric_limitations`（指標の限界）を追加する。

### Phase B: コンテキスト分離

1. `GAME_CONTEXT` を `halo_knowledge` 系モジュールに移動する。
2. マップの `notes`（メモ）から日付・アイテム・構造を独立フィールド化する。
3. `equipment`（装備/アビリティ）と `power_items`（パワーアイテム）を追加する。
4. `build_relevant_context(stat_df)`（対象データ用の文脈抽出）を作り、対象データに出るマップ/ルールだけを渡す。

### Phase C: セオリー補強

1. `fundamentals`（共通基礎）を追加する。
2. モード別に `common_mistakes`（よくあるミス）, `data_signals`（データシグナル）, `counter_evidence`（反証条件）を追加する。
3. `community_heuristics`（コミュニティ由来の仮説）を追加する。
4. 公式ソースとコミュニティソースを分ける。

### Phase D: ルール仕様の追加

1. `mode_rules`（ルール仕様）を追加する。
2. `game_terms`（ゲーム内用語）を追加する。
3. `rule_diagnostics`（ルール別診断ルール）を追加する。
4. `mode_metric_limitations`（ルール別のデータ限界）を追加する。
5. CTF / Strongholds / KOTH / Oddball / Slayer の仕様を公式情報ベースで整理する。

### Phase E: ロール推定の追加

1. `roles`（ロール/役割）コンテキストを追加する。
2. `features.role_profile`（ロール傾向）を追加する。
3. ロール推定用の特徴量を追加する。
4. AIプロンプトに「ロールは固定職ではなく傾向」と明記する。
5. ロール別の改善提案を出せるようにする。

## 目指す出力

AIに以下のような診断をさせたい。

```text
直近20戦ではK-RPIがベースラインより下がっているが、D-RPIは維持できている。
特にOddballで engagement_density が低く、ball_time も高くないため、
単にボール役でキルが低いというより、仕掛けの遅さか外側カバー不足の可能性がある。
ただし位置情報はないため仮説。

改善提案:
1. Oddballではボールを持つ前に、敵の戻りルート側へ1枚分だけ押し上げる。
   根拠: OddballのK-RPI低下、engagement_density低下。
2. 先撃ちされた撃ち合いは離脱優先。
   根拠: damage_taken_per_min高、D-RPI低。
```

## メモ

このリファクタリングの核心は、セオリーをたくさん書くことではなく、AIが使える診断形式にすること。

良い形:

```text
文脈 + データシグナル + 反証条件 + 信頼度
```

悪い形:

```text
長い一般論だけを渡す
```
