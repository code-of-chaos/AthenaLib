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
def return_self_classmethod(fnc):
    """
    Decorator to make a class method return self consitently
    """
    def wrapper(self, *args, **kwargs):
        fnc(self, *args, **kwargs)
        return self
    return wrapper