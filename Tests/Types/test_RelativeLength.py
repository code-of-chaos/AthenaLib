# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import operator

# Custom Library
from AthenaLib.Types.RelativeLength import *

# Custom Packages
from .TypesTesting import TypesTesting

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RelativeLength(TypesTesting):
    @staticmethod
    def casesDunderFunctions(ValueType_):
        return (
            #operation          left,               right,                  result
            (operator.add,      ValueType_(100),         1,                 ValueType_(101)),
            (operator.sub,      ValueType_(100),         ValueType_(25),    ValueType_(75)),
            (operator.mul,      ValueType_(100),         2,                 ValueType_(200)),
            (operator.floordiv, ValueType_(100),         30,                ValueType_(3)),
            (operator.truediv,  ValueType_(100),         30,                ValueType_(3.3333333333333335)),
            (operator.pow,      ValueType_(4),           4,                 ValueType_(256)),
            (operator.mod,      ValueType_(100),         30,                ValueType_(10)),

            (operator.eq,       ValueType_(100),         100,               True),
            (operator.eq,       ValueType_(100),         ValueType_(100),   True),
            (operator.eq,       ValueType_(100),         2,                 False),
            (operator.eq,       ValueType_(100),         ValueType_(1),     False),

            (operator.ne,       ValueType_(100),         100,               False),
            (operator.ne,       ValueType_(100),         ValueType_(100),   False),
            (operator.ne,       ValueType_(100),         2,                 True),
            (operator.ne,       ValueType_(100),         ValueType_(1),     True),

            (operator.gt,       ValueType_(100),         50,                True),
            (operator.gt,       ValueType_(100),         ValueType_(50),    True),
            (operator.gt,       ValueType_(100),         200,               False),
            (operator.gt,       ValueType_(100),         ValueType_(200),   False),

            (operator.lt,       ValueType_(100),         50,                False),
            (operator.lt,       ValueType_(100),         ValueType_(50),    False),
            (operator.lt,       ValueType_(100),         200,               True),
            (operator.lt,       ValueType_(100),         ValueType_(200),   True),

            (operator.ge,       ValueType_(100),         50,                True),
            (operator.ge,       ValueType_(100),         ValueType_(50),    True),
            (operator.ge,       ValueType_(100),         200,               False),
            (operator.ge,       ValueType_(100),         ValueType_(200),   False),
            (operator.ge,       ValueType_(100),         100,               True),
            (operator.ge,       ValueType_(100),         ValueType_(100),   True),

            (operator.le,       ValueType_(100),         50,                False),
            (operator.le,       ValueType_(100),         ValueType_(50),    False),
            (operator.le,       ValueType_(100),         200,               True),
            (operator.le,       ValueType_(100),         ValueType_(200),   True),
            (operator.le,       ValueType_(100),         100,               True),
            (operator.le,       ValueType_(100),         ValueType_(100),   True),

        )

    # ----------------------------------------------------------------------------------------------------------------------
    # - TESTS -
    # ----------------------------------------------------------------------------------------------------------------------
    def test_ElementFontSize(self):
        ValueType_ = ElementFontSize
        cases = (
            # value,        result,
            ((100,),        ElementFontSize(100)),
            ((.101,),       ElementFontSize(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oargs  okwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100em"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      ElementFontSize(100)),
            (repr,          (),     {},       (100,),         {},      "ElementFontSize(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      ElementFontSize(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)
