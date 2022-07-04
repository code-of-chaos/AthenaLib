# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Union, Any

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def type_check_error(obj:object, types:Union[type,...]|type) -> Any:
    if not isinstance(obj, types):
        raise TypeError(f"{obj} was not of the allowed types of: {types}")
    return obj

