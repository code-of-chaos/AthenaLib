# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os

# Custom Library

# Custom Packages
from AthenaLib.StrictAnnotated.StrictAnnotated import StrictAnnotated
from .Paths import PathTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def FileExist(file_path:PathTypes, fatal:bool=False) -> bool:
    if not (exsists:=os.path.isfile(file_path)) and fatal:
        raise FileNotFoundError
    return exsists

@StrictAnnotated
def FileExistNot(file_path:PathTypes, fatal:bool=False) -> bool:
    if (exsists:=os.path.isfile(file_path)) and fatal:
        raise FileExistsError
    return not exsists
