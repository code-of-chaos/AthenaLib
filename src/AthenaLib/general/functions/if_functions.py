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
def choice_if_None(main_choice:Any, optional_choice:Any|None) -> Any:
    """
    Simple function that always returns `main_choice` if `optional_choice` is None.
    Otherwise, it will return `optional_choice`
    """
    return main_choice if optional_choice is None else optional_choice