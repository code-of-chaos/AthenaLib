# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect
import itertools
from typing import Callable,get_type_hints

# Custom Library

# Custom Packages
from AthenaLib.Fixes.SubscriptedGeneric import fix_SubscriptedGeneric_Full

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "StrictAnnotated", "StrictAnnotatedMethod", "StrictError"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class StrictError(TypeError):
    pass

def _PrepFunction(fnc:Callable) -> tuple[inspect.FullArgSpec,list[str], dict,int]:
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec: inspect.FullArgSpec = inspect.getfullargspec(fnc)
    fncspec_args = [a for a in fncspec.args if a != 'self']

    if fncspec.varargs is not None:
        fncspec_args.append(fncspec.varargs)

    # Fix any Subscripted Generics so only the base type is checked
    annotation = fix_SubscriptedGeneric_Full(get_type_hints(fnc))
    for a in fncspec.args:
        if a not in annotation:
            annotation[a] = object

    return fncspec,fncspec_args, annotation,len(fncspec_args)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def StrictAnnotated(fnc):
    # Prepare and extract all information from function
    fncspec,fncspec_args,annotation,len_fncspec_args = _PrepFunction(fnc)

    if list(fncspec.annotations.keys()) == ['return']:
        def wrapper(*args, **kwargs):
            if not isinstance(result := fnc(*args, **kwargs), annotation["return"]):
                raise StrictError
            return result

    elif fncspec.annotations and "return" not in annotation:
        def wrapper(*args, **kwargs):
            for i in range(len_fncspec_args):
                if not isinstance(args[i], annotation[fncspec_args[i]]):
                    raise StrictError
            for k in kwargs:
                if not isinstance(kwargs[k], annotation[k]):
                    raise StrictError
            return fnc(*args, **kwargs)

    elif fncspec.annotations:
        def wrapper(*args, **kwargs):
            for i in range(len_fncspec_args):
                if not isinstance(args[i], annotation[fncspec_args[i]]):
                    raise StrictError
            for k in kwargs:
                if not isinstance(kwargs[k], annotation[k]):
                    raise StrictError

            if not isinstance(result:=fnc(*args, **kwargs), annotation["return"]):
                raise StrictError
            return result

    else:
        def wrapper(*args, **kwargs):
            return fnc(*args, **kwargs)

    return wrapper

def StrictAnnotatedMethod(fnc):
    # Prepare and extract all information from function
    fncspec,fncspec_args,annotation,len_fncspec_args = _PrepFunction(fnc)

    if list(fncspec.annotations.keys()) == ['return']:
        def wrapper(self,*args, **kwargs):
            if not isinstance(result := fnc(self,*args, **kwargs), annotation["return"]):
                raise StrictError
            return result

    elif fncspec.annotations and "return" not in annotation:
        def wrapper(self,*args, **kwargs):
            for i in range(len_fncspec_args):
                if not isinstance(args[i], annotation[fncspec_args[i]]):
                    raise StrictError
            for k in kwargs:
                if not isinstance(kwargs[k], annotation[k]):
                    raise StrictError
            return fnc(self,*args, **kwargs)

    elif fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            for i in range(len_fncspec_args):
                if not isinstance(args[i], annotation[fncspec_args[i]]):
                    raise StrictError
            for k in kwargs:
                if not isinstance(kwargs[k], annotation[k]):
                    raise StrictError

            if not isinstance(result:=fnc(self,*args, **kwargs), annotation["return"]):
                raise StrictError
            return result

    else:
        def wrapper(self,*args, **kwargs):
            return fnc(self,*args, **kwargs)

    return wrapper