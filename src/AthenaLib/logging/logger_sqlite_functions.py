# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import contextlib
import pathlib
import enum
import sqlite3
from typing import Any

# Athena Packages

# Local Imports
from AthenaLib.logging._logger import LoggerLevels
from AthenaLib.general.sql import sanitize_sql

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@contextlib.contextmanager
def connect(path:pathlib.Path, *, commit: bool = True, **kwargs):
    """
    Async Context manager to easily connect to the database
    Commits all changes to the db, before closing the connection
    """
    isolation_level = None if commit else "DEFERRED"

    with sqlite3.connect(path,isolation_level=isolation_level,**kwargs) as db:
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

def db_create(path:pathlib.Path, queries:str):
    """
    Method is run by the `bot_constructor` on startup, as it creates the tables the logger needs,
    but only if they don't exist already
    """
    with connect(path, commit=True) as db:
        for sql in queries:
            db.executescript(sql)

def execute_log(path:pathlib.Path, level:LoggerLevels, section:str|enum.StrEnum, data:Any|None, table_to_use:str, commit: bool = True):
    with connect(path, commit=commit) as db:
        # If text is None, cast to None
        #   If this isn't done, will raise an error
        txt = "Null" if data is None else f"'{sanitize_sql(data)}'"

        # noinspection SqlNoDataSourceInspection,SqlResolve
        db.execute(f"""
            INSERT INTO {table_to_use} (lvl, section, txt)
            VALUES ('{sanitize_sql(level)}', '{sanitize_sql(section)}', {txt});
            """
       )
