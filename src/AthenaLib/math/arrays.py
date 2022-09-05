# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import numpy as np
from numpy.typing import ArrayLike
import math

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def calculate_largest_radius(center_point:ArrayLike, outside_points:ArrayLike) -> float:
    return np.amax(
        np.array([
            calculate_distance_between_two_coords(center_point, coord)
            for coord in outside_points
        ]),
        axis=0
    )

def calculate_distance_between_two_coords(point_1:ArrayLike, point_2:ArrayLike) -> float:
    return math.sqrt(
        math.pow(point_1[0] - point_2[0] , 2)
        + math.pow(point_1[1] - point_2[1], 2)
    )

def calculate_center(points:ArrayLike) -> ArrayLike:
    return np.array([
        points[:, 0].sum() / (length := len(points)) ,
        points[:, 1].sum() / length
    ])