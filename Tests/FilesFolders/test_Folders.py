# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest
import os

# Custom Library

# Custom Packages
from AthenaLib.FilesFolders.Folders import (
    folder_content, folder_content_folders, folder_content_files, folder_exists, folder_content_files_extensions,
    folder_existsNot, folder_content_walk
)


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_FolderContent(self):
        self.assertEqual(folder_content("Data"), {"Data\\test", "Data\\test.txt"})

    def test_FolderContent_Fullpaths(self):
        self.assertEqual(
            folder_content("Data", fullpaths=True),
            {f'{os.getcwd()}\\Data\\test',
             f'{os.getcwd()}\\Data\\test.txt'}
        )

    def test_FolderContentFolders(self):
        self.assertEqual(folder_content_folders("Data"), {"Data\\test"})

    def test_FolderContentFolders_Fullpaths(self):
        self.assertEqual(folder_content_folders("Data", fullpaths=True), {f'{os.getcwd()}\\Data\\test'})

    def test_FolderContentFiles(self):
        self.assertEqual(folder_content_files("Data"), {"Data\\test.txt"})

    def test_FolderContentFiles_Fullpaths(self):
        self.assertEqual(folder_content_files("Data", fullpaths=True), {f'{os.getcwd()}\\Data\\test.txt'})

    def test_FolderExsists(self):
        self.assertFalse(folder_exists("DoesNotExsist"))
        self.assertTrue(folder_exists("Data"))
        with self.assertRaises(FileNotFoundError):
            self.assertFalse(folder_exists("DoesNotExsist", fatal=True))

    def test_FolderExsistsNot(self):
        self.assertFalse(folder_existsNot("Data"))
        self.assertTrue(folder_existsNot("DoesNotExsist"))
        with self.assertRaises(FileExistsError):
            self.assertFalse(folder_existsNot("Data", fatal=True))

    def test_FolderContentFiles_Extensions(self):
        self.assertEqual(
            folder_content_files_extensions("Data", extension=['.txt']),
            {r'Data\test.txt'}
        )
        self.assertEqual(
            folder_content_files_extensions("Data", extension='.txt'),
            {r'Data\test.txt'}
        )
        self.assertEqual(
            folder_content_files_extensions("Data", extension=['.txt'], fullpaths=True),
            {fr'{os.getcwd()}\Data\test.txt'}
        )
        self.assertEqual(
            folder_content_files_extensions("Data", extension='.txt', fullpaths=True),
            {fr'{os.getcwd()}\Data\test.txt'}
        )

    def test_FolderContentWalk(self):
        self.assertSetEqual(
            folder_content_walk("Data"),
            {r"Data\test.txt"}
        )
