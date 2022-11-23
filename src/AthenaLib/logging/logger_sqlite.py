# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import contextlib
import pathlib
import aiosqlite
import enum

# Athena Packages

# Local Imports
from AthenaLib.constants.types import PATHLIKE
from AthenaLib.logging._logger import AthenaLogger
from AthenaLib.general.functions.sql import sanitize_sql

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class LoggerLevels(enum.StrEnum):
    PRINT = enum.auto()
    DEBUG = enum.auto()
    WARN = enum.auto()
    ERROR = enum.auto()

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaSqliteLogger(AthenaLogger):
    path:pathlib.Path

    # noinspection SqlNoDataSourceInspection
    SQL_CREATE_TABLES: list[str] = [
        f"""
        CREATE TABLE IF NOT EXISTS `logger` (
            `id` INTEGER PRIMARY KEY,
            `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `lvl` TEXT NOT NULL,
            `section` TEXT,
            `txt` TEXT
        );
        """,
    ]

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

    async def create_tables(self):
        """
        Method is run by the `bot_constructor` on startup, as it creates the tables the logger needs,
        but only if they don't exist already
        """
        with self.if_enabled():
            async with self._db_connect() as db:
                for sql in self.SQL_CREATE_TABLES:
                    await db.execute(sql)

    # ------------------------------------------------------------------------------------------------------------------
    # - Logger functions that write to the database -
    # ------------------------------------------------------------------------------------------------------------------
    async def log(self, level:LoggerLevels, section:str|enum.StrEnum, text:str|None):
        with self.if_enabled():
            # If text is None, cast to None
            #   If this sin't done, will raise an error
            txt = "Null" if text is None else f"'{sanitize_sql(text)}'"

            async with self._db_connect() as db:
                # noinspection SqlNoDataSourceInspection,SqlResolve
                await db.execute(f"""
                    INSERT INTO logger (lvl, section, txt)
                    VALUES ('{sanitize_sql(level)}', '{sanitize_sql(section)}', {txt});
                """)

    async def log_print(self, section:str|enum.StrEnum, text:str|None=None):
        print(text)
        await self.log(level=LoggerLevels.PRINT, section=section, text=text)

    async def log_debug(self, section:str|enum.StrEnum, text:str|None=None):
        await self.log(level=LoggerLevels.DEBUG, section=section, text=text)

    async def log_warning(self, section:str|enum.StrEnum, text:str|None=None):
        await self.log(level=LoggerLevels.WARN, section=section, text=text)

    async def log_error(self, section:str|enum.StrEnum, text:str|None=None):
        await self.log(level=LoggerLevels.ERROR, section=section, text=text)

