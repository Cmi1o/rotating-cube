from abc import ABC, abstractmethod

from matrix import Matrix2D


class Figure(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @property
    @abstractmethod
    def surface_points(self) -> Matrix2D[int]: ...
