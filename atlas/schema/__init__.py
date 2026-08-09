"""Atlas schema package — SQLite migrations with rollback support.

Extracted from Yggdrasil's schema patterns. All migrations are
SQLite-first with explicit rollback sections.
"""

# Re-export the main schema string for convenience
from atlas.core.job_store import _DB_SCHEMA as CORE_SCHEMA

__all__ = ["CORE_SCHEMA"]
