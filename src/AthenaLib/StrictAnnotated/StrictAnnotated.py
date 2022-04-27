# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import inspect
from typing import Callable

# Custom Library

# Custom Packages
from AthenaLib.Fixes.SubscriptedGeneric import fix_SubscriptedGeneric, fix_SubscriptedGeneric_Full

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

_ErrorMsg= lambda val, t: f"'{val}' was not the same type as the expected Strongly typed: '{t}'"

def _TypeChecker(CombinedInput,annotations):
    for k, v in CombinedInput:
        if k in annotations:
            if not isinstance(v, annotations[k]):
                raise StrictError(_ErrorMsg(v, annotations[k]))

def _PrepFunction(fnc:Callable, method:bool=False) -> tuple[inspect.FullArgSpec,list[str], dict]:
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec: inspect.FullArgSpec = inspect.getfullargspec(fnc)
    if method:
        fncspec_args = [a for a in fncspec.args if a != 'self']
    else:
        fncspec_args = fncspec.args

    if fncspec.varargs is not None:
        fncspec_args.append(fncspec.varargs)

    # Fix any Subscripted Generics so only the base type is checked
    return fncspec,fncspec_args, fix_SubscriptedGeneric_Full(fncspec.annotations)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def StrictAnnotated(fnc):
    # Prepare and extract all information from function
    fncspec,fncspec_args,annotations = _PrepFunction(fnc)

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotations=annotations)
            _TypeChecker(CombinedInput=kwargs.items(), annotations=annotations)

            # noinspection PyTypeHints
            if not isinstance(result := fnc(*args, **kwargs),annotations["return"]):
                raise StrictError(_ErrorMsg(result, fncspec.annotations["return"]))
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

def StrictAnnotatedMethod(fnc):
    # Prepare and extract all information from method
    fncspec,fncspec_args,annotations = _PrepFunction(fnc)

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), annotations=annotations)
            _TypeChecker(CombinedInput=kwargs.items(), annotations=annotations)
            # noinspection PyTypeHints
            if not isinstance(result := fnc(self,*args, **kwargs),annotations["return"]):
                raise StrictError(_ErrorMsg(result, fncspec.annotations["return"]))
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