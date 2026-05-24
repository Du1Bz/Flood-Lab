"""
utils/display.py
----------------
内部カラム名（英語スネークケース）と表示名（日本語）の対応。
API 数値 → 内部値への変換定数もここで管理する。
"""

from __future__ import annotations

# ==================================================
# API 数値 → 内部値への変換（parser.py で使用）
# ==================================================

OUTCOME_MAP: dict[int, str] = {
    1: "draw",
    2: "win",
    3: "loss",
    4: "did_not_finish",
}

# プレイリスト PublicName（lowercase）→ playlist 内部値
# 長い文字列を先に定義（部分一致なので順序重要）
PLAYLIST_NAME_MAP: list[tuple[str, str]] = [
    ("ranked arena",   "ranked_arena"),
    ("ranked slayer",  "ranked_slayer"),
    ("ranked doubles", "ranked_doubles"),
    ("ranked ffa",     "ranked_ffa"),
    ("ranked snipers", "ranked_snipers"),
    ("joint ops",      "pve"),
    ("new btb",        "btb"),
    ("big team",       "btb"),
    ("btb",            "btb"),
    # 上記に当てはまらないマッチメイドはすべてカジュアル
]

# LifecycleMode=3 × PlaylistExperience → playlist 内部値（フォールバック用）
# 注意: PlaylistExperienceはHalo側で統一されておらず信頼性が低い。
# 主分類はPLAYLIST_NAME_MAPで行い、こちらはあくまで最終フォールバック。
PLAYLIST_EXPERIENCE_MAP: dict[int, str] = {
    2: "casual",       # ranked_arena と同値だが名前マッチが優先される
    3: "casual",       # ranked_slayer と同値だが名前マッチが優先される
    5: "casual",
    6: "minigame",
    9: "btb",
}

# ==================================================
# 内部値 → 表示名への変換（ビュー側で使用）
# ==================================================

DISPLAY_NAMES: dict[str, str] = {
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
    "is_solo":                "ソロ",
    "is_party":               "パーティ",
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
    "team_pw_kills":          "自チームPWキル",
    "enemy_pw_kills":         "敵チームPWキル",
    "pw_control_rate":        "PWコントロール率",
    "engagement_density":     "エンゲージメント密度",
}

PLAYLIST_DISPLAY: dict[str, str] = {
    "ranked_arena":   "ランクアリーナ",
    "ranked_slayer":  "ランクスレイヤー",
    "ranked_doubles": "ランクダブルス",
    "ranked_ffa":     "ランクFFA",
    "ranked_snipers": "ランクスナイパーズ",
    "casual":         "カジュアル",
    "btb":            "BTB",
    "pve":            "PvE",
    "minigame":       "ミニゲーム",
    "custom":         "カスタムゲーム",
    "other":          "Other",
}

RESULT_DISPLAY: dict[str, str] = {
    "win":            "勝ち",
    "loss":           "負け",
    "draw":           "引き分け",
    "did_not_finish": "途中抜け",
}

PARTY_TYPE_DISPLAY: dict[int, str] = {
    1: "ソロ",
    2: "デュオ",
    3: "トリオ",
    4: "フルパ",
}


def display_name(col: str) -> str:
    """内部カラム名 → 表示名。未登録の場合はカラム名をそのまま返す。"""
    return DISPLAY_NAMES.get(col, col)


def display_playlist(val: str) -> str:
    """playlist 内部値 → 表示名。"""
    return PLAYLIST_DISPLAY.get(val, val)


def display_result(val: str) -> str:
    """result 内部値 → 表示名。"""
    return RESULT_DISPLAY.get(val, val)


def display_party_type(size: int) -> str:
    """party_size → パーティタイプ表示名。"""
    return PARTY_TYPE_DISPLAY.get(size, f"{size}人")