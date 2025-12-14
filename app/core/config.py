"""Runtime configuration.

Kept intentionally small for the bootstrap.
"""

from __future__ import annotations

import os


def get_env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name)
    if value is None:
        return default
    return value


DB_PATH: str = get_env("DB_PATH", "./tinyanalytics.sqlite") or "./tinyanalytics.sqlite"
HASH_SALT: str = get_env("HASH_SALT", "") or ""
