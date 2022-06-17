# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect
from typing import Callable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def get_class_from_bound_method(meth) -> None|type:
    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
            if meth.__name__ in cls.__dict__:
                return cls
    return None

def get_class_from_unbound_method(meth) -> None|type:
    if inspect.isfunction(meth):
        return getattr(
            inspect.getmodule(meth),
            meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
            None
        )
    return None

def get_class_from_method(meth) -> None|type:
    if (unbound_method := get_class_from_bound_method(meth)) is not None:
        return unbound_method
    # the function below already either returns a None value or the class
    return get_class_from_unbound_method(meth)
