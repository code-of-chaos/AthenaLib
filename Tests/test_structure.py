# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest
from typing import Any, Callable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestStructure(unittest.TestCase):
    def subtest_multiple_cases(self, *cases:tuple[Any, Callable]):
        for result, obj_creator in cases:
            with self.subTest(result=result, obj_creator=obj_creator):
                self.assertEqual(result, obj_creator())