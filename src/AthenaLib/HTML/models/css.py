# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
from dataclasses import dataclass

# Custom Library
from AthenaColor import HEX, RGB, RGBA

# Custom Packages
from AthenaLib.HTML.models.html import HTMLElement
from AthenaLib.HTML.data.css_selection_type import CSSSelectionType
from AthenaLib.data.text import NEW_LINE,NOTHING

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, unsafe_hash=True)
class CSSProperty:
    name:str
    value:Any

    def __str__(self) -> str:
        # proper parsing of values which inherit from AthenaLib components
        match self.value:
            case HEX():
                value = f"#{self.value}"
            case RGB(r=r,g=g,b=b):
                value = f"rgb({r},{g},{b})"
            case RGBA(r=r,g=g,b=b, a=a):
                value = f"rgba({r},{g},{b},{a})"
            case _:
                value = str(self.value)

        return f"{self.name}: {value};"

@dataclass(slots=True, unsafe_hash=True, init=False)
class CSSSelection:
    selectors:tuple[HTMLElement,...]
    type:CSSSelectionType=CSSSelectionType.default

    def __init__(self, *selectors:HTMLElement, selector_type:CSSSelectionType=CSSSelectionType.default):
        self.selectors = selectors
        self.type = selector_type

    def __str__(self) -> str:
        return self.type.value.join(s.to_css_selector() for s in self.selectors)

@dataclass(slots=True, unsafe_hash=True, init=False)
class CSSRule:
    selections: tuple[CSSSelection,...]
    properties: tuple[CSSProperty,...]
    force_one_line:bool=False

    def __init__(
            self,
            selections:tuple[CSSSelection,...]|CSSSelection,
            properties:tuple[CSSProperty,...]|CSSProperty,
            force_one_line:bool=False
    ):
        self.selections = (selections,) if isinstance(selections, CSSSelection) else selections
        self.properties = (properties,) if isinstance(properties, CSSProperty) else properties
        self.force_one_line = force_one_line

    def to_text(self,*,indent:bool=True, indentation:int=4) -> str:
        new_line = NEW_LINE if indent else NOTHING
        indent_str = f'{NEW_LINE}{" " * indentation}'

        if self.force_one_line or not indent:
            properties = f'{indent_str.join(str(p) for p in self.properties)} '
            selections = ",".join(str(s) for s in self.selections)
        else:
            properties = f'{indent_str}{indent_str.join(str(p) for p in self.properties)}{new_line}'
            selections = f'{f",{new_line}".join(str(s) for s in self.selections)}'
        return f"{selections} {{{properties}}}"

    def __str__(self) -> str:
        return self.to_text(indent=True, indentation=4)

@dataclass(slots=True, unsafe_hash=True)
class CSSComment:
    text:str
    def __str__(self) -> str:
        return f"/* {self.text} */"