# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os

# Custom Library

# Custom Packages
from AthenaLib.StronglyTyped.StronglyTyped import StronglyTyped

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StronglyTyped
def PathCombine(*PathSegments:str, Cwd:bool=False) -> str:
    if Cwd:
        return os.path.join(os.getcwd(), *PathSegments)
    else:
        return os.path.join(*PathSegments)