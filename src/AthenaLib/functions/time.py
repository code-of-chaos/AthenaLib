# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaLib.models.time import Second, Minute, Hour

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def convert_time_to_seconds(time:int|Second|Minute|Hour, to_int:bool=False) -> Second|int:
    if isinstance(time, int):
        if to_int:
            return time
        return Second(time)
    if isinstance(time, Second):
        if to_int:
            return int(time)
        return time
    elif isinstance(time, Minute):
        if to_int:
            return int(time)*60
        return Second(int(time)*60)
    elif isinstance(time, Hour):
        if to_int:
            return int(time)*3600
        return Second(int(time)*3600)
    else:
        return NotImplemented(time)

