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
def convert_time_to_seconds(time:int|Second|Minute|Hour) -> Second|int:
    if isinstance(time, int):
        return Second(time)
    if isinstance(time, Second):
        return time
    elif isinstance(time, Minute):
        return Second(int(time)*60)
    elif isinstance(time, Hour):
        return Second(int(time)*3600)
    else:
        return NotImplemented(time)

def convert_time_to_int(time: int | Second | Minute | Hour) -> Second | int:
    if isinstance(time, int):
        return time
    if isinstance(time, Second):
        return int(time)
    elif isinstance(time, Minute):
        return int(time) * 60
    elif isinstance(time, Hour):
        return int(time) * 3600
    else:
        return NotImplemented(time)

