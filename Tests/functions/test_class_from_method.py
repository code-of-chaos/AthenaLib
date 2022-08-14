# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.functions import class_from_method

# Custom Packages
from Tests.test_structure import TestStructure

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class A:
    b_str:str
    def __init__(self):
        self.b_str = "b has been called"
    def a(self):
        pass

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestClassFromMethod(TestStructure):
    def test_get_class_from_bound_method(self):
        self.assertIs(
            A, class_from_method.get_class_from_bound_method(A().a)
        )
    def test_get_class_from_unbound_method(self):
        self.assertIs(
            A, class_from_method.get_class_from_unbound_method(A.a)
        )

    def test_get_class_from_method(self):
        self.assertIs(
            A, class_from_method.get_class_from_bound_method(A().a)
        )
        self.assertIs(
            A, class_from_method.get_class_from_unbound_method(A.a)
        )
        self.assertIs(
            A, class_from_method.get_class_from_method(A().a)
        )
        self.assertIs(
            A, class_from_method.get_class_from_method(A.a)
        )