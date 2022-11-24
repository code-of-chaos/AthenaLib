# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def default_or_optional(default:Any, optional:Any|None) -> Any:
    """
    Simple function that always returns `main_choice` if `optional_choice` is None.
    Otherwise, it will return `optional_choice`
    """
    return default if optional is None else optional