# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os
import shutil

# Custom Library

# Custom Packages
from AthenaLib.StrictAnnotated.StrictAnnotated import StrictAnnotated
from .Paths import PathTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def file_exists(file_path:PathTypes, fatal:bool=False) -> bool:
    if not (exsists:=os.path.isfile(file_path)) and fatal:
        raise FileNotFoundError
    return exsists

@StrictAnnotated
def file_existsNot(file_path:PathTypes, fatal:bool=False) -> bool:
    if (exsists:=os.path.isfile(file_path)) and fatal:
        raise FileExistsError
    return not exsists

@StrictAnnotated
def file_move(file_path_start:PathTypes,file_path_end:PathTypes, fatal:bool=True) -> None:
    file_exists(file_path_start, fatal)
    file_existsNot(file_path_end, fatal)

    shutil.copy2(file_path_start,file_path_end)
