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

    # noinspection SqlNoDataSourceInspection
    async def test_Connection(self):
        connection: AsyncSqliteConnection = AsyncSqliteConnection.connect(db_path=pathlib.Path("test_connection.sqlite"))
        async with connection:
            cursor:AsyncSqliteCursor = await connection.cursor()
            await cursor.execute("CREATE TABLE IF NOT EXISTS temp_table1( name TEXT );")
            await cursor.execute("SELECT * FROM sqlite_schema;")

            self.assertEqual(
                [('table', 'temp_table1', 'temp_table1', 2, 'CREATE TABLE temp_table1( name TEXT )')],
                await cursor.fetchall()
            )
