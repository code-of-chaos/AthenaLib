# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import pathlib
import sqlite3
import asyncio
import queue
import threading
from typing import Any, Optional, Callable, Self, AsyncIterator, Iterable, Coroutine, TypeVar
import functools
from dataclasses import dataclass

# Athena Packages

# Local Imports
from AthenaLib.aio._contextmanger_or_coroutine import ContextMangerOrCoroutine

# ----------------------------------------------------------------------------------------------------------------------
# - Info -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = ["AsyncSqliteConnection", "AsyncSqliteCursor"]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
_QueueTask = tuple[asyncio.Future, Callable]
_ConnectorCallback = Callable[[...], sqlite3.Connection]

def set_future_result(future:asyncio.Future, result:Any) -> None:
    if not future.done():
        future.set_result(result)

def set_future_exception(future:asyncio.Future, exception:Exception) -> None:
    if not future.done():
        future.set_exception(exception)

class _ContextMangerOrCoroutine(ContextMangerOrCoroutine):
    async def __aexit__(self, exc_type, exc, traceback) -> None:
        if isinstance(self._obj, AsyncSqliteCursor):
            await self._obj.close()

def async_contextmanager_or_coroutine(fnc: Callable[..., Coroutine]) -> Callable[..., ContextMangerOrCoroutine]:
    @functools.wraps(fnc)
    def wrapper(*args, **kwargs) -> ContextMangerOrCoroutine:
        return _ContextMangerOrCoroutine(fnc(*args, **kwargs))
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AsyncSqliteConnection(threading.Thread):
    _db_connection:sqlite3.Connection|None
    _db_connector_factory:_ConnectorCallback
    _queue:queue.Queue
    _chunk_size:int
    _is_active:bool

    def __init__(self,
                 db_path:str|pathlib.Path,
                 *,
                 connector:_ConnectorCallback=None,
                 chunk_size:int=64
                 ):
        self._db_connector_factory = sqlite3.Connection(str(db_path), chunk_size) if connector is None else connector
        self._db_connection = None
        self._queue = queue.Queue()
        self._chunk_size = chunk_size

        self._is_active = True

        super().__init__()

    @property
    def _db_conn(self) -> sqlite3.Connection:
        assert self._db_connection, "No Connection has been established yet"
        return self._db_connection

    # ------------------------------------------------------------------------------------------------------------------
    # - Threading stuff -
    # ------------------------------------------------------------------------------------------------------------------
    def _queue_get(self) -> _QueueTask:
        return self._queue.get(timeout=0.1)

    def _queue_put(self, future:asyncio.Future, callback:Callable):
        self._queue.put_nowait((future,callback))

    def run(self) -> None:
        while self._is_active:
            # To only have one Try catch block
            #   Assign the var to None, and check if the future is not None
            future:Optional[asyncio.Future] = None

            try:
                future, callback = self._queue_get()

                future.get_loop().call_soon_threadsafe(
                    set_future_result, future, callback()
                )

            except BaseException as exception:
                if future is not None:
                    future.get_loop().call_soon_threadsafe(
                        set_future_exception, future, exception
                    )

            except queue.Empty:
                # Queue is empty,
                #   means we have resolved all our requests
                break

    # ------------------------------------------------------------------------------------------------------------------
    # - Context manager or Coroutine -
    # ------------------------------------------------------------------------------------------------------------------
    async def __aenter__(self) -> Self:
        # Start the thread
        self.start()

        # Establish the connection
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        # Close the connection
        await self.close()
        self._is_active = False

    def __await__(self):
        # Start the thread
        self.start()

        # Await the db connection
        return self._connect().__await__()

    # ------------------------------------------------------------------------------------------------------------------
    # - Sqlite Commands -
    # ------------------------------------------------------------------------------------------------------------------
    async def _execute(self, callback, *args, **kwargs) -> Any:
        # Puts the task in the queue as a non wait
        self._queue_put(
            future=(future:=asyncio.get_event_loop().create_future()),
            callback=functools.partial(callback, *args, **kwargs)
        )

        # Wait until the task is done
        return await future

    async def _connect(self):
        # A connection has not previously been established
        if self._db_connection is None:

            # No connect has been established yet
            try:
                self._queue_put(
                    future=(future := asyncio.get_event_loop().create_future()),
                    callback=self._db_connector_factory
                )
                self._db_connection = await future

            except BaseException:
                self._db_connection = None
                raise
    @classmethod
    def connect(cls, db_path:str|pathlib.Path,*,chunk_size:int=64, **kwargs) -> Self:
        return cls(
            db_path=db_path,
            connector=lambda: sqlite3.connect(db_path, **kwargs),
            chunk_size=chunk_size
        )

    # ------------------------------------------------------------------------------------------------------------------
    async def close(self) -> None:
        # call the sqlite3 database close
        await self._execute(self._db_connection.close)
        self._db_connection = None

    async def commit(self) -> None:
        # call the sqlite3 database commit command
        await self._execute(self._db_connection.commit)

    @async_contextmanager_or_coroutine
    async def execute(self,sql:str, *extra_param:Any) -> AsyncSqliteCursor:
        return AsyncSqliteCursor(
            _connection=self,
            _cursor = await self._execute(
                self._db_connection.execute, sql, extra_param
            )
        )

    @async_contextmanager_or_coroutine
    async def execute_insert(self,sql:str, *extra_param:Any) -> Iterable[Any]:
        cursor:AsyncSqliteCursor = AsyncSqliteCursor(
            _connection=self,
            _cursor=await self._execute(
                self._db_connection.execute, sql, extra_param
            )
        )
        await cursor.execute("SELECT last_insert_rowid()")
        return await cursor.fetchone()

    @async_contextmanager_or_coroutine
    async def execute_fetchall(self,sql:str, *extra_param:Any) -> Iterable[Any]:
        cursor:AsyncSqliteCursor = AsyncSqliteCursor(
            _connection=self,
            _cursor=await self._execute(
                self._db_connection.execute, sql, extra_param
            )
        )
        return await cursor.fetchall()

    @async_contextmanager_or_coroutine
    async def execute_many(self,sql:str, *extra_param:Any) -> AsyncSqliteCursor:
        return AsyncSqliteCursor(
            _connection=self,
            _cursor=await self._execute(
                self._db_connection.executemany, sql, extra_param
            )
        )

    @async_contextmanager_or_coroutine
    async def execute_script(self,sql:str) -> AsyncSqliteCursor:
        return AsyncSqliteCursor(
            _connection=self,
            _cursor=await self._execute(
                self._db_connection.executescript, sql
            )
        )

    async def create_function(self, name:str, num_params:int, func:Callable, deterministic: bool = False):
        await self._execute(
            self._db_connection.create_function,
            name,
            num_params,
            func,
            deterministic=deterministic,
        )

    async def rollback(self) -> None:
        # call the sqlite3 database rollback command
        await self._execute(self._db_connection.commit)

    # ------------------------------------------------------------------------------------------------------------------
    # - Extra info of connection -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def in_transaction(self) -> bool:
        return self._db_connection.in_transaction

    @property
    def isolation_level(self) -> str:
        return self._db_connection.isolation_level

    @isolation_level.setter
    def isolation_level(self, value: str) -> None:
        self._db_connection.isolation_level = value

    @property
    def row_factory(self) -> type|None:
        return self._db_connection.row_factory

    @row_factory.setter
    def row_factory(self, value: type) -> None:
        self._db_connection.row_factory = value

    @property
    def text_factory(self) -> type:
        return self._db_connection.text_factory

    @text_factory.setter
    def text_factory(self, value: type) -> None:
        self._db_connection.text_factory = value

    @property
    def total_changes(self) -> int:
        return self._db_connection.total_changes

