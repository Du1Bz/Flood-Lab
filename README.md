# 🌊 Flood-Lab

OpenSpartan のローカル DB → Python で加工 → Streamlit でブラウザ分析。  
[Flood](https://github.com/Du1Bz/Flood)（Notion 同期ツール）の精神的後継。

## 設計理念

**取捨選択はビューで行う。ストレージには全部入れる。**  
JSON の全フィールドを展開し、絞り込みはフィルター・グラフのレイヤーで行う。

**フィルタはデータを捨てない。除外フラグで表現する。**  
途中抜け・短時間試合もデータとして保持し、`exclude_flag` で管理する。

---

## セットアップ

### 1. 前提条件

- Python 3.11 以上
- [OpenSpartan Workshop](https://openspartan.com/) でデータ同期済みであること

### 2. 仮想環境の作成と依存関係のインストール

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. 設定ファイル（省略可能）

OpenSpartan の DB は自動検出されます。  
複数アカウントを使用する場合のみ `config.ini` を作成してください。

```bash
cp config.ini.example config.ini
# config.ini を編集して xuid を指定
```

### 4. 起動

```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` が開きます。

---

## ディレクトリ構成

```
Flood-Lab/
├── app.py                  # エントリポイント
├── src/
│   ├── core/
│   │   ├── config.py       # 設定・XUID 自動検出
│   │   └── database.py     # SQLite 読み込み・JSON 展開
│   ├── logic/
│   │   ├── parser.py       # パーティ検出・セッション分割
│   │   ├── metrics.py      # eMMR v2・K-RPI・D-RPI 等
│   │   └── processor.py    # パイプライン統合
│   ├── utils/
│   │   ├── helpers.py      # 日付変換・数値ユーティリティ
│   │   └── display.py      # カラム名対応表・表示名変換
│   └── pages/
│       └── dashboard.py    # 自由分析ビュー
├── docs/                   # ドキュメント
├── sandbox/                # 実験用 Jupyter Notebook
└── config.ini.example
```

---

## Phase ロードマップ

- [x] **Phase 1** — コア: データ読み込み・自由分析ビュー
- [ ] **Phase 2** — レポート・インサイトエンジン
- [ ] **Phase 3** — AI エクスポート・ゲーマータグ変換
