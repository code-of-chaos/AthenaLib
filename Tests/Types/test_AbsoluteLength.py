# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import operator

# Custom Library
from AthenaLib.Types.AbsoluteLength import *

# Custom Packages
from .TypesTesting import TypesTesting

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AbsoluteLength(TypesTesting):
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

    def test_ConversionsToPixel(self):
        decimalPlaces = 9
        cases = (
            # value,        result,
            (Pixel(1),      Pixel(1)),
            (Pixel(16),     Pica(1)),
            (Pixel(20),     Point(15)),
            (Pixel(96),     Inch(1)),
            (Pixel(3),      MilliMeter(0.79375)),
            (Pixel(30),     CentiMeter(0.79375)),
            (Pixel(300),    DeciMeter(0.79375)),
            (Pixel(3000),   Meter(0.79375)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)

    def test_ConversionsToPica(self):
        decimalPlaces = 9
        cases = (
            # value,        result,
            (Pica(1),      Pixel(16)),
            (Pica(1),      Pica(1)),
            (Pica(1),      Point(12)),
            (Pica(1),      Inch(0.166666667)),
            (Pica(3),      MilliMeter(12.7)),
            (Pica(30),     CentiMeter(12.7)),
            (Pica(300),    DeciMeter(12.7)),
            (Pica(3000),   Meter(12.7)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)

    def test_ConversionsToPoint(self):
        decimalPlaces = 4
        cases = (
            # value,        result,
            (Point(10),     Pixel(13.3333)),
            (Point(1),      Pica(0.0833333333)),
            (Point(1),      Point(1)),
            (Point(10),     Inch(0.1388888889)),
            (Point(10),     MilliMeter(3.5277777778)),
            (Point(100),    CentiMeter(3.5277777778)),
            (Point(1000),   DeciMeter(3.5277777778)),
            (Point(10000),  Meter(3.5277777778)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)

    def test_ConversionsToInch(self):
        decimalPlaces = 4
        cases = (
            # value,                    result,
            (Inch(1),                   Pixel(96)),
            (Inch(1),                   Pica(6)),
            (Inch(0.1388888889),        Point(10)),
            (Inch(10),                  Inch(10)),
            (Inch(1),                   MilliMeter(25.4)),
            (Inch(10),                  CentiMeter(25.4)),
            (Inch(100),                 DeciMeter(25.4)),
            (Inch(1000),                Meter(25.4)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)

    def test_ConversionsToMilliMeter(self):
        decimalPlaces = 4
        cases = (
            # value,                    result,
            (MilliMeter(100),           Pixel(377.9527559055)),
            (MilliMeter(50 ),           Pica(11.811023622)),
            (MilliMeter(5),             Point(14.173219418444)),
            (MilliMeter(100),           Inch(3.937007874)),
            (MilliMeter(1),             MilliMeter(1)),
            (MilliMeter(10),            CentiMeter(1)),
            (MilliMeter(100),           DeciMeter(1)),
            (MilliMeter(1000),          Meter(1)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)

    def test_ConversionsToCentiMeter(self):
        decimalPlaces = 4
        cases = (
            # value,                    result,
            (CentiMeter(10),            Pixel(377.9527559055)),
            (CentiMeter(5),             Pica(11.811023622)),
            (CentiMeter(.5),            Point(14.173219418444)),
            (CentiMeter(10),            Inch(3.937007874)),
            (CentiMeter(1),             MilliMeter(10)),
            (CentiMeter(10),            CentiMeter(10)),
            (CentiMeter(100),           DeciMeter(10)),
            (CentiMeter(1000),          Meter(10)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)

    def test_ConversionsToDeciMeter(self):
        decimalPlaces = 4
        cases = (
            # value,                    result,
            (DeciMeter(1),              Pixel(377.9527559055)),
            (DeciMeter(.5),             Pica(11.811023622)),
            (DeciMeter(.05),            Point(14.173219418444)),
            (DeciMeter(1),              Inch(3.937007874)),
            (DeciMeter(1),              MilliMeter(100)),
            (DeciMeter(10),             CentiMeter(100)),
            (DeciMeter(100),            DeciMeter(100)),
            (DeciMeter(1000),           Meter(100)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)

    def test_ConversionsToMeter(self):
        decimalPlaces = 4
        cases = (
            # value,        result,
            (Meter(.1),     Pixel(377.9527559055)),
            (Meter(.05),    Pica(11.811023622)),
            (Meter(.005),   Point(14.173219418444)),
            (Meter(.1),     Inch(3.937007874)),
            (Meter(1),      MilliMeter(1000)),
            (Meter(10),     CentiMeter(1000)),
            (Meter(100),    DeciMeter(1000)),
            (Meter(1000),   Meter(1000)),
        )
        for value, result in cases:
            with self.subTest(value=value, result=result):
                self.assertAlmostEqual(value, result, decimalPlaces)