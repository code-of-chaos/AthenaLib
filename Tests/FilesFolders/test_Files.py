# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library

# Custom Packages
from AthenaLib.FilesFolders.Files import FileExist, FileExistNot

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_FileExsists(self):
        self.assertTrue(FileExist("Data/test.txt"))
        self.assertFalse(FileExist("Data/NotPresent.txt"))
        with self.assertRaises(FileNotFoundError):
            FileExist("Data/NotPresent.txt", fatal=True)

    def test_FileExsistsNot(self):
        self.assertTrue(FileExistNot("Data/NotPresent.txt"))
        self.assertFalse(FileExistNot("Data/test.txt"))
        with self.assertRaises(FileExistsError):
            FileExistNot("Data/test.txt", fatal=True)
