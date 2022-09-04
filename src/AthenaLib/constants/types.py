# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import typing

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
PATHLIKE = str|bytes|os.PathLike
NUMBER = float|int
POINT = tuple[NUMBER, NUMBER] | list[NUMBER, NUMBER]
COLOR = tuple[NUMBER,NUMBER,NUMBER] | tuple[NUMBER,NUMBER,NUMBER,NUMBER]
CV_INT = typing.ClassVar[int]
CV_COLOR = typing.ClassVar[COLOR]

_T = typing.TypeVar('_T') # needed for dataclass