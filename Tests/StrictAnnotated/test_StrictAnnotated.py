# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library
from AthenaLib.StrictAnnotated import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def alpha(a:str):
    return a

@StrictAnnotated
def beta(a:str, b:int=1):
    return a, b

@StrictAnnotated
def gamma(a:str, b, c:list):
    return a, b,c


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_Args(self):
        self.assertEqual(alpha( "b"),"b")
        self.assertEqual(beta(  "b"),("b",1))
        self.assertEqual(gamma( "b","a", []),("b","a",[]))
        self.assertEqual(gamma( "b",2, []),("b",2,[]))

    def test_Kwargs(self):
        self.assertEqual(alpha( a="b"),"b")
        self.assertEqual(beta(  a="b"),("b",1))
        self.assertEqual(gamma( a="b",b="a", c=[]),("b","a",[]))
        self.assertEqual(gamma( a="b",b=2, c=[]),("b",2,[]))

    def test_ArgsAndKwargs(self):
        self.assertEqual(alpha( a="b"),"b")
        self.assertEqual(beta(  "b"),("b",1))
        self.assertEqual(gamma( "b","a", c=[]),("b","a",[]))
        self.assertEqual(gamma( "b",b=2, c=[]),("b",2,[]))