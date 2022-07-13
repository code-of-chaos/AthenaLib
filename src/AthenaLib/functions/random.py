# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import random
import typing

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def random_int_no_duplicates(start:int, end:int, *, return_amount:int=None, end_correction:bool=False):
    """
    A generator function which returns a unique integer value between the start and end value.
    Created because twitch viewer 'officialmrcoffee' wanted it.

    Parameters:
    - start:int -> the integer the range function that constructs the choices list starts on.
    - end:int -> the integer the range function that constructs the choices list ends on.
        The resulted choices will go up to `end-1` if `end_correction` is not enabled
    - return_amount:int -> The amount of elements to return. If set to None it will return all elements in the choices
    - end_correction:bool -> allows for the end of the choices list to implement the final integer
    """
    # choices has to be defined first for the return_amount to be defined correctly
    choices:list[int] = list(range(start, end+1 if end_correction else end))
    if return_amount is None:
        return_amount = len(choices)
    elif return_amount > len(choices):
        # If the function tries to return more elements than arte in the list, it will cause error,
        #   so a boundary is defined
        return_amount = len(choices)

    # don't store the range int as this doesn't matter to the choice
    for _ in range(return_amount):
        result = random.choice(choices)
        yield result
        # remove the actual result from the choices
        #   so that in the following iteration of the for loop the sample result can't be yield again
        choices.remove(result)

def random_bool(probability:float=0.5) -> bool:
    return random.random() < probability