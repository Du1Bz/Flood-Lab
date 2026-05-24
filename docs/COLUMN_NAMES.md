# Flood-Lab カラム名対応表

内部DataFrame（英語スネークケース）と表示名（日本語）の対応。  
Floodとの互換性は考慮しない。Flood-Lab単体として設計。

凡例：
- **ソース** = OpenSpartan DBのどのフィールドから取るか
- **Flood内部名** = Floodのparser.py/metrics.pyで使っていた名前（参考）
- **内部カラム名** = Flood-LabのDataFrameで使う名前（英語スネークケース）
- **表示名** = UIに出す日本語名

---

## 識別・メタ情報

| Flood内部名 | 内部カラム名 | 表示名 | ソース |
|---|---|---|---|
| MatchID | `match_id` | 試合ID | `MatchStats.MatchId` |
| 日時 | `played_at` | 日時 | `MatchStats.MatchInfo.StartTime`（JST変換） |
| 区分 | `playlist` | 区分 | `MatchInfo.Playlist` から分類 |
| マップ | `map_name` | マップ | `PlaylistMapModePair.PublicName` から抽出 |
| ルール | `rule_name` | ルール | `PlaylistMapModePair.PublicName` から抽出 |
| 勝敗 | `result` | 勝敗 | `Players[].Outcome`（`"win"` / `"loss"` / `"draw"`） |
| - | `result_flag` | 勝敗フラグ | `result` から計算（`1` / `0`） |
| - | `exclude_flag` | 除外フラグ | ルールベースで自動付与（`""` / `"short_match"` / `"incomplete"` / `"manual"`） |
| - | `session_id` | セッションID | `build_sessions()` で付与 |
| - | `session_seq` | セッション内試合番号 | セッション分割後に連番付与（1始まり） |

### `result`（勝敗）の値

API の `Outcome` フィールドは数値で返ってくる。parser.py で文字列に変換する。

| API値 | 内部値 | 表示名 |
|---|---|---|
| `1` | `"win"` | 勝ち |
| `2` | `"loss"` | 負け |
| `3` | `"draw"` | 引き分け |
| `4` | `"did_not_finish"` | 途中抜け |

`Outcome=4` または `PresentAtEndOfMatch=false` のとき `exclude_flag = "incomplete"` を付与する。

### `playlist`（区分）の値

`LifecycleMode` と `PlaylistExperience` の組み合わせで分類する。

**`LifecycleMode`**

| API値 | 意味 |
|---|---|
| `1` | カスタムゲーム → `"custom"` |
| `3` | マッチメイド → `PlaylistExperience` で細分化 |

**`PlaylistExperience`**（`LifecycleMode=3` のとき）

| API値 | 内部値 | 表示名 |
|---|---|---|
| `2` | `"ranked_arena"` | ランクアリーナ |
| `3` | `"ranked_slayer"` | ランクスレイヤー |
| `5` | `"social"` | ソーシャル |
| `6` | `"minigame"` | ミニゲーム |
| `9` | `"btb"` | BTB |
| その他 | `"other"` | Other |

> Flood では `"ランクアリーナ"` 等の日本語を使っていたが、Flood-Lab では英語で統一する。

### `PlayerType`（プレイヤー種別）

XUID絞り込み時に `PlayerType=1` でBotを除外する。

| API値 | 意味 |
|---|---|
| `1` | 人間プレイヤー |
| `2` | Bot |

---

## 基礎スタッツ

