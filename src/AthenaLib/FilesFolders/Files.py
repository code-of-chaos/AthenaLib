# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os

# Custom Library

# Custom Packages
from AthenaLib.StronglyTyped.StronglyTyped import StronglyTyped
from .Paths import PathTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StronglyTyped
def FileExist(file_path:PathTypes, fatal:bool=False) -> bool:
    if not (exsists:=os.path.isfile(file_path)) and fatal:
        raise FileNotFoundError
    return exsists

@StronglyTyped
def FileExistNot(file_path:PathTypes, fatal:bool=False) -> bool:
    if (exsists:=os.path.isfile(file_path)) and fatal:
        raise FileExistsError
    return not exsists
