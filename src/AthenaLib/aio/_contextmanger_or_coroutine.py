# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any, Callable, Coroutine, TypeVar,Generator, AsyncContextManager
import functools

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
_Type = TypeVar("_Type")
_Coroutine = Coroutine[Any, Any, _Type]

def async_contextmanager_or_coroutine(fnc: Callable[..., _Coroutine]) -> Callable[..., ContextMangerOrCoroutine]:
    @functools.wraps(fnc)
    def wrapper(*args, **kwargs) -> ContextMangerOrCoroutine:
        return ContextMangerOrCoroutine(fnc(*args, **kwargs))
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ContextMangerOrCoroutine(AsyncContextManager[_Type], _Coroutine):
    __slots__ = ("_coro", "_obj")

    def __init__(self, coro: _Coroutine):
        self._coro = coro
        self._obj: _Type

    # ------------------------------------------------------------------------------------------------------------------
    # - Coroutine -
    # ------------------------------------------------------------------------------------------------------------------
    def __await__(self) -> Generator[Any, None, _Type]:
        return self._coro.__await__()

    def close(self) -> None:
        return self._coro.close()

    def send(self, value) -> None:
        return self._coro.send(value)

    def throw(self, type_, value=None, traceback=None) -> None:
        return self._coro.throw(*(v for v in (type_, value, traceback) if v is not None))

    # ------------------------------------------------------------------------------------------------------------------
    # - Context manager -
    # ------------------------------------------------------------------------------------------------------------------
    async def __aenter__(self) -> _Type:
        self._obj = await self._coro
        return self._obj

    async def __aexit__(self, exc_type, exc, traceback) -> None:
        return