| Flood内部名 | 内部カラム名 | 表示名 | ソース |
|---|---|---|---|
| キル | `kills` | キル | `PlayerTeamStats[0].Stats.CoreStats.Kills` |
| デス | `deaths` | デス | `PlayerTeamStats[0].Stats.CoreStats.Deaths` |
| アシスト | `assists` | アシスト | `PlayerTeamStats[0].Stats.CoreStats.Assists` |
| 命中数 | `shots_hit` | 命中数 | `CoreStats.ShotsHit` |
| 発射数 | `shots_fired` | 発射数 | `CoreStats.ShotsFired` |
| 与ダメージ | `damage_dealt` | 与ダメージ | `CoreStats.DamageDealt` |
| 被ダメージ | `damage_taken` | 被ダメージ | `CoreStats.DamageTaken` |
| 個人スコア | `score` | 個人スコア | `CoreStats.Score` |
| 重火器キル | `power_kills` | 重火器キル | `CoreStats.PowerWeaponKills` |
| パーフェクトキル | `perfect_kills` | パーフェクトキル | `Medals[NameId=1512363953].Count`（再帰走査） |
| チーム内順位 | `team_rank` | チーム内順位 | `Players[].Rank` |
| 自チームMMR | `team_mmr` | 自チームMMR | `PlayerMatchStats.Result.TeamMmrs[自チームID]` |
| 敵チームMMR | `enemy_mmr` | 敵チームMMR | `PlayerMatchStats.Result.TeamMmrs[敵チームID]` |
| チームスコア（自） | `team_score` | 自チームスコア | `Teams[自チーム].Stats.CoreStats.Score` |
| チームスコア（敵） | `enemy_score` | 敵チームスコア | `Teams[敵チーム].Stats.CoreStats.Score` |
| 自チームPWキル | `team_pw_kills` | 自チームPWキル | `Teams[自チーム].Stats.CoreStats.PowerWeaponKills` |
| 敵チームPWキル | `enemy_pw_kills` | 敵チームPWキル | `Teams[敵チーム].Stats.CoreStats.PowerWeaponKills` |
| 試合時間 | `duration_sec` | 試合時間（秒） | `MatchInfo.Duration`（ISO 8601 → 秒） |
| パーティ人数 | `party_size` | パーティ人数 | `build_party_map()` で推定 |
| - | `party_type` | パーティタイプ | `party_size` から計算（ソロ/デュオ/トリオ/フルパ） |

> **`duration_sec` は秒数（int）で持つ。**  
> Flood では `"7:06"` という文字列で持っていたため `試合時間(計算用)` という変換カラムが別途必要だった。  
> Flood-Lab では秒数で保持し、表示時に `MM:SS` 形式に変換する。

---

## CSR 系

| Flood内部名 | 内部カラム名 | 表示名 | ソース |
|---|---|---|---|
| 試合前CSR | `csr_pre` | 試合前CSR | `PlayerMatchStats.Result.RankRecap.PreMatchCsr.Value` |
| 試合後CSR | `csr_post` | 試合後CSR | `PlayerMatchStats.Result.RankRecap.PostMatchCsr.Value` |
| CSR増減（Notion数式） | `csr_delta` | CSR増減 | `csr_post - csr_pre` |
| AvgCSR20 | `csr_avg20` | 直近20試合平均CSR | `build_avg_csr_map_from_parsed()` |

---

## TrueSkill2 系

| Flood内部名 | 内部カラム名 | 表示名 | ソース / 計算式 |
|---|---|---|---|
| 期待キル | `expected_kills` | 期待キル | `PlayerMatchStats.Result.StatPerformances.Kills.Expected` |
| 期待デス | `expected_deaths` | 期待デス | `PlayerMatchStats.Result.StatPerformances.Deaths.Expected` |
| K-RPI(相対パフォーマンス指数) | `k_rpi` | K-RPI | `kills / expected_kills` |
| D-RPI(相対パフォーマンス指数) | `d_rpi` | D-RPI | `expected_deaths / deaths` |
| LGAI: ロビー格差補正インパクト | `lgai` | LGAI | `enemy_mmr - csr_pre` |
| インパクトスコア | `impact_score` | インパクトスコア | `(k_rpi + d_rpi) / 2` |
| 生存貢献度 | `survival_contribution` | 生存貢献度 | `(expected_deaths - deaths) × (enemy_mmr / csr_pre)` |

