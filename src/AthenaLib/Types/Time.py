# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .ValueType import ValueType

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Second(ValueType):
    value:int
    def __init__(self, value:int):
        if not isinstance(value, int):
            raise TypeError
        self.value = value

    def __repr__(self) -> str:
        return f"<Second value={str(self.value)}>"

    def __eq__(self, other):
        if isinstance(other, Second):
            return other.value == self.value
        elif isinstance(other, MilliSecond):
            return other.value == (self.value*1000)
        elif isinstance(other, (int, float)):
            return other == self.value

    def __str__(self):
        return f"{str(self.value)}s"

    def __abs__(self) -> Second:
        return Second(abs(self.value))

# ----------------------------------------------------------------------------------------------------------------------
class MilliSecond(ValueType):
    value:int
    def __init__(self, value:int):
        if not isinstance(value, int):
            raise TypeError
        self.value = value

    def __repr__(self) -> str:
        return f"<MilliSecond value={str(self.value)}>"

    def __eq__(self, other):
        if isinstance(other, MilliSecond):
            return other.value == self.value
        elif isinstance(other, Second):
            return other.value == (self.value/1000)
        elif isinstance(other, (int, float)):
            return other == self.value
        else:
            return NotImplemented

    def __str__(self):
        return f"{str(self.value)}ms"

    def __abs__(self) -> MilliSecond:
        return MilliSecond(abs(self.value))