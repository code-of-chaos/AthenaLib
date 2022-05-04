# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .ValueType import ValueType

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Url(ValueType):
    _url:str
    def __init__(self, value:str):
        self.url = value

    @property
    def url(self):
        return

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._url = value

    def __str__(self) -> str:
        return self._url
    def __repr__(self) -> str:
        return f"<Url {self.url=}>"