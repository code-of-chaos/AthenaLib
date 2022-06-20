# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, unsafe_hash=True, eq=True)
class Version:
    """
    A class to hold a standardized version format.
    """
    major: int|str
    minor: int|str
    fix: int|str

    def to_str(self, sep:str=".") -> str:
        """Returns the full version in string format"""
        return sep.join((str(self.major), str(self.minor), str(self.fix)))

    def to_dict(self, *, major_str:str="Major", minor_str:str="Minor", fix_str:str="Fix") -> dict:
        return {
            major_str:self.major,
            minor_str:self.minor,
            fix_str:self.fix
        }

    def __str__(self):
        return self.to_str()