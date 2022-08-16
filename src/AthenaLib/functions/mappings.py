# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Iterable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def append_or_extend_list_to_mapping(mapping:dict, key, value):
    if key not in mapping:
        mapping[key] = [value]
    else:
        mapping[key].append(value)

def skip_keys_in_mapping(mapping:dict, skipables:set|list|Iterable) -> dict:
    """Skip certain key value pairs if the key can be found in `skipables`"""
    return {k:v for k, v in mapping.items() if k not in skipables}

def skip_values_in_mapping(mapping:dict, skipables:set|list|Iterable) -> dict:
    """Skip certain key value pairs if the value can be found in `skipables`"""
    return {k:v for k, v in mapping.items() if v not in skipables}