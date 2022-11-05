# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import pathlib
import re
import os
from typing import Generator

# Athena Packages
from AthenaLib.constants.types import PATHLIKE

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
# MAKE SURE THE PATTERN STRING IS A `r""` !!!
RE_FIND_VARS:re.Pattern = re.compile(r"""^([a-zA-Z_]+[a-zA-Z0-9_])[ =]*(["']+)([^"']*)\2""", flags=re.MULTILINE)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class DotEnv:
    """
    Simple parser to get all environment variables from a `.env` file

    ---
    - filepath: PATHLIKE ; The file to parse
    - auto_run: bool ; When True, the init function will automatically parse the env file and populate `os.environ`
    """
    filepath: pathlib.Path

    __slots__ = ("filepath",)

    def __init__(self, filepath:PATHLIKE, *, auto_run:bool=False) -> None:
        self.filepath = pathlib.Path(filepath)
        if not self.filepath.exists() or not self.filepath.is_file():
            raise FileNotFoundError(self.filepath)

        # Ease of use autorun
        if auto_run:
            self.run()

    def run(self) -> None:
        """
        Main Function of the DotEnv class
        Runs the `self.parse` and then populates `os.environ` with the data
        """
        # need to have populated the self.vars with some data,
        #   else no vars could be added to environ
        for name, value in self._parse_generator():
            if name in os.environ:
                raise ValueError(f"Duplicate environment variable name of '{name}'")

            # set them to environment
            os.environ.setdefault(name, value)

    def _parse_generator(self) -> Generator[tuple[str,str], None,None]:
        """
        Generator to output the name and value of found Environment variables with the given file
        """
        with open(self.filepath, "r") as file:
            # Because re.findall splits the output into the different match groups
            #   The name and value can easily be extracted from the tuple
            for env_name, _,env_value in RE_FIND_VARS.findall(file.read()): #type:str,_,str
                yield env_name, env_value

    def to_dict(self) -> dict:
        """
        Parses the given file
        Outputs the found variables as a dictionary
        """
        return {k:v for k,v in self._parse_generator()}

