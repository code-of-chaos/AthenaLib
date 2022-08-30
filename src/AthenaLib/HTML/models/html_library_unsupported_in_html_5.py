# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaLib.HTML.models.html import HTMLElement
from AthenaLib.functions.type_check import type_check_error
from AthenaLib.decorators.dataclass import dataclass

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Acronym(HTMLElement):
    name="acronym"

    def __init__(self, *wraps, **kwargs):
        super(Acronym, self).__init__(*wraps,name=Acronym.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Applet(HTMLElement):
    name="applet"

    def __init__(self, *wraps, **kwargs):
        super(Applet, self).__init__(*wraps,name=Applet.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Big(HTMLElement):
    name="big"

    def __init__(self, *wraps, **kwargs):
        super(Big, self).__init__(*wraps,name=Big.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Center(HTMLElement):
    name="center"

    def __init__(self, *wraps, **kwargs):
        super(Center, self).__init__(*wraps,name=Center.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Frame(HTMLElement):
    name="frame"

    def __init__(self, *wraps, **kwargs):
        super(Frame, self).__init__(*wraps,name=Frame.name,**kwargs)

@dataclass(unsafe_hash=True, match_args=True, eq=True, order=False, init=False)
class Frameset(HTMLElement):
    name="frameset"

    def __init__(self, *wraps, **kwargs):
        super(Frameset).__init__(*wraps,name=Frameset.name,**kwargs)