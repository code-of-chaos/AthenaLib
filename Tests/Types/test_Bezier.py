# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import operator

# Custom Library
from AthenaLib.Types.Bezier import *

# Custom Packages
from .TypesTesting import TypesTesting

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Bezier(TypesTesting):
    # ----------------------------------------------------------------------------------------------------------------------
    # - TESTS -
    # ----------------------------------------------------------------------------------------------------------------------
    def test_CubicBezier(self):
        ValueType_ = CubicBezier
        cases = (
            # value,        result,
            ((1,1,1,1),     CubicBezier(1,1,1,1)),
            ((2,-1,2,-1),   CubicBezier(1,0,1,0)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     value,          result,
            (repr,          (1,1,1,1),      "CubicBezier(x1=1,y1=1,x2=1,y2=1)"),
            (repr,          (1,2,3,4),      "CubicBezier(x1=1,y1=1.0,x2=1.0,y2=1.0)"),
            (str,           (1,2,3,4),      "cubic-bezier(1, 1.0, 1.0, 1.0)"),
            (abs,           (-1,-1,-1,-1),  CubicBezier(0,0,0,0)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",), TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)