from math import cos, sin

from matrix import Matrix2D, TNumber


def Rx(phi: float) -> Matrix2D[TNumber]:
    return Matrix2D([1, 0, 0], [0, cos(phi), -sin(phi)], [0, sin(phi), cos(phi)])


def Ry(phi: float) -> Matrix2D[TNumber]:
    return Matrix2D([cos(phi), 0, sin(phi)], [0, 1, 0], [-sin(phi), 0, cos(phi)])


def Rz(phi: float) -> Matrix2D[TNumber]:
    return Matrix2D([cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1])
