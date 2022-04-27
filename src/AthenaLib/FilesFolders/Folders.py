# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os
import sys
from typing import Iterable

# Custom Library

# Custom Packages
from AthenaLib.StronglyTyped.StronglyTyped import StronglyTyped
from .Paths import PathCombine

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StronglyTyped
def FolderExsist(folder_path:str, fatal:bool=False) -> bool:
    exsists = os.path.isdir(folder_path)
    if not exsists and fatal:
        raise FileNotFoundError
    return exsists

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

@StronglyTyped
def FolderContent_Files_Extension(folder_path:str, extension:str|Iterable[str], fullpaths:bool=False) -> set:
    extension = [
        ext.replace(".", "")
        for ext in (
            [extension] if isinstance(extension, str) else extension
        )
    ]
    return set(
        f
        for f in FolderContent_All(folder_path, fullpaths=fullpaths)
        if os.path.isfile(f) and f.split('.')[-1] in extension
    )

@StronglyTyped
def FolderMove(folder_path_start:str,folder_path_end:str):
    pass