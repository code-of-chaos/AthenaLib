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
class TestVectors(TestStructure):
    def test_Vector1D(self):
        self.subtest_multiple_cases(
            ((1,),lambda : Vector1D(1).export()),
        )

    def test_Vector2D(self):
        self.subtest_multiple_cases(
            ((1,2),lambda : Vector2D(1,2).export()),
        )

    def test_Vector3D(self):
        self.subtest_multiple_cases(
            ((1,2,3),lambda : Vector3D(1,2,3).export()),
        )