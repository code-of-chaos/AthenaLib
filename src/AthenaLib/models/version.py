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
@dataclass()
class Version:
    major: int|str
    minor: int|str
    fix: int|str

    @classmethod
    def factory(cls) -> Version:
        return Version(
            major=0,
            minor=0,
            fix=0
        )