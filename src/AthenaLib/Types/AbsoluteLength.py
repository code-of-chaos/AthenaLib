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
    "absoluteLengthConverion",
    "Pixel", "Pica", "Point",
    "Inch",
    "Meter", "DeciMeter", "CentiMeter", "MilliMeter"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Functions -
# ----------------------------------------------------------------------------------------------------------------------
def absoluteLengthConverion(original: int | float | _AbsoluteLength, cast: int | float | _AbsoluteLength, *, pixels_per_inch:int=96) -> int | float | _AbsoluteLength:
    match original, cast:
        # General catches for throwing to and from numbers
        case int()|float(), _AbsoluteLength():
            return type(cast)(original)
        case _AbsoluteLength(), int() | float():
            return type(cast)(original.value)

        # To length Types, if both types are the same (Pixel->Pixel)
        case a,b if type(a) is type(b) and isinstance(a, _AbsoluteLength) and isinstance(b, _AbsoluteLength):
            return type(cast)(original.value)

        # Pica
        case Pica(), Pixel():
            return Pixel(original.value * 16)
        case Pica(), Point():
            return Point(original.value * 12)
        case Pica(), Inch():
            return Inch(original.value/6)
        case Pica(), MilliMeter():
            inch_value = original.value/6
            return MilliMeter(inch_value*25.4)
        case Pica(), CentiMeter():
            inch_value = original.value/6
            return CentiMeter(inch_value*2.54)
        case Pica(), DeciMeter():
            inch_value = original.value/6
            return DeciMeter(inch_value*.254)
        case Pica(), Meter():
            inch_value = original.value/6
            return Meter(inch_value*.0254)

        # Point
        case Point(), Pixel():
            inch_value = original.value/72
            return Pixel(inch_value*pixels_per_inch)
        case Point(), Pica():
            return Pica(original.value/12)
        case Point(), Inch():
            return Inch(original.value/72)
        case Point(), MilliMeter():
            inch_value = original.value/72
            return MilliMeter(inch_value*25.4)
        case Point(), CentiMeter():
            inch_value = original.value/72
            return CentiMeter(inch_value*2.54)
        case Point(), DeciMeter():
            inch_value = original.value/72
            return DeciMeter(inch_value*.254)
        case Point(), Meter():
            inch_value = original.value/72
            return Meter(inch_value*.0254)

        # Pixel
        case Pixel(), Pica():
            return Pica(original.value/16)
        case Pixel(), Point():
            inch_value = original.value/pixels_per_inch
            return Point(inch_value*72)
        case Pixel(), Inch():
            return Inch(original.value/pixels_per_inch)
        case Pixel(), MilliMeter():
            inch_value = original.value/pixels_per_inch
            return MilliMeter(inch_value*25.4)
        case Pixel(), CentiMeter():
            inch_value = original.value/pixels_per_inch
            return CentiMeter(inch_value*2.54)
        case Pixel(), DeciMeter():
            inch_value = original.value/pixels_per_inch
            return DeciMeter(inch_value*.254)
        case Pixel(), Meter():
            inch_value = original.value/pixels_per_inch
            return Meter(inch_value*.0254)

        # Inch
        case Inch(), Pixel():
            return Pixel(original.value*pixels_per_inch)
        case Inch(), Pica():
            return Pica(original.value/0.166666667)
        case Inch(), Point():
            return Point(original.value*72)
        case Inch(), MilliMeter():
            return MilliMeter(original.value*25.4)
        case Inch(), CentiMeter():
            return CentiMeter(original.value*2.54)
        case Inch(), DeciMeter():
            return DeciMeter(original.value*.254)
        case Inch(), Meter():
            return Meter(original.value*.0254)

        # MilliMeter
        case MilliMeter(), Pixel():
            inch_value = original.value/25.4
            return Pixel(inch_value*96)
        case MilliMeter(), Pica():
            inch_value = original.value/25.4
            return Pica(inch_value*6)
        case MilliMeter(), Point():
            inch_value = original.value/25.4
            return Point(72*inch_value)
        case MilliMeter(), Inch():
            return Inch(original.value/25.4)
        case MilliMeter(), CentiMeter():
            return CentiMeter(original.value/10)
        case MilliMeter(), DeciMeter():
            return DeciMeter(original.value/100)
        case MilliMeter(), Meter():
            return Meter(original.value/1000)

        # CentiMeter
        case CentiMeter(), Pixel():
            inch_value = original.value/2.54
            return Pixel(inch_value*96)
        case CentiMeter(), Pica():
            inch_value = original.value/2.54
            return Pica(inch_value*6)
        case CentiMeter(), Point():
            inch_value = original.value/2.54
            return Point(72*inch_value)
        case CentiMeter(), Inch():
            return Inch(original.value/2.54)
        case CentiMeter(), MilliMeter():
            return MilliMeter(original.value*10)
        case CentiMeter(), DeciMeter():
            return DeciMeter(original.value/10)
        case CentiMeter(), Meter():
            return Meter(original.value/100)

        # DeciMeter
        case DeciMeter(), Pixel():
            inch_value = original.value/.254
            return Pixel(inch_value*96)
        case DeciMeter(), Pica():
            inch_value = original.value/.254
            return Pica(inch_value*6)
        case DeciMeter(), Point():
            inch_value = original.value/.254
            return Point(72*inch_value)
        case DeciMeter(), Inch():
            return Inch(original.value/.254)
        case DeciMeter(), MilliMeter():
            return MilliMeter(original.value*100)
        case DeciMeter(), CentiMeter():
            return CentiMeter(original.value*10)
        case DeciMeter(), Meter():
            return Meter(original.value/10)

        # Meter
        case Meter(), Pixel():
            inch_value = original.value/.0254
            return Pixel(inch_value*96)
        case Meter(), Pica():
            inch_value = original.value/.0254
            return Pica(inch_value*6)
        case Meter(), Point():
            inch_value = original.value/.0254
            return Point(72*inch_value)
        case Meter(), Inch():
            return Inch(original.value/.0254)
        case Meter(), MilliMeter():
            return MilliMeter(original.value*1000)
        case Meter(), CentiMeter():
            return CentiMeter(original.value*100)
        case Meter(), DeciMeter():
            return DeciMeter(original.value*10)

        case _:
            return NotImplemented

