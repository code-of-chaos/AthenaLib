# TODO EVERYTHING
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
#   -
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import inspect
from typing import Callable, _UnionGenericAlias, _GenericAlias, GenericAlias, Union, Any
from types import UnionType

# Custom Library

# Custom Packages
from .StrictAnnotated import StrictError, _ErrorMsg

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "StrictAnnotated_Full", "StrictAnnotatedMethod_Full"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyTypeHints
def _TypeCheckerPartial(PartialInput,annotation:dict):
    if annotation["base"] is UnionType:
        if annotation["child"] is type:
            if not isinstance(PartialInput, tuple(annotation["child"])):
                raise StrictError(_ErrorMsg(PartialInput,annotation["base"]))
        elif isinstance(annotation["child"], list) and all(c is type for c in annotation["child"]):
            if not isinstance(PartialInput, tuple(annotation["child"])):
                raise StrictError(_ErrorMsg(PartialInput,annotation["base"]))
        print(PartialInput,annotation)
    else:
        if not isinstance(PartialInput, annotation["base"]) \
            or len(PartialInput) != len(annotation["child"]):
            raise StrictError(_ErrorMsg(PartialInput,f"{annotation['base']}{annotation['child']}"))

        for i, v_ in enumerate(PartialInput):
            if isinstance(annotation["child"][i], dict):
                _TypeCheckerPartial(v_, annotation["child"][i])
            elif not isinstance(v_,annotation["child"][i]):
                raise StrictError(_ErrorMsg(v_,annotation["child"][i]))

def _TypeChecker(CombinedInput,annotations):
    for k, v in CombinedInput:
        if k in annotations:
            if annotations[k] is type:
                if not isinstance(v, annotations[k]):
                    raise StrictError(_ErrorMsg(v, annotations[k]))
            elif isinstance(annotations[k], dict):
                _TypeCheckerPartial(v, annotations[k])

def _TypeFinder(t:_UnionGenericAlias|_GenericAlias|GenericAlias|Union[Any])-> dict:
    # Uses recursive function to go through the entire thing
    if isinstance(t, _UnionGenericAlias|UnionType):
        found = UnionType
    elif isinstance(t, GenericAlias | _GenericAlias):
        found = t.__origin__
    else:
        return t

    return {
        "base": found,
        "child": [_TypeFinder(t_) for t_ in t.__args__]
    }

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

    # Every nested Subscripted Generic is checked
    return fncspec,fncspec_args, {k:_TypeFinder(v) for k,v in fncspec.annotations.items()}

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def StrictAnnotated_Full(fnc):
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

def StrictAnnotatedMethod_Full(fnc):
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