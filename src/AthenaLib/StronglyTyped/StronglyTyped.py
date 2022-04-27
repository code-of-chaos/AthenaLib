# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import inspect
from types import GenericAlias, UnionType
from typing import _UnionGenericAlias,_GenericAlias

# Custom Library

# Custom Packages
from AthenaLib.Fixes.SubscriptedGenerics import Fix_SubscriptedGenerics

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "StronglyTyped", "StronglyTypedMethod", "StrongError"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
_ErrorMsg= lambda val, t: f"'{val}' was not the same type as the expected Strongly typed: '{t}'"

def _TypeChecker(CombinedInput,annotations:dict):
    for k, v in CombinedInput:
        assert isinstance(v, annotations[k]), _ErrorMsg(v, annotations[k])

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StrongError(Exception):
    pass

def StronglyTyped(fnc):
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec:inspect.FullArgSpec = inspect.getfullargspec(fnc)
    fncspec_args = fncspec.args
    if fncspec.varargs is not None:
        fncspec_args.append(fncspec.varargs)

    # Fix any Subscripted Generics so only the base type is checked
    annotations = {k:Fix_SubscriptedGenerics(v) for k,v in fncspec.annotations.items()}

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotations=annotations)
            _TypeChecker(CombinedInput=kwargs.items(), annotations=annotations)
            assert isinstance(
                result := fnc(*args, **kwargs),
                fncspec.annotations["return"]
            ), _ErrorMsg(result, fncspec.annotations["return"])
            return result

    elif fncspec.annotations:
        def wrapper(*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotations=annotations)
            _TypeChecker(CombinedInput=kwargs.items(), annotations=annotations)
            return fnc(*args, **kwargs)
    else:
        def wrapper(*args, **kwargs):
            return fnc(*args, **kwargs)
    return wrapper

def StronglyTypedMethod(fnc):
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec: inspect.FullArgSpec = inspect.getfullargspec(fnc)
    fncspec_args = [a for a in fncspec.args if a != 'self']
    if fncspec.varargs is not None:
        fncspec_args.append(fncspec.varargs)

    # Fix any Subscripted Generics so only the base type is checked
    annotations = {k:Fix_SubscriptedGenerics(v) for k,v in fncspec.annotations.items()}

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotations=annotations)
            _TypeChecker(CombinedInput=kwargs.items(), annotations=annotations)
            assert isinstance(
                result := fnc(self,*args, **kwargs),
                fncspec.annotations["return"]
            ), _ErrorMsg(result,fncspec.annotations["return"])
            return result
    elif fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotations=annotations)
            _TypeChecker(CombinedInput=kwargs.items(), annotations=annotations)
            return fnc(self,*args, **kwargs)
    else:
        def wrapper(self,*args, **kwargs):
            return fnc(self,*args, **kwargs)
    return wrapper