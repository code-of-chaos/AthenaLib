# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import aiomysql
import asyncio
from dataclasses import field

# Custom Library

# Custom Packages
from AthenaLib.decorators.dataclass import dataclass

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class AsyncDatabaseMariaDB:
    host:str
    port:int
    pool:aiomysql.Pool = field(init=False)

    async def connect(self,user:str,password:str, loop:asyncio.AbstractEventLoop):
        self.pool = await aiomysql.create_pool(
            host=self.host,
            port=self.port,
            user=user,
            password=password,
            loop=loop
        )

    async def acquire_cursor(self) -> aiomysql.Cursor:
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor: #type: aiomysql.Cursor
                return cursor

    async def close(self):
        self.pool.close()
        await self.pool.wait_closed()
