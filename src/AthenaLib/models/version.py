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
@dataclass(
    slots=True
)
class Version:
    major: int|str
    minor: int|str
    fix: int|str

    def to_str(self, sep:str=".") -> str:
        """Returns the full version in string format"""
        return sep.join((self.major, self.minor, self.fix))

    def to_dict(self, *, major_str:str="Major", minor_str:str="Minor", fix_str:str="Fix") -> dict:
        return {
            major_str:self.major,
            minor_str:self.minor,
            fix_str:self.fix
        }

    def __str__(self):
        return self.to_str()