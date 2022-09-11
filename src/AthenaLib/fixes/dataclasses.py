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
# - Parts of dataclasses that don't need fixes -
# ----------------------------------------------------------------------------------------------------------------------
field = dataclasses.field
Field = dataclasses.Field
FrozenInstanceError = dataclasses.FrozenInstanceError
InitVar = dataclasses.InitVar
MISSING = dataclasses.MISSING

if sys.version >= (3, 10):
    KW_ONLY = dataclasses.KW_ONLY

# ----------------------------------------------------------------------------------------------------------------------
# - Objects that have to be fixed -
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
