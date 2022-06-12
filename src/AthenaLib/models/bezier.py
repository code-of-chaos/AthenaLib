# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Callable

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
# - Support Functions -
# ----------------------------------------------------------------------------------------------------------------------
def dunder_func(func:Callable,left:CubicBezier,right:CubicBezier|int|float|tuple):
    if type(left) is type(right):
        return func(
            (left.x1,left.y1,left.x2,left.y2),
            (right.x1,right.y1,right.x2,right.y2)
        )
    elif isinstance(right, (int, float)):
        return func(
            (left.x1,left.y1,left.x2,left.y2),
            (right,right,right,right)
        )
    elif isinstance(right, tuple) and len(right) == 4:
        return func(
            (left.x1,left.y1,left.x2,left.y2),
            right
        )
    else:
        return NotImplemented
# ----------------------------------------------------------------------------------------------------------------------
# - Classes -
# ----------------------------------------------------------------------------------------------------------------------
class CubicBezier:
    _x1:float
    _y1:float
    _x2:float
    _y2:float

    def __init__(self, x1:float,y1:float,x2:float,y2:float):
        self.x1, self.y1, self.x2, self.y2 = x1,y1,x2,y2

    @property
    def x1(self) -> float:
        return self._x1
    @x1.setter
    def x1(self, value):
        if not isinstance(value, int|float):
            raise TypeError
        self._x1 = max(min(value, 1.0),0.0)

    @property
    def y1(self) -> float:
        return self._y1
    @y1.setter
    def y1(self, value):
        if not isinstance(value, int|float):
            raise TypeError
        self._y1 = value

    @property
    def x2(self) -> float:
        return self._x2
    @x2.setter
    def x2(self, value):
        if not isinstance(value, int|float):
            raise TypeError
        self._x2 = max(min(value, 1.0),0.0)

    @property
    def y2(self) -> float:
        return self._y2
    @y2.setter
    def y2(self, value):
        if not isinstance(value, int|float):
            raise TypeError
        self._y2 = value

    # ------------------------------------------------------------------------------------------------------------------
    # - cast dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __abs__(self) -> CubicBezier:
        return CubicBezier(abs(self.x1),abs(self.y1),abs(self.x2),abs(self.y2))
    def __hash__(self) -> int:
        return hash((self.x1,self.y1,self.x2,self.y2))
    def __repr__(self) -> str:
        return f"CubicBezier(x1={self.x1},y1={self.y1},x2={self.x2},y2={self.y2})"
    def __str__(self):
        # Written this was because of css output
        return f"cubic-bezier({self.x1}, {self.y1}, {self.x2}, {self.y2})"
    def __round__(self, n=None):
        return type(self)(*(round(i, n) for i in (self.x1, self.y1, self.x2, self.y2)))

    # ------------------------------------------------------------------------------------------------------------------
    # - Comparison Operations -
    # ------------------------------------------------------------------------------------------------------------------
    def __eq__(self, other: CubicBezier | int | float) -> bool:
        return dunder_func(func=dunder_math.eq, left=self, right=other)
    def __ne__(self, other: CubicBezier | int | float) -> bool:
        return dunder_func(func=dunder_math.ne, left=self, right=other)
    def __gt__(self, other: CubicBezier | int | float) -> bool:
        return dunder_func(func=dunder_math.gt, left=self, right=other)
    def __lt__(self, other: CubicBezier | int | float) -> bool:
        return dunder_func(func=dunder_math.lt, left=self, right=other)
    def __ge__(self, other: CubicBezier | int | float) -> bool:
        return dunder_func(func=dunder_math.ge, left=self, right=other)
    def __le__(self, other: CubicBezier | int | float) -> bool:
        return dunder_func(func=dunder_math.le, left=self, right=other)

    # ------------------------------------------------------------------------------------------------------------------
    # - math Operations -
    # ------------------------------------------------------------------------------------------------------------------
    def __add__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.add, left=self, right=other)) is NotImplemented:
            return result
        return type(self)(*result)
    def __sub__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.sub, left=self, right=other)) is NotImplemented:
            return result
        return type(self)(*result)
    def __mul__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.mul, left=self, right=other)) is NotImplemented:
            return result
        return type(self)(*result)
    def __floordiv__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.floordiv, left=self, right=other)) is NotImplemented:
            return result
        return type(self)(*result)
    def __truediv__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.truediv, left=self, right=other)) is NotImplemented:
            return result
        return type(self)(*result)
    def __pow__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.power, left=self, right=other)) is NotImplemented:
            return result
        return type(self)(*result)
    def __mod__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.mod, left=self, right=other)) is NotImplemented:
            return result
        return type(self)(*result)

    def __iadd__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.add, left=self, right=other)) is NotImplemented:
            return result
        self.x1,self.y1,self.x2,self.y2 = result
        return self
    def __isub__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.sub, left=self, right=other)) is NotImplemented:
            return result
        self.x1,self.y1,self.x2,self.y2 = result
        return self
    def __imul__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.mul, left=self, right=other)) is NotImplemented:
            return result
        self.x1,self.y1,self.x2,self.y2 = result
        return self
    def __ifloordiv__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.floordiv, left=self, right=other)) is NotImplemented:
            return result
        self.x1,self.y1,self.x2,self.y2 = result
        return self
    def __itruediv__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.truediv, left=self, right=other)) is NotImplemented:
            return result
        self.x1,self.y1,self.x2,self.y2 = result
        return self
    def __ipow__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.power, left=self, right=other)) is NotImplemented:
            return result
        self.x1,self.y1,self.x2,self.y2 = result
        return self
    def __imod__(self, other) -> CubicBezier:
        if (result:= dunder_func(func=dunder_math.mod, left=self, right=other)) is NotImplemented:
            return result
        self.x1,self.y1,self.x2,self.y2 = result
        return self