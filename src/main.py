import time

import constants as consts
from figures.cube import Cube
from matrix import Matrix2D
from screen import Screen
from utils import clear_terminal, get_point_char, get_rounded_and_shifted_point
from utils.space_translator import AxisRotationAngles, space_translator


def main() -> None:
    cube = Cube(consts.cube_size)
    screen = Screen()
    alpha = beta = theta = 0

    while True:
        for point in cube.surface_points:
            rotated_point = space_translator.rotate_point(
                Matrix2D(point), AxisRotationAngles(alpha, beta, theta)
            )
            rotated_point = get_rounded_and_shifted_point(rotated_point)

            x, y, _ = rotated_point

            screen.screen[y][x] = get_point_char(point, cube.size)

        print(screen)
        time.sleep(0.0084)

        clear_terminal()
        screen.clear()

        alpha += 5
        beta += 5
        theta += 5


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Done')
