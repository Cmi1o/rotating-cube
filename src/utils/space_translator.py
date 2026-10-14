from math import radians
from typing import NamedTuple

from matrix import Matrix2D, TNumber
from utils.rotation import Rx, Ry, Rz


class PointSizeException(Exception):
    '''Exception class for invalid size of the point'''

    def __init__(self, *, message: str = 'point must be a 1x3 matrix') -> None:
        super().__init__(message)


class ScreenParams(NamedTuple):
    screen_width: int
    screen_height: int


class AxisRotationAngles(NamedTuple):
    x: float
    y: float
    z: float


class SpaceTranslator:
    @staticmethod
    def is_point(point: Matrix2D[int]) -> bool:
        return point.rows == 1 and point.cols == 3

    def rotate_point(
        self, point: Matrix2D[int], angles: AxisRotationAngles
    ) -> list[TNumber]:
        if not self.is_point(point):
            raise PointSizeException()

        x_rads, y_rads, z_rads = map(radians, angles)

        # do NOT change the order of multiplication
        return (point * Rx(x_rads) * Ry(y_rads) * Rz(z_rads))[0]


space_translator = SpaceTranslator()
