# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import inspect

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StrongError(Exception):
    pass

def StronglyTyped(fnc):
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec = inspect.getfullargspec(fnc)
    def wrapper(*args, **kwargs):
        for k, v in zip(
            (*fncspec.args, *kwargs),
            (*args,*kwargs.values())
        ):
            if not isinstance(v, fncspec.annotations[k]):
                raise StrongError(f"{v} was not the same type as the Strongly typed: {fncspec.annotations[k]}")
        return fnc(*args,**kwargs)
    return wrapper

def StronglyTypedMethod(fnc):
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec = inspect.getfullargspec(fnc)
    def wrapper(self, *args, **kwargs):
        for k, v in zip(
            (*(a for a in fncspec.args if a != 'self'), *kwargs),
            (*args,*kwargs.values())
        ):
            if not isinstance(v, fncspec.annotations[k]):
                raise StrongError(f"{v} was not the same type as the Strongly typed: {fncspec.annotations[k]}")
        return fnc(self, *args,**kwargs)
    return wrapper