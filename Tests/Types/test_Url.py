# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import unittest

import operator

# Custom Library
from AthenaLib.Types.Url import Url

# Custom Packages
from .TypesTesting import TypesTesting

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class WebsiteUrl(TypesTesting):
    # ----------------------------------------------------------------------------------------------------------------------
    # - TESTS -
    # ----------------------------------------------------------------------------------------------------------------------
    @unittest.SkipTest
    def test_Url(self):
        ValueType_ = Url
        cases = (
            # value,                                                    result,
            (("https://github.com/DirectiveAthena/VerSC-AthenaColor",), Url("https://www.github.com/DirectiveAthena/VerSC-AthenaColor")),
            (("github.com/DirectiveAthena/VerSC-AthenaColor",),         Url("https://www.github.com/DirectiveAthena/VerSC-AthenaColor")),
            (("www.github.com/DirectiveAthena/VerSC-AthenaColor",),     Url("https://www.github.com/DirectiveAthena/VerSC-AthenaColor")),
            (("https://github.com/",),                                  Url("https://www.github.com/")),
            (("github.com",),                                           Url("https://www.github.com/")),

        )
        self.SubtestFunction(ValueType_, cases)

        casesOperations = (
            # operation     value,              result,
            (repr,          ("github.com",),    "Url(value='https://www.github.com/')"),
            (str,           ("github.com",),    "https://www.github.com/"),
        )
        self.SubtestFunctionOperations(ValueType_, casesOperations)

        casesDunderFunctions = (
            #operation          left,                       right,              result

            # TUPLE

        )
        self.SubtestFunctionDunderFunctions(casesDunderFunctions)

        casesFail = (
            # value                  #error
            (("RAISES_ERROR",), ValueError),
            ((0,),              TypeError),
        )
        self.SubtestFunctionFails(ValueType_, casesFail)