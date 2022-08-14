# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def gather_all_filepaths(directory:str, *,extensions:set[str]|None=None, skip_folders:set[str]|None=None) -> list[str]:
    # assign mutable variables
    if extensions is None:
        extensions = set()
    if skip_folders is None:
        skip_folders = set()

    # go over all files and store paths if they are within the given boundaries
    all_filepaths:list[str] = []
    for entry in os.listdir(directory):
        if os.path.isdir(fullPath := os.path.join(directory, entry)) and fullPath not in skip_folders:
            all_filepaths.extend(gather_all_filepaths(fullPath, extensions=extensions, skip_folders=skip_folders))
        else:
            all_filepaths.append(fullPath)

    # go over the list once more if extensions is enabled
    if extensions:
        return [
            filepath
            for filepath in all_filepaths
            if filepath.split(".")[-1] in extensions
        ]
    else:
        return all_filepaths
