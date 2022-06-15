# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.models import *

# Custom Packages
from Tests.test_structure import TestStructure

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestBezier(TestStructure):
    def test_CubicBezier(self):
        self.subtest_multiple_cases(
            ((1,2,1,2), lambda: CubicBezier(2,2,2,2).export()), # exports as a tuple
            (CubicBezier(1,2,1,2), lambda: CubicBezier(2,2,2,2)), # should use the __eq__ dunder
            ((1,2,1,2), lambda: (CubicBezier(1,1,1,1) + CubicBezier(1,1,1,1)).export()), # should use the __add__ dunder
            ((0,-1,0,-1), lambda: (CubicBezier(1,1,1,1) - CubicBezier(1,2,2,2)).export()),
            ([0,-1,0,-1], lambda: list(CubicBezier(1,1,1,1) - CubicBezier(1,2,2,2))),
            ((0,1,0,1), lambda: abs(CubicBezier(1,1,1,1) - CubicBezier(1,2,2,2)).export()),
        )