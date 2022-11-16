# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import contextlib
import pathlib
import aiosqlite

# Athena Packages

# Local Imports
from AthenaLib.constants.types import PATHLIKE
from AthenaLib.logging._logger import AthenaLogger

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaSqliteLogger(AthenaLogger):
    path:pathlib.Path

    def __init__(self, path:PATHLIKE, enabled:bool):
        self.path = pathlib.Path(path)
        self.enabled = enabled

    @contextlib.asynccontextmanager
    async def _db_connect(self, auto_commit:bool=True):
        """
        Async Context manager to easily connect to the database
        Commits all changes to the db, before closing the connection
        """
        async with aiosqlite.connect(self.path) as db:

            yield db

            if auto_commit:
                await db.commit()
