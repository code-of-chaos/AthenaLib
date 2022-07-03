# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy
from dataclasses import dataclass,field

# Custom Library

# Custom Packages
from AthenaLib.functions.string import enclose_double_quote

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False)
class HTMLElement:
    name:str

    # all possible attributes
    classes:list[str]=field(default_factory=list)
    id:str=False
    href:str=False
    img:str=False
    width:str|int=False
    height:str|int=False
    alt:str=False
    style:str=False
    lang:str=False
    title:str=False

    # ------------------------------------------------------------------------------------------------------------------
    # - Casting -
    # ------------------------------------------------------------------------------------------------------------------
    def _to_tag_generator(self) -> str:
        yield self.name # always yield an element name
        if self.classes:
            yield f"class={enclose_double_quote(' '.join(self.classes))}"

        for attr_name, attr_value in self.__dict__.items():
            if attr_value and attr_name not in ("name", "classes"):
                yield f"{attr_name}={enclose_double_quote(attr_value)}"


    def to_tag(self) -> str:
        # because every element in segments is truthy, we can just skip False statements
        return f"<{' '.join(self._to_tag_generator())}>"

    def to_tag_end(self) -> str:
        return f"</{self.name}>"

    def to_dict(self) -> dict:
        return copy.copy(self.__dict__)

    # ------------------------------------------------------------------------------------------------------------------
    # - Special methods -
    # ------------------------------------------------------------------------------------------------------------------
    def wrap(self, *text:str|HTMLElement, sep="", **_) -> str:
        return f"{self.to_tag()}{sep.join(text)}{self.to_tag_end()}"

    def __call__(self, *args, **kwargs):
        # because of Pycharm and dataclass not working together:
        #   noinspection PyArgumentList
        new_obj = type(self)(
            name=self.name,
            **{k:v for k,v in kwargs.items() if k in self.__dict__.keys()}
        )
        return new_obj.wrap(*args, **kwargs)
