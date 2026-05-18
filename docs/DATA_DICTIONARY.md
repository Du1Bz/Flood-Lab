# Flood-Lab データディクショナリ

OpenSpartan DB に格納されている API レスポンス JSON の全フィールドと、  
Flood-Lab がそれをどう解釈・加工して DataFrame にしているかを網羅する。

---

## 目次

1. [概要：データフロー](#1-概要データフロー)
2. [テーブル一覧](#2-テーブル一覧)
3. [テーブル別 JSON フィールド定義](#3-テーブル別-json-フィールド定義)
   - 3.1 [MatchStats（試合データ）](#31-matchstats試合データ)
   - 3.2 [PlayerMatchStats（プレイヤー別統計）](#32-playermatchstatsプレイヤー別統計)
   - 3.3 [Maps（マップメタデータ）](#33-mapsマップメタデータ)
   - 3.4 [Playlists（プレイリスト定義）](#34-playlistsプレイリスト定義)
   - 3.5 [PlaylistMapModePairs（プレイリスト-マップ紐付け）](#35-playlistmapmodepairsプレイリスト-マップ紐付け)
   - 3.6 [GameVariants（UGC ゲームバリアント）](#36-gamevariantsugc-ゲームバリアント)
   - 3.7 [EngineGameVariants（エンジンバリアント）](#37-enginegamevariantsエンジンバリアント)
   - 3.8 [InventoryItems（インベントリアイテム）](#38-inventoryitemsインベントリアイテム)
   - 3.9 [OwnedInventoryItems（所有アイテム）](#39-ownedinventoryitems所有アイテム)
   - 3.10 [OperationRewardTracks（報酬トラック）](#310-operationrewardtracks報酬トラック)
   - 3.11 [PlaylistCSRSnapshots（CSRスナップショット）](#311-playlistcsrsnapshots-csrスナップショット)
   - 3.12 [ServiceRecordSnapshots（通算戦績）](#312-servicerecordsnapshots通算戦績)
4. [API 生値 → 内部値 変換マップ](#4-api-生値--内部値-変換マップ)
5. [Flood-Lab DataFrame カラム一覧（内部カラム名）](#5-flood-lab-dataframe-カラム一覧内部カラム名)
6. [計算指標の定義](#6-計算指標の定義)
7. [除外フラグ判定ルール](#7-除外フラグ判定ルール)
8. [eMMR 計算パラメータ](#8-emmr-計算パラメータ)

---

## 1. 概要：データフロー

```
Halo Infinite API (343 Industries)
  ↓ OpenSpartan Workshop が定期的に同期
SQLite DB (%LOCALAPPDATA%\OpenSpartan.Workshop\data\{xuid}.db)
  ↓ database.py: 各テーブルの ResponseBody (JSON) を読み取り raw DataFrame に展開
  ↓ processor.py: パイプライン処理（パーティ検出 → セッション分割 → 指標計算）
  ↓
分析用 DataFrame（各ビューで利用）
```

## 2. テーブル一覧

| No. | テーブル名 | レコード数（実測） | 説明 |
|-----|-----------|-------------------|------|
| 1 | `MatchStats` | 3,374 | **試合単位の全データ**。最も重要なテーブル |
| 2 | `PlayerMatchStats` | 3,374 | **プレイヤー個人の TrueSkill2・CSR 情報**。MatchId で MatchStats と結合 |
| 3 | `Maps` | 246 | マップのメタデータ（名前・作者・タグ） |
| 4 | `Playlists` | 28 | プレイリスト定義（名称・ローテーション） |
| 5 | `PlaylistMapModePairs` | 465 | プレイリスト×マップ×ルールの組み合わせ |
| 6 | `GameVariants` | 106 | UGC（ユーザー作成）ゲームバリアント |
| 7 | `EngineGameVariants` | 55 | エンジン標準ゲームバリアント（Slayer/CTF/Strongholds 等） |
| 8 | `InventoryItems` | 1,007 | 全インベントリアイテムの定義（カタログ） |
| 9 | `OwnedInventoryItems` | 9,168 | プレイヤーが所有するアイテム（所持数・取得日） |
| 10 | `OperationRewardTracks` | 31 | オペレーション（バトルパス）の報酬トラック |
| 11 | `PlaylistCSRSnapshots` | 20 | プレイリスト別 CSR スナップショット履歴 |
| 12 | `ServiceRecordSnapshots` | 5 | 通算戦績スナップショット（全期間集計） |

> Flood-Lab が分析に使うのは主に **MatchStats** と **PlayerMatchStats**。  
> 他のテーブルはマップ名解決・プレイリスト分類などの補助に使われる。

---

## 3. テーブル別 JSON フィールド定義

各テーブルは `ResponseBody` カラムに JSON 文字列として全データを格納する。  
加えて、よく使われるパスは Generated Always の virtual column として抽出されている。

---

### 3.1. MatchStats（試合データ）

#### DB スキーマ

```sql
CREATE TABLE MatchStats (
    ResponseBody TEXT,
    MatchId  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MatchId'))  VIRTUAL,
    MatchInfo Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MatchInfo')) VIRTUAL,
    Teams    Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Teams'))    VIRTUAL,
    Players  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Players'))  VIRTUAL
)
```

> `json_extract` は JSON オブジェクトのまま抽出するため、TEXT 型だが中身は JSON string。

#### トップレベル（ResponseBody JSON）

| フィールド | 型 | null | 説明 | 備考 |
|-----------|----|------|------|------|
| `MatchId` | string (UUID) | 0% | 試合の一意識別子 | `PlayerMatchStats.MatchId` と結合キー |
| `MatchInfo` | object | 0% | 試合の基本情報 | 下記詳細 |
| `Players` | array[Player] | 0% | 参加プレイヤー全員のリスト | Bot も含む。要素数: 1〜31 |
| `Teams` | array[Team] | 0% | チーム情報（0/1 の2チーム） | FFA 等で空配列の場合あり（5.7%） |

> ResponseBody JSON のトップレベルキーは **この4つだけ**。  
> `GameVersion` や `IsBuildLobby` 等のフィールドは MatchStats には存在しない。

#### MatchInfo（MatchStats.MatchInfo）

| フィールド | 型 | null | 説明 |
|-----------|----|------|------|
| `StartTime` | string (ISO 8601) | 0% | 試合開始時刻（UTC）。例: `"2026-05-06T14:58:55.16Z"` |
| `EndTime` | string (ISO 8601) | 0% | 試合終了時刻（UTC）。例: `"2026-05-06T15:03:38.261Z"` |
| `Duration` | string (ISO 8601 期間) | 0% | 試合時間。例: `"PT4M43.0870026S"` → 4分43秒 |
| `PlayableDuration` | string (ISO 8601 期間) | 0% | 実際にプレイ可能だった時間（フリーズ等を除く）。 |
| `LifecycleMode` | int | 0% | **1**=カスタムゲーム, **3**=マッチメイド |
| `PlaylistExperience` | int? | 30.2% | `LifecycleMode=3` のときのプレイリスト種別（2/3/5/6/9 等）。カスタム時は None |
| `GameVariantCategory` | int | 0% | ゲームバリアントカテゴリ（6=Arena 等） |
| `LevelId` | string (UUID) | 0% | マップレベルID（マップアセットIDとは別） |
| `MapVariant` | object | 0% | マップバリアントアセット参照 `{AssetKind, AssetId, VersionId}`（常に存在） |
| `UgcGameVariant` | object | 0% | UGC ゲームバリアントアセット参照 `{AssetKind, AssetId, VersionId}`（常に存在） |
| `Playlist` | object? | 30.2% | プレイリストアセット参照 `{AssetId, VersionId}`。マッチメイドのみ |
| `PlaylistMapModePair` | object? | 30.2% | プレイリスト-マップ-ルールのアセット参照 `{AssetId, VersionId}`。マッチメイドのみ |
| `SeasonId` | string? | 30.2% | シーズンID。例: `"Csr/Seasons/CsrSeason13-2.json"`。カスタム時は None |
| `ClearanceId` | string (UUID) | 0% | クリアランスID（マッチ品質管理） |
| `TeamsEnabled` | bool | 0% | チーム戦か（true=チーム戦, false=FFA） |
| `TeamScoringEnabled` | bool | 0% | チームスコア集計ありか |
| `GameplayInteraction` | int | 0% | ゲームプレイ種別（1=標準 等） |

> **注意**: カスタムゲーム（LifecycleMode=1）では `Playlist`, `PlaylistExperience`, `PlaylistMapModePair`, `SeasonId` は None。

#### Player（MatchStats.Players[] の要素）

| フィールド | 型 | null | 説明 |
|-----------|----|------|------|
| `PlayerId` | string | 0% | プレイヤー識別子。`"xuid(数字)"` または `"bid(数字)"`（Bot） |
| `PlayerType` | int | 0% | **1**=人間, **2**=Bot |
| `BotAttributes` | object? | 100% | Bot 属性（人間の場合は常に None） |
| `LastTeamId` | int | 0% | 所属チームID（**0** または **1**） |
| `Outcome` | int | 0% | 勝敗: **1**=draw, **2**=win, **3**=loss, **4**=did_not_finish |
| `Rank` | int | 0% | チーム内順位（**1**=最良, 数字が大きいほど下位） |
| `ParticipationInfo` | object | 0% | 参加情報（下記） |
| `PlayerTeamStats` | array[TeamStats] | 0% | チーム別個人統計（通常1要素） |

##### ParticipationInfo

| フィールド | 型 | 説明 |
|-----------|----|------|
| `JoinedInProgress` | bool | 試合途中から参加したか |
| `PresentAtCompletion` | bool | 試合終了時にフィールドにいたか |
| `CompletionPercentage` | float? | 試合完了度合い（0.0〜1.0） |

##### TeamStats（PlayerTeamStats[] の要素）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `TeamId` | int | チームID（0 または 1） |
| `Stats` | object | 個人スタッツ |
| `Stats.CoreStats` | object | コア統計（下記） |
| `Stats.Medals` | array[Medal] | 獲得メダル一覧 |

#### CoreStats（PlayerTeamStats[].Stats.CoreStats）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Kills` | int | キル数 |
| `Deaths` | int | デス数 |
| `Assists` | int | アシスト数 |
| `ShotsHit` | int | 命中数 |
| `ShotsFired` | int | 発射数 |
| `DamageDealt` | int | 与ダメージ |
| `DamageTaken` | int | 被ダメージ |
| `Score` | int | ゲーム内個人スコア |
| `PowerWeaponKills` | int | パワーウェポンによるキル数 |
| `Medals` | array[Medal] | メダル配列 |

#### Medal（CoreStats.Medals[] の要素）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `NameId` | int | メダル種別ID。例: `1512363953` = Perfect Kill |
| `Count` | int | 獲得数 |
| `Conditions` | array? | 条件データ（未使用） |

##### 既知の NameId

| NameId | メダル名 | 説明 |
|--------|---------|------|
| `1512363953` | Perfect Kill | パーフェクトキル（ヘッドショットフィニッシュ等） |

#### Team（MatchStats.Teams[] の要素）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `TeamId` | int | 0 または 1 |
| `Outcome` | int | チーム勝敗: 2=win, 3=loss |
| `Rank` | int | チーム順位（1=勝ちチーム） |
| `Stats` | object | チーム統計 |
| `Stats.CoreStats` | object | チームコア統計 |
| `Stats.CoreStats.Score` | int | チームスコア（総合） |

---

### 3.2. PlayerMatchStats（プレイヤー別統計）

#### DB スキーマ

```sql
CREATE TABLE PlayerMatchStats (
    ResponseBody TEXT,
    MatchId TEXT,
    PlayerStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Value')) VIRTUAL
)
```

> `MatchId` カラムが `MatchStats.MatchId` との結合キー。

#### トップレベル（ResponseBody JSON）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Value` | array[PlayerEntry] | プレイヤー別エントリの配列 |

#### PlayerEntry（Value[] の要素）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Id` | string | `"xuid(数字)"` 形式 |
| `Result` | object | TrueSkill2・CSR・MMR データ（下記） |

#### Result（Value[].Result）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `StatPerformances` | object | TrueSkill2 が算出した期待値 |
| `StatPerformances.Kills` | object | キルの期待値 `{Expected: float}` |
| `StatPerformances.Kills.Expected` | float | 期待キル数 |
| `StatPerformances.Deaths` | object | デスの期待値 `{Expected: float}` |
| `StatPerformances.Deaths.Expected` | float | 期待デス数 |
| `RankRecap` | object | CSR 詳細（下記） |
| `TeamMmrs` | object | チーム別平均MMR |
| `TeamMmrs["0"]` | float | チーム0の平均MMR（例: `1349.0`） |
| `TeamMmrs["1"]` | float | チーム1の平均MMR（例: `1265.1`） |
| `TeamMmr` | float | 自チームの平均MMR（TeamMmrs から自チーム分を抽出したもの） |
| `TeamId` | int | プレイヤーの所属チームID（0 または 1） |
| `RankedRewards` | object? | ランク報酬情報（通常 None） |
| `Counterfactuals` | object? | 反実仮想分析データ（通常 None） |

##### RankRecap

| フィールド | 型 | 説明 |
|-----------|----|------|
| `PreMatchCsr` | object | 試合前CSR（下記） |
| `PostMatchCsr` | object | 試合後CSR（下記） |

###### CSR オブジェクト（PreMatchCsr / PostMatchCsr）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Value` | int | CSR値。**0**=未ランク/計測中, **100〜2500** 程度が実戦値 |
| `Tier` | string | ティア名。`""`=未ランク, `"Bronze"`〜`"Onyx"` |
| `TierStart` | int | ティア開始CSR値 |
| `SubTier` | int | サブティア（1〜6）。0=未ランク |
| `NextTier` | string | 次のティア名 |
| `NextTierStart` | int | 次のティア開始CSR値 |
| `NextSubTier` | int | 次のサブティア |
| `InitialMeasurementMatches` | int | 初期計測試合数（10） |
| `MeasurementMatchesRemaining` | int | 残り計測試合数 |
| `DemotionProtectionMatchesRemaining` | int | 降格防止残り試合数 |
| `InitialDemotionProtectionMatches` | int | 初期降格防止試合数 |

##### CSR 値の実測範囲

| 統計 | 値 |
|------|-----|
| 最小値 | 456 |
| 最大値 | 2,342 |
| 平均値 | 1,336 |
| CSR>0 のエントリ割合 | 15,878 / 25,727 (約62%) |

> 残り38%は `Value=0`（未ランク期間中またはカスタム/ソーシャル/BTB）。

##### StatPerformances の有無

| 統計 | 値 |
|------|-----|
| StatPerformances あり | 21,826 / 25,727 (約85%) |
| StatPerformances なし | 約15%（カスタムゲーム等） |

---

### 3.3. Maps（マップメタデータ）

#### DB スキーマ

```sql
CREATE TABLE Maps (
    ResponseBody TEXT,
    CustomData     Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,
    Tags           Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,
    PrefabLinks    Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PrefabLinks')) VIRTUAL,
    AssetId        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,
    VersionId      Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,
    PublicName     Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,
    Description    Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,
    Files          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,
    Contributors   Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,
    AssetHome      Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,
    AssetStats     Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,
    InspectionResult Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,
    CloneBehavior  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,
    "Order"        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,
    PublishedDate  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,
    VersionNumber  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,
    Admin          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL
)
```

#### ResponseBody JSON

| フィールド | 型 | 説明 |
|-----------|----|------|
| `AssetId` | string (UUID) | マップの一意識別子 |
| `VersionId` | string (UUID) | バージョンID |
| `PublicName` | string | マップ表示名（例: `"Lattice - Ranked"`） |
| `Description` | string | マップ説明文 |
| `CustomData` | object | 内部データ |
| `CustomData.NumOfObjectsOnMap` | int | マップ上のオブジェクト数 |
| `CustomData.TagLevelId` | int | タグレベルID |
| `CustomData.IsBaked` | bool | ベイク済みか |
| `CustomData.HasNodeGraph` | bool | ノードグラフありか |
| `Tags` | array[string] | タグ一覧（通常空配列） |
| `PrefabLinks` | array | プレハブリンク一覧（通常空配列） |
| `Files` | object | Blob ストレージ上のファイル情報 |
| `Files.Prefix` | string (URL) | Blob ストレージプレフィックス |
| `Files.FileRelativePaths` | array[string] | ファイル相対パス一覧（hero画像, サムネイル, mvar等） |
| `Files.PrefixEndpoint` | object | エンドポイント設定（下記） |
| `Contributors` | array[string] | コントリビューターXUID一覧 |
| `AssetHome` | int | **1**=343 Industries, **2**=ユーザー作成 |
| `AssetStats` | object | アセット人気統計（下記） |
| `InspectionResult` | int | **0**=正常, **50**=検査保留中 |
| `CloneBehavior` | int | **0**=通常（クローン可能）, **1**=読み取り専用 |
| `Order` | int | 並び順 |
| `PublishedDate` | object | 公開日 `{ISO8601Date: string}` |
| `PublishedDate.ISO8601Date` | string | ISO 8601 日付 |
| `VersionNumber` | int | バージョン番号 |
| `Admin` | string | 管理者ID（`"xuid(...)"` または `"aaid(...)"`） |

##### PrefixEndpoint（Files.PrefixEndpoint）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `AuthorityId` | string | 認証局ID（例: `"iUgcFiles"`） |
| `Path` | string | エンドポイントパス |
| `QueryString` | string? | クエリ文字列（通常 null） |
| `RetryPolicyId` | string | リトライポリシー（例: `"linearretry"`） |
| `TopicName` | string | トピック名（通常空文字） |
| `AcknowledgementTypeId` | int | 確認応答タイプ |
| `AuthenticationLifetimeExtensionSupported` | bool | 認証延長対応 |
| `ClearanceAware` | bool | クリアランス対応 |

##### AssetStats

| フィールド | 型 | 説明 |
|-----------|----|------|
| `PlaysRecent` | int | 直近のプレイ数 |
| `PlaysAllTime` | int | 全期間のプレイ数 |
| `Favorites` | int | お気に入り数 |
| `Likes` | int | いいね数（常に0） |
| `Bookmarks` | int | ブックマーク数（常に0） |
| `ParentAssetCount` | int | 派生元アセット数 |
| `AverageRating` | float | 平均評価（0.0〜5.0） |
| `NumberOfRatings` | int | 評価数 |

##### AssetHome の値

| 値 | 意味 | 実測件数 |
|----|------|---------|
| `1` | 343 Industries（公式） | 大多数 |
| `2` | ユーザー作成（UGC） | 少数 |

##### InspectionResult の値

| 値 | 意味 |
|----|------|
| `0` | 正常（公開済み） |
| `50` | 検査保留中 / 未検査 |

##### CloneBehavior の値

| 値 | 意味 |
|----|------|
| `0` | 通常（クローン・フォーク可能） |
| `1` | 読み取り専用（クローン不可） |

---

### 3.4. Playlists（プレイリスト定義）

#### DB スキーマ

```sql
CREATE TABLE Playlists (
    ResponseBody TEXT,
    CustomData       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,
    Tags             Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,
    RotationEntries  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.RotationEntries')) VIRTUAL,
    AssetId          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,
    VersionId        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,
    PublicName       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,
    Description      Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,
    Files            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,
    Contributors     Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,
    AssetHome        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,
    AssetStats       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,
    InspectionResult Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,
    CloneBehavior    Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,
    "Order"          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,
    PublishedDate    Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,
    VersionNumber    Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,
    Admin            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL
)
```

> `RotationEntries` が PlaylistMapModePairs へのリンクとして使われる。

#### ResponseBody JSON

| フィールド | 型 | 説明 |
|-----------|----|------|
| `AssetId` | string (UUID) | プレイリストの一意識別子 |
| `VersionId` | string (UUID) | バージョンID |
| `PublicName` | string | プレイリスト名（例: `"Ranked Slayer"`, `"Quick Play"`） |
| `Description` | string | 説明文 |
| `CustomData` | object | カスタムデータ |
| `Tags` | array[string] | タグ一覧 |
| `RotationEntries` | array[AssetLink] | ローテーションエントリ（PlaylistMapModePairs へのリンク） |
| `RotationEntries[].AssetId` | string (UUID) | Pairs アセットID |
| `RotationEntries[].VersionId` | string (UUID) | バージョンID |
| `Files` | object | ファイル情報（Maps と同構造） |
| `Contributors` | array[string] | コントリビューター |
| `AssetHome` | int | 1=343i, 2=ユーザー |
| `AssetStats` | object | アセット統計（Maps と同構造） |
| `InspectionResult` | int | 検査結果 |
| `CloneBehavior` | int | クローン動作 |
| `Order` | int | 並び順 |
| `PublishedDate` | object | 公開日 |
| `VersionNumber` | int | バージョン番号 |
| `Admin` | string | 管理者ID |

##### PublicName の実測値（抜粋）

| PublicName | 分類される PlaylistExperience |
|-----------|------------------------------|
| `Ranked Slayer` | 3 (ranked_slayer) |
| `Ranked Arena` | 2 (ranked_arena) |
| `Ranked Doubles` | 3 (ranked_slayer) |
| `Quick Play` | 5 (social) |
| `Team Doubles` | 5 (social) |
| `BTB` 系 | 9 (btb) |
| その他（Extraction, Snipers, FFA, Tactical 等） | 5 (social) |

---

### 3.5. PlaylistMapModePairs（プレイリスト-マップ紐付け）

#### DB スキーマ

```sql
CREATE TABLE PlaylistMapModePairs (
    ResponseBody TEXT,
    CustomData          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,
    Tags                Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,
    MapLink             Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MapLink')) VIRTUAL,
    UgcGameVariantLink  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.UgcGameVariantLink')) VIRTUAL,
    AssetId             Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,
    VersionId           Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,
    PublicName          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,
    Description         Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,
    Files               Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,
    Contributors        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,
    AssetHome           Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,
    AssetStats          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,
    InspectionResult    Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,
    CloneBehavior       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,
    "Order"             Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,
    PublishedDate       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,
    VersionNumber       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,
    Admin               Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL
)
```

> `MapLink` が Maps テーブルへの、`UgcGameVariantLink` が GameVariants への外部キー。

#### ResponseBody JSON

他のアセットテーブルと共通のフィールドに加え、以下の固有フィールドを持つ:

| フィールド | 型 | 説明 |
|-----------|----|------|
| `PublicName` | string | **"ルール名 on マップ名"** 形式（例: `"Ranked:Slayer on Lattice - Ranked"`） |
| `MapLink` | object | マップアセット参照 `{AssetId, VersionId, PublicName}` |
| `UgcGameVariantLink` | object? | UGC バリアントアセット参照 `{AssetId, VersionId, PublicName}`（カスタム用） |

##### PublicName の命名規則

| カテゴリ | パターン | ルール抽出 | マップ抽出 | 実例 |
|---------|---------|-----------|-----------|------|
| Ranked | `"Ranked:{Rule} on {Map} - Ranked"` | `{Rule}` | `{Map}` | `"Ranked:Slayer on Lattice - Ranked"` |
| Ranked | `"Ranked:{Rule} on {Map}"` | `{Rule}` | `{Map}` | `"Ranked:King of the Hill on Live Fire"` |
| Ranked | `"Ranked:{Rule} {N} Captures on {Map}"` | `{Rule}` | `{Map}` | `"Ranked:CTF 3 Captures on Empyrean"` |
| BTB | `"BTB:{Rule} on {Map}"` | Other | 抽出対象外 | `"BTB:Slayer on Fragmentation"` |
| Arena | `"Arena:{Rule} on {Map}"` | Other | 抽出対象外 | `"Arena:Slayer on Recharge"` |

> `" - Ranked"` サフィックスは `_clean_map()` で除去される。

##### ルール名の正規化

`_parse_pair_name()` で以下の正規化が行われる:

| 入力（PublicName から抽出後） | 正規化後 |
|------------------------------|---------|
| `"slayer"` (大文字小文字不問) | `"Slayer"` |
| `"ctf"` | `"CTF"` |
| `"oddball"` | `"Oddball"` |
| `"king"` or `"king of the hill"` | `"KOTH"` |
| `"stronghold"` | `"Strongholds"` |

---

### 3.6. GameVariants（UGC ゲームバリアント）

#### DB スキーマ

```sql
CREATE TABLE GameVariants (
    ResponseBody TEXT,
    CustomData           Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,
    Tags                 Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,
    EngineGameVariantLink Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.EngineGameVariantLink')) VIRTUAL,
    AssetId              Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,
    VersionId            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,
    PublicName           Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,
    Description          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,
    Files                Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,
    Contributors         Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,
    AssetHome            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,
    AssetStats           Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,
    InspectionResult     Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,
    CloneBehavior        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,
    "Order"              Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,
    PublishedDate        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,
    VersionNumber        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,
    Admin                Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL
)
```

#### ResponseBody JSON（Maps と共通フィールドに加えて）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `CustomData` | object | カスタム設定（下記） |
| `Tags` | array[string] | タグ一覧（例: `["343i", "Ranked", "Slayer"]`） |
| `EngineGameVariantLink` | object | 紐付くエンジンバリアント参照 `{AssetId, VersionId, PublicName, ...}` |
| `PublicName` | string | バリアント名（例: `"Ranked:Slayer"`, `"BRT"`, `"Octagon"`） |

##### CustomData

| フィールド | 型 | 説明 |
|-----------|----|------|
| `KeyValues` | object | キー-値ペアマップ |
| `KeyValues.{key}` | object | 各キーは `{uint_value, int_value, double_value, string_value, wstring_value, nothing}` の6フィールドを持つ |
| `HasNodeGraph` | bool | ノードグラフ（スクリプティング）ありか |

###### 各エントリの値格納ルール

| フィールド | 型 | 用途 |
|-----------|----|------|
| `uint_value` | int | 符号なし整数（0/1 フラグ, ID 等） |
| `int_value` | int | 符号付き整数（通常0） |
| `double_value` | float | 浮動小数点値（通常0.0） |
| `string_value` | string | 文字列値（通常空文字） |
| `wstring_value` | string | ワイド文字列値（通常空文字） |
| `nothing` | bool | 未設定フラグ（true=値なし） |

###### KeyValues の既知のキー

| キー | 説明 | 型 |
|-----|------|----|
| `globalMalleableProperties.InfiniteAmmo` | 無限弾薬 | uint (0/1) |
| `globalMalleableProperties.MotionTrackerEnabled` | モーショントラッカー有効 | uint (0/1) |
| `loadoutOptions.Loadout[0].PrimaryWeapon` | プライマリ武器ID | uint |
| `loadoutOptions.Loadout[0].PrimaryWeaponAndConfigurationIdentifier` | 武器構成ID | uint |
| `loadoutOptions.Loadout[0].SecondaryWeapon` | セカンダリ武器ID | uint |
| `loadoutOptions.Loadout[0].SecondaryWeaponAndConfigurationIdentifier` | 武器構成ID | uint |
| `matchFlowOptions.RoundTimeLimit` | ラウンド時間制限（分） | uint |
| `matchFlowOptions.ScoreToWinRound` | 勝利スコア | uint |
| `respawnOptions.MinimumRespawnTimeInSeconds` | 最小リスポーン時間（秒） | uint |

##### Tags の実測値（抜粋）

| タグ | 使われるバリアント |
|-----|------------------|
| `"343i"` | 公式バリアント |
| `"Ranked"` | ランク用バリアント |
| `"Slayer"` | スレイヤールール |
| `"Arena"` | アリーナ |
| `"CTF"` | キャプチャー・ザ・フラッグ |
| `"Oddball"` | オッドボール |
| `"KotH"` / `"King"` / `"Hill"` | KOTH |
| `"Strongholds"` | ストロングホールド |
| `"Flag"` / `"Multi-Flag"` | CTF マルチフラッグ |
| `"1v1"` / `"FFA"` | 1v1 / FFA |
| `"Training"` | トレーニング用 |

---

### 3.7. EngineGameVariants（エンジンバリアント）

GameVariants とほぼ同じ構造だが、`CustomData.SubsetData` が追加で存在する。

| フィールド | 型 | 説明 |
|-----------|----|------|
| `CustomData.SubsetData` | object | エンジンサブセット情報 |
| `CustomData.SubsetData.StatBucketGameType` | int | 統計バケット種別 |
| `CustomData.SubsetData.EngineName` | string | エンジン名 |
| `CustomData.SubsetData.VariantName` | string | バリアント名 |
| その他 | （GameVariants と共通） | |

#### PublicName 一覧（55件 全リスト）

**Slayer 系統**
- `Slayer`, `Slayer-Competitive`, `Slayer-CompetitiveFFA`, `Slayer-CompetitiveSlayerDoubles`
- `Slayer-SlayerARBR`, `Slayer-CompetitiveSnipers`, `Slayer-TeamSnipers`
- `Slayer-ShottySnipes`, `Slayer-ShottySnipesFFA`, `Slayer-Tactical`
- `Slayer-TacticalStalkers`, `Slayer-TacticalSidekicks`, `Slayer-TacticalCommandos`
- `Slayer-SlayerBR`, `Slayer-SlayerDoubles`, `Slayer-FFA`
- `Slayer-Arena`, `Slayer-FiestaSlayerFFA`, `Slayer-NinjaSlayerFFA`
- `Slayer-BruteSnipes`, `Big Team Slayer`, `Slayer-BTBSkockets`
- `Slayer-BTBFiesta`

**CTF 系統**
- `Capture the Flag`, `Big Team CTF`, `CTF-PhantomsOneFlag`
- `CTF-NinjaMultiFlag`, `CTF-BTBFiesta`, `One Flag CTF`
- `MultiFlag Competitive`

**Oddball 系統**
- `Oddball`, `Oddball Competitive`, `Oddball-Doubles`, `Oddball-FFA`
- `Oddball-VampireballFFA`

**KOTH 系統**
- `King of the Hill`, `Ranked King of the Hill`

**Strongholds 系統**
- `Strongholds`, `Strongholds-DefaultCompetitive`, `Strongholds-Slayholds`

**BTB 系統**
- `TotalControl-BTB`, `TotalControl-BTBFiesta`, `Stockpile-BTB`
- `Stockpile-BTBFiesta`, `Big Team Slayer`, `Big Team CTF`

**FFA / Doubles**
- `Slayer-FFA`, `Bastion-FFA`, `Escalation-CompetitiveFFA`
- `Oddball-FFA`, `Slayer-Doubles`, `Bastion-Doubles`, `Oddball-Doubles`

**その他**
- `Attrition`, `Attrition-AttritionFFAS2Event`
- `Extraction`, `Extraction Competitive`
- `Escalation-Event`
- `LandGrab-Default`
- `Bastion-BTB`, `Bastion-FFA`
- `Firefight-Bastion`

---

### 3.8. InventoryItems（インベントリアイテム定義）

全アイテムのカタログ。レコード数: 1,007。

#### DB スキーマ

```sql
CREATE TABLE InventoryItems (
    ResponseBody TEXT,
    Path TEXT,
    LastUpdated DATETIME,
    Id      Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CommonData.Id')) VIRTUAL,
    Quality Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CommonData.Quality')) VIRTUAL
)
```

#### JSON 構造

| フィールド | 型 | 説明 |
|-----------|----|------|
| `TagId` | int | タグID（-1 または 0 の場合あり） |
| `MeshIndex` | int | メッシュインデックス（-1=なし） |
| `ThemeName` | object? | テーマ名 `{m_identifier: int}`（エンブレム等） |
| `EmblemShaderName` | object? | エンブレムシェーダー名 `{m_identifier: int}` |
| `AvailableConfigurations` | array? | 利用可能なコンフィグレーション一覧（エンブレム用） |
| `AvailableConfigurations[].ConfigurationId` | int | コンフィグID |
| `AvailableConfigurations[].ConfigurationPath` | string | コンフィグファイルパス |
| `CommonData` | object | **共通データ**（下記） |

##### CommonData

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Id` | string | アイテムID（例: `"4241927-011-olympus"`） |
| `HideUntilOwned` | bool | 未所有時は非表示か |
| `Title` | LocalizedString | アイテム名（多言語対応） |
| `Title.value` | string | 英語名 |
| `Title.translations.ja-JP` | string? | 日本語名（あれば） |
| `Title.translations` | object | 他言語翻訳マップ（cs-CZ, da-DK, de-DE, ja-JP, ko-KR, zh-CN, zh-TW 等 20+ 言語） |
| `Description` | LocalizedString | 説明文（多言語対応、Title と同構造） |
| `FeatureFlag` | bool | フィーチャーフラグ（ほぼ常に true） |
| `ItemAvailability` | LocalizedString | 入手可能性ステータス（`status: "Test"` 等） |
| `DateReleased` | object | リリース日 `{ISO8601Date: string}`（空文字の場合あり） |
| `AltName` | LocalizedString | 代替名（通常はファイルパス形式のID） |
| `IconStringId` | object? | アイコン文字列ID `{m_identifier: int}` |
| `SpriteBitmap` | int | スプライトビットマップ |
| `SpriteFrameIndex` | int | スプライトフレームインデックス |
| `AltSpriteBitmap` | int | 代替スプライトビットマップ |
| `AltSpriteFrameIndex` | int | 代替スプライトフレームインデックス |
| `DisplayPath` | object | 画像表示パス（下記） |
| `Quality` | string | レアリティ（下記 enum） |
| `ManufacturerId` | int | メーカーID（8=エンブレム, 9=アーマー 等） |
| `Type` | string | アイテム種別（下記 enum） |
| `RewardTrack` | string | 関連報酬トラックパス（通常空文字） |
| `ParentPaths` | array[ParentPath] | 親アセットパス一覧 |
| `ParentPaths[].Path` | string | 親パス（例: `"Inventory/Armor/Themes/007-001-olympus-c13d0b38.json"`） |
| `ParentPaths[].Type` | string | 親タイプ（例: `"ArmorTheme"`） |
| `SortingMetadata` | object | ソートメタ情報 `{categoryWeight: int, subCategoryWeight: int}` |
| `SeasonNumber` | int | シーズン番号（13001=標準） |
| `OriginalSeasonNumber` | int | オリジナルシーズン番号 |
| `IsCrossCompatible` | bool | クロスプラットフォーム互換性ありか |
| `Season` | LocalizedString? | シーズン情報（あれば） |

##### DisplayPath（CommonData.DisplayPath）

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Width` | int | 画像幅（px） |
| `Height` | int | 画像高さ（px） |
| `Media` | object | メディア情報 |
| `Media.MediaUrl` | object | 画像URL |
| `Media.MediaUrl.AuthorityId` | string | 認証局ID（通常空文字） |
| `Media.MediaUrl.Path` | string | 画像相対パス（例: `"progression/Inventory/Armor/WristAttachments/xxx.png"`） |
| `Media.MediaUrl.RetryPolicyId` | string | リトライポリシー |
| `Media.MediaUrl.AcknowledgementTypeId` | string | 確認応答タイプ |
| `Media.MimeType` | string | MIMEタイプ（例: `"image/png"`） |
| `Caption` | LocalizedString | キャプション |
| `AlternateText` | LocalizedString | 代替テキスト |
| `FolderPath` | string | フォルダパス |
| `FileName` | string | ファイル名 |

##### Quality の値（レアリティ）

| 値 | 説明 |
|----|------|
| `Common` | コモン |
| `Uncommon` | アンコモン |
| `Rare` | レア |
| `Epic` | エピック |
| `Legendary` | レジェンダリー |

##### Type の値（InventoryItems で確認されたもの）

| Type | 説明 | 件数（参考） |
|------|------|-------------|
| `ArmorCoating` | アーマーコーティング | 多数 |
| `WeaponCoating` | ウェポンコーティング | 多数 |
| `WeaponEmblem` | ウェポンエンブレム | 多数 |
| `SpartanEmblem` | スパルタンエンブレム | 多数 |
| `ArmorEmblem` | アーマーエンブレム | 多数 |
| `VehicleEmblem` | ビークルエンブレム | 多数 |
| `VehicleCoating` | ビークルコーティング | 300+ |
| `ArmorRightShoulderPad` | 右ショルダーパッド | ~290 |
| `ArmorLeftShoulderPad` | 左ショルダーパッド | ~290 |
| `ArmorHelmet` | ヘルメット | ~290 |
| `ArmorVisor` | バイザー | ~278 |
| `ArmorHelmetAttachment` | ヘルメットアタッチメント | ~255 |
| `ArmorChestAttachment` | チェストアタッチメント | ~240 |
| `SpartanBackdropImage` | バックドロップ画像 | ~179 |
| `ArmorKneePad` | ニーパッド | ~175 |
| `SpartanActionPose` | アクションポーズ | ~165 |
| `WeaponCharm` | ウェポンチャーム | ~150 |
| `ArmorHipAttachment` | ヒップアタッチメント | ~131 |
| `ArmorWristAttachment` | リストアタッチメント | ~130 |
| `WeaponTheme` | ウェポンテーマ | ~120 |
| `ArmorTheme` | アーマーテーマ | ~90 |
| `ArmorGlove` | グローブ | ~80 |
| `AiColor` | AI カラー | ~60 |
| `WeaponAlternateGeometryRegion` | 武器代替形状 | ~55 |
| `ArmorFx` | アーマーエフェクト | ~45 |
| `SpartanVoice` | スパルタンボイス | ~40 |
| `WeaponDeathFx` | 武器デスエフェクト | ~35 |
| `VehicleTheme` | ビークルテーマ | ~35 |
| `AiModel` | AI モデル | ~30 |
| `ArmorMythicFx` | アーマーミシックエフェクト | ~20 |

---

### 3.9. OwnedInventoryItems（所有アイテム）

プレイヤーが実際に所有しているアイテムのリスト。レコード数: 9,168。

#### DB スキーマ

```sql
CREATE TABLE OwnedInventoryItems (
    Amount INTEGER,
    ItemId TEXT,
    ItemPath TEXT,
    ItemType TEXT,
    FirstAcquiredDate DATETIME
)
```

#### カラム

| カラム | 型 | 説明 |
|--------|----|------|
| `Amount` | INTEGER | 所有数（通常1） |
| `ItemId` | TEXT | アイテムID（InventoryItems.CommonData.Id に対応） |
| `ItemPath` | TEXT | アイテムパス（例: `"Inventory/armor/coatings/..."`） |
| `ItemType` | TEXT | アイテム種別（InventoryItems の Type と同じ） |
| `FirstAcquiredDate` | DATETIME | 初回取得日時 |

> `Amount > 1` になるのは消耗品・重複取得可能なアイテムのみ。

---

### 3.10. OperationRewardTracks（報酬トラック）

オペレーション（バトルパス）の定義。レコード数: 31。

#### DB スキーマ

```sql
CREATE TABLE OperationRewardTracks (
    ResponseBody TEXT,
    Path TEXT,
    LastUpdated DATETIME,
    TrackId              Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.TrackId')) VIRTUAL,
    XpPerRank            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.XpPerRank')) VIRTUAL,
    HideIfNotOwned       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.HideIfNotOwned')) VIRTUAL,
    Ranks                Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Ranks')) VIRTUAL,
    Name                 Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Name')) VIRTUAL,
    Description          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,
    OperationNumber      Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.OperationNumber')) VIRTUAL,
    DateRange            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.DateRange')) VIRTUAL,
    IsRitual             Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.IsRitual')) VIRTUAL,
    SummaryImagePath     Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.SummaryImagePath')) VIRTUAL,
    WeekNumber           Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.WeekNumber')) VIRTUAL,
    BackgroundImagePath  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.BackgroundImagePath')) VIRTUAL
)
```

#### ResponseBody JSON

| フィールド | 型 | 説明 |
|-----------|----|------|
| `TrackId` | string | トラックID |
| `Name` | object? | トラック名（LocalizedString） |
| `Description` | object? | 説明（LocalizedString） |
| `XpPerRank` | int | 1ランクあたりの必要XP |
| `HideIfNotOwned` | bool | 未所有時に非表示か |
| `Ranks` | array[Rank] | ランク別報酬一覧 |
| `Ranks[].Rank` | int | ランク番号 |
| `Ranks[].Reward` | object | 報酬アイテム |
| `Ranks[].Reward.ItemPath` | string | 報酬アイテムパス |
| `Ranks[].Reward.ItemId` | string | 報酬アイテムID |
| `Ranks[].Reward.Quantity` | int | 報酬数量 |
| `OperationNumber` | int | オペレーション番号 |
| `DateRange` | object | 期間 `{Start: ISO8601, End: ISO8601}` |
| `IsRitual` | bool | リチュアル（イベント）トラックか |
| `WeekNumber` | int | 週番号（リチュアル用） |
| `SummaryImagePath` | string | サマリー画像パス |
| `BackgroundImagePath` | string | 背景画像パス |

---

### 3.11. PlaylistCSRSnapshots（CSRスナップショット）

プレイリスト別のCSR履歴スナップショット。レコード数: 20。

#### DB スキーマ

```sql
CREATE TABLE PlaylistCSRSnapshots (
    ResponseBody TEXT,
    PlaylistId TEXT,
    PlaylistVersion TEXT,
    SnapshotTimestamp DATETIME,
    Value Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Value')) VIRTUAL
)
```

#### カラム

| カラム | 型 | 説明 |
|--------|----|------|
| `PlaylistId` | TEXT | プレイリストアセットID |
| `PlaylistVersion` | TEXT | プレイリストバージョンID |
| `SnapshotTimestamp` | DATETIME | スナップショット取得日時 |
| `Value` | TEXT (JSON) | CSR値（json_extract で抽出） |

#### ResponseBody JSON

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Value` | int | その時点のCSR値 |

---

### 3.12. ServiceRecordSnapshots（通算戦績）

プレイヤーの通算戦績スナップショット。レコード数: 5。

#### DB スキーマ

```sql
CREATE TABLE ServiceRecordSnapshots (
    ResponseBody TEXT,
    SnapshotTimestamp DATETIME,
    Subqueries        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Subqueries')) VIRTUAL,
    TimePlayed        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.TimePlayed')) VIRTUAL,
    MatchesCompleted  Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MatchesCompleted')) VIRTUAL,
    Wins              Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Wins')) VIRTUAL,
    Losses            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Losses')) VIRTUAL,
    Ties              Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Ties')) VIRTUAL,
    CoreStats         Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CoreStats')) VIRTUAL,
    BombStats         Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.BombStats')) VIRTUAL,
    CaptureTheFlagStats   Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CaptureTheFlagStats')) VIRTUAL,
    EliminationStats      Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.EliminationStats')) VIRTUAL,
    ExtractionStats       Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.ExtractionStats')) VIRTUAL,
    InfectionStats        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InfectionStats')) VIRTUAL,
    OddballStats          Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.OddballStats')) VIRTUAL,
    ZonesStats            Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.ZonesStats')) VIRTUAL,
    StockpileStats        Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.StockpileStats')) VIRTUAL
)
```

#### ResponseBody JSON

| フィールド | 型 | 説明 |
|-----------|----|------|
| `Subqueries` | object? | サブクエリデータ |
| `TimePlayed` | string (ISO 8601 期間) | 通算プレイ時間 |
| `MatchesCompleted` | int | 通算試合数 |
| `Wins` | int | 通算勝利数 |
| `Losses` | int | 通算敗北数 |
| `Ties` | int | 通算引き分け数 |
| `CoreStats` | object | 通算コア統計（Kills, Deaths, Assists 等） |
| `BombStats` | object? | ボムモード統計 |
| `CaptureTheFlagStats` | object? | CTF 統計 |
| `EliminationStats` | object? | エリミネーション統計 |
| `ExtractionStats` | object? | 抽出モード統計 |
| `InfectionStats` | object? | インフェクション統計 |
| `OddballStats` | object? | オッドボール統計 |
| `ZonesStats` | object? | ゾーン（Strongholds/KOTH）統計 |
| `StockpileStats` | object? | ストックパイル統計 |

---

## 4. API 生値 → 内部値 変換マップ

### `LifecycleMode`（試合種別）

| API値 | 内部値 | 表示名 | 説明 |
|-------|--------|--------|------|
| `1` | `"custom"` | カスタムゲーム | プライベートマッチ |
| `3` | ※右記 | （PlaylistExperience 次第） | マッチメイド |

#### 実測分布（n=2,000）

| LifecycleMode | 件数 | 割合 |
|---------------|------|------|
| `1` (custom) | 604 | 30.2% |
| `3` (matchmade) | 1,396 | 69.8% |

### `PlaylistExperience`（マッチメイドの区分、LifecycleMode=3 のとき）

| API値 | 内部値 | 表示名 | 実測件数 |
|-------|--------|--------|---------|
| `2` | `"ranked_arena"` | ランクアリーナ | 1,283 |
| `3` | `"ranked_slayer"` | ランクスレイヤー | 54 |
| `5` | `"social"` | ソーシャル | 59 |
| `6` | `"minigame"` | ミニゲーム | 未確認 |
| `9` | `"btb"` | BTB | 未確認 |
| None | `"custom"` 扱い | （LifecycleMode=1 の場合） | 604 |
| その他 | `"other"` | Other | — |

### `PlayerType`（プレイヤー種別）

| API値 | 意味 | 処理 | 実測件数 |
|-------|------|------|---------|
| `1` | 人間プレイヤー | 分析対象 | 14,272 |
| `2` | Bot | 分析対象外 | 544 |

→ Bot の割合: 約 3.7%

### `Outcome`（勝敗）

| API値 | 内部値 | 表示名 | 実測件数 |
|-------|--------|--------|---------|
| `1` | `"draw"` | 引き分け | 631 |
| `2` | `"win"` | 勝ち | 6,669 |
| `3` | `"loss"` | 負け | 6,655 |
| `4` | `"did_not_finish"` | 途中抜け | 861 |

> **注意**: display.py の `OUTCOME_MAP` は `1=draw, 2=win, 3=loss` の順。Halo API の仕様に基づく。

### `Outcome`（Teams[] レベル）

| API値 | 意味 |
|-------|------|
| `2` | 勝ちチーム |
| `3` | 負けチーム |

### `PartySize` → `PartyType`

| PartySize | 表示名 |
|-----------|--------|
| `1` | ソロ |
| `2` | デュオ |
| `3` | トリオ |
| `4` | フルパ |

### `ExcludeFlag`（除外理由）

| 値 | 意味 | 判定条件 |
|----|------|---------|
| `""`（空文字） | 正常データ（分析対象） | 全ての条件をクリア |
| `"short_match"` | 試合時間1分未満 | `duration_sec < 60` |
| `"incomplete"` | 不完全な試合 | 途中参加 / 途中抜け / Outcome=4 / PresentAtCompletion=false |
| `"manual"` | 手動除外 | ユーザーが手動で設定（UI から） |

---

## 5. Flood-Lab DataFrame カラム一覧（内部カラム名）

DataFrame の全カラム。`database.py` で生値がセットされ、`processor.py` で計算指標が追加される。

### 5.1 識別・メタ情報（database.py でセット）

| 内部カラム名 | 型 | 表示名 | ソース（API パス） |
|-------------|----|--------|-------------------|
| `match_id` | string (UUID) | 試合ID | `MatchStats.MatchId` |
| `played_at` | datetime (UTC) | 日時 | `MatchStats.MatchInfo.StartTime`（JST 変換後） |
| `playlist` | string | 区分 | LifecycleMode + PlaylistExperience から分類 |
| `map_name` | string | マップ | PlaylistMapModePair.PublicName から抽出 |
| `rule_name` | string | ルール | PlaylistMapModePair.PublicName から抽出 |
| `result` | string | 勝敗 | `Players[].Outcome` → OUTCOME_MAP 変換 |
| `result_flag` | int (0/1) | 勝敗フラグ | `result == "win" → 1, else 0` |
| `exclude_flag` | string | 除外フラグ | ルールベース判定（7章参照） |

### 5.2 基礎スタッツ（database.py でセット）

| 内部カラム名 | 型 | 表示名 | ソース（API パス） |
|-------------|----|--------|-------------------|
| `kills` | int | キル | `CoreStats.Kills` |
| `deaths` | int | デス | `CoreStats.Deaths` |
| `assists` | int | アシスト | `CoreStats.Assists` |
| `shots_hit` | int | 命中数 | `CoreStats.ShotsHit` |
| `shots_fired` | int | 発射数 | `CoreStats.ShotsFired` |
| `damage_dealt` | int | 与ダメージ | `CoreStats.DamageDealt` |
| `damage_taken` | int | 被ダメージ | `CoreStats.DamageTaken` |
| `score` | int | 個人スコア | `CoreStats.Score` |
| `power_kills` | int | 重火器キル | `CoreStats.PowerWeaponKills` |
| `perfect_kills` | int | パーフェクトキル | Medal[NameId=1512363953].Count（再帰走査） |
| `team_rank` | int? | チーム内順位 | `Players[].Rank` |
| `team_score` | int? | 自チームスコア | `Teams[自チーム].Stats.CoreStats.Score` |
| `enemy_score` | int? | 敵チームスコア | `Teams[敵チーム].Stats.CoreStats.Score` |
| `team_mmr` | int? | 自チームMMR | `PlayerMatchStats.Result.TeamMmrs[自チームID]` |
| `enemy_mmr` | int? | 敵チームMMR | `PlayerMatchStats.Result.TeamMmrs[敵チームID]` |
| `duration_sec` | int? | 試合時間（秒） | `MatchInfo.Duration`（ISO 8601 期間文字列 → 秒） |

### 5.3 CSR 系（database.py + metrics.py でセット）

| 内部カラム名 | 型 | 表示名 | ソース / 計算式 |
|-------------|----|--------|----------------|
| `csr_pre` | int? | 試合前CSR | `RankRecap.PreMatchCsr.Value`（0 の場合は None） |
| `csr_post` | int? | 試合後CSR | `RankRecap.PostMatchCsr.Value`（0 の場合は None） |
| `csr_delta` | int? | CSR増減 | `csr_post - csr_pre`（いずれかが None なら None） |
| `csr_avg20` | float? | 直近20試合平均CSR | 区分別 rolling mean(csr_pre, 20) |

### 5.4 TrueSkill2 系（database.py + metrics.py でセット）

| 内部カラム名 | 型 | 表示名 | ソース / 計算式 |
|-------------|----|--------|----------------|
| `expected_kills` | float? | 期待キル | `StatPerformances.Kills.Expected` |
| `expected_deaths` | float? | 期待デス | `StatPerformances.Deaths.Expected` |
| `k_rpi` | float? | K-RPI | `kills / expected_kills` |
| `d_rpi` | float? | D-RPI | `expected_deaths / deaths` |
| `lgai` | float? | LGAI | `enemy_mmr - csr_pre` |
| `impact_score` | float? | インパクトスコア | `(k_rpi + d_rpi) / 2` |
| `survival_contribution` | float? | 生存貢献度 | `(expected_deaths - deaths) × (enemy_mmr / csr_pre)` |

### 5.5 eMMR 系（metrics.py でセット）

| 内部カラム名 | 型 | 表示名 | 計算元 |
|-------------|----|--------|--------|
| `emmr_pre` | float? | eMMR（試合前） | 前試合の `emmr_post` |
| `emmr_post` | float? | eMMR（試合後） | `csr_avg20 + 200 × ln(k_ratio) - penalty` |
| `emmr_delta` | float? | eMMR増減 | `emmr_post - emmr_pre` |
| `emmr_v2` | float? | eMMR v2 | カルマンフィルタ適用後 |
| `emmr_v2_sigma` | float? | eMMR v2 不確実性 | カルマン分散の平方根 |

### 5.6 計算指標（metrics.py でセット）

| 内部カラム名 | 型 | 表示名 | 計算式 |
|-------------|----|--------|--------|
| `kd_ratio` | float | K/D | `kills / deaths`（deaths=0 のとき `kills`） |
| `kda` | float | KDA | `kills - deaths + assists / 3` |
| `accuracy` | float? | 命中率 | `shots_hit / shots_fired`（0除算は None） |
| `damage_diff` | int | ダメージ差 | `damage_dealt - damage_taken` |
| `kill_efficiency` | float? | キル効率 | `damage_dealt / (kills + assists/3)` |
| `death_efficiency` | float? | デス効率 | `damage_taken / deaths` |
| `perfect_rate` | float? | パーフェクト率 | `perfect_kills / kills` |
| `kpm` | float? | KPM | `kills / (duration_sec / 60)` |
| `dpm` | float? | DPM | `deaths / (duration_sec / 60)` |
| `damage_dealt_per_min` | float? | 与ダメージ/分 | `damage_dealt / (duration_sec / 60)` |
| `damage_taken_per_min` | float? | 被ダメージ/分 | `damage_taken / (duration_sec / 60)` |
| `power_kill_density` | float? | 重火器キル密度 | `power_kills / (duration_sec / 60)` |

### 5.7 パーティ・セッション系（parser.py でセット）

| 内部カラム名 | 型 | 表示名 | 計算元 |
|-------------|----|--------|--------|
| `party_size` | int | パーティ人数 | `build_party_map()` で推定（1〜4） |
| `party_type` | string | パーティタイプ | party_size → ラベル変換 |
| `is_solo` | bool | ソロフラグ | `party_size == 1` |
| `is_party` | bool | パーティフラグ | `party_size > 1` |
| `session_id` | int | セッションID | 時系列ギャップ（2時間）で分割 |
| `session_seq` | int | セッション内試合番号 | セッション内の連番（1始まり） |

---

## 6. 計算指標の定義

### K/D（キルデスレシオ）

```
K/D = kills / deaths
     deaths=0 のとき kills
```

### KDA（キルデスアシスト）

```
KDA = kills - deaths + (assists / 3)
```

アシスト3回をキル1回相当とみなす。

### 命中率

```
accuracy = shots_hit / shots_fired
         shots_fired=0 のとき None
```

### K-RPI（相対キルパフォーマンス指数）

```
K-RPI = kills / expected_kills
```

| 値 | 解釈 |
|----|------|
| `= 1.0` | 期待通りにキルできている |
| `< 1.0` | 期待より取れていない（アグレッション不足 or ポジション問題） |
| `> 1.0` | 期待を上回るキル（ポップオフ） |

### D-RPI（相対デスパフォーマンス指数）

```
D-RPI = expected_deaths / deaths
```

| 値 | 解釈 |
|----|------|
| `= 1.0` | 期待通りの死に数 |
| `> 1.0` | 期待より死ななかった（生存力が高い） |
| `< 1.0` | 期待より多く死んでいる（立ち回りの問題） |

### LGAI（ロビー格差補正インパクト）

```
LGAI = enemy_mmr - csr_pre
```

| 値 | 解釈 |
|----|------|
| `正` | 格上相手のロビー |
| `0` 付近 | 均衡マッチ |
| `負` | 格下相手のロビー |

### インパクトスコア

```
Impact Score = (K-RPI + D-RPI) / 2
```

TrueSkill2 基準の総合パフォーマンス指標。1.0 が平均。

### 生存貢献度

```
Survival = (expected_deaths - deaths) × (enemy_mmr / csr_pre)
```

格上相手にどれだけ死なずに戦えたかを測る。正の値が望ましい。

### eMMR v1

```
emmr_post = AvgCSR20 + 200 × ln((kills + 1) / (expected_kills + 1)) - penalty
penalty   = min((party_size - 1) / 3 × 50, 50)
```

### eMMR v2（カルマンフィルタ）

複合スタッツ（k_z × 0.6 + dmg_z × 0.3 + ast_z × 0.1）と CSR ストッパーを用いた
カルマンフィルタで平滑化した推定MMR。

---

## 7. 除外フラグ判定ルール

`load_matches()` 内で以下の優先順位で判定される。

```
1. duration_sec < 60         → "short_match"   （試合時間1分未満）
2. JoinedInProgress == true  → "incomplete"     （途中参加）
3. Outcome == 4              → "incomplete"     （途中抜け）
4. PresentAtCompletion == false → "incomplete"  （終了時不在）
5. 上記すべてクリア          → ""（空文字）      （正常データ）
```

> 除外フラグが付いてもデータは削除されない。各ビューでフィルタリング可能。

---

## 8. eMMR 計算パラメータ

| パラメータ | 値 | 説明 |
|-----------|-----|------|
| `PROCESS_NOISE (Q)` | `400.0`（v2） | カルマンフィルタのプロセスノイズ（MMRの真の変動の大きさ） |
| `PERF_NOISE (R_PERF)` | `20.0`（v2） | パフォーマンス観測ノイズ |
| `CSR_NOISE (R_CSR)` | `50.0`（v2） | CSR観測ノイズ |
| `INITIAL_SIGMA` | `10000.0`（v2 初期分散） | 初期不確実性 |
| `V1_PENALTY_MAX` | `50` | eMMR v1 のパーティペナルティ上限 |
| `SESSION_GAP_SEC` | `7200`（2時間） | セッション分割の閾値 |

### カルマンフィルタ更新式

```
1. 予測:     mu_prior = mu, sigma_sq_prior = sigma_sq + Q
2. 更新(perf):  k_gain = sigma_sq_prior / (sigma_sq_prior + R_PERF)
               mu = mu_prior + k_gain × (meas_perf - mu_prior)
               sigma_sq = (1 - k_gain) × sigma_sq_prior
3. 更新(csr):   k_gain = sigma_sq_prior / (sigma_sq_prior + R_CSR)
               mu = mu_prior + k_gain × (csr - mu_prior)
               sigma_sq = (1 - k_gain) × sigma_sq_prior
```

### デフォルト初期値（プレイリスト別）

| プレイリスト | `DEFAULT_MU` | 備考 |
|-------------|-------------|------|
| `ranked_arena` | `900.0` | ランクアリーナの初期値 |
| `ranked_slayer` | `1200.0` | ランクスレイヤーの初期値 |
| その他 | `1000.0` | グローバルデフォルト |