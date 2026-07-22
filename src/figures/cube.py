from itertools import product

from figures.figure import Figure
from matrix import Matrix2D


class Cube(Figure):
    def __init__(self, size: int) -> None:
        '''
        Creates a cube in the begin of axis coordinates with size of `size`

        Parameters
        ----------
        size : int, optional
            size of the cube
        '''
        self._size = size

    @property
    def size(self) -> int:
        return self._size

    def __is_surface(self, coordinate: int) -> bool:
        return coordinate in (0, self._size)

    @property
    def surface_points(self) -> Matrix2D[int]:
        temp_row, temp_index = [0, 0, 0], 0

        points = Matrix2D[int](temp_row)

        for z, y, x in product(range(self._size + 1), repeat=3):
            if self.__is_surface(x) or self.__is_surface(y) or self.__is_surface(z):
                points.add_row([x, y, z])

        points.delete_row(temp_index)

        return points
