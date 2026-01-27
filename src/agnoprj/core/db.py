from __future__ import annotations # Traite toutes les annotations de types comme des chaînes de caractères, pas comme des objets Python réels.

"""
🧠 Exemple SANS __future__
class Agent:
    def next(self) -> Workflow:
        return Workflow()


❌ ERREUR :

NameError: name 'Workflow' is not defined

Parce que Workflow n existe pas encore.
"""
from agno.db.sqlite import SqliteDb
from core.config import SETTINGS
from utils.paths import PATHS


def get_sqlite_db() -> SqliteDb:
    db_file = SETTINGS.SQLITE_DB_FILE
    db_path = (PATHS.root / db_file).resolve() if not db_file.startswith("/") else db_file
    return SqliteDb(db_file=str(db_path))
