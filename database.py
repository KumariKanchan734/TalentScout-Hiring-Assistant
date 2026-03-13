from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "candidates_data.json"


def _read_file() -> list[dict]:
    if not DB_PATH.exists():
        return []
    try:
        with DB_PATH.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        return []


def _write_file(records: list[dict]) -> None:
    with DB_PATH.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=4, ensure_ascii=False)


def load_candidates() -> list[dict]:
    return _read_file()


def save_candidate(candidate_info: dict) -> bool:
    records = _read_file()
    candidate_info = {**candidate_info, "timestamp": datetime.now().isoformat()}
    records.append(candidate_info)
    try:
        _write_file(records)
        return True
    except OSError as exc:
        print(f"[database] Failed to write candidate data: {exc}")
        return False


def clear_candidates() -> None:
    _write_file([])


def save_candidate_data(candidate_info: dict) -> bool:
    return save_candidate(candidate_info)
