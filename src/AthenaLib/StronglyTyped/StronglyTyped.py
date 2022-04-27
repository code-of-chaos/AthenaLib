# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import inspect

# Custom Library

# Custom Packages

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

def _TypeChecker(CombinedInput,fncspec:inspect.FullArgSpec):
    for k, v in CombinedInput:
        assert isinstance(v, fncspec.annotations[k]), _ErrorMsg(v, fncspec.annotations[k])

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

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), fncspec=fncspec)
            _TypeChecker(CombinedInput=kwargs.items(), fncspec=fncspec)
            assert isinstance(
                result := fnc(*args, **kwargs),
                fncspec.annotations["return"]
            ), _ErrorMsg(result, fncspec.annotations["return"])
            return result

    elif fncspec.annotations:
        def wrapper(*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), fncspec=fncspec)
            _TypeChecker(CombinedInput=kwargs.items(), fncspec=fncspec)
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

    if fncspec.annotations and 'return' in fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), fncspec=fncspec)
            _TypeChecker(CombinedInput=kwargs.items(), fncspec=fncspec)
            assert isinstance(
                result := fnc(self,*args, **kwargs),
                fncspec.annotations["return"]
            ), _ErrorMsg(result,fncspec.annotations["return"])
            return result
    elif fncspec.annotations:
        def wrapper(self,*args, **kwargs):
            _TypeChecker(CombinedInput=zip(fncspec_args, args), fncspec=fncspec)
            _TypeChecker(CombinedInput=kwargs.items(), fncspec=fncspec)
            return fnc(self,*args, **kwargs)
    else:
        def wrapper(self,*args, **kwargs):
            return fnc(self,*args, **kwargs)
    return wrapper