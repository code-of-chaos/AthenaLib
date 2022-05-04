# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaLib.Types.ValueType import ValueType
from AthenaLib.Types.Time import Second, MilliSecond
from AthenaLib.Types.CubicBezier import CubicBezier
from AthenaLib.Types.Url import Url

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperties(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # - Support Functions -
    # ------------------------------------------------------------------------------------------------------------------
    def SubtestFunction(self, ValueType_, cases):
        for value, result, str_output, abs_output in cases:
            with self.subTest(value=value, result=result, str_output=str_output):
                self.assertEqual(ValueType_(*value), result)
                self.assertEqual(ValueType_(*value).__str__(), str_output)
                if hasattr(ValueType_, "__abs__"):
                    self.assertEqual(ValueType_(*value).__abs__(), abs_output)

    def SubtestFunctionFails(self, ValueType_, cases):
        for value, error in cases:
            with self.subTest(value=value, error=error):
                with self.assertRaises(error):
                    ValueType_(*value)
                    print(ValueType_(*value))

    # ----------------------------------------------------------------------------------------------------------------------
    # - TESTS -
    # ----------------------------------------------------------------------------------------------------------------------
    def test_Second(self):
        ValueType_ = Second
        cases = (
            #value,             result,             str_output,     abs_output
            ((0,),              Second(0),          "0s",           Second(0)),
            ((-100,),           Second(-100),       "-100s",        Second(100)),
            ((1,),              MilliSecond(1000),  "1s",           Second(1)),
        )
        self.SubtestFunction(ValueType_, cases)

        casesFail = (
            #value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)