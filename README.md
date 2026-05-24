# 🌊 Flood-Lab — Halo Infinite 戦績分析ツール

OpenSpartan のローカル DB からデータを読み込み、Streamlit でブラウザ上に可視化する戦績分析ツールです。  
[Flood](https://github.com/Du1Bz/Flood)（Notion 同期ツール）の精神的後継で、より自由な分析を目的としています。

> **これは現在進行中のプロジェクト（Work In Progress）です**  
> **このツールは個人用途で作成されたものであり、環境構築やトラブルシュートを自力で行える方向けです。**  
> **ただしできるだけ導線は整えました。セットアップは bat ファイルをダブルクリックするだけです。**

---

## 📋 必要なもの

| 必要なもの | 備考 |
|---|---|
| Windows 10 / 11 | Mac 非対応 |
| [Halo Infinite](https://www.halowaypoint.com/) | Xbox / PC 版どちらでも可 |
| [OpenSpartan Workshop](https://github.com/OpenSpartan/openspartan-workshop/releases) | 戦績を取得するツール |
| [Python 3.11 以上](https://www.python.org/downloads/) | 無料 |

---

## 🚀 セットアップ手順

### Step 1｜ファイルをダウンロードする

右側の [Releases](https://github.com/Du1Bz/Flood-Lab/releases) ページから最新版の `Source code (zip)` をダウンロードして解凍します。  
または Git を使える方は以下を実行してください。

```
git clone https://github.com/Du1Bz/Flood-Lab.git
```

### Step 2｜Python をインストールする

1. [https://www.python.org/downloads/](https://www.python.org/downloads/) を開く
2. 「Download Python 3.x.x」をクリックしてダウンロード
3. インストーラーを起動し、**「Add Python to PATH」に必ずチェックを入れてから** Install Now をクリック

> ⚠️ このチェックを忘れるとツールが動きません。チェックし忘れた場合は Python をアンインストールして入れ直してください。

### Step 3｜OpenSpartan Workshop をインストールする

> ⚠️ **必ず 1.0.10 以下をインストールしてください。**  
> 1.0.11、1.0.12では現在、データの一部が正しく取得できないバグが確認されています。

**① Windows App Runtime のインストール（先にやる）**

以下の URL を開いてダウンロード・インストールします。

```
https://aka.ms/windowsappsdk/1.6/latest/windowsappruntimeinstall-x64.exe
```

> ⚠️ OpenSpartan1.0.10では、最新版（1.8.x）だとクラッシュします。必ず 1.6.x をインストールしてください。

**② OpenSpartan Workshop 1.0.10 のインストール**

[リリースページ](https://github.com/OpenSpartan/openspartan-workshop/releases) から `1.0.10` の `.exe` をダウンロードしてインストールします。

**③ 起動後すぐクラッシュする場合**

エクスプローラーのアドレスバーに `%LOCALAPPDATA%\OpenSpartan.Workshop\` と入力して Enter を押し、`settings.json` を開いて `extraRitualEvents` の行を削除して保存。  
その後ファイルを右クリック →「プロパティ」→「読み取り専用」にチェックを入れます。

**④ データの同期**

1. OpenSpartan Workshop を起動して Xbox アカウントでログイン
2. データが同期されるまで待つ（初回は数分かかります）
3. 以下のフォルダに `.db` ファイルが生成されれば OK

```
C:\Users\あなたのユーザー名\AppData\Local\OpenSpartan.Workshop\data\
```

> `AppData` が見えない場合はエクスプローラーの「表示」→「隠しファイル」を表示にしてください。

### Step 4｜起動する

`Flood-Lab.bat` をダブルクリックするだけで、自動で以下が行われたあと Streamlit が起動します。

- Python 仮想環境（`.venv`）がなければ作成
- 必要な Python パッケージの自動インストール
- `config.ini` がなければ `config.ini.example` からコピー
- OpenSpartan の `.db` ファイルが存在するか確認（なくても起動は可能）
- Streamlit 起動 → ブラウザで `http://localhost:8501` が開く

すでに Flood-Lab が起動中の場合は、再度バッチを実行するとブラウザのタブが開くだけです。

---

## 🖥️ 画面構成

| ページ | 内容 |
|---|---|
| 🌊 **ホーム** | サマリーカード・カレンダーヒートマップ・eMMR推移・インサイト |
| 📊 **分析** | フィルターで絞り込んでグラフを自由に探索（トレンド・マップ/ルール・TrueSkill2・オブジェクト） |
| 📅 **レポート** | 期間指定でレポートを生成（サマリー・セッション・トップ試合・マップ別パフォーマンス） |
| 🔬 **仮説検証** | 各種統計検定（t検定・ANOVA・相関・回帰分析） |
| 📋 **試合履歴** | 全試合一覧（CSVエクスポート機能付き） |

---

## 📂 ディレクトリ構成

```
Flood-Lab/
├── app.py                  # エントリポイント
├── Flood-Lab.bat           # セットアップ兼起動バッチ
├── config.ini.example      # 設定ファイルサンプル
├── requirements.txt        # Python 依存パッケージ一覧
├── src/
│   ├── core/
│   │   ├── config.py       # 設定・XUID自動検出
│   │   └── database.py     # SQLite読み込み・JSON展開
│   ├── logic/
│   │   ├── parser.py       # パーティ検出・セッション分割
│   │   ├── metrics.py      # eMMR v2・K-RPI・D-RPI 等
│   │   ├── processor.py    # パイプライン統合
│   │   ├── insights.py     # インサイトエンジン
│   │   └── exporter.py     # AI相談用JSONエクスポート
│   ├── utils/
│   │   ├── helpers.py      # 日付変換・数値ユーティリティ
│   │   ├── display.py      # カラム名対応表・表示名変換
│   │   └── session.py      # Streamlitセッション管理
│   ├── components/
│   │   └── calendar_heatmap.py  # カレンダーヒートマップ（SVG不使用）
│   └── pages/
│       ├── app_home.py     # ホーム画面
│       ├── analysis.py     # 分析画面
│       ├── report.py       # レポート画面
│       ├── hypothesis.py   # 仮説検証画面
│       └── history.py      # 試合履歴画面
├── docs/                   # ドキュメント
└── sandbox/                # 実験用スクリプト
```

---

## 📊 記録される主なデータ

| カラム | 内容 |
|---|---|
| マップ / ルール | 試合のマップとゲームモード |
| 勝敗 / チームスコア | 試合結果 |
| K/D / KDA | キル・デス・アシスト比 |
| 命中率 / ダメージ差 | 精度と攻守バランス |
| 期待キル / 期待デス | TrueSkill2 がそのプレイヤーに期待する値 |
| eMMR | 推定 MMR（独自計算） |
| K-RPI / D-RPI | キル達成率・生存率（TrueSkill2 ベース） |
| 自チーム / 敵チーム MMR | マッチングの実力帯 |
| CSR | ランクの増減 |
| パーティ人数 | ソロ・パーティの別 |
| PWコントロール率 | パワーウェポン支配率 |
| エンゲージメント密度 | 試合への関与の濃さ |

詳細は [`docs/METRICS.md`](docs/METRICS.md) を参照してください。

---

---

## ❓ よくあるエラー

**「Python が見つかりません」**  
→ Python インストール時に「Add Python to PATH」をチェックしたか確認してください。

**「OpenSpartan のデータベースファイルが見つかりません」**  
→ OpenSpartan Workshop を起動してデータを同期してください。

**「○○というカラムがありません」**  
→ OpenSpartan 1.0.11 以降のバグです。**1.0.10 以下を使用してください。**

---

## 🔧 設計思想

詳細は [`docs/PROJECT.md`](docs/PROJECT.md) を参照してください。

**取捨選択はビューで行う。ストレージには全部入れる。**  
JSON の全フィールドを展開し、絞り込みはフィルター・グラフのレイヤーで行います。

**フィルタはデータを捨てない。除外フラグで表現する。**  
途中抜け・短時間試合もデータとして保持し、`exclude_flag` で管理します。

---

## 注意

これは趣味の個人プロジェクトです。  
このプロジェクトは Du1Bz 個人が利用するために作ったプログラムを公開しているものです。  
このプロジェクト、OpenSpartan を利用したことで発生したいかなる事象、損害に対しても責任は負いません。

---

## 📄 ライセンス

MIT License