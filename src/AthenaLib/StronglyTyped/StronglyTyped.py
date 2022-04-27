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
        # Only run the check if there are actually are any annotations
        #   Else you just loose time
        if fncspec.annotations:
            for k, v in zip((*fncspec.args, *kwargs),(*args,*kwargs.values())):
                # If no annotations are placed on the function,
                #   then the given variable will not be strongly typed
                if not isinstance(v, fncspec.annotations[k]):
                    raise StrongError(
                        f"'{v}' was not the same type as the expected Strongly typed: '{fncspec.annotations[k]}'"
                    )
        # Run the actual function
        #   Won't reach this point if the 'StrongError' was raised
        return fnc(*args,**kwargs)
    return wrapper

def StronglyTypedMethod(fnc):
    # do the inspection before a function is esxecuted
    #   as now it is only done once, instead of every function
    fncspec = inspect.getfullargspec(fnc)
    fncspec_args = [a for a in fncspec.args if a != 'self']
    def wrapper(self, *args, **kwargs):
        # Only run the check if there are actually are any annotations
        #   Else you just loose time
        if fncspec.annotations:
            for k, v in zip((*fncspec_args, *kwargs),(*args,*kwargs.values())
            ):
                # If no annotations are placed on the function,
                #   then the given variable will not be strongly typed
                if not isinstance(v, fncspec.annotations[k]):
                    raise StrongError(
                        f"'{v}' was not the same type as the expected Strongly typed: '{fncspec.annotations[k]}'"
                    )
        # Run the actual function
        #   Won't reach this point if the 'StrongError' was raised
        return fnc(self, *args,**kwargs)
    return wrapper