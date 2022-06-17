# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.functions import *

# Custom Packages
from Tests.test_structure import TestStructure

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class A:
    def a(self):
        pass
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestClassFromMethod(TestStructure):
    def test_get_class_from_bound_method(self):
        print(
            class_from_method.get_class_from_bound_method(A().a)
        )
    def test_get_class_from_unbound_method(self):
        print(
            class_from_method.get_class_from_unbound_method(A.a)
        )
    def test_test_get_class_from_method(self):
        print(
            class_from_method.get_class_from_method(A().a)
        )
        print(
            class_from_method.get_class_from_method(A.a)
        )