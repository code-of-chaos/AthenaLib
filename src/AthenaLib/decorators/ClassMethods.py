# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import asyncio
import copy

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def return_self_classmethod(fnc):
    """
    Decorator to make a class method return self consitently
    """
    def wrapper(*args, **kwargs):
        self, *args_ = args
        fnc(self, *args_, **kwargs)
        return self
    return wrapper

def return_copy_classmethod(fnc):
    """
    Decorator to make a class method return a copy of itself
    """
    def wrapper(*args, **kwargs):
        self, *args_ = args
        fnc(self, *args_, **kwargs)
        return copy.deepcopy(self)
    return wrapper

def use_copy_classmethod(fnc):
    """
    Decorator to make a class method use a copy of itself and return the copy
    """
    def wrapper(self, *args, **kwargs):
        new_self = copy.deepcopy(self)
        return fnc(new_self, *args, **kwargs)
    return wrapper
