# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import datetime
import json
import dataclasses
from typing import Any

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

class GeneralCustomJsonEncoder(json.JSONEncoder):
    """
    Encodes objects like datetime.datetime(), ...
    """
    def default(self, o) -> str|int|bool|dict|list:
        match o:
            case datetime.datetime():
                return o.isoformat()

            case _:
                return super(GeneralCustomJsonEncoder, self).default(o)