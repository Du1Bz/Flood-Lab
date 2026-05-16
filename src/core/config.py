"""
core/config.py
--------------
config.ini の読み込みと XUID 自動検出。

設計方針:
- Notion 関連は一切持たない（Flood-Lab 専用設定）
- XUID は OpenSpartan DB ファイル名から自動検出
- sys.exit() はここに集約しない（Streamlit との相性が悪いため例外で返す）
"""

from __future__ import annotations

import configparser
import os
from dataclasses import dataclass
from pathlib import Path


# ==================================================
# プロジェクトルートの解決
# ==================================================

def _find_project_root() -> Path:
    """src/core/ から2階層上がったディレクトリをプロジェクトルートとする。"""
    return Path(__file__).resolve().parent.parent.parent


PROJECT_ROOT = _find_project_root()
CONFIG_PATH  = PROJECT_ROOT / "config.ini"


# ==================================================
# 設定データクラス
# ==================================================

@dataclass
class AppConfig:
    """アプリケーション全体の設定。"""
    my_xuid:      str          # "xuid(数字)" 形式
    db_path:      Path         # OpenSpartan SQLite ファイルパス
    latest_count: int = 500    # 一度に処理する最大試合数


# ==================================================
# XUID 自動検出
# ==================================================

def _openspartan_data_dir() -> Path | None:
    r"""%LOCALAPPDATA%\OpenSpartan.Workshop\data を返す。存在しない場合は None。"""
    appdata = os.getenv("LOCALAPPDATA")
    if not appdata:
        return None
    d = Path(appdata) / "OpenSpartan.Workshop" / "data"
    return d if d.exists() else None


def find_openspartan_dbs() -> list[Path]:
    """
    OpenSpartan の data ディレクトリから、ファイル名が数字のみの .db を探す。
    見つかった順にリストで返す。見つからなければ空リスト。
    """
    data_dir = _openspartan_data_dir()
    if not data_dir:
        return []
    return [f for f in data_dir.glob("*.db") if f.stem.isdigit()]


def auto_detect_xuid_and_path() -> tuple[str, Path] | None:
    """
    XUID と DB パスを自動検出する。
    DB が1つだけ見つかれば (xuid, path) を返す。
    複数 or 0件は None を返す（呼び出し側で UI 処理）。
    """
    dbs = find_openspartan_dbs()
    if len(dbs) == 1:
        db = dbs[0]
        return f"xuid({db.stem})", db
    return None


# ==================================================
# config.ini の読み込み
# ==================================================

def load_config(config_path: Path = CONFIG_PATH) -> AppConfig:
    """
    config.ini を読み込んで AppConfig を返す。
    config.ini が存在しない場合は XUID 自動検出を試みる。
    自動検出も失敗した場合は ValueError を送出する。
    """
    cfg = configparser.ConfigParser()

    xuid_raw: str | None = None
    db_path:  Path | None = None
    latest_count = 500

    # --- config.ini が存在すれば読む ---
    if config_path.exists():
        cfg.read(config_path, encoding="utf-8")
        xuid_raw = cfg.get("Player", "xuid", fallback="").strip() or None
        db_path_str = cfg.get("Player", "db_path", fallback="").strip() or None
        if db_path_str:
            db_path = Path(db_path_str)
        try:
            latest_count = int(cfg.get("Settings", "latest_count", fallback="500"))
        except ValueError:
            latest_count = 500

    # --- XUID / db_path が未設定なら自動検出 ---
    if not xuid_raw or not db_path:
        detected = auto_detect_xuid_and_path()
        if detected:
            auto_xuid, auto_db = detected
            if not xuid_raw:
                xuid_raw = auto_xuid
            if not db_path:
                db_path = auto_db

    if not xuid_raw or not db_path:
        raise ValueError(
            "OpenSpartan の DB が見つかりませんでした。\n"
            "config.ini に xuid と db_path を設定するか、\n"
            "OpenSpartan Workshop を起動してデータを同期してください。"
        )

    if not db_path.exists():
        raise FileNotFoundError(f"DB ファイルが見つかりません: {db_path}")

    # xuid の形式を統一
    xuid = xuid_raw if xuid_raw.startswith("xuid(") else f"xuid({xuid_raw})"

    return AppConfig(
        my_xuid=xuid,
        db_path=db_path,
        latest_count=latest_count,
    )
