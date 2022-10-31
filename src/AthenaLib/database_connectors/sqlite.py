# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import contextlib
import sqlite3
from dataclasses import dataclass, field

# Custom Library
from AthenaLib.constants.types import PATHLIKE

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True)
class ConnectorSqlite3:
    """
    A simple connector system to connect to sqlite database files.
    """
    path:PATHLIKE

    def create_db(self, queries:str):
        """
        Method to set up a database sqlite file.
        It is expected for the `queries` argument to be multiple sql commands
        """
        with self.get_cursor(commit=True) as cursor:
            cursor.executescript(queries)

    @contextlib.contextmanager
    def connect(self, commit:bool = False) -> sqlite3.Connection:
        """
        Context managed method which yields a 'DEFERRED' sqlite3 connection object.
        If commit is set to true,
            the executed commands within the connection will be committed,
            else rolled back.
        """
        isolation_level = None if commit else "DEFERRED"
        with contextlib.closing(sqlite3.connect(self.path, isolation_level=isolation_level)) as conn:
            try:
                yield conn
            except sqlite3.Error:
                conn.rollback()
                raise
            else:
                # only commit if there were no errors,
                #   Otherwise always rollback to previous state
                if commit:
                    conn.commit()
                else:
                    conn.rollback()

    @contextlib.contextmanager
    def get_cursor(self, commit:bool = False) -> sqlite3.Cursor:
        """
        Context managed method which yields a sqlite3 cursor object.
        If commit is set to true,
            the executed commands within the connection will be committed,
            else rolled back.
        """
        with self.connect(commit) as conn:
            yield conn.cursor()
