# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library

# Custom Packages
from AthenaLib.FileFolderManipulation.Files import file_exists, file_existsNot

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_FileExsists(self):
        self.assertTrue(file_exists("Data/test.txt"))
        self.assertFalse(file_exists("Data/NotPresent.txt"))
        with self.assertRaises(FileNotFoundError):
            file_exists("Data/NotPresent.txt", fatal=True)

    def test_FileExsistsNot(self):
        self.assertTrue(file_existsNot("Data/NotPresent.txt"))
        self.assertFalse(file_existsNot("Data/test.txt"))
        with self.assertRaises(FileExistsError):
            file_existsNot("Data/test.txt", fatal=True)