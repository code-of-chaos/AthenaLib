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
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
_ErrorMsg= lambda val, t: f"'{val}' was not the same type as the expected Strongly typed: '{t}'"

class StrongError(Exception):
    pass

def StronglyTyped(fnc):
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec = inspect.getfullargspec(fnc)
    fncspec_args = fncspec.args
    if fncspec.varargs is not None:
        fncspec_args.append(fncspec.varargs)
    # If a return is defined, it can be used to Strongly Type the result
    if 'return' in fncspec.annotations:
        return_type = fncspec.annotations['return']
    else:
        return_type = None

    print(fncspec)
    def wrapper(*args, **kwargs):
        # Only run the check if there are actually are any annotations
        #   Else you just loose time
        if fncspec.annotations:
            for k, v in zip((*fncspec_args, *kwargs),(*args,*kwargs.values())):
                # If no annotations are placed on the function,
                #   then the given variable will not be strongly typed
                if not isinstance(v, fncspec.annotations[k]):
                    raise StrongError(_ErrorMsg(v,fncspec.annotations[k]))
        # Run the actual function
        #   Won't reach this point if the 'StrongError' was raised
        result = fnc(*args,**kwargs)
        if return_type is not None and not isinstance(result, return_type):
            raise StrongError(_ErrorMsg(result,return_type))
        return result
    return wrapper

def StronglyTypedMethod(fnc):
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec = inspect.getfullargspec(fnc)
    fncspec_args = [a for a in fncspec.args if a != 'self']
    if fncspec.varargs is not None:
        fncspec_args.append(fncspec.varargs)
    # If a return is defined, it can be used to Strongly Type the result
    if 'return' in fncspec.annotations:
        return_type = fncspec.annotations['return']
    else:
        return_type = None

    def wrapper(self, *args, **kwargs):
        # Only run the check if there are actually are any annotations
        #   Else you just loose time
        if fncspec.annotations:
            for k, v in zip((*fncspec_args, *kwargs),(*args,*kwargs.values())
            ):
                # If no annotations are placed on the function,
                #   then the given variable will not be strongly typed
                if not isinstance(v, fncspec.annotations[k]):
                    raise StrongError(_ErrorMsg(v,fncspec.annotations[k]))
        # Run the actual function
        #   Won't reach this point if the 'StrongError' was raised
        result = fnc(self,*args,**kwargs)
        if return_type is not None and not isinstance(result, return_type):
            raise StrongError(_ErrorMsg(result,return_type))
        return result
    return wrapper