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
@StrictAnnotated_Full
def alpha(a:list[tuple[str,str],tuple[int]]):
    return a

@StrictAnnotated_Full
def beta(a:list[list[list[str,int]],list[str|int]]):
    return a

@StrictAnnotated_Full
def gamma(c:list[list[list[str]]]):
    return c


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@unittest.SkipTest
class Test(unittest.TestCase):
    def test_Args(self):
        with self.assertRaises(StrictError):
            gamma([[["a", 1]]])
        with self.assertRaises(StrictError):
            beta([[["a","a"]],["a"]])

        self.assertEqual(beta([[["a",1]],["a"]]), [[["a",1]],["a"]])
        self.assertEqual(beta([[["a",1]],[1]]), [[["a",1]],[1]])

        alpha([(1,)])
        with self.assertRaises(StrictError):
            alpha([([],)])