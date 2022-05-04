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
    "Minute", "Second", "MilliSecond", "Hour",
    "timeConversion"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def timeConversion(original:int|float|_Time, cast:int|float|_Time) -> int|float|_Time:
    match original, cast:
        # General catches for throwing to and from numbers
        case int()|float(),_Time():
            return type(cast)(original)
        case _Time(), int()|float():
            return type(cast)(original.value)

        # To Time Types, if both types are the same (Second-> Second, Mili-> Mili)
        case a,b if type(a) is type(b):
            return type(cast)(original.value)

        # Conversion functions between types
        case Second(), MilliSecond():
            return MilliSecond(original.value * 1000)
        case Second(), Minute():
            return Minute(original.value/60)
        case Second(), Hour():
            return Hour(original.value/60/60)

        case MilliSecond(), Second():
            return Second(original.value/1000)
        case MilliSecond(), Minute():
            return Minute(original.value/1000/60)
        case MilliSecond(), Hour():
            return Hour(original.value/1000/60/60)

        case Minute(), MilliSecond():
            return MilliSecond(original.value*60*1000)
        case Minute(), Second():
            return Second(original.value*60)
        case Minute(), Hour():
            return Hour(original.value/60)

        case Hour(), MilliSecond():
            return MilliSecond(original.value*60*1000*60)
        case Hour(), Second():
            return Second(original.value*60*60)
        case Hour(), Minute():
            return Minute(original.value*60)

        case _:
            return NotImplemented

def _timeConversionInput(fnc):
    def wrapper(self,*args,**kwargs):
        if isinstance(args, tuple):
            other,*_ = args
        else:
            other, _ = args, ()

        if (otherConverted := timeConversion(other, self)) is NotImplemented:
            return NotImplemented
        return fnc(self,otherConverted, *_,**kwargs)
    return wrapper

class _Time(ValueType, ABC):
    _value:int|float
    def __init__(self, value:int|float|Second|MilliSecond):
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
    def __abs__(self) -> _Time:
        return type(self)(abs(self.value))

    @abstractmethod
    def __str__(self)->str:...
    @abstractmethod
    def __repr__(self) -> str:...

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_timeConversionInput
    def __eq__(self, other:_Time|int|float) -> bool:
        return self.value == other.value
    @_timeConversionInput
    def __ne__(self, other:_Time|int|float) -> bool:
        return self.value != other.value
    @_timeConversionInput
    def __gt__(self, other:_Time|int|float) -> bool:
        return self.value > other.value
    @_timeConversionInput
    def __lt__(self, other:_Time|int|float) -> bool:
        return self.value < other.value
    @_timeConversionInput
    def __ge__(self, other:_Time|int|float) -> bool:
        return self.value >= other.value
    @_timeConversionInput
    def __le__(self, other:_Time|int|float) -> bool:
        return self.value <= other.value

    # ------------------------------------------------------------------------------------------------------------------
    # - math Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_timeConversionInput
    def __add__(self, other:_Time|int|float) -> _Time:
        return type(self)(self.value + other.value)
    @_timeConversionInput
    def __sub__(self, other: _Time | int | float) -> _Time:
        return type(self)(self.value - other.value)
    @_timeConversionInput
    def __mul__(self, other: _Time | int | float) -> _Time:
        return type(self)(self.value * other.value)
    @_timeConversionInput
    def __floordiv__(self, other: _Time | int | float) -> _Time:
        return type(self)(self.value // other.value)
    @_timeConversionInput
    def __truediv__(self, other: _Time | int | float) -> _Time:
        return type(self)(self.value / other.value)
    @_timeConversionInput
    def __pow__(self, other: _Time | int | float) -> _Time:
        return type(self)(self.value ** other.value)
    @_timeConversionInput
    def __mod__(self, other: _Time | int | float) -> _Time:
        return type(self)(self.value % other.value)

    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__sub__(other)
    def __imul__(self, other):
        return self.__mul__(other)
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
    def __itruediv__(self, other):
        return self.__truediv__(other)
    def __imod__(self, other):
        return self.__mod__(other)
    def __ipow__(self, other):
        return self.__pow__(other)

# ----------------------------------------------------------------------------------------------------------------------
class Hour(_Time):
    def __str__(self):
        return f"{str(self.value)}h"
    def __repr__(self) -> str:
        return f"Hour(value={str(self.value)})"
# ----------------------------------------------------------------------------------------------------------------------
class Minute(_Time):
    def __str__(self):
        return f"{str(self.value)}m"
    def __repr__(self) -> str:
        return f"Minute(value={str(self.value)})"
# ----------------------------------------------------------------------------------------------------------------------
class Second(_Time):
    def __str__(self):
        return f"{str(self.value)}s"
    def __repr__(self) -> str:
        return f"Second(value={str(self.value)})"
# ----------------------------------------------------------------------------------------------------------------------
class MilliSecond(_Time):
    def __str__(self):
        return f"{str(self.value)}ms"
    def __repr__(self) -> str:
        return f"MilliSecond(value={str(self.value)})"

