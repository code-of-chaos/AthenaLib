# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import operator

# Custom Library
from AthenaLib.Types.Time import *

# Custom Packages
from .TypesTesting import TypesTesting

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Time(TypesTesting):
    # ----------------------------------------------------------------------------------------------------------------------
    # - TESTS -
    # ----------------------------------------------------------------------------------------------------------------------
    def test_Hour(self):
        ValueType_ = Hour
        cases = (
            # value,            result,
            ((1,),              Minute(60)),
            ((1,),              Hour(1)),
            ((1,),              MilliSecond(3_600_000)),
        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     value,      result,
            (repr,          (0,),       "Hour(value=0)"),
            (str,           (0,),       "0h"),
            (int,           (0,),       0),
            (float,         (1,),       1.0),
            (abs,           (-100,),    Hour(value=100)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesFail = (
            #value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_Minute(self):
        ValueType_ = Minute
        cases = (
            #value,             result,
            ((1,),              Second(60)),
            ((60,),             Hour(1)),
            ((1,),              MilliSecond(60_000)),
        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            #operation      value,      result,
            (repr,          (0,),       "Minute(value=0)"),
            (str,           (0,),       "0m"),
            (int,           (0,),       0),
            (float,         (1,),       1.0),
            (abs,           (-100,),    Minute(value=100)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesFail = (
            #value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_Second(self):
        ValueType_ = Second
        cases = (
            #value,             result,
            ((0,),              Second(0)),
            ((-100,),           Second(-100)),
            ((1,),              MilliSecond(1000)),
            ((60,),             Minute(1)),
        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            #operation      value,      result,
            (repr,          (0,),       "Second(value=0)"),
            (str,           (0,),       "0s"),
            (int,           (0,),       0),
            (abs,           (-100,),    Second(value=100)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesDunderFunctions = (
            #operation          left,           right,  result

            # INTEGERS
            (operator.add,      Second(1),      2,      Second(3)),
            (operator.sub,      Second(5),      1,      Second(4)),
            (operator.mul,      Second(5),      2,      Second(10)),
            (operator.floordiv, Second(7),      2,      Second(3)),
            (operator.truediv,  Second(7),      2,      Second(3.5)),
            (operator.pow,      Second(4),      4,      Second(256)),
            (operator.mod,      Second(7),      3,      Second(1)),

            (operator.eq,       Second(1),      1,      True),
            (operator.eq,       Second(1),      2,      False),
            (operator.ne,       Second(5),      1,      True),
            (operator.ne,       Second(5),      5,      False),
            (operator.gt,       Second(5),      2,      True),
            (operator.gt,       Second(5),      6,      False),
            (operator.lt,       Second(5),      6,      True),
            (operator.lt,       Second(5),      2,      False),
            (operator.ge,       Second(7),      2,      True),
            (operator.ge,       Second(7),      7,      True),
            (operator.ge,       Second(7),      9,      False),
            (operator.le,       Second(4),      8,      True),
            (operator.le,       Second(4),      4,      True),
            (operator.le,       Second(4),      1,      False),

            # FLOATS
            (operator.add,      Second(1),      .2,      Second(1.2)),
            (operator.sub,      Second(5),      .1,      Second(4.9)),
            (operator.mul,      Second(5),      .2,      Second(1.0)),
            (operator.floordiv, Second(7),      .2,      Second(34.0)),
            (operator.truediv,  Second(7),      .2,      Second(35.0)),
            (operator.pow,      Second(4),      .4,      Second(1.7411011265922482)),
            (operator.mod,      Second(7),      .3,      Second(0.10000000000000026)),

            # OTHER TIME OBJECTS
            (operator.add,      Second(1),      MilliSecond(2),      Second(1.002)),
            (operator.sub,      Second(5),      MilliSecond(1),      Second(4.999)),
            (operator.mul,      Second(5),      MilliSecond(2),      Second(0.01)),
            (operator.floordiv, Second(7),      MilliSecond(2),      Second(3499.0)),
            (operator.truediv,  Second(7),      MilliSecond(2),      Second(3500.0)),
            (operator.pow,      Second(4),      MilliSecond(4),      Second(1.0055605803984682)),
            (operator.mod,      Second(7),      MilliSecond(3),      Second(0.0009999999999998543)),

            (operator.eq,       Second(1),      MilliSecond(1000),   True),
            (operator.eq,       Second(1),      MilliSecond(2000),   False),
            (operator.ne,       Second(5),      MilliSecond(1000),   True),
            (operator.ne,       Second(5),      MilliSecond(5000),   False),
            (operator.gt,       Second(5),      MilliSecond(2000),   True),
            (operator.gt,       Second(5),      MilliSecond(6000),   False),
            (operator.lt,       Second(5),      MilliSecond(6000),   True),
            (operator.lt,       Second(5),      MilliSecond(2000),   False),
            (operator.ge,       Second(7),      MilliSecond(2000),   True),
            (operator.ge,       Second(7),      MilliSecond(7000),   True),
            (operator.ge,       Second(7),      MilliSecond(9000),   False),
            (operator.le,       Second(4),      MilliSecond(8000),   True),
            (operator.le,       Second(4),      MilliSecond(4000),   True),
            (operator.le,       Second(4),      MilliSecond(1000),   False),

            (operator.add,      Second(1),      Minute(2),      Second(121)),
            (operator.sub,      Second(5),      Minute(1),      Second(-55)),
            (operator.mul,      Second(5),      Minute(2),      Second(5*120)),
            (operator.floordiv, Second(7),      Minute(2),      Second(7//120)),
            (operator.truediv,  Second(7),      Minute(2),      Second(7/120)),
            (operator.pow,      Second(4),      Minute(1),      Second(4**60)),
            (operator.mod,      Second(7),      Minute(3),      Second(7%180)),

            (operator.iadd,     Second(1),      .2,      Second(1.2)),
            (operator.isub,     Second(5),      .1,      Second(4.9)),
            (operator.imul,     Second(5),      .2,      Second(1.0)),
            (operator.ifloordiv,Second(7),      .2,      Second(34.0)),
            (operator.itruediv, Second(7),      .2,      Second(35.0)),
            (operator.ipow,     Second(4),      .4,      Second(1.7411011265922482)),
            (operator.imod,     Second(7),      .3,      Second(0.10000000000000026)),


        )
        self.SubtestFunctionDunderFunctions(casesDunderFunctions)

        casesFail = (
            #value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_MilliSecond(self):
        ValueType_ = MilliSecond
        cases = (
            #value,             result,
            ((1,),              Second(0.001)),
            ((-1000,),          Second(-1)),
            ((1,),              MilliSecond(1)),
            ((-1,),             MilliSecond(-1)),
            ((60_000,),         Minute(1)),
            ((3_600_000,),      Hour(1)),
        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            #operation      value,      result,
            (repr,          (0,),       "MilliSecond(value=0)"),
            (str,           (0,),       "0ms"),
            (int,           (0,),       0),
            (float,         (1,),       1.0),
            (abs,           (-100,),    MilliSecond(value=100)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesFail = (
            #value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)