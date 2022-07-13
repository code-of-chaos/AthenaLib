# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def slice_into_steps(source:str, step:int):
    for s in (source[i::step] for i in range(step)):
        yield s

def slice_into_equal_lengths(source:str, length:int):
    for i in range(0, len(source), length):
        yield source[i:i+length]
