from __future__ import annotations

import dataclasses
import sys
import typing


_T = typing.TypeVar('_T')


def dataclass(cls, **kwargs) -> typing.Callable[[typing.Type[_T]], typing.Type[_T]]:
    if sys.version_info >= (3, 10):
        return dataclasses.dataclass(cls, **kwargs)
    else:
        kwargs.pop('match_args', None)
        kwargs.pop('slots', None)
        kwargs.pop('kw_only', None)
        return dataclasses.dataclass(cls, **kwargs)
