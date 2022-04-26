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
    def wrapper(*args, **kwargs):
        fncspec:inspect.FullArgSpec = inspect.getfullargspec(fnc)
        for k,v in (kwargs
                      | {a:v for a, v in zip(fncspec.args,args)}
                      | {fncspec.varargs:args[len(fncspec.args):]}).items():
            try:
                if not isinstance(v, fncspec.annotations[k]):
                    raise StrongError(f"{v} was not the same type as the Strictly typed: {fncspec.annotations[k]}")
            except KeyError:
                continue

        return fnc(*args,**kwargs)
    return wrapper