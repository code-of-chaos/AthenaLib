# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import NamedTuple

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(unsafe_hash=True, slots=True)
class Vector1D(NamedTuple):
    x:int|float = 0.

    # todo math

@dataclass(unsafe_hash=True, slots=True)
class Vector2D(NamedTuple):
    x:int|float = 0.
    y:int|float = 0.

    # todo math

@dataclass(unsafe_hash=True, slots=True)
class Vector3D(NamedTuple):
    x:int|float = 0.
    y:int|float = 0.
    z:int|float = 0.

    # todo math