# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import os

# Custom Library

# Custom Packages
from AthenaLib.StrictAnnotated.StrictAnnotated import StrictAnnotated

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
PathTypes = str | bytes | os.PathLike

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def PathCombine(*PathSegments:PathTypes, Cwd:bool=False) -> str:
    if Cwd:
        return os.path.join(os.getcwd(), *PathSegments)
    else:
        return os.path.join(*PathSegments)