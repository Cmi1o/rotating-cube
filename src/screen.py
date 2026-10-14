from typing import NamedTuple

import constants as consts
from matrix import TMatrix2D


class PointCoords(NamedTuple):
    x: int
    y: int


class Screen:
    def __init__(self, background_symbol: str = ' ') -> None:
        self._screen = self.__generate_new_screen(background_symbol)
        self._symbol = background_symbol

    @property
    def screen(self) -> TMatrix2D[str]:
        return self._screen

    @property
    def background_symbol(self) -> str:
        return self._symbol

    @staticmethod
    def __generate_new_screen(symbol: str) -> TMatrix2D[str]:
        return [
            [symbol for _ in range(consts.screen_width)]
            for _ in range(consts.screen_height)
        ]

    def __str__(self) -> str:
        # in ' '.join(row) for row in self._screen we use ' ' to increase figures on the screen size
        return '\n'.join(' '.join(row) for row in self._screen)

    def clear(self) -> None:
        for i in range(len(self._screen)):
            for j in range(len(self._screen[0])):
                self._screen[i][j] = self._symbol
