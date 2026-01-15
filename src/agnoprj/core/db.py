from __future__ import annotations

from agno.db.sqlite import SqliteDb
from core.config import SETTINGS
from utils.paths import PATHS


def get_sqlite_db() -> SqliteDb:
    db_file = SETTINGS.SQLITE_DB_FILE
    db_path = (PATHS.root / db_file).resolve() if not db_file.startswith("/") else db_file
    return SqliteDb(db_file=str(db_path))
