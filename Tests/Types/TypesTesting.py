# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TypesTesting(unittest.TestCase):
    def SubtestFunction(self, ValueType_, cases):
        for value, result in cases:
            with self.subTest(value=value, result=result, ):
                self.assertEqual(ValueType_(*value), result)

    def SubtestFunctionOperations(self, ValueType_, cases):
        for operation, value, result in cases:
            with self.subTest(value=value, result=result, ):
                self.assertEqual(operation(ValueType_(*value)), result)

    def SubtestFunctionDunderFunctions(self, cases):
        for operation, left, right, result in cases:
            with self.subTest(operation=operation,left=left, right=right, result=result):
                self.assertEqual(operation(left, right), result)

    def SubtestFunctionFails(self, ValueType_, cases):
        for value, error in cases:
            with self.subTest(value=value, error=error):
                with self.assertRaises(error):
                    ValueType_(*value)