def _absoluteLengthConversionInput(fnc):
    def wrapper(self:_AbsoluteLength, *args, **kwargs):
        if isinstance(args, tuple):
            other,*_ = args
        else:
            other, _ = args, ()

        if (otherConverted := absoluteLengthConverion(other, self, pixels_per_inch=self.pixels_per_inch)) is NotImplemented:
            return NotImplemented
        return fnc(self,otherConverted, *_,**kwargs)
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Classes -
# ----------------------------------------------------------------------------------------------------------------------
class _AbsoluteLength(ValueType, ABC):
    _value:int|float
    pixels_per_inch:int
    def __init__(self, value: int | float | _AbsoluteLength):
        self.value = value
        self.pixels_per_inch=96

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
    def __abs__(self) -> _AbsoluteLength:
        return  type(self)(abs(self.value))
    def __round__(self, n=None):
        return  type(self)(round(self.value, n))

    @abstractmethod
    def __str__(self)->str:...
    @abstractmethod
    def __repr__(self) -> str:...

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_absoluteLengthConversionInput
    def __eq__(self, other: _AbsoluteLength | int | float) -> bool:
        return self.value == other.value
    @_absoluteLengthConversionInput
    def __ne__(self, other: _AbsoluteLength | int | float) -> bool:
        return self.value != other.value
    @_absoluteLengthConversionInput
    def __gt__(self, other: _AbsoluteLength | int | float) -> bool:
        return self.value > other.value
    @_absoluteLengthConversionInput
    def __lt__(self, other: _AbsoluteLength | int | float) -> bool:
        return self.value < other.value
    @_absoluteLengthConversionInput
    def __ge__(self, other: _AbsoluteLength | int | float) -> bool:
        return self.value >= other.value
    @_absoluteLengthConversionInput
    def __le__(self, other: _AbsoluteLength | int | float) -> bool:
        return self.value <= other.value

    # ------------------------------------------------------------------------------------------------------------------
    # - math Operations -
    # ------------------------------------------------------------------------------------------------------------------
    @_absoluteLengthConversionInput
    def __add__(self, other: _AbsoluteLength | int | float) -> _AbsoluteLength:
        return type(self)(self.value + other.value)
    @_absoluteLengthConversionInput
    def __sub__(self, other: _AbsoluteLength | int | float) -> _AbsoluteLength:
        return type(self)(self.value - other.value)
    @_absoluteLengthConversionInput
    def __mul__(self, other: _AbsoluteLength | int | float) -> _AbsoluteLength:
        return type(self)(self.value * other.value)
    @_absoluteLengthConversionInput
    def __floordiv__(self, other: _AbsoluteLength | int | float) -> _AbsoluteLength:
        return type(self)(self.value // other.value)
    @_absoluteLengthConversionInput
    def __truediv__(self, other: _AbsoluteLength | int | float) -> _AbsoluteLength:
        return type(self)(self.value / other.value)
    @_absoluteLengthConversionInput
    def __pow__(self, other: _AbsoluteLength | int | float) -> _AbsoluteLength:
        return type(self)(self.value ** other.value)
    @_absoluteLengthConversionInput
    def __mod__(self, other: _AbsoluteLength | int | float) -> _AbsoluteLength:
        return type(self)(self.value % other.value)

    @_absoluteLengthConversionInput
    def __iadd__(self, other: _AbsoluteLength | int | float):
        self.value += other.value
        return self
    @_absoluteLengthConversionInput
    def __isub__(self, other: _AbsoluteLength | int | float):
        self.value -= other.value
        return self
    @_absoluteLengthConversionInput
    def __imul__(self, other: _AbsoluteLength | int | float):
        self.value *= other.value
        return self
    @_absoluteLengthConversionInput
    def __ifloordiv__(self, other: _AbsoluteLength | int | float):
        self.value //= other.value
        return self
    @_absoluteLengthConversionInput
    def __itruediv__(self, other: _AbsoluteLength | int | float):
        self.value /= other.value
        return self
    @_absoluteLengthConversionInput
    def __ipow__(self, other: _AbsoluteLength | int | float):
        self.value **= other.value
        return self
    @_absoluteLengthConversionInput
    def __imod__(self, other: _AbsoluteLength | int | float):
        self.value %= other.value
        return self

# ----------------------------------------------------------------------------------------------------------------------
class Pica(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}pc"
    def __repr__(self) -> str:
        return f"Pica(value={str(self.value)})"

# ----------------------------------------------------------------------------------------------------------------------
class Point(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}pt"
    def __repr__(self) -> str:
        return f"Point(value={str(self.value)})"

# ----------------------------------------------------------------------------------------------------------------------
class Pixel(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}px"
    def __repr__(self) -> str:
        return f"Pixel(value={str(self.value)})"

# ----------------------------------------------------------------------------------------------------------------------
class Inch(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}in"
    def __repr__(self) -> str:
        return f"Inch(value={str(self.value)})"

# ----------------------------------------------------------------------------------------------------------------------
class MilliMeter(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}mm"
    def __repr__(self) -> str:
        return f"MilliMeter(value={str(self.value)})"

# ----------------------------------------------------------------------------------------------------------------------
class CentiMeter(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}cm"
    def __repr__(self) -> str:
        return f"CentiMeter(value={str(self.value)})"

# ----------------------------------------------------------------------------------------------------------------------
class DeciMeter(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}dm"
    def __repr__(self) -> str:
        return f"DeciMeter(value={str(self.value)})"

# ----------------------------------------------------------------------------------------------------------------------
class Meter(_AbsoluteLength):
    def __str__(self):
        return f"{str(self.value)}m"
    def __repr__(self) -> str:
        return f"Meter(value={str(self.value)})"
