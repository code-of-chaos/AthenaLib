# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import dataclasses
from typing import Any
import json

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def cast_as_is(obj:Any):
    return obj

def cast_to_string(obj:Any) -> str:
    if dataclasses.is_dataclass(obj):
        return json.dumps({k: str(v) for k, v in dataclasses.asdict(obj).items()})

    match obj:
        case dict():
            return json.dumps(obj)
        case _:
            return str(obj)