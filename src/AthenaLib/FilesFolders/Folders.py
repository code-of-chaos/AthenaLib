# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os
from typing import Iterable

# Custom Library

# Custom Packages
from AthenaLib.StronglyTyped.StronglyTyped import StronglyTyped
from .Paths import PathCombine,PathTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StronglyTyped
def FolderExist(folder_path:PathTypes, fatal:bool=False) -> bool:
    if not (exsists:=os.path.isdir(folder_path)) and fatal:
        raise FileNotFoundError
    return exsists

@StronglyTyped
def FolderExistNot(folder_path:PathTypes, fatal:bool=False) -> bool:
    if (exsists:=os.path.isdir(folder_path)) and fatal:
        raise FileExistsError
    return not exsists

@StronglyTyped
def FolderContent_All(folder_path:PathTypes, fullpaths:bool=False) -> set:
    return set(
        PathCombine(folder_path,f, Cwd=fullpaths)
        for f in os.listdir(folder_path)
    )

@StronglyTyped
def FolderContent_Folders(folder_path:PathTypes, fullpaths:bool=False) -> set:
    return set(f for f in FolderContent_All(folder_path, fullpaths=fullpaths) if os.path.isdir(f))

@StronglyTyped
def FolderContent_Files(folder_path:PathTypes, fullpaths:bool=False) -> set:
    return set(f for f in FolderContent_All(folder_path, fullpaths=fullpaths) if os.path.isfile(f))

@StronglyTyped
def FolderContent_Files_Extension(folder_path:PathTypes, extension:str|Iterable[str], fullpaths:bool=False) -> set:
    return set(
        f
        for f in FolderContent_Files(folder_path, fullpaths=fullpaths)
        if f.split('.')[-1] in [
            ext.replace(".", "")
            for ext in (
                [extension] if isinstance(extension, str) else extension
    )])

@StronglyTyped
def FolderMove(folder_path_start:PathTypes,folder_path_end:PathTypes, fatal:bool=True):
    FolderExist(folder_path_start, fatal)
    FolderExistNot(folder_path_end, fatal)

    os.rename(folder_path_start,folder_path_end)