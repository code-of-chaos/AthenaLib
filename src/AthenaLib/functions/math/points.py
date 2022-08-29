# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import numpy as np
import math

# Custom Library

# Custom Packages
from AthenaLib.data.types import NUMBER, POINT

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def closest_point_index(point:POINT, points:list[POINT]) -> np.ndarray[int]:
    return np.argmin(np.sum((np.asarray(points) - point)**2, axis=1))

def closest_point(point:POINT, points:list[POINT]) -> POINT:
    return points[closest_point_index(point, points)]

def midpoint(point0:POINT, point1:POINT) -> POINT:
    x0, y0 = point0
    x1, y1 = point1
    return ((x0+x1)/2, (y0+y1)/2)

def midpoint_relative(point0:POINT, midpoint:POINT, point1:POINT) -> NUMBER:
    dist_left = math.dist(point0, midpoint)
    dist_right = math.dist(midpoint, point1)
    return max((dist_right, dist_left)) - min((dist_right, dist_left))
