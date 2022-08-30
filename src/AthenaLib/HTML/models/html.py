# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy
from typing import Any

# Custom Library

# Custom Packages
from AthenaLib.functions.string import enclose_double_quote
from AthenaLib.functions.type_check import type_check_error
from AthenaLib.decorators.dataclass import dataclass

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class HTMLElement:
    """
    A bare HTML element. This is a base class to be used to define already establish HTML elements or create a totally
    new named elements.

    Parameters:
    - name:str -> HTML element name, like "p"/ "span"/ ...
    - *wrap:list[HTMLElement|str|int|...] -> other objects the element wraps.
    - accesskey:str
    - classes:tuple[str]
    - contenteditable:str
    - dir:str
    - draggable:str
    - hidden:str
    - id:str
    - lang: str
    - spellcheck:str
    - style:str
    - tabindex:str
    - title:str
    - translate:str
    """
    name:str
    wraps:tuple[HTMLElement|str|int|...]

    # default attributes
    accesskey:str
    classes:tuple[str,...]
    contenteditable:str
    dir:str
    draggable:str
    hidden:str
    id:str
    lang: str
    spellcheck:str
    style:str
    tabindex:str
    title:str
    translate:str


    def __init__(
            self,
            *wrap:Any,
            name:str=False,
            access_key:str=False,
            classes:tuple[str,...]|str=False,
            content_editable:str=False,
            direction:str=False,
            draggable:str=False,
            hidden:str=False,
            id_str:str=False,
            lang:str=False,
            spellcheck:str=False,
            style:str=False,
            tabindex:int=False,
            title:str=False,
            translate:str=False,
        ):
        self.name = type_check_error(name, str) if name else False
        self.wraps = wrap

        # all below can have a truthy FALSE value
        self.accesskey = type_check_error(access_key, str) if access_key else False
        if isinstance(classes, str):
            self.classes = (classes,) if classes else False
        elif isinstance(classes, tuple):
            self.classes = tuple(cls for cls in classes if cls) if classes else False
        else:
            self.classes = type_check_error(classes, tuple|str) if classes else False
        self.contenteditable = type_check_error(content_editable, str) if content_editable else False
        self.dir = type_check_error(direction, str) if direction else False
        self.draggable = type_check_error(draggable, str) if draggable else False
        self.hidden = type_check_error(hidden, str) if hidden else False
        self.id = type_check_error(id_str, str) if id_str else False
        self.lang = type_check_error(lang, str) if lang else False
        self.spellcheck = type_check_error(spellcheck, str) if spellcheck else False
        self.style = type_check_error(style, str) if style else False
        self.tabindex = type_check_error(tabindex, int|str) if tabindex else False
        self.title = type_check_error(title, str) if title else False
        self.translate = type_check_error(translate, str) if translate else False


    # ------------------------------------------------------------------------------------------------------------------
    # - Casting -
    # ------------------------------------------------------------------------------------------------------------------
    def _to_tag_generator(self) -> str:
        if not self.name:
            raise ValueError("no name was set for the tag")
        yield self.name # always yield an element name
        if self.classes:
            yield f"class={enclose_double_quote(' '.join(self.classes))}"

        for attr_name, attr_value in self.__dict__.items():
            # skip any attributes which should not be present in the tag of the element
            if attr_value and attr_name not in ("name", "classes", "wraps"):
                yield f"{attr_name}={enclose_double_quote(attr_value)}"

    def to_tag(self) -> str:
        """Returns the start tag of the HTML element with all correctly defined attributes"""
        # because every element in segments is truthy, we can just skip False statements
        return f"<{' '.join(self._to_tag_generator())}>"

    def to_tag_end(self) -> str:
        if not self.name:
            raise ValueError("no name was set for the tag")
        """Returns the end tag of the HTML element"""
        return f"</{self.name}>"

    def to_dict(self) -> dict:
        """Returns a copy of the object's attributes"""
        return copy.copy(self.__dict__)

    def to_css_selector(self, full:bool=False) -> str:
        classes = f".{'.'.join(self.classes)}" if self.classes else ""
        id_str = f"#{self.id}" if self.id else ""

        attr: list[str] = []
        for attr_name, attr_value in self.__dict__.items():
            # skip any attributes which should not be present in the tag of the element
            if attr_value and attr_name not in ("name", "classes", "wraps"):
                attr.append(f"{attr_name}={enclose_double_quote(attr_value)}")

        if not full or not attr:
            return f"{self.name if self.name else ''}{classes}{id_str}"
        else:
            return f"{self.name if self.name else ''}{classes}{id_str}[{','.join(attr)}]"

    def __str__(self):
        """Returns a completely wrapped html element, meaning it has with all the content within it, and it's end tag"""
        return f"{self.to_tag()}{' '.join(str(w) for w in self.wraps)}{self.to_tag_end()}"
