# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import operator

# Custom Library
from AthenaLib.models.length_relative import *
from AthenaLib.models.math import Percent

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
            # operation     oArgs  oKwargs    args,           kwargs   result,
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

    def test_ElementFontHeight(self):
        ValueType_ = ElementFontHeight
        cases = (
            # value,        result,
            ((100,),        ElementFontHeight(100)),
            ((.101,),       ElementFontHeight(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100ex"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      ElementFontHeight(100)),
            (repr,          (),     {},       (100,),         {},      "ElementFontHeight(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      ElementFontHeight(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_ZeroCharacterWidth(self):
        ValueType_ = ZeroCharacterWidth
        cases = (
            # value,        result,
            ((100,),        ZeroCharacterWidth(100)),
            ((.101,),       ZeroCharacterWidth(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100ch"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      ZeroCharacterWidth(100)),
            (repr,          (),     {},       (100,),         {},      "ZeroCharacterWidth(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      ZeroCharacterWidth(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_RootElementFontSize(self):
        ValueType_ = RootElementFontSize
        cases = (
            # value,        result,
            ((100,),        RootElementFontSize(100)),
            ((.101,),       RootElementFontSize(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100rem"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      RootElementFontSize(100)),
            (repr,          (),     {},       (100,),         {},      "RootElementFontSize(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      RootElementFontSize(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_ViewportWidthPercent(self):
        ValueType_ = ViewportWidthPercent
        cases = (
            # value,        result,
            ((100,),        ViewportWidthPercent(100)),
            ((.101,),       ViewportWidthPercent(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100vw"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      ViewportWidthPercent(100)),
            (repr,          (),     {},       (100,),         {},      "ViewportWidthPercent(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      ViewportWidthPercent(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_ViewportHeightPercent(self):
        ValueType_ = ViewportHeightPercent
        cases = (
            # value,        result,
            ((100,),        ViewportHeightPercent(100)),
            ((.101,),       ViewportHeightPercent(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100vh"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      ViewportHeightPercent(100)),
            (repr,          (),     {},       (100,),         {},      "ViewportHeightPercent(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      ViewportHeightPercent(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_ViewportSmallerPercent(self):
        ValueType_ = ViewportSmallerPercent
        cases = (
            # value,        result,
            ((100,),        ViewportSmallerPercent(100)),
            ((.101,),       ViewportSmallerPercent(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100vmin"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      ViewportSmallerPercent(100)),
            (repr,          (),     {},       (100,),         {},      "ViewportSmallerPercent(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      ViewportSmallerPercent(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_ViewportLargerPercent(self):
        ValueType_ = ViewportLargerPercent
        cases = (
            # value,        result,
            ((100,),        ViewportLargerPercent(100)),
            ((.101,),       ViewportLargerPercent(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100vmax"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      ViewportLargerPercent(100)),
            (repr,          (),     {},       (100,),         {},      "ViewportLargerPercent(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      ViewportLargerPercent(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)

    def test_Percent(self):
        ValueType_ = Percent
        cases = (
            # value,        result,
            ((100,),        Percent(100)),
            ((.101,),       Percent(0.101)),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     oArgs  oKwargs    args,           kwargs   result,
            (str,           (),     {},       (100,),         {},      "100%"),
            (int,           (),     {},       (100,),         {},      100),
            (abs,           (),     {},       (-100,),        {},      Percent(100)),
            (repr,          (),     {},       (100,),         {},      "Percent(value=100)"),
            (round,         (3,),   {},       (.0157,),       {},      Percent(.016)),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        self.SubtestFunctionDunderFunctions(self.casesDunderFunctions(ValueType_))

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",),     TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)