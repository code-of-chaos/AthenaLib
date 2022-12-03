# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import contextlib
import pathlib
import sqlite3
from dataclasses import dataclass
from typing import AsyncContextManager

# Custom Library

# Custom Packages
from AthenaLib.constants.types import PATHLIKE
from AthenaLib.aio.sqlite import AsyncSqliteCursor, AsyncSqliteConnection
import aiosqlite

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True)
class ConnectorAioSqlite:
    """
    A simple connector system to connect to sqlite database files.
    """
    path:pathlib.Path

    def __init__(self, path:PATHLIKE):
        self.path = pathlib.Path(path)

    @contextlib.asynccontextmanager
    async def connect(self, commit: bool = True, **kwargs) -> AsyncContextManager[AsyncSqliteConnection]:
        """
        Async Context manager to easily connect to the database
        Commits all changes to the db, before closing the connection
        """
        isolation_level = None if commit else "DEFERRED"

        async with AsyncSqliteConnection.connect(self.path,isolation_level=isolation_level,**kwargs) as db:
            db.row_factory = sqlite3.Row

            try:
                yield db

            except sqlite3.Error:
                await db.rollback()
                raise

            else:
                # only commit if there were no errors,
                #   Otherwise always rollback to previous state
                await db.commit() if commit else await db.rollback()


    async def db_create(self, queries:str):
        """
        Method to set up a database sqlite file.
        """
        async with self.connect(commit=True) as db: #type: aiosqlite.Connection
            await db.executescript(queries)
