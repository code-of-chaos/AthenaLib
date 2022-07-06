# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
import enum
from dataclasses import dataclass

# Custom Library

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

    def __str__(self):
        return f"{self.name}: {self.value};"

@dataclass(slots=True, unsafe_hash=True)
class CSSSelection:
    selectors:tuple[HTMLElement,...]
    type:CSSSelectionType=CSSSelectionType.default

    def __str__(self):
        return self.type.value.join(s.to_css_selector() for s in self.selectors)

@dataclass(slots=True, unsafe_hash=True)
class CSSRule:
    selections: tuple[CSSSelection,...]
    properties: tuple[CSSProperty,...]

    def to_text(self,*,indent:bool=True, indentation:int=4):
        new_line = NEW_LINE if indent else NOTHING
        indent_str = f'{NEW_LINE}{" "*indentation}' if indent else NOTHING

        properties = f'{indent_str if indent else NOTHING}{indent_str.join(str(p) for p in self.properties)}{new_line}'
        selections = f'{f",{new_line if indent else NOTHING}".join(str(s) for s in self.selections)}'
        return f"{selections}{{{properties}}}"

    def __str__(self):
        return self.to_text(indent=True, indentation=4)