# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import asyncio

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def Timeout(max_time:int|float):
    def decorator(fnc):
        def wrapper(*args, **kwargs):
            try:
                return asyncio.run(
                    asyncio.wait_for(
                        fnc(*args, **kwargs),
                        timeout=max_time
                    )
                )
            except asyncio.exceptions.TimeoutError:
                raise TimeoutError
        return wrapper
    return decorator