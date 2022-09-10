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
    """
    Determines the largest radius of all points compared to a center point.
    Both the center_point and the outside_points should be Numpy Arrays
    """
    return np.amax(
        np.array([
            calculate_distance_between_two_coords(center_point, coord)
            for coord in outside_points
        ]),
        axis=0
    )

def calculate_distance_between_two_coords(point_1:ArrayLike, point_2:ArrayLike) -> float:
    """
    Determines the distance between two points which are stored as Numpy arrays.
    """
    return math.sqrt(
        math.pow(point_1[0] - point_2[0] , 2)
        + math.pow(point_1[1] - point_2[1], 2)
    )

def calculate_center(points:ArrayLike) -> ArrayLike:
    """
    Returns a Numpy Array which is equal distance away from the Array of points.
    Points is a Numpy Array of Numpy Arrays which describe the 2d points
    """
    return np.array([
        points[:, 0].sum() / (length := len(points)) ,
        points[:, 1].sum() / length
    ])

def calculate_nearest(center_point:ArrayLike, points:list):
    return min(
        points,
        key=lambda p: math.hypot(p[0]-center_point[0], p[1]-center_point[1])
    )
