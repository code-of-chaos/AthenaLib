# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import pathlib

# Athena Packages
from AthenaLib.constants.types import PATHLIKE

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def path_as_pathlib(path:PATHLIKE)-> pathlib.Path:
    """
    Simple function to always return a pathlib.Path
    """
    if isinstance(path, str|bytes|os.PathLike):
        return pathlib.Path(path)
    elif isinstance(path, pathlib.Path):
        return path
    else:
        raise TypeError(f"'{path}' was not a Pathlike object (str | bytes | os.PathLike | pathlib.Path")