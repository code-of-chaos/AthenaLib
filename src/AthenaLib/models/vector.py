# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(unsafe_hash=True, slots=True)
class vector1D:
    x:int|float = 0.

    # todo math

@dataclass(unsafe_hash=True, slots=True)
class vector2D:
    x:int|float = 0.
    y:int|float = 0.

    # todo math

@dataclass(unsafe_hash=True, slots=True)
class vector3D:
    x:int|float = 0.
    y:int|float = 0.
    z:int|float = 0.

    # todo math