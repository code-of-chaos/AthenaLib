# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Class -
# ----------------------------------------------------------------------------------------------------------------------
class Singleton:
    """
    A class which inherits from this class, will only be able to be created once in the run.
    This means, if a user tries to call a new instance of the class, it will simply return the first created class.
    """
    def __new__(cls, *args,**kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls).__init__(*args,**kwargs)
        return cls._instance