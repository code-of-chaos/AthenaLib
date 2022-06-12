# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library

# Custom Packages
from AthenaLib.functions.Split.Split import split_evenly, SplitError
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_SplitEvently_Segments2(self):
        self.assertTupleEqual(
            split_evenly([0,1,2,3,4,5,6,7],segments=2),
            ([0,1,2,3],[4,5,6,7])
        )
        self.assertTupleEqual(
            split_evenly({0, 1, 2, 3, 4, 5, 6, 7},segments=2),
            ({0, 1, 2, 3}, {4, 5, 6, 7})
        )
        self.assertTupleEqual(
            split_evenly((0,1,2,3,4,5,6,7),segments=2),
            ((0,1,2,3),(4,5,6,7))
        )
        self.assertTupleEqual(
            split_evenly({"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,},segments=2),
            ({"0":0,"1":1,"2":2,"3":3}, {"4":4,"5":5,"6":6,"7":7})
        )
    def test_SplitEvently_Segments3(self):
        self.assertTupleEqual(
            split_evenly([0,1,2,3,4,5,6,7],segments=3),
            ([0,1,2],[3,4,5],[6,7])
        )
        self.assertTupleEqual(
            split_evenly({0, 1, 2, 3, 4, 5, 6, 7},segments=3),
            ({0, 1, 2}, {3, 4, 5}, {6, 7})
        )
        self.assertTupleEqual(
            split_evenly((0,1,2,3,4,5,6,7),segments=3),
            ((0,1,2),(3,4,5),(6,7))
        )
        self.assertTupleEqual(
            split_evenly({"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,},segments=3),
            ({"0":0,"1":1,"2":2},{"3":3,"4":4,"5":5},{"6":6,"7":7})
        )
    def test_SplitEvently_Segments7(self):
        self.assertTupleEqual(
            split_evenly([*range(64)],segments=7),
            (
                [*range(0,10)],
                [*range(10,20)],
                [*range(20,30)],
                [*range(30,40)],
                [*range(40,50)],
                [*range(50,60)],
                [*range(60,64)],
            )
        )
        self.assertTupleEqual(
            split_evenly({*range(64)}, segments=7),
            (
                {*range(0, 10)},
                {*range(10, 20)},
                {*range(20, 30)},
                {*range(30, 40)},
                {*range(40, 50)},
                {*range(50, 60)},
                {*range(60, 64)},
            )
        )
        self.assertTupleEqual(
            split_evenly((*range(64),), segments=7),
            (
                (*range(0, 10),),
                (*range(10, 20),),
                (*range(20, 30),),
                (*range(30, 40),),
                (*range(40, 50),),
                (*range(50, 60),),
                (*range(60, 64),),
            )
        )
        self.assertTupleEqual(
            split_evenly({str(i):i for i in range(64)},segments=7),
            (
                {str(i):i for i in range(0, 10)},
                {str(i):i for i in range(10, 20)},
                {str(i):i for i in range(20, 30)},
                {str(i):i for i in range(30, 40)},
                {str(i):i for i in range(40, 50)},
                {str(i):i for i in range(50, 60)},
                {str(i):i for i in range(60, 64)},
            )
        )

    def test_SplitEvently_Fail(self):
        with self.assertRaises(NotImplementedError):
            split_evenly("Andreas Sas made this", segments=2)

        with self.assertRaises(SplitError):
            split_evenly({*range(1)}, segments=2)