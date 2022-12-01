# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import pathlib
import unittest

# Athena Packages
from AthenaLib.aio.sqlite import AsyncSqliteCursor, AsyncSqliteConnection

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test_AioSqlite(unittest.IsolatedAsyncioTestCase):

    async def test_Connection(self):
        async with AsyncSqliteConnection.connect(db_path=pathlib.Path("data.sqlite")) as db: #type: AsyncSqliteConnection
            async with db.execute("CREATE TABLE temp_table1( name TEXT );") as cursor: #type: AsyncSqliteCursor
                print(await cursor.fetchall())
            async with db.execute("SELECT * FROM sqlite_schema;") as cursor:
                print(await cursor.fetchall())