# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.models.degree import Degree

# Custom Packages
from Tests.test_structure import TestStructure

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestDegree(TestStructure):
    def test_Degree(self):
        self.subtest_multiple_cases(
            ((120,),lambda : Degree(120).export()),
            (120,lambda : int(Degree(120.5))),
            (120.5,lambda : float(Degree(120.5))),
            (Degree(120), lambda: abs(Degree(-120))),
            (Degree(170), lambda: Degree(890).truncate_to_circle()),
        )