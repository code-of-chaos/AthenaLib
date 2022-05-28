# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import shutil
from dataclasses import dataclass
from pathlib import Path

# Custom Library

# Custom Packages
from AthenaLib.FileFolderManipulation.Paths import PATH_TYPES

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class FileManipulation:
    fatal:bool = False

    # ----------------------------------------------------------------------------------------------------------------------
    # - Checks -
    # ----------------------------------------------------------------------------------------------------------------------
    def exists(self, path:PATH_TYPES) -> bool:
        if not (exsists:=os.path.isfile(path)) and self.fatal:
            raise FileNotFoundError
        return exsists

    def exists_not(self, path:PATH_TYPES) -> bool:
        if (exsists:=os.path.isfile(path)) and self.fatal:
            raise FileNotFoundError
        return exsists

    # ----------------------------------------------------------------------------------------------------------------------
    # - Operations -
    # ----------------------------------------------------------------------------------------------------------------------
    def move(self, path_original:PATH_TYPES, path_result:PATH_TYPES):
        self.exists(path_original)
        self.exists_not(path_result)
        shutil.copy2(path_original,path_result)



