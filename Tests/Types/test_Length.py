# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import operator

# Custom Library
from AthenaLib.Types.Length import *

# Custom Packages
from .TypesTesting import TypesTesting

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Length(TypesTesting):
    # ----------------------------------------------------------------------------------------------------------------------
    # - TESTS -
    # ----------------------------------------------------------------------------------------------------------------------
    def test_Pixel(self):
        ValueType_ = Pixel
        cases = (
            # value,        result,
            ((100,),        Pixel(100)),
            ((.101,),       Pixel(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     value,          result,
            (str,           (100,),         "100px"),
            (int,           (100,),         100),
            (abs,           (-100,),        Pixel(100)),
            (repr,          (100,),         "Pixel(value=100)"),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesDunderFunctions = (
            #operation          left,               right,                  result

            # TUPLE
            (operator.add,      Pixel(100),         1,                      Pixel(101)),
            (operator.sub,      Pixel(100),         Pixel(25),              Pixel(75)),
            (operator.mul,      Pixel(100),         2,                      Pixel(200)),
            (operator.floordiv, Pixel(100),         30,                     Pixel(3)),
            (operator.truediv,  Pixel(100),         30,                     Pixel(3.3333333333333335)),
            (operator.pow,      Pixel(4),           4,                      Pixel(256)),
            (operator.mod,      Pixel(100),         30,                     Pixel(10)),

            (operator.eq,       Pixel(100),         100,                    True),
            (operator.eq,       Pixel(100),         Pixel(100),             True),
            (operator.eq,       Pixel(100),         2,                      False),
            (operator.eq,       Pixel(100),         Pixel(1),               False),

            (operator.ne,       Pixel(100),         100,                    False),
            (operator.ne,       Pixel(100),         Pixel(100),             False),
            (operator.ne,       Pixel(100),         2,                      True),
            (operator.ne,       Pixel(100),         Pixel(1),               True),

            (operator.gt,       Pixel(100),         50,                     True),
            (operator.gt,       Pixel(100),         Pixel(50),              True),
            (operator.gt,       Pixel(100),         200,                    False),
            (operator.gt,       Pixel(100),         Pixel(200),             False),

            (operator.lt,       Pixel(100),         50,                     False),
            (operator.lt,       Pixel(100),         Pixel(50),              False),
            (operator.lt,       Pixel(100),         200,                    True),
            (operator.lt,       Pixel(100),         Pixel(200),             True),

            (operator.ge,       Pixel(100),         50,                     True),
            (operator.ge,       Pixel(100),         Pixel(50),              True),
            (operator.ge,       Pixel(100),         200,                    False),
            (operator.ge,       Pixel(100),         Pixel(200),             False),
            (operator.ge,       Pixel(100),         100,                    True),
            (operator.ge,       Pixel(100),         Pixel(100),             True),

            (operator.le,       Pixel(100),         50,                     False),
            (operator.le,       Pixel(100),         Pixel(50),              False),
            (operator.le,       Pixel(100),         200,                    True),
            (operator.le,       Pixel(100),         Pixel(200),             True),
            (operator.le,       Pixel(100),         100,                    True),
            (operator.le,       Pixel(100),         Pixel(100),             True),

        )
        self.SubtestFunctionDunderFunctions(casesDunderFunctions)

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)