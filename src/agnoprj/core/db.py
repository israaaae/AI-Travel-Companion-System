from __future__ import annotations # Traite toutes les annotations de types comme des chaînes de caractères, pas comme des objets Python réels.

from agno.db.sqlite import SqliteDb
from agnoprj.core.config import SETTINGS
from agnoprj.utils.paths import PATHS


def get_sqlite_db() -> SqliteDb:
    db_file = SETTINGS.SQLITE_DB_FILE
    db_path = (PATHS.root / db_file).resolve() if not db_file.startswith("/") else db_file
    return SqliteDb(db_file=str(db_path))
