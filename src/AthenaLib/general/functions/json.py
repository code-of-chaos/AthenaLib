# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json
import dataclasses

# Custom Library
from AthenaLib.constants.types import PATHLIKE

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def load_jsonfile(filepath:PATHLIKE) -> dict:
    with open(filepath, "r") as file:
        return json.load(file)

def dump_dataclass_to_jsonfile(obj:dataclasses.dataclass, filepath:PATHLIKE, **json_kwargs):
    with open(filepath, "w+") as file:
        json.dump(
            obj=dataclasses.asdict(obj),
            fp=file,
            **json_kwargs
        )