# ----------------------------------------------------------------------------------------------------------------------
@dataclass()
class AsyncSqliteCursor:
    _connection: AsyncSqliteConnection
    _cursor: sqlite3.Cursor

    # ------------------------------------------------------------------------------------------------------------------
    # - Context Manager -
    # ------------------------------------------------------------------------------------------------------------------
    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    # ------------------------------------------------------------------------------------------------------------------
    # - Helper methods -
    # ------------------------------------------------------------------------------------------------------------------
    def __aiter__(self) -> AsyncIterator[sqlite3.Row]:
        return self._fetch_data_in_chunks()

    async def _fetch_data_in_chunks(self):
        while True:
            # noinspection PyProtectedMember
            rows = await self.fetchmany(self._connection._chunk_size)
            if not rows:
                return
            for row in rows:
                yield row

    # ------------------------------------------------------------------------------------------------------------------
    # - Sqlite Commands -
    # ------------------------------------------------------------------------------------------------------------------
    async def execute(self, sql:str, *extra_param:Any) -> Self:
        # noinspection PyProtectedMember
        await self._connection._execute(
            self._cursor.execute, sql, list(extra_param)
        )
        return self

    async def executemany(self, sql:str, *extra_param:Any) -> Self:
        # noinspection PyProtectedMember
        await self._connection._execute(
            self._cursor.executemany, sql, list(extra_param)
        )
        return self

    async def executescript(self, sql:str) -> Self:
        # noinspection PyProtectedMember
        await self._connection._execute(
            self._cursor.executescript, sql
        )
        return self

    async def fetchone(self) -> sqlite3.Row | None:
        # noinspection PyProtectedMember
        return await self._connection._execute(
            self._cursor.fetchone
        )

    async def fetchmany(self, size: int = None) -> Iterable[sqlite3.Row]:
        # noinspection PyProtectedMember
        return await self._connection._execute(
            self._cursor.fetchmany,
            *(() if size is None else (size,))
        )

    async def fetchall(self) -> Iterable[sqlite3.Row]:
        # noinspection PyProtectedMember
        return await self._connection._execute(
            self._cursor.fetchall
        )

    async def close(self) -> None:
        """Close the cursor."""
        # noinspection PyProtectedMember
        return await self._connection._execute(
            self._cursor.close
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - Extra info of cursor -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def arraysize(self):
        return self._cursor.arraysize

    @property
    def connection(self):
        return self._cursor.connection

    @property
    def description(self):
        return self._cursor.description

    @property
    def lastrowid(self):
        return self._cursor.lastrowid

    @property
    def rowcount(self):
        return self._cursor.rowcount

    @property
    def row_factory(self):
        return self._cursor.row_factory