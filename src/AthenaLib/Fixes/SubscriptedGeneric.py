# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# noinspection PyProtectedMember
from typing import _UnionGenericAlias,_GenericAlias,GenericAlias,Union, Iterable
from types import UnionType

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------

SubscriptedGenericTypes = _UnionGenericAlias | GenericAlias | _GenericAlias | UnionType

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def fix_SubscriptedGeneric(annotation:type|SubscriptedGenericTypes) -> type:
    if isinstance(annotation, _UnionGenericAlias):
        for a in annotation.__args__:
            if isinstance(a, GenericAlias|_GenericAlias):
                return a.__origin__

    elif isinstance(annotation, GenericAlias|_GenericAlias):
        return annotation.__origin__

    elif isinstance(annotation, UnionType):
        return Union[tuple(a.__origin__ if isinstance(a, GenericAlias|_GenericAlias) else a for a in annotation.__args__)]

    return annotation

def fix_SubscriptedGeneric_Full(Iter:Iterable|dict) -> Iterable|dict:
    if isinstance(Iter, type):
        raise ValueError("A type cannot be in itself multi stripped")
    elif isinstance(Iter, dict):
        content = [(k, (fix_SubscriptedGeneric(v) if isinstance(v, SubscriptedGenericTypes) else v)) for k,v in Iter.items()]
    else:
        content = [fix_SubscriptedGeneric(i) if isinstance(i, SubscriptedGenericTypes) else i for i in Iter]
    return type(Iter)(content)