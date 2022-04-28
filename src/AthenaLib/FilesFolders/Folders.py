# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os
from typing import Iterable
import shutil

# Custom Library

# Custom Packages
from AthenaLib.StrictAnnotated.StrictAnnotated import StrictAnnotated
from .Paths import path_combine,PathTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def folder_exists(folder_path:PathTypes, fatal:bool=False) -> bool:
    if not (exsists:=os.path.isdir(folder_path)) and fatal:
        raise FileNotFoundError
    return exsists

@StrictAnnotated
def folder_existsNot(folder_path:PathTypes, fatal:bool=False) -> bool:
    if (exsists:=os.path.isdir(folder_path)) and fatal:
        raise FileExistsError
    return not exsists

@StrictAnnotated
def folder_content(folder_path:PathTypes, fullpaths:bool=False) -> set:
    return set(
        path_combine(folder_path, f, Cwd=fullpaths)
        for f in os.listdir(folder_path)
    )

@StrictAnnotated
def folder_content_folders(folder_path:PathTypes, fullpaths:bool=False) -> set:
    return set(f for f in folder_content(folder_path, fullpaths=fullpaths) if os.path.isdir(f))

@StrictAnnotated
def folder_content_files(folder_path:PathTypes, fullpaths:bool=False) -> set:
    return set(f for f in folder_content(folder_path, fullpaths=fullpaths) if os.path.isfile(f))

@StrictAnnotated
def folder_content_files_extensions(folder_path:PathTypes, extension:str|Iterable[str], fullpaths:bool=False) -> set:
    return set(
        f
        for f in folder_content_files(folder_path, fullpaths=fullpaths)
        if f.split('.')[-1] in [
            ext.replace(".", "")
            for ext in (
                [extension] if isinstance(extension, str) else extension
    )])

@StrictAnnotated
def folder_move(folder_path_start:PathTypes,folder_path_end:PathTypes, fatal:bool=True, content=False) -> None:
    folder_exists(folder_path_start, fatal)
    folder_existsNot(folder_path_end, fatal)

    if content:
        shutil.copytree(folder_path_start, folder_path_end)
    else:
        os.rename(folder_path_start,folder_path_end)

@StrictAnnotated
def folder_content_walk(folder_path:PathTypes, Cwd:bool=False, topdown:bool=False) -> set:
    return {
        path_combine(dir_path, file_name, Cwd=Cwd)
        for dir_path, _, file_names in os.walk(folder_path,topdown=topdown)
            for file_name in file_names
    }
