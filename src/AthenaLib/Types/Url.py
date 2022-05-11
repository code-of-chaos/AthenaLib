# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import re

# Custom Library

# Custom Packages
from .ValueType import ValueType

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Url(ValueType):
    _value:str
    pattern=r'[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi'
    def __init__(self, value:str):
        self.url = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise TypeError
        if re.match(self.pattern, value) is None:
            raise ValueError
        self._url = value

    def __str__(self) -> str:
        return f'url("{self.url}")'
    def __repr__(self) -> str:
        return f"Url(value={self.url})"

    def __hash__(self) -> int:
        return hash(self.url)

    def __eq__(self, other: Url | str) -> bool:
        if isinstance(other, Url):
            return self.url == other.url
        elif isinstance(other, str):
            return self.url == str(other)
        else:
            raise NotImplemented

