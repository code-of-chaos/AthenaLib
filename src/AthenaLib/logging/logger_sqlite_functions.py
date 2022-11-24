# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import contextlib
import pathlib
import enum
import sqlite3

# Athena Packages

# Local Imports
from AthenaLib.logging._logger import LoggerLevels
from AthenaLib.general.sql import sanitize_sql
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@contextlib.contextmanager
def _db_connect(sqlite_path:pathlib.Path, *, commit: bool = True):
    """
    Async Context manager to easily connect to the database
    Commits all changes to the db, before closing the connection
    """
    with sqlite3.connect(sqlite_path) as db:
        yield db

        if commit:
            db.commit()

def create_tables(sqlite_path:pathlib.Path, queries:list[str]):
    """
    Method is run by the `bot_constructor` on startup, as it creates the tables the logger needs,
    but only if they don't exist already
    """
    with _db_connect(sqlite_path, commit=True) as db:
        for sql in queries:
            db.execute(sql)

def execute_log(sqlite_path:pathlib.Path, level:LoggerLevels, section:str|enum.StrEnum, text:str|None, table_to_use:str, commit: bool = True):
    with _db_connect(sqlite_path, commit=commit) as db:
        # If text is None, cast to None
        #   If this isn't done, will raise an error
        txt = "Null" if text is None else f"'{sanitize_sql(text)}'"

        # noinspection SqlNoDataSourceInspection,SqlResolve
        db.execute(f"""
        INSERT INTO {table_to_use} (lvl, section, txt)
        VALUES ('{sanitize_sql(level)}', '{sanitize_sql(section)}', {txt});
        """)
