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
            ((2,-1,2,-1),   CubicBezier(1,-1,1,-1)),
            ((2,-10,2,-1),   CubicBezier(1,-10,1,-1)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oargs  okwargs    value,          kwargs   result,
            (repr,          (),     {},       (1,1,1,1),      {},      "CubicBezier(x1=1,y1=1,x2=1,y2=1)"),
            (repr,          (),     {},       (1,2,3,4),      {},      "CubicBezier(x1=1,y1=2,x2=1.0,y2=4)"),
            (str,           (),     {},       (1,2,3,4),      {},      "cubic-bezier(1, 2, 1.0, 4)"),
            (abs,           (),     {},       (-1,-1,-1,-1),  {},      CubicBezier(0,1,0,1)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesDunderFunctions = (
            #operation          left,                       right,              result

            # TUPLE
            (operator.add,      CubicBezier(0,0,0,0),       (1,.5,.25,2),           CubicBezier(1,.5,.25,2)),
            (operator.sub,      CubicBezier(1,1,1,1),       CubicBezier(0,2,5,1),   CubicBezier(1,-1,0,0)),
            (operator.mul,      CubicBezier(.5,8,.25,-4),   2,                      CubicBezier(1,16,.5,-8)),
            (operator.floordiv, CubicBezier(1,8,1,-4),      2,                      CubicBezier(0,4,0,-2)),
            (operator.truediv,  CubicBezier(1,8,1,-4),      (1,2,5,1),              CubicBezier(1,4.0,0.2,-4.0)),
            (operator.pow,      CubicBezier(1,8,1,-4),      4,                      CubicBezier(1,4096,1,256)),
            (operator.mod,      CubicBezier(1,8,1,-4),      (1,2,5,1),              CubicBezier(0,0,1,0)),

            (operator.eq,       CubicBezier(1,1,1,1),       1,                      True),
            (operator.eq,       CubicBezier(1,1,1,1),       (1,1,1,1),              True),
            (operator.eq,       CubicBezier(1,1,1,1),       CubicBezier(1,1,1,1),   True),
            (operator.eq,       CubicBezier(1,1,1,1),       2,                      False),
            (operator.eq,       CubicBezier(1,1,1,1),       (1,0,1,1),              False),
            (operator.eq,       CubicBezier(1,1,1,1),       CubicBezier(1,0,1,1),   False),

            (operator.ne,       CubicBezier(1,1,1,1),       1,                      False),
            (operator.ne,       CubicBezier(1,1,1,1),       (1,1,1,1),              False),
            (operator.ne,       CubicBezier(1,1,1,1),       CubicBezier(1,1,1,1),   False),
            (operator.ne,       CubicBezier(1,1,1,1),       2,                      True),
            (operator.ne,       CubicBezier(1,1,1,1),       (0,0,0,0),              True),
            (operator.ne,       CubicBezier(1,1,1,1),       CubicBezier(0,0,0,0),   True),

            (operator.gt,       CubicBezier(1,1,1,1),       0.5,                    True),
            (operator.gt,       CubicBezier(1,1,1,1),       (0.5,0.5,0.5,0.5),      True),
            (operator.gt,       CubicBezier(1,1,1,1),       CubicBezier(.5,.5,.5,0),True),
            (operator.gt,       CubicBezier(1,1,1,1),       2,                      False),
            (operator.gt,       CubicBezier(1,1,1,1),       (0,2,.5,.5),            False),
            (operator.gt,       CubicBezier(1,1,1,1),       CubicBezier(0,2,.5,.5), False),

            (operator.lt,       CubicBezier(1,1,1,1),       0.5,                    False),
            (operator.lt,       CubicBezier(1,1,1,1),       (0.5,0.5,0.5,0.5),      False),
            (operator.lt,       CubicBezier(1,1,1,1),       CubicBezier(.5,.5,.5,0),False),
            (operator.lt,       CubicBezier(1,1,1,1),       2,                      True),
            (operator.lt,       CubicBezier(.5,1,.5,1),     (1,2,1,2),              True),
            (operator.lt,       CubicBezier(.5,1,.5,1),     CubicBezier(1,2,1,2),   True),

            (operator.ge,       CubicBezier(1,1,1,1),       0.5,                    True),
            (operator.ge,       CubicBezier(1,1,1,1),       (0.5,0.5,1,0.5),        True),
            (operator.ge,       CubicBezier(1,1,1,1),       CubicBezier(.5,.5,.5,1),True),
            (operator.ge,       CubicBezier(1,1,1,1),       2,                      False),
            (operator.ge,       CubicBezier(1,1,1,1),       (0,2,1,1),              False),
            (operator.ge,       CubicBezier(1,1,1,1),       CubicBezier(0,2,1,1),   False),

            (operator.le,       CubicBezier(1,1,1,1),       .5,                     False),
            (operator.le,       CubicBezier(1,1,1,1),       (0.5,0.5,1,0.5),        False),
            (operator.le,       CubicBezier(1,1,1,1),       CubicBezier(.5,.5,.5,1),False),
            (operator.le,       CubicBezier(1,1,1,1),       2,                      True),
            (operator.le,       CubicBezier(1,1,1,1),       (1,2,1,1),              True),
            (operator.le,       CubicBezier(1,1,1,1),       CubicBezier(1,2,1,1),   True),

        )
        self.SubtestFunctionDunderFunctions(casesDunderFunctions)

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",), TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)