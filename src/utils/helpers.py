"""
utils/helpers.py
----------------
日付変換・数値の丸め・共通ユーティリティ関数。
他のモジュールに依存しない純粋関数のみを置く。
"""

from __future__ import annotations

import math
import re
from datetime import datetime, timezone, timedelta
from typing import Any

# 日本標準時
JST = timezone(timedelta(hours=9))


# ==================================================
# 汎用アクセサ
# ==================================================

def safe_get(d: Any, *keys: Any, default: Any = None) -> Any:
    """
    ネストした辞書・リストを安全に辿る。
    途中でキーが存在しなければ default を返す。

    例: safe_get(obj, "MatchInfo", "StartTime")
    """
    cur = d
    for k in keys:
        try:
            cur = cur[k]
        except (KeyError, IndexError, TypeError):
            return default
    return cur


# ==================================================
# 数値ユーティリティ
# ==================================================

def safe_number(
    value: Any,
    decimals: int | None = None,
) -> int | float | None:
    """
    数値サニタイザ。

    - None → None
    - nan / inf → None
    - decimals 指定時は四捨五入
    - 整数に丸められる値は int で返す
    """
    if value is None:
        return None
    try:
        x = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(x):
        return None
    if decimals is not None:
        return round(x, decimals)
    if abs(x - round(x)) < 1e-9:
        return int(round(x))
    return x


def nn(
    value: Any,
    decimals: int | None = None,
    default: Any = None,
) -> int | float | None:
    """safe_number の短縮版。default を指定すると None の代わりにその値を返す。"""
    result = safe_number(value, decimals)
    return default if result is None else result


# ==================================================
# 日付ユーティリティ
# ==================================================

def utc_to_jst(s: str | None) -> str | None:
    """
    ISO 8601 UTC 文字列（末尾 Z 可）を JST の isoformat 文字列に変換する。
    変換失敗時は None を返す。
    """
    if not s:
        return None
    try:
        return (
            datetime.fromisoformat(s.replace("Z", "+00:00"))
            .astimezone(JST)
            .isoformat()
        )
    except (ValueError, TypeError):
        return None


def parse_dt_jst(s: str | None) -> datetime | None:
    """
    ISO 8601 UTC 文字列を JST の datetime オブジェクトに変換する。
    変換失敗時は None を返す。
    """
    if not s:
        return None
    try:
        return (
            datetime.fromisoformat(s.replace("Z", "+00:00"))
            .astimezone(JST)
        )
    except (ValueError, TypeError):
        return None


def week_label(dt: datetime) -> str:
    """datetime → '2026年5月2週' 形式の文字列"""
    return f"{dt.year}年{dt.month}月{(dt.day - 1) // 7 + 1}週"


def month_label(dt: datetime) -> str:
    """datetime → '2026年5月' 形式の文字列"""
    return f"{dt.year}年{dt.month}月"


# ==================================================
# 試合データユーティリティ
# ==================================================

def parse_seconds(text: str | None) -> int | None:
    """
    ISO 8601 期間文字列（例: "PT9M7S", "PT1H2M30S"）を秒数（int）に変換する。
    変換失敗時は None を返す。
    """
    if not text:
        return None
    try:
        h = m = s = 0
        if a := re.search(r"(\d+)H", text):
            h = int(a.group(1))
        if b := re.search(r"(\d+)M", text):
            m = int(b.group(1))
        if c := re.search(r"(\d+(?:\.\d+)?)S", text):
            s = float(c.group(1))
        return int(h * 3600 + m * 60 + s)
    except (ValueError, AttributeError):
        return None


def format_duration(seconds: int | None) -> str:
    """秒数 → 'MM:SS' 形式の文字列"""
    if seconds is None:
        return "--:--"
    return f"{seconds // 60}:{seconds % 60:02d}"
