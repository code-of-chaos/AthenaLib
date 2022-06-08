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

    def to_str(self, sep=".") -> str:
        """Returns the full version in string format"""
        return f"{self.major}{sep}{self.minor}{sep}{self.fix}"

    def to_dict(self) -> dict:
        return {
            "Major":self.major,
            "Minor":self.minor,
            "Fix":self.fix
        }

    def __str__(self):
        return self.to_str()