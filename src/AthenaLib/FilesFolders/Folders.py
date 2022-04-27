# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os
import sys

# Custom Library

# Custom Packages
from AthenaLib.StronglyTyped.StronglyTyped import StronglyTyped
from .Paths import PathCombine

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StronglyTyped
def FolderContent_All(folder_path:str, fullpaths:bool=False) -> set:
    return set(
        PathCombine(folder_path,f, Cwd=fullpaths)
        for f in os.listdir(folder_path)
    )


@StronglyTyped
def FolderContent_Folders(folder_path:str, fullpaths:bool=False) -> set:
    return set(f for f in FolderContent_All(folder_path, fullpaths=fullpaths) if os.path.isdir(f))

@StronglyTyped
def FolderContent_Files(folder_path:str, fullpaths:bool=False) -> set:
    return set(f for f in FolderContent_All(folder_path, fullpaths=fullpaths) if os.path.isfile(f))
