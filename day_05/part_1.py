from os import PathLike
from pathlib import Path
from typing import Final
from typing import Iterable
from typing import Iterator


class Puzzle:

    def __init__(self, data_file: PathLike) -> None:

        self.data_file: Final[Path] = Path(data_file)
        self._process_data()

    def solve(self) -> int:
        """Solve the puzzle."""
        ...

    @property
    def data(self) -> Iterable[str]:
        return self._get_data()

    def _get_data(self) -> Iterator[str]:
        with open(self.data_file, 'r') as fin:
            for line in fin:
                yield line.strip()

    def _process_data(self) -> None:

        input_lines: Iterable[str] = self.data
        for line in input_lines:
            start, end = line.split(' -> ')
            x_1, y_1 = map(int, start.split(','))
            x_2, y_2 = map(int, end.split(','))


if __name__ == '__main__':

    data_file: Path = Path(__file__).parent / 'input.txt'

    puzzle: Puzzle = Puzzle(data_file=data_file)
    # solution: int = puzzle.solve()

    # print(f'{solution=}')
