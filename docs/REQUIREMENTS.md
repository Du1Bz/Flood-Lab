# Flood-Lab 要件定義

## 理念

**取捨選択はビューで行う。ストレージには全部入れる。**

OpenSpartan が持つ JSON の全フィールドを捨てずに DataFrame に展開する。  
どのデータが後で意味を持つかは分析してみないとわからない。  
絞り込みはフィルター・集計・可視化のレイヤーで行う。

**フィルタはデータを捨てない。除外フラグで表現する。**

途中抜け試合・1分未満の試合など、統計上ノイズになるデータも取り込む。  
集計・インサイトの対象から外すだけで、データとしては保持する。

| 除外理由 | `exclude_flag` の値 |
|---|---|
| 試合時間が1分未満 | `short_match` |
| 途中参加・途中抜け | `incomplete` |
| BOT参加試合 | `bot_match` |
| 発射数30以下（AFK・マップラン等） | `low_shots` |
| カスタムゲームで非ランクルール / 非ランクマップ | `custom_non_ranked` |
| 手動除外 | `manual` |

集計・インサイトは `exclude_flag` が空の試合のみを対象にする。  
試合履歴ビューは除外フラグの有無にかかわらず全件表示する。

---

## プロジェクトのゴール

OpenSpartan のローカル DB → Python で加工 → セルフホスティング Streamlit → ブラウザで分析・可視化

Flood（Notion同期ツール）の分析ロジックを流用しつつ、**ローカル完結で自由に可視化できる環境**を作る。

---

## アーキテクチャ

### データフロー（一方向・循環参照なし）

```
OpenSpartan ローカルDB（読み取り専用）
  %LOCALAPPDATA%\OpenSpartan.Workshop\data\{xuid}.db
       │
       ▼ 読み取り専用接続・JSON展開・st.cache_data キャッシュ
┌──────────────────────────────────┐
│  src/core/database.py           │
│  src/core/config.py             │  ← XUID自動検出・設定読み込み
└──────────────┬───────────────────┘
               │ raw DataFrame（全フィールド展開済み）
               ▼
┌──────────────────────────────────┐
│  src/logic/parser.py            │  ← マップ名/モード名紐付け
│                                  │    パーティ検出
└──────────────┬───────────────────┘
               │ parsed DataFrame
               ▼
┌──────────────────────────────────┐
│  src/logic/metrics.py           │  ← eMMR v2・K-RPI・D-RPI・CSR
└──────────────┬───────────────────┘
               │ metrics付き DataFrame
               ▼
┌──────────────────────────────────┐
│  src/logic/processor.py         │  ← セッション分割・時系列集計
│                                  │    マップ別/プレイリスト別集計
└──────────────┬───────────────────┘
               │ 集計済み DataFrameセット
               ▼
┌──────────────────────────────────┐
│  src/logic/insights.py          │  ← 統計ベース異常検出（Lv.2）
└──────────────┬───────────────────┘
               │ インサイトリスト
               ▼
┌──────────────────────────────────┐
│  app.py + src/pages/            │
│  st.navigation() で4ページ管理  │
│                                  │
│  src/pages/app_home.py          │  ← ホーム（カレンダーHM含む）
│  src/pages/dashboard.py         │  ← 自由分析ビュー
│  src/pages/report.py            │  ← 定型レポートビュー
│  src/pages/history.py           │  ← 試合履歴ビュー
└──────────────────────────────────┘
```

**原則：各レイヤーは1つ上のレイヤーにしか依存しない。逆方向・横断的な依存は禁止。**

---

## Floodからの流用方針

Flood-Lab は Flood の可視化専用フォーク。Notion 関連コードを除いた以下をほぼそのまま移植する。

| Flood のファイル | Flood-Lab への流用 | 変更点 |
|---|---|---|
| `src/core/database.py` | `src/core/database.py` | `st.cache_data` デコレータを追加 |
| `src/core/config.py` | `src/core/config.py` | Notion 関連フィールドを全削除 |
| `src/logic/parser.py` | `src/logic/parser.py` | `build_match_props`（Notion形式変換）を削除 |
| `src/logic/metrics.py` | `src/logic/metrics.py` | そのまま流用 |
| `src/utils/helpers.py` | `src/utils/helpers.py` | そのまま流用 |