---

## eMMR 系

| Flood内部名 | 内部カラム名 | 表示名 | ソース / 計算式 |
|---|---|---|---|
| eMMR(試合前) | `emmr_pre` | eMMR（試合前） | `calc_emmr()` で計算（前試合の試合後） |
| eMMR(試合後) | `emmr_post` | eMMR（試合後） | `calc_emmr()` で計算 |
| eMMR_v2 | `emmr_v2` | eMMR v2 | `batch_calc_emmr_v2()` カルマンフィルタ |
| eMMR_v2_sigma | `emmr_v2_sigma` | eMMR v2 不確実性 | `batch_calc_emmr_v2()` カルマン分散 |

---

## 計算指標（processor.py で生成）

| Flood内部名（Notion数式） | 内部カラム名 | 表示名 | 計算式 |
|---|---|---|---|
| K/D | `kd_ratio` | K/D | `kills / deaths`（deaths=0 のとき `kills`） |
| KDA | `kda` | KDA | `kills - deaths + assists / 3` |
| 命中率 | `accuracy` | 命中率 | `shots_hit / shots_fired`（0除算は `None`） |
| ダメージ差 | `damage_diff` | ダメージ差 | `damage_dealt - damage_taken` |
| キル効率 | `kill_efficiency` | キル効率 | `damage_dealt / (kills + assists/3)`（0除算は `None`） |
| デス効率 | `death_efficiency` | デス効率 | `damage_taken / deaths`（0除算は `None`） |
| パーフェクト率 | `perfect_rate` | パーフェクト率 | `perfect_kills / kills`（0除算は `None`） |
| 試合時間(計算用) | ― | ― | 廃止。`duration_sec` を直接使う |
| KPM | `kpm` | KPM | `kills / (duration_sec / 60)` |
| DPM | `dpm` | DPM | `deaths / (duration_sec / 60)` |
| 与ダメージ/分 | `damage_dealt_per_min` | 与ダメージ/分 | `damage_dealt / (duration_sec / 60)` |
| 被ダメージ/分 | `damage_taken_per_min` | 被ダメージ/分 | `damage_taken / (duration_sec / 60)` |
| 重火器キル密度 | `power_kill_density` | 重火器キル密度 | `power_kills / (duration_sec / 60)` |
| PWコントロール率 | `pw_control_rate` | PWコントロール率 | `team_pw_kills / (team_pw_kills + enemy_pw_kills)`（両チーム0のとき`None`） |
| エンゲージメント密度 | `engagement_density` | エンゲージメント密度 | `(kills + deaths + assists) / (duration_sec / 60)` |
| eMMR増減 | `emmr_delta` | eMMR増減 | `emmr_post - emmr_pre` |

---

## フラグ・補助カラム（内部用・集計用）

| Flood内部名 | 内部カラム名 | 表示名 | 計算式 |
|---|---|---|---|
| 勝敗フラグ | `result_flag` | 勝敗フラグ | `1` if `result == "win"` else `0` |
| ソロフラグ | `is_solo` | ソロフラグ | `party_size == 1` |
| パーティフラグ | `is_party` | パーティフラグ | `party_size > 1` |
| パーティタイプ | `party_type` | パーティタイプ | `party_size` を `"ソロ"/"デュオ"/"トリオ"/"フルパ"` にラベル化 |
| 試合数 | ― | ― | 廃止。`count()` で代替 |
| 勝利数 | ― | ― | 廃止。`sum(result_flag)` で代替 |
| ソロ勝利フラグ | ― | ― | 廃止。`is_solo & result_flag` で代替 |
| パーティ勝利フラグ | ― | ― | 廃止。`is_party & result_flag` で代替 |
| 論理削除フラグ | `exclude_flag` | 除外フラグ | 文字列。空文字 = 対象、`"short_match"` / `"incomplete"` / `"manual"` = 除外 |

> Floodでは集計ロールアップのために `勝利数=if(勝敗フラグ==1, 1, 0)` や `試合数=1` という迂回カラムが必要だった。  
> Flood-Labでは Pandas の `groupby().agg()` で直接集計するため不要。

---

## 表示名変換ユーティリティ

`src/utils/display.py` に定数を定義し、ビュー側で参照する。

```python
# API数値 → 内部値への変換（parser.pyで使用）
OUTCOME_MAP = {
    1: "win",
    2: "loss",
    3: "draw",
    4: "did_not_finish",
}

PLAYLIST_MAP = {
    # LifecycleMode=1
    "custom": "custom",
    # LifecycleMode=3 × PlaylistExperience
    2: "ranked_arena",
    3: "ranked_slayer",
    5: "social",
    6: "minigame",
    9: "btb",
}

# 内部値 → 表示名への変換（ビュー側で使用）
DISPLAY_NAMES = {
    "match_id":               "試合ID",
    "played_at":              "日時",
    "playlist":               "区分",
    "map_name":               "マップ",
    "rule_name":              "ルール",
    "result":                 "勝敗",
    "result_flag":            "勝敗フラグ",
    "exclude_flag":           "除外フラグ",
    "session_id":             "セッションID",
    "session_seq":            "セッション内試合番号",
    "kills":                  "キル",
    "deaths":                 "デス",
    "assists":                "アシスト",
    "shots_hit":              "命中数",
    "shots_fired":            "発射数",
    "damage_dealt":           "与ダメージ",
    "damage_taken":           "被ダメージ",
    "score":                  "個人スコア",
    "power_kills":            "重火器キル",
    "perfect_kills":          "パーフェクトキル",
    "team_rank":              "チーム内順位",
    "team_mmr":               "自チームMMR",
    "enemy_mmr":              "敵チームMMR",
    "team_score":             "自チームスコア",
    "enemy_score":            "敵チームスコア",
    "duration_sec":           "試合時間（秒）",
    "party_size":             "パーティ人数",
    "party_type":             "パーティタイプ",
    "csr_pre":                "試合前CSR",
    "csr_post":               "試合後CSR",
    "csr_delta":              "CSR増減",
    "csr_avg20":              "直近20試合平均CSR",
    "expected_kills":         "期待キル",
    "expected_deaths":        "期待デス",
    "k_rpi":                  "K-RPI",
    "d_rpi":                  "D-RPI",
    "lgai":                   "LGAI",
    "impact_score":           "インパクトスコア",
    "survival_contribution":  "生存貢献度",
    "emmr_pre":               "eMMR（試合前）",
    "emmr_post":              "eMMR（試合後）",
    "emmr_delta":             "eMMR増減",
    "emmr_v2":                "eMMR v2",
    "emmr_v2_sigma":          "eMMR v2 不確実性",
    "kd_ratio":               "K/D",
    "kda":                    "KDA",
    "accuracy":               "命中率",
    "damage_diff":            "ダメージ差",
    "kill_efficiency":        "キル効率",
    "death_efficiency":       "デス効率",
    "perfect_rate":           "パーフェクト率",
    "kpm":                    "KPM",
    "dpm":                    "DPM",
    "damage_dealt_per_min":   "与ダメージ/分",
    "damage_taken_per_min":   "被ダメージ/分",
    "power_kill_density":     "重火器キル密度",
    "is_solo":                "ソロ",
    "is_party":               "パーティ",
}

PLAYLIST_DISPLAY = {
    "ranked_arena":  "ランクアリーナ",
    "ranked_slayer": "ランクスレイヤー",
    "social":        "ソーシャル",
    "minigame":      "ミニゲーム",
    "btb":           "BTB",
    "custom":        "カスタムゲーム",
    "other":         "Other",
}

RESULT_DISPLAY = {
    "win":            "勝ち",
    "loss":           "負け",
    "draw":           "引き分け",
    "did_not_finish": "途中抜け",
}
```