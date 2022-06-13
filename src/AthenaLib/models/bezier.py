# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
import AthenaLib.functions.dunder_math as dunder_math

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CubicBezier"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Classes -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, init=False, eq=True, order=True)
class CubicBezier:
    _x1:float|int
    y1:float|int
    _x2:float|int
    y2:float|int

    def __init__(self, x1:float|int=0,y1:float|int=0,x2:float|int=0,y2:float|int=0):
        self.x1, self.y1, self.x2, self.y2 = x1,y1,x2,y2

    @property
    def x1(self) -> float:
        return self._x1
    @x1.setter
    def x1(self, value:int|float):
        self._x1 = max(min(value, 1.0),0.0)

    @property
    def x2(self) -> float:
        return self._x2
    @x2.setter
    def x2(self, value:int|float):
        self._x2 = max(min(value, 1.0),0.0)

    # ------------------------------------------------------------------------------------------------------------------
    # - cast dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __abs__(self) -> CubicBezier:
        return self.__class__(abs(self.x1),abs(self.y1),abs(self.x2),abs(self.y2))
    def __round__(self, n=None):
        return self.__class__(*(round(i, n) for i in (self.x1, self.y1, self.x2, self.y2)))

    def __iter__(self):
        yield self.x1
        yield self.y1
        yield self.x2
        yield self.y2

    def export(self) -> tuple:
        return self.x1,self.y1,self.x2,self.y2

    # ------------------------------------------------------------------------------------------------------------------
    # - math Operations -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other:CubicBezier) -> CubicBezier:
        return self.__class__(*dunder_math.add(left=self.export(), right=other.export()))
    def __sub__(self, other:CubicBezier) -> CubicBezier:
        return self.__class__(*dunder_math.sub(left=self.export(), right=other.export()))
    def __mul__(self, other:CubicBezier) -> CubicBezier:
        return self.__class__(*dunder_math.mul(left=self.export(), right=other.export()))
    def __floordiv__(self, other:CubicBezier) -> CubicBezier:
        return self.__class__(*dunder_math.floordiv(left=self.export(), right=other.export()))
    def __truediv__(self, other:CubicBezier) -> CubicBezier:
        return self.__class__(*dunder_math.truediv(left=self.export(), right=other.export()))
    def __pow__(self, other:CubicBezier) -> CubicBezier:
        return self.__class__(*dunder_math.power(left=self.export(), right=other.export()))
    def __mod__(self, other:CubicBezier) -> CubicBezier:
        return self.__class__(*dunder_math.mod(left=self.export(), right=other.export()))

    def __iadd__(self, other:CubicBezier) -> CubicBezier:
        self.x1,self.y1,self.x2,self.y2 = dunder_math.add(left=self.export(), right=other.export())
        return self
    def __isub__(self, other:CubicBezier) -> CubicBezier:
        self.x1,self.y1,self.x2,self.y2 = dunder_math.sub(left=self.export(), right=other.export())
        return self
    def __imul__(self, other:CubicBezier) -> CubicBezier:
        self.x1,self.y1,self.x2,self.y2 = dunder_math.mul(left=self.export(), right=other.export())
        return self
    def __ifloordiv__(self, other:CubicBezier) -> CubicBezier:
        self.x1,self.y1,self.x2,self.y2 = dunder_math.floordiv(left=self.export(), right=other.export())
        return self
    def __itruediv__(self, other:CubicBezier) -> CubicBezier:
        self.x1,self.y1,self.x2,self.y2 = dunder_math.truediv(left=self.export(), right=other.export())
        return self
    def __ipow__(self, other:CubicBezier) -> CubicBezier:
        self.x1,self.y1,self.x2,self.y2 = dunder_math.power(left=self.export(), right=other.export())
        return self
    def __imod__(self, other:CubicBezier) -> CubicBezier:
        self.x1,self.y1,self.x2,self.y2 = dunder_math.mod(left=self.export(), right=other.export())
        return self