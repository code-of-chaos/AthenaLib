# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import dataclasses
import sys
import typing

# Custom Library

# Custom Packages
from AthenaLib.constants.types import _T

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def dataclass(**kwargs) -> typing.Callable[[typing.Type[_T]], typing.Type[_T]]:
    """
    Fix for backwards compatibility with older Python version than the current main development version.
    See original `dataclasses.dataclass` for full documentation
    """
    # TODO
    #   Update this when projects get bumped to Python 3.11

    if sys.version_info < (3, 10):
        kwargs.pop('match_args', None)
        kwargs.pop('slots', None)
        kwargs.pop('kw_only', None)

    return dataclasses.dataclass(**kwargs)
