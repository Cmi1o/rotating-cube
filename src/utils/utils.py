import os

import constants as consts
from matrix import TNumber


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_rounded_and_shifted_point(point: list[TNumber]) -> list[int]:
    return [
        round(point[0] + consts.x_shift),
        round(point[1] + consts.y_shift),
        round(point[2] + consts.z_shift),
    ]


def get_point_char(src_point: list[int], cube_size: int) -> str:
    x, y, z = src_point

    if 0 < z < cube_size:
        if y == 0 and x not in (0, cube_size):
            return '"'

        if y == cube_size and x not in (0, cube_size):
            return '*'

        if x == 0:
            return '~'

        return '^'

    if z == 0:
        return '+'

    return ':'
