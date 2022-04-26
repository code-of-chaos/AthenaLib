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
    fncspec:inspect.FullArgSpec = inspect.getfullargspec(fnc)
    error = lambda k,v : f"{v} was not the same type as the Strictly typed: {fncspec.annotations[k]}"

    if fncspec.varargs is not None:
        def wrapper(*args, **kwargs):
            for k,v in {**kwargs,
                        **dict(zip(fncspec.args, args)),
                        **{fncspec.varargs: args[len(fncspec.args):]}
                        }.items() :
                if not isinstance(v, fncspec.annotations[k]):
                    raise StrongError(error(k,v))
            return fnc(*args,**kwargs)
    else:
        def wrapper(*args, **kwargs):
            for k,v in {**kwargs,
                        **dict(zip(fncspec.args, args))
                        }.items():
                if not isinstance(v, fncspec.annotations[k]):
                    raise StrongError(error(k,v))
            return fnc(*args, **kwargs)
    return wrapper