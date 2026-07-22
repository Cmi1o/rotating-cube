from typing import Any, Generator, Sequence, overload

__all__ = ('TMatrix2D', 'TNumber', 'Matrix2D', 'TMatrix3D')

type TMatrix2D[T] = list[list[T]]
type TMatrix3D[T] = list[list[list[T]]]
type TNumber = int | float


class MatrixDimError(Exception):
    def __init__(self, message: str = 'error with matrices dimensions') -> None:
        super().__init__(message)


class Matrix2D[N: TNumber]:
    def __init__(self, *rows: list[N]) -> None:
        self.__validate_rows_lens(rows)

        self.as_list = [*rows]

    @property
    def cols(self) -> int:
        return len(self.as_list[0])

    @property
    def rows(self) -> int:
        return len(self.as_list)

    def add_row(self, row: list[N]) -> None:
        if len(row) != self.cols:
            raise MatrixDimError('count of cols must be equal in all rows')
        self.as_list.append(row)

    def add_col(self, col: list[N]) -> None:
        if len(col) != self.rows:
            raise MatrixDimError('count of rows must be equal in all cols')

        mT = self.T
        mT.add_row(col)

        self.as_list = mT.T.as_list

    def delete_row(self, index: int) -> None:
        del self.as_list[index]

    @property
    def T(self) -> 'Matrix2D[N]':
        return Matrix2D(
            *([self[j][i] for j in range(self.rows)] for i in range(self.cols))
        )

    @staticmethod
    def E(shape: tuple[int, int]) -> 'Matrix2D[int]':
        rows, cols = shape
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(min(rows, cols)):
            matrix[i][i] = 1

        return Matrix2D(*matrix)

    @staticmethod
    def __validate_rows_lens(matrix: Sequence[list[N]]) -> None:
        prev = len(matrix[0])

        for row in matrix:
            if len(row) != prev:
                raise MatrixDimError('count of cols must be equal in all rows')

    def __call__(self) -> TMatrix2D[N]:
        return self.as_list

    def __repr__(self) -> str:
        return f'{self.as_list}'

    @overload
    def __add__(self, other: 'Matrix2D[Any]') -> 'Matrix2D[TNumber]': ...

    @overload
    def __add__(self, other: TNumber) -> 'Matrix2D[TNumber]': ...

    def __add__(self, other: 'Matrix2D[Any] | TNumber') -> 'Matrix2D[TNumber]':
        f = lambda m: Matrix2D(
            *(
                [(self[i][j] + m[i][j]) for j in range(self.cols)]
                for i in range(self.rows)
            )
        )

        if isinstance(other, Matrix2D):
            if self.rows != other.rows or self.cols != other.cols:
                raise MatrixDimError(
                    'Matrices must have the same dimensions for addition'
                )

            return f(other)

        return f(self.E((self.rows, self.cols)) * other)

    def __sub__(self, other: 'Matrix2D[Any]') -> 'Matrix2D[TNumber]':
        return self.__add__(other * -1)

    def __iter__(self) -> Generator[list[N], Any, None]:
        for row in self():
            yield row

    def __setitem__(self, key, new_row: list[N]) -> None:
        self.as_list[key] = new_row

    @overload
    def __getitem__(self, key: int) -> list[N]: ...

    @overload
    def __getitem__(self, key: slice) -> list[list[N]]: ...

    def __getitem__(self, key: int | slice) -> list[N] | list[list[N]]:
        return self.as_list[key]

    @overload
    def __mul__(self, other: 'Matrix2D[Any]') -> 'Matrix2D[TNumber]': ...

    @overload
    def __mul__(self, other: TNumber) -> 'Matrix2D[TNumber]': ...

    def __mul__(self, other: 'Matrix2D[Any] | TNumber') -> 'Matrix2D[Any]':
        if isinstance(other, Matrix2D):
            if self.cols != other.rows:
                raise MatrixDimError(
                    'Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication'
                )

            return Matrix2D(
                *(
                    [
                        sum(self[i][k] * other[k][j] for k in range(self.cols))
                        for j in range(other.cols)
                    ]
                    for i in range(self.rows)
                )
            )

        return Matrix2D(
            *(
                [other * self[i][j] for j in range(self.cols)]
                for i in range(self.rows)
            )
        )
