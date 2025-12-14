"""DB engine and session factory.

SQLite is used intentionally per ARCHITECTURE.md.
"""

from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DB_PATH


def _sqlite_url(db_path: str) -> str:
    # Use a file path, not an in-memory DB, so the container can mount persistence.
    return f"sqlite+pysqlite:///{db_path}"


engine = create_engine(
    _sqlite_url(DB_PATH),
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
