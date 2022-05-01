# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library
from AthenaLib.Fixes.SubscriptedGeneric import fix_SubscriptedGeneric, fix_SubscriptedGeneric_Full

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_General(self):
        annotations_fixed = tuple(fix_SubscriptedGeneric(a) for a in (str,int,list[str]))
        self.assertEqual(
            annotations_fixed,
            (str,int,list)
        )

    def test_WithUnion(self):
        annotations_fixed = tuple(fix_SubscriptedGeneric(a) for a in (str|int,list[str]))
        self.assertEqual(
            annotations_fixed,
            (str|int,list)
        )

    def test_SubscriptedWithUnion(self):
        annotations_fixed = tuple(fix_SubscriptedGeneric(a) for a in (str|int,list[str]|tuple[str]))
        self.assertEqual(
            annotations_fixed,
            (str|int,list|tuple)
        )

    def test_full(self):
        self.assertEqual(
            fix_SubscriptedGeneric_Full((str|int,list[str]|tuple[str])),
            (str | int, list | tuple)
        )

    def test_fullDict(self):
        self.assertEqual(
            fix_SubscriptedGeneric_Full({
                "alpha":str|int,
                "beta": list[str]|tuple[str],
                "gamme": bool|tuple[bool]
            }),
            {
                "alpha": str | int,
                "beta": list | tuple,
                "gamme": bool | tuple
            }
        )