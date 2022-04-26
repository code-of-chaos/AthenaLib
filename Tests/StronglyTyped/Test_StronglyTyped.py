# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library
from AthenaLib.StronglyTyped import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestCase_StronglyTyped(unittest.TestCase):
    def test_SingleArg(self):
        @StronglyTyped
        def a(b:str):
            return b
        self.assertEqual(a("b"), result:="b")
        self.assertEqual(a(b="b"), result)

    def test_SingleKwarg(self):
        @StronglyTyped
        def a(b:str="b"):
            return b
        self.assertEqual(a(), result:="b")
        self.assertEqual(a("b"), result)
        self.assertEqual(a(b="b"), result)

    def test_SingleKwarg_SingleArg(self):
        @StronglyTyped
        def a(b:str,c:int=0):
            return b,c
        self.assertEqual(a("b"), result:=("b", 0))
        self.assertEqual(a(b="b"), result)
        self.assertEqual(a("b",0), result)
        self.assertEqual(a("b",c=0), result)
        self.assertEqual(a(b="b",c=0), result)

    def test_MultipleArg(self):
        @StronglyTyped
        def a(b:str,c:str,d:str,e:str):
            return b,c,d,e
        self.assertEqual(a("b","c","d","e"), result:=("b","c","d","e"))
        self.assertEqual(a("b","c","d",e="e"), result)
        self.assertEqual(a("b","c",d="d",e="e"), result)
        self.assertEqual(a("b",c="c",d="d",e="e"), result)
        self.assertEqual(a(b="b",c="c",d="d",e="e"), result)

    def test_MultipleKwarg(self):
        @StronglyTyped
        def a(*,b:str="b",c:str="c",d:str="d",e:str="e"):
            return b,c,d,e
        self.assertEqual(a(b="b",c="c",d="d",e="e"), result:=("b","c","d","e"))

    def test_Fail(self):
        @StronglyTyped
        def function(a:str, b:int, c:str|None=None):
            return a,b,c

        with self.assertRaises(StrongError):
            function("a","b","c")
        with self.assertRaises(StrongError):
            function("a",0,0)
        with self.assertRaises(StrongError):
            function(0,"a",None)