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
class CubicBezier(ValueType):
    x1:float
    y1:float
    x2:float
    y2:float

    def __init__(self, x1:float,y1:float,x2:float,y2:float):
        self.x1, self.y1, self.x2, self.y2 = x1,y1,x2,y2

    @property
    def x1(self):
        return self._x1
    @x1.setter
    def x1(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError
        self._x1 = max(min(value, 1.0),0.0)
    @property
    def x2(self):
        return self._x2
    @x2.setter
    def x2(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError
        self._x2 = max(min(value, 1.0),0.0)
    @property
    def y1(self):
        return self._y1
    @y1.setter
    def y1(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError
        self._y1 = max(min(value, 1.0),0.0)
    @property
    def y2(self):
        return self._y2
    @y2.setter
    def y2(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError
        self._y2 = max(min(value, 1.0),0.0)

    def __repr__(self) -> str:
        return f"<CubicBezier x1={str(self.x1)},y1={str(self.y1)},x2={str(self.x2)},y2={str(self.y2)}>"

    def __eq__(self, other):
        if isinstance(other, CubicBezier):
            return all(a==b for a,b in zip(
                (self.x1,self.y1,self.x2,self.y2),
                (other.x1,other.y1,other.x2,other.y2),
            ))
        elif isinstance(other, tuple) and len(other) == 4 and all(isinstance(t,(int|float)) for t in other):
            return all(a==b for a,b in zip(
                (self.x1,self.y1,self.x2,self.y2),
                (*other,),
            ))
        else:
            return NotImplemented

    def __str__(self):
        return f"cubic-bezier({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    def __abs__(self) -> CubicBezier:
        return CubicBezier(abs(self.x1),abs(self.y1),abs(self.x2),abs(self.y2))
