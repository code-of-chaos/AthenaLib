# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from .ValueType import ValueType

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "ElementFontSize", "ElementFontHeight", "ZeroCharacterWidth", "RootElementFontSize", "ViewportWidthPercent",
    "ViewportHeightPercent", "ViewportLargerPercent", "ViewportSmallerPercent","Percent"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Functions -
# ----------------------------------------------------------------------------------------------------------------------
def _relativeLengthConversionInput(fnc):
    def wrapper(self:_RelativeLength, *args, **kwargs):
        if isinstance(args, tuple):
            other,*args_ = args
        else:
            other = args
            args_ = ()

        if isinstance(other, int|float):
            return fnc(self, type(self)(value=other), *args_, **kwargs)
        elif isinstance(other, type(self)):
            return fnc(self, *args, **kwargs)
        else:
            return NotImplemented
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Classes -
# ----------------------------------------------------------------------------------------------------------------------
class _RelativeLength(ValueType, ABC):
    _value:int|float
    def __init__(self, value: int | float | _RelativeLength):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int|float):
            raise TypeError
        self._value = value

    # ------------------------------------------------------------------------------------------------------------------
    # - cast dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __int__(self) -> int:
        return int(self.value)
    def __float__(self) -> float:
        return float(self.value)
    def __abs__(self) -> _RelativeLength:
        return type(self)(abs(self.value))
    def __round__(self, n=None):
        return type(self)(round(self.value, n))

    def __hash__(self) -> int:
        return hash(self.value)

    @abstractmethod
    def __str__(self)->str:...
    @abstractmethod
    def __repr__(self) -> str:...

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_relativeLengthConversionInput
    def __eq__(self, other: _RelativeLength | int | float) -> bool:
        return self.value == other.value
    @_relativeLengthConversionInput
    def __ne__(self, other: _RelativeLength | int | float) -> bool:
        return self.value != other.value
    @_relativeLengthConversionInput
    def __gt__(self, other: _RelativeLength | int | float) -> bool:
        return self.value > other.value
    @_relativeLengthConversionInput
    def __lt__(self, other: _RelativeLength | int | float) -> bool:
        return self.value < other.value
    @_relativeLengthConversionInput
    def __ge__(self, other: _RelativeLength | int | float) -> bool:
        return self.value >= other.value
    @_relativeLengthConversionInput
    def __le__(self, other: _RelativeLength | int | float) -> bool:
        return self.value <= other.value

    # ------------------------------------------------------------------------------------------------------------------
    # - math Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_relativeLengthConversionInput
    def __add__(self, other: _RelativeLength | int | float) -> _RelativeLength:
        return type(self)(self.value + other.value)
    @_relativeLengthConversionInput
    def __sub__(self, other: _RelativeLength | int | float) -> _RelativeLength:
        return type(self)(self.value - other.value)
    @_relativeLengthConversionInput
    def __mul__(self, other: _RelativeLength | int | float) -> _RelativeLength:
        return type(self)(self.value * other.value)
    @_relativeLengthConversionInput
    def __floordiv__(self, other: _RelativeLength | int | float) -> _RelativeLength:
        return type(self)(self.value // other.value)
    @_relativeLengthConversionInput
    def __truediv__(self, other: _RelativeLength | int | float) -> _RelativeLength:
        return type(self)(self.value / other.value)
    @_relativeLengthConversionInput
    def __pow__(self, other: _RelativeLength | int | float) -> _RelativeLength:
        return type(self)(self.value ** other.value)
    @_relativeLengthConversionInput
    def __mod__(self, other: _RelativeLength | int | float) -> _RelativeLength:
        return type(self)(self.value % other.value)

    @_relativeLengthConversionInput
    def __iadd__(self, other: _RelativeLength | int | float):
        self.value += other.value
        return self
    @_relativeLengthConversionInput
    def __isub__(self, other: _RelativeLength | int | float):
        self.value -= other.value
        return self
    @_relativeLengthConversionInput
    def __imul__(self, other: _RelativeLength | int | float):
        self.value *= other.value
        return self
    @_relativeLengthConversionInput
    def __ifloordiv__(self, other: _RelativeLength | int | float):
        self.value //= other.value
        return self
    @_relativeLengthConversionInput
    def __itruediv__(self, other: _RelativeLength | int | float):
        self.value /= other.value
        return self
    @_relativeLengthConversionInput
    def __ipow__(self, other: _RelativeLength | int | float):
        self.value **= other.value
        return self
    @_relativeLengthConversionInput
    def __imod__(self, other: _RelativeLength | int | float):
        self.value %= other.value
        return self

# ----------------------------------------------------------------------------------------------------------------------
class ElementFontSize(_RelativeLength):
    def __str__(self):
        return f"{self.value}em"
    def __repr__(self) -> str:
        return f"ElementFontSize(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class ElementFontHeight(_RelativeLength):
    def __str__(self):
        return f"{self.value}ex"
    def __repr__(self) -> str:
        return f"ElementFontHeight(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class ZeroCharacterWidth(_RelativeLength):
    def __str__(self):
        return f"{self.value}ch"
    def __repr__(self) -> str:
        return f"ZeroCharacterWidth(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class RootElementFontSize(_RelativeLength):
    def __str__(self):
        return f"{self.value}rem"
    def __repr__(self) -> str:
        return f"RootElementFontSize(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class ViewportWidthPercent(_RelativeLength):
    def __str__(self):
        return f"{self.value}vw"
    def __repr__(self) -> str:
        return f"ViewportWidthPercent(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class ViewportHeightPercent(_RelativeLength):
    def __str__(self):
        return f"{self.value}vh"
    def __repr__(self) -> str:
        return f"ViewportHeightPercent(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class ViewportSmallerPercent(_RelativeLength):
    def __str__(self):
        return f"{self.value}vmin"
    def __repr__(self) -> str:
        return f"ViewportSmallerPercent(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class ViewportLargerPercent(_RelativeLength):
    def __str__(self):
        return f"{self.value}vmax"
    def __repr__(self) -> str:
        return f"ViewportLargerPercent(value={self.value})"

# ----------------------------------------------------------------------------------------------------------------------
class Percent(_RelativeLength):
    def __str__(self):
        return f"{self.value}%"
    def __repr__(self) -> str:
        return f"Percent(value={self.value})"