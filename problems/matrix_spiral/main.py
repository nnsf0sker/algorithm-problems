from typing import Generator
from typing import List


def up(row: int, col: int) -> (int, int):
    return row - 1, col


def down(row: int, col: int) -> (int, int):
    return row + 1, col


def left(row: int, col: int) -> (int, int):
    return row, col - 1


def right(row: int, col: int) -> (int, int):
    return row, col + 1


def unroll_matrix(matrix: List[List[int]]) -> Generator[int, None, None]:
    n = len(matrix)
    i, j = n // 2, n // 2
    for current_radius in range(n - 1):
        first_step, second_step = (down, left) if current_radius % 2 else (up, right)
        for step_method in (
            *(first_step for _ in range(current_radius + 1)),
            *(second_step for _ in range(current_radius + 1, 2 * current_radius + 2))
        ):
            yield matrix[i][j]
            i, j = step_method(i, j)
    for _ in range(n - 1):
        yield matrix[i][j]
        i, j = up(i, j)
    yield matrix[0][0]


def __check_matrix(matrix: List[List[int]]) -> None:
    rows_n = len(matrix)
    for col in matrix:
        assert rows_n == len(col)


if __name__ == "__main__":
    print(list(unroll_matrix([
        [1, 2, 3],
        [4, 5, 7],
        [8, 9, 1]
    ])))
