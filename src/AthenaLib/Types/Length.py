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
__all__=[
    "lengthConverion",
    "Pixel"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Functions -
# ----------------------------------------------------------------------------------------------------------------------
def lengthConverion(original:int|float|_Length, cast:int|float|_Length, *,pixels_per_inch:int=300) -> int|float|_Length:
    match original, cast:
        # General catches for throwing to and from numbers
        case int()|float(),_Length():
            return type(cast)(original)
        case _Length(), int()|float():
            return type(cast)(original.value)

        # To length Types, if both types are the same (Pixel->Pixel)
        case a,b if type(a) is type(b):
            return type(cast)(original.value)

        case _:
            return NotImplemented

def _lengthConversionInput(fnc):
    def wrapper(self:_Length,*args,**kwargs):
        if isinstance(args, tuple):
            other,*_ = args
        else:
            other, _ = args, ()

        if (otherConverted := lengthConverion(other, self,pixels_per_inch=self.pixels_per_inch)) is NotImplemented:
            return NotImplemented
        return fnc(self,otherConverted, *_,**kwargs)
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Classes -
# ----------------------------------------------------------------------------------------------------------------------
class _Length(ValueType, ABC):
    _value:int|float
    pixels_per_inch:int
    def __init__(self, value:int|float|_Length):
        self.value = value
        self.pixels_per_inch=300

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
    def __abs__(self) -> _Length:
        return type(self)(abs(self.value))

    @abstractmethod
    def __str__(self)->str:...
    @abstractmethod
    def __repr__(self) -> str:...

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_lengthConversionInput
    def __eq__(self, other: _Length | int | float) -> bool:
        return self.value == other.value
    @_lengthConversionInput
    def __ne__(self, other: _Length | int | float) -> bool:
        return self.value != other.value
    @_lengthConversionInput
    def __gt__(self, other: _Length | int | float) -> bool:
        return self.value > other.value
    @_lengthConversionInput
    def __lt__(self, other: _Length | int | float) -> bool:
        return self.value < other.value
    @_lengthConversionInput
    def __ge__(self, other: _Length | int | float) -> bool:
        return self.value >= other.value
    @_lengthConversionInput
    def __le__(self, other: _Length | int | float) -> bool:
        return self.value <= other.value

    # ------------------------------------------------------------------------------------------------------------------
    # - math Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_lengthConversionInput
    def __add__(self, other: _Length | int | float) -> _Length:
        return type(self)(self.value + other.value)
    @_lengthConversionInput
    def __sub__(self, other: _Length | int | float) -> _Length:
        return type(self)(self.value - other.value)
    @_lengthConversionInput
    def __mul__(self, other: _Length | int | float) -> _Length:
        return type(self)(self.value * other.value)
    @_lengthConversionInput
    def __floordiv__(self, other: _Length | int | float) -> _Length:
        return type(self)(self.value // other.value)
    @_lengthConversionInput
    def __truediv__(self, other: _Length | int | float) -> _Length:
        return type(self)(self.value / other.value)
    @_lengthConversionInput
    def __pow__(self, other: _Length | int | float) -> _Length:
        return type(self)(self.value ** other.value)
    @_lengthConversionInput
    def __mod__(self, other: _Length | int | float) -> _Length:
        return type(self)(self.value % other.value)

    @_lengthConversionInput
    def __iadd__(self, other: _Length | int | float):
        self.value += other.value
        return self
    @_lengthConversionInput
    def __isub__(self, other: _Length | int | float):
        self.value -= other.value
        return self
    @_lengthConversionInput
    def __imul__(self, other: _Length | int | float):
        self.value *= other.value
        return self
    @_lengthConversionInput
    def __ifloordiv__(self, other: _Length | int | float):
        self.value //= other.value
        return self
    @_lengthConversionInput
    def __itruediv__(self, other: _Length | int | float):
        self.value /= other.value
        return self
    @_lengthConversionInput
    def __ipow__(self, other: _Length | int | float):
        self.value **= other.value
        return self
    @_lengthConversionInput
    def __imod__(self, other: _Length | int | float):
        self.value %= other.value
        return self

# ----------------------------------------------------------------------------------------------------------------------
class Pixel(_Length):
    def __str__(self):
        return f"{str(self.value)}px"
    def __repr__(self) -> str:
        return f"Pixel(value={str(self.value)})"