---

## 設定ファイル

Flood と Flood-Lab は **完全に別の `config.ini`** を持つ。Notion トークン等は不要。

```ini
[Player]
# xuid は通常省略可能（自動検出される）
# 複数アカウントのDBがある場合のみ手動指定
# xuid = 1234567890

[Settings]
latest_count = 500
```

### XUID 自動検出フロー

OpenSpartan は `%LOCALAPPDATA%\OpenSpartan.Workshop\data\` に
**ファイル名が数字のみ**（= XUID）の `.db` ファイルを生成する。

| ケース | 挙動 |
|---|---|
| 1ファイルだけ見つかった | 自動採用（確認不要） |
| 複数見つかった | サイドバーのセレクトボックスで選択させる |
| 見つからない | エラーメッセージ＋手動パス入力UIを表示 |
| `config.ini` に `xuid` が明示されている | 自動検出をスキップして `config.ini` の値を使用 |

実装は Flood の `setup.py:get_openspartan_db_info()` のロジックを参考にする。

---

## データ更新方針

- データ収集は **OpenSpartan に完全に任せる**。Flood-Lab は読み取り専用。
- 起動時に SQLite を全件読み込み → `st.cache_data` でキャッシュ（TTL なし）。
- サイドバーの **「🔄 データ更新」ボタン** を押すと `st.cache_data.clear()` で再読み込み。
- 試合後に OpenSpartan が DB を更新したら、このボタン1回で反映される。

---

## セッション分割

- マッチの **終了時刻と次のマッチの開始時刻の差が 2 時間以上** で別セッションとみなす。
- 実装は Flood の `sync.py:build_sessions()` をそのまま流用する。
- セッション内の試合番号（1試合目、2試合目…）をセッション疲労分析に使用する。

---

## パーティ検出

Flood の `parser.py:build_party_map()` をそのまま流用する。

- **カスタムゲーム**（Playlist なし）: 4人固定
- **ランク試合**: 前後2試合を含むウィンドウ（最大5試合）で、同チームに **3回以上** 登場した味方 = パーティメンバー
- 条件を満たさない = ソロ（1人）

---

## 3つのビュー

### ① 自由分析ビュー（ダッシュボード）

サイドバーで条件を自由に変更して、インタラクティブに分析する画面。

**サイドバー：**
- 「🔄 データ更新」ボタン
- 期間：直近N戦 / 今月 / 今週 / カスタム期間
- 区分選択（ランクアリーナ / ランクスレイヤー / ランクダブルス / ランクFFA / ランクスナイパーズ / カジュアル / BTB / PvE / カスタムゲーム / 全部）
- マップ選択
- ルール選択
- ※3つの絞り込みは AND 条件で連動する（区分 × マップ × ルール）

**表示するもの：**
- KDA / Accuracy / Damage の時系列折れ線（Plotly）＋移動平均線（デフォルト：直近10試合）を重ねて表示
- 区分 × マップ × ルール のクロス集計（勝率 / 平均K/D / 平均ダメージ差）
- マップ別 KDA・勝率の棒グラフ
- 区分別比較
- KDA vs Accuracy の散布図
- eMMR v2 推移グラフ
- CSR 推移グラフ（区分ごとに管理）
- マッチ一覧テーブル（フィルター連動）

### ③ 試合履歴ビュー

全試合を時系列で確認できるビュー。除外フラグの有無にかかわらず全件表示する。

**サイドバーフィルター：**
- 期間
- 区分 / マップ / ルール
- 除外フラグの表示 / 非表示切り替え

**表示：**
- 1行1試合のテーブル（日時 / マップ / ルール / 勝敗 / K/D / ダメージ差 / CSR増減 / 除外フラグ）
- 行クリックで全フィールドの詳細展開
- CSV エクスポートボタン（AI相談用途を想定。Phase 3）

### ② 定型レポートビュー（スナップショット）

期間を選ぶと、決まったレイアウトで「週次レポート」として表示。

**期間選択：**
- 週単位（例：2026年5月第2週）
- 月単位
- カスタム期間

**表示レイアウト（固定）：**
- KPM（Kills Per Minute）推移グラフ
- 最も活躍したマップ TOP3
- 最も KDA が高かった / 低かった試合
- 区分別勝率
- 前週比の変化（KDA / Accuracy / WinRate）
- **インサイト（統計ベース Lv.2）**（後述）

---

## インサイトエンジン（Lv.2 統計ベース）

定型レポートビューの下部に表示する。閾値は当面ハードコード。  
移動平均・標準偏差・信頼区間を使い「統計的に有意な変化」のみ検出して通知する。

> **閾値について**：以下の判定基準はすべて初期値（仮置き）。  
> 実運用で誤検知・見逃しを確認しながら `insights.py` 内の定数を調整する。

### パフォーマンス系

| 検出内容 | 判定基準 |
|---|---|
| スランプ検知 | 直近10戦の KDA / Accuracy が過去移動平均から **1σ 以上低下** |
| 連敗アラート | 同一セッション内で **5連敗以上** |

### 弱点検出系

| 検出内容 | 判定基準 |
|---|---|
| 苦手マップ検出 | マップ別勝率の **95%信頼区間の上限が全体平均を下回り、かつ10試合以上** |
| 苦手ルール検出 | ルール別 KDA の **95%信頼区間の上限が全体平均を下回り、かつ10試合以上** |
| パーティ編成の異常 | パーティタイプ別勝率の **95%信頼区間の上限が全体平均を下回り、かつ10試合以上** |

### TrueSkill2 系

| 検出内容 | 判定基準 |
|---|---|
| キル不足パターン | K-RPI が直近10戦で **連続して1.0未満** |
| 生存できているのにキルが取れていない | D-RPI > 1.1 かつ K-RPI < 0.9 が直近10戦で過半数 |

### ロビー系

| 検出内容 | 判定基準 |
|---|---|
| 格上ロビー連続 | LGAI（ロビー格差）が直近5戦で **全て正（格上）** |

### セッション疲労系

| 検出内容 | 判定基準 |
|---|---|
| セッション後半パフォーマンス低下 | セッション内で試合番号が進むほど KDA が低下する **負の相関（r < -0.4）** が複数セッションで観測される |
| 推奨引き時点 | セッション内で N 試合目以降の勝率が前半より **有意に低い** 場合、平均的な「やめどき」を表示 |

---

## 開発フロー

新しい指標・分析アイデアは **`sandbox/` 以下の Jupyter Notebook で先に試す**。  
有用だと判断したものだけ `src/logic/metrics.py` や `src/logic/processor.py` に正式実装する。

```
sandbox/
├── explore_kda.ipynb       # 例：KDA分布の探索
├── explore_emmr.ipynb      # 例：eMMR v2 の挙動確認
└── ...                     # 実験用。コミット任意
```

- Notebook は使い捨て前提。再現性より速度を優先。
- 正式実装時に初めてテスタブルな関数として `src/` に切り出す。
- `docs/METRICS.md` に指標の定義・計算式・採用理由を記録する。

---

## Phase スコープ

### Phase 1 — コア ✅ 完了

**目標：データ読み込み → Streamlit 起動 → 自由分析ビューで KDA / Accuracy が見られる**

- [x] `src/core/config.py`: XUID 自動検出、`config.ini` 読み込み（Flood から移植・Notion 関連削除）
- [x] `src/core/database.py`: SQLite 接続（読み取り専用）、マッチデータ JSON 展開、`st.cache_data` キャッシュ（Flood から移植）
- [x] `src/logic/parser.py`: マッチサマリ DataFrame 生成、マップ名 / モード名の紐付け、パーティ検出（Flood から移植・Notion 形式変換削除）
- [x] `src/logic/metrics.py`: eMMR v2、K-RPI / D-RPI、CSR（Flood からそのまま移植）
- [x] `src/logic/processor.py`: 時系列集計、マップ別 / プレイリスト別集計（新規）
- [x] `src/utils/helpers.py`: 共通ユーティリティ（Flood からそのまま移植）
- [x] `app.py` + `src/pages/dashboard.py`: サイドバーナビ、自由分析ビュー（フィルター + KDA 時系列折れ線 + マップ別棒グラフ + マッチ一覧）
- [x] 環境セットアップ（.venv, requirements.txt, pyproject.toml）
- [x] README にセットアップ手順・使い方を記載

### Phase 2 — レポート・インサイト強化 ✅ 完了

- [x] セッション自動分割（Flood の `build_sessions()` 移植）
- [x] CSR 推移グラフ追加（区分別）
- [x] 散布図（KDA vs Accuracy 等）追加
- [x] 区分 × マップ × ルール クロス集計ビュー実装
- [x] `src/pages/report.py`: 定型レポートビュー実装
- [x] `src/pages/history.py`: 試合履歴ビュー実装（除外フラグ表示・詳細展開）
- [x] `src/logic/insights.py`: インサイトエンジン実装（Lv.2 統計ベース）

### Phase 3 — 実験・応用

- [ ] メダル分析（NameId の解釈）
- [ ] 対戦相手分析
- [ ] 時系列の移動平均切り替え
- [ ] カスタムクエリ入力
- [ ] AI 相談用データエクスポート（集計済み DataFrame → CSV / JSON 出力）
- [ ] `src/utils/gamertag.py`: XUID → ゲーマータグ変換（Halo 公開 API + ローカルキャッシュ）

---

## 技術スタック

| レイヤー | 技術 | 用途 |
|---|---|---|
| データソース | SQLite (OpenSpartan) | 読み取り専用で接続 |
| 抽出・加工 | Python + Pandas + NumPy | JSON 展開、正規化、集計、eMMR 計算 |
| 可視化 | Streamlit + Plotly | ダッシュボード、チャート |
| 統計 | scipy | インサイトエンジン（信頼区間・相関） |
| 環境管理 | Python .venv + pyproject.toml | 依存関係分離 |

---

## ディレクトリ構成

```
Flood-Lab/
├── app.py                      # エントリポイント（streamlit run の対象）
├── src/
│   ├── core/
│   │   ├── config.py           # config.ini 読み込み・XUID 自動検出
│   │   └── database.py         # SQLite 接続・JSON 展開・キャッシュ管理
│   ├── logic/
│   │   ├── parser.py           # 試合データのパース・パーティ検出
│   │   ├── metrics.py          # eMMR v2・K-RPI・D-RPI 等の計算ロジック
│   │   ├── processor.py        # 集計・セッション分割の統合
│   │   └── insights.py         # インサイトエンジン（Phase 2）
│   ├── utils/
│   │   ├── helpers.py          # 共通ユーティリティ
│   │   └── gamertag.py         # XUID→ゲーマータグ変換・キャッシュ（Phase 3）
│   ├── components/
│   │   └── calendar_heatmap.py # デイリーアクティビティ カレンダーHM
│   └── pages/
│       ├── app_home.py         # ホーム（サマリー + カレンダーHM）
│       ├── dashboard.py        # 自由分析ビュー
│       ├── report.py           # 定型レポートビュー（Phase 2）
│       └── history.py          # 試合履歴ビュー（Phase 2）
├── docs/
│   ├── REQUIREMENTS.md         ← これ
│   ├── METRICS.md              # 指標定義書（計算式・採用理由）
│   └── DB_SCHEMA.md
├── sandbox/                    # 実験用 Jupyter Notebook（コミット任意）
│   └── .gitkeep
├── data/                       # .gitignore 対象（キャッシュ用）
├── config.ini.example
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

※ OpenSpartan DB はプロジェクト内に置かない。  
　`%LOCALAPPDATA%\OpenSpartan.Workshop\data\{xuid}.db` を読み取り専用で開く。  
　`config.ini` は Flood とは完全に別ファイル（Notion トークン不要）。