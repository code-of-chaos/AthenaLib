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
    _value:str
    def __init__(self, value:str):
        self.url = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise TypeError
        # todo write some magic function to check urls
        self._url = value

    def __str__(self) -> str:
        return f'url("{self.url}")'
    def __repr__(self) -> str:
        return f"Url(value={self.url})"

    def __eq__(self, other: Url | str) -> bool:
        if isinstance(other, Url):
            return self.url == other.url
        elif isinstance(other, str):
            return self.url == str(other)
        else:
            raise NotImplemented

