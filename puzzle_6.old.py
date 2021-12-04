""" Get the episilon and gamma values """
import configparser
import functools
from collections import Counter
from pathlib import Path
from typing import Final
from typing import Iterator
from os import PathLike


CONFIG_FILE: Final[Path] = Path(__file__).parent / 'config.ini'
config: configparser.ConfigParser = configparser.ConfigParser()
config.read(CONFIG_FILE)


class Puzzle:
    """ Represets Puzzle """

    def __init__(self, data_file: PathLike = '') -> None:

        self.data_file: Final[Path] = Path(data_file)
        self._counters: list[Counter] = []

        self.process()

    def solve(self) -> int:
        """ Solve the puzzle """

        return self.power_consumption

    def process(self) -> None:
        """ Process data """

        first_line: str = next(self.data)
        self._counters: list[Counter] = [
            Counter() for _ in range(len(first_line))
        ]
        for report in self.data:
            self.update(report)

    @property
    def data(self) -> Iterator[str]:

        with open(self.data_file, 'r') as fin:
            for line in fin:
                yield line.strip()

    @property
    def power_consumption(self):

        value: int = self.epsilon * self.gamma
        return value

    @property
    def epsilon(self) -> int:
        if not hasattr(self, '_epsilon'):
            value: str = ''.join(
                [c.most_common()[0][0] for c in self._counters]
            )
            self._epsilon: int = int(value, base=2)
        return self._epsilon

    @property
    def gamma(self) -> int:
        if not hasattr(self, '_gamma'):
            value: str = ''.join(
                [c.most_common()[-1][0] for c in self._counters]
            )
            self._gamma: int = int(value, base=2)
        return self._gamma

    def update(self, data: str) -> None:
        """ Update data using current data input. """
        for index, char in enumerate(data):
            self._counters[index].update(char)


if __name__ == '__main__':

    data_path: Path = Path(config.get('paths', 'data'))
    data_file: Path = data_path / 'input_3.txt'

    puzzle: Puzzle = Puzzle(data_file=data_file)
    solution: int = puzzle.solve()

    print(f'{solution=}')
