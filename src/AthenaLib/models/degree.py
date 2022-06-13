# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, eq=True, order=True)
class Degree:
    value:int|float=0

    # ------------------------------------------------------------------------------------------------------------------
    # - cast dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __abs__(self):
        return self.__class__(value=abs(self.value))
    def __round__(self, n=None):
        return self.__class__(value=round(self.value, n))
    def __int__(self)-> int:
        return int(self.value)
    def __float__(self):
        return float(self.value)
    def __iter__(self):
        yield self.value
    def export(self) -> tuple:
        return tuple(self)
    def truncate_to_circle(self) -> Degree:
        return self.__class__(value=self.value%360)

    # ------------------------------------------------------------------------------------------------------------------
    # - math Operations -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other:Degree) -> Degree:
        return self.__class__(self.value + other.value)
    def __sub__(self, other:Degree) -> Degree:
        return self.__class__(self.value - other.value)
    def __mul__(self, other:Degree) -> Degree:
        return self.__class__(self.value * other.value)
    def __floordiv__(self, other:Degree) -> Degree:
        return self.__class__(self.value // other.value)
    def __truediv__(self, other:Degree) -> Degree:
        return self.__class__(self.value / other.value)
    def __pow__(self, other:Degree) -> Degree:
        return self.__class__(self.value ** other.value)
    def __mod__(self, other:Degree) -> Degree:
        return self.__class__(self.value % other.value)

    def __iadd__(self, other:Degree) -> Degree:
        self.value += other.value
        return self
    def __isub__(self, other:Degree) -> Degree:
        self.value -= other.value
        return self
    def __imul__(self, other:Degree) -> Degree:
        self.value *= other.value
        return self
    def __ifloordiv__(self, other:Degree) -> Degree:
        self.value //= other.value
        return self
    def __itruediv__(self, other:Degree) -> Degree:
        self.value /= other.value
        return self
    def __ipow__(self, other:Degree) -> Degree:
        self.value **= other.value
        return self
    def __imod__(self, other:Degree) -> Degree:
        self.value %= other.value
        return self