import configparser
from os import PathLike
from pathlib import Path
from typing import Final
from typing import Iterable
from typing import Iterator
from typing import Literal
from typing import TypeAlias  # type: ignore

import numpy as np


CONFIG_FILE: Final[Path] = Path(__file__).parent / 'config.ini'
config: configparser.ConfigParser = configparser.ConfigParser()
config.read(CONFIG_FILE)
Bit: TypeAlias = Literal['0', '1', 0, 1]


class BingoBoard:

    size: int = 5

    def __init__(self, numbers: Iterable[Iterable[int]]):
        self.board: np.matrix = np.matrix(numbers)
        self.matches: np.matrix = np.matrix(
            [[False for _ in range(self.size)] for _ in range(self.size)],
            dtype='?',
        )

    def match(self, number: int):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == number:
                    self.matches[i, j] = True

    @property
    def solved(self) -> bool:

        for row in self.matches:
            if row.all():
                return True

        for col in self.matches.T:
            if col.all():
                return True

        return False

    @property
    def unmatched(self) -> np.matrix:
        """Return all numbers on that board that have not been matched."""
        return self.board[~self.matches]

    def score(self, last_called: int) -> int:
        """Return the score of the board."""
        return last_called * self.unmatched.sum()


class Puzzle:
    def __init__(self, data_file: PathLike) -> None:

        self.data_file: Final[Path] = Path(data_file)
        self.boards: list[BingoBoard] = []
        self._process_data()

    def solve(self) -> int:
        """Solve the puzzle."""
        for number in self.numbers:
            self.match_boards(number)
            if self.solved_boards:
                break
        scores: list[int] = [
            board.score(number) for board in self.solved_boards
        ]
        return max(scores)

    @property
    def data(self) -> Iterable[str]:
        return self._get_data()

    def _get_data(self) -> Iterator[str]:
        with open(self.data_file, 'r') as fin:
            for line in fin:
                yield line.strip()

    def _process_data(self) -> None:

        input_lines: Iterable[str] = self.data

        first_line: str = next(input_lines)  # type: ignore
        self.numbers: list[int] = list(int(i) for i in first_line.split(','))

        while True:
            try:
                _ = next(input_lines)  # type: ignore
                board_numbers: list[list[int]] = [
                    [int(i) for i in next(input_lines).split()]  # type: ignore
                    for _ in range(BingoBoard.size)
                ]
                board = BingoBoard(board_numbers)
                self.boards.append(board)
            except StopIteration:
                break

    def match_boards(self, number: int) -> None:
        """Match number to boards."""
        for board in self.boards:
            board.match(number)

    @property
    def solved_boards(self):
        solved_boars: list[BingoBoard] = []
        for board in self.boards:
            if board.solved:
                solved_boars.append(board)
        return solved_boars


if __name__ == '__main__':

    data_path: Path = Path(config.get('paths', 'data'))
    data_file: Path = data_path / 'input_4.txt'

    puzzle: Puzzle = Puzzle(data_file=data_file)
    solution: int = puzzle.solve()

    # 870 - Too Low
    assert solution > 870, 'Solution is too low.'

    print(f'{solution=}')
