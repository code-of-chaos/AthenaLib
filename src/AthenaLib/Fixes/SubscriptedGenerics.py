# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from types import GenericAlias, UnionType
from typing import _UnionGenericAlias,_GenericAlias

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def Fix_SubscriptedGenerics(annotation) -> type|UnionType:
    if isinstance(annotation, _UnionGenericAlias):
        for a in annotation.__args__:
            if isinstance(a, _GenericAlias):
                return a.__origin__
        return annotation
    else:
        return annotation