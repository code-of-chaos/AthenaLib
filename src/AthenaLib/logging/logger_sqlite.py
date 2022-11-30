# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Self,Any
import contextlib
import pathlib
import enum
import sqlite3

# Athena Packages

# Local Imports
from AthenaLib.logging._logger import AthenaLogger, LoggerLevel
from AthenaLib.general.sql import sanitize_sql

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@contextlib.contextmanager
def _connect(path:pathlib.Path, *, commit: bool = True, **kwargs) -> None:
    """
    Async Context manager to easily connect to the database
    Commits all changes to the db, before closing the connection
    """
    with sqlite3.connect(path,isolation_level=None if commit else "DEFERRED",**kwargs) as db:
        db.row_factory = sqlite3.Row

        try:
            yield db

        except sqlite3.Error:
            db.rollback()
            raise

        else:
            # only commit if there were no errors,
            #   Otherwise always rollback to previous state
            db.commit() if commit else db.rollback()

def _db_create(path:pathlib.Path, queries:str) -> None:
    """
    Method is run by the `bot_constructor` on startup, as it creates the tables the logger needs,
    but only if they don't exist already
    """
    with _connect(path, commit=True) as db:
        for sql in queries:
            db.executescript(sql)

def _execute_log(path:pathlib.Path, level:LoggerLevel, section: str | enum.StrEnum, data:Any, table_to_use:str, commit:bool=True) -> None:
    with _connect(path, commit=commit) as db:
        # noinspection SqlNoDataSourceInspection,SqlResolve
        db.execute(f"""
            INSERT INTO {table_to_use} (lvl, section, txt)
            VALUES (
                '{sanitize_sql(level)}', 
                '{sanitize_sql(section)}', 
                {"Null" if data is None else f"'{sanitize_sql(data)}'"}
            );"""
       )

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class AthenaSqliteLogger(AthenaLogger):
    sqlite_path:pathlib.Path = pathlib.Path("data/logger.irc")
    table_to_use:str = "logging"
    cast_to_str:Callable = str

    # ------------------------------------------------------------------------------------------------------------------
    # - Context manager for ease of use -
    # ------------------------------------------------------------------------------------------------------------------
    def __enter__(self) -> Self:
        # Check if the file exists
        if not self.sqlite_path.exists():
            raise FileNotFoundError(self.sqlite_path)

        # Makes sure the table will exist
        self._pool_executor.submit(
            _db_create,
            path=self.sqlite_path,
            queries=[
                f"""# noinspection SqlNoDataSourceInspectionForFile
                CREATE TABLE IF NOT EXISTS `{self.table_to_use}` (
                    `id` INTEGER PRIMARY KEY,
                    `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    `lvl` TEXT NOT NULL,
                    `section` TEXT,
                    `txt` TEXT
                );
                """,
            ]
        )

        # After the table has been created
        #   Go through the buffer
        return super(AthenaSqliteLogger, self).__enter__()

    # ------------------------------------------------------------------------------------------------------------------
    # - Logger functions that write to the database -
    # ------------------------------------------------------------------------------------------------------------------
    def log(self, level: LoggerLevel, section: str | enum.StrEnum, data: str | None) -> None:
        # If the logger itself hasn't been entered yet,
        #   Store the log to the buffer, and execute at a later date
        if not self._logger_entered:
            self._buffer.append((level, section, self.cast_to_str(data)))
            return

        # Let the pool execute the call to the database
        self._pool_executor.submit(
            _execute_log,
            path=self.sqlite_path,
            level=level,
            section=section,
            data=self.cast_to_str(data),
            table_to_use=self.table_to_use,
            commit=True
        )