# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Iterable
import math
import itertools

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class SplitError(Exception):
    pass
_ErrorMsg= lambda content, segments: f"{content} was smaller than the given {segments=} to be split into"

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def split_evenly(content:Iterable, segments:int) -> tuple:
    return *split_evenly_generator(content,segments),

def split_evenly_generator(content:Iterable, segments:int):
    match content:
        case (list(a) | set(a) | tuple(a)) if (content_len:=len(a)) >= segments:
            step = math.ceil(content_len / segments)
            for i in range(0, content_len, step):
                yield type(a)(itertools.islice(content, i, (i+step)))

        # If the Content is smaller than the given segments
        case (list() | set() | tuple()):
            raise SplitError(_ErrorMsg(content,segments))

        # Dict seperated from other types, as the k,v pair needs to recreated
        case dict(a) if (content_len:=len(a)) >= segments:
            step = math.ceil(content_len / segments)
            for i in range(0, content_len, step):
                yield {k:v for k,v in itertools.islice(content.items(), i, (i+step))}

        # If the Content is smaller than the given segments
        case dict():
            raise SplitError(_ErrorMsg(content,segments))

        case _:
            raise NotImplementedError