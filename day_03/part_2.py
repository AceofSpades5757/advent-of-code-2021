""" Get the episilon and gamma values """
import configparser
import itertools
from collections import Counter
from os import PathLike
from pathlib import Path
from typing import Final
from typing import Iterable
from typing import Iterator
from typing import Literal
from typing import Protocol
from typing import TypeAlias  # type: ignore


CONFIG_FILE: Final[Path] = Path(__file__).parent / 'config.ini'
config: configparser.ConfigParser = configparser.ConfigParser()
config.read(CONFIG_FILE)


Bit: TypeAlias = Literal['0', '1', 0, 1]


class IPuzzle(Protocol):
    """Protocol for the puzzle"""

    def __init__(self) -> None:
        """Initialize the puzzle"""
        ...
        self._process_data()
        ...

    def solve(self):
        ...

    def _process_data(self):
        ...


class Puzzle:
    def __init__(self, data_file: PathLike) -> None:

        self.data_file: Final[Path] = Path(data_file)

        self._process_data()

    def solve(self) -> int:
        """Solve the puzzle."""
        return self.life_support_rating

    def _process_data(self) -> None:

        input_lines: Iterable[str] = self.data

        first_line: str = next(input_lines)  # type: ignore
        self.bit_counters: list[Counter] = [
            Counter() for _ in range(len(first_line))
        ]
        for report in input_lines:
            self._update_bit_counters(report)

    @property
    def data(self) -> Iterable[str]:
        return self._get_data()

    def _get_data(self) -> Iterator[str]:
        with open(self.data_file, 'r') as fin:
            for line in fin:
                yield line.strip()

    def _update_bit_counters(
        self,
        line: str,
        bit_counters: list[Counter] = None,
    ) -> None:
        """Update the counters"""

        if bit_counters is None:
            bit_counters = self.bit_counters

        for index, char in enumerate(line):
            bit_counters[index].update(char)

    def _get_most_common_bit(
        self,
        bit_counter: Counter,
        default_bit: Bit = '0',
    ) -> str:
        """Get the most common bit"""

        all_equal: bool = 1 == len(
            list(itertools.groupby(bit_counter.values()))
        )

        if all_equal:
            return default_bit

        return bit_counter.most_common()[0][0]

    def _get_least_common_bit(
        self,
        bit_counter: Counter,
        default_bit: Bit = '0',
    ) -> str:
        """Get the least common bit"""

        all_equal: bool = 1 == len(
            list(itertools.groupby(bit_counter.values()))
        )

        if all_equal:
            return default_bit

        return bit_counter.most_common()[-1][0]

    @property
    def epsilon(self) -> int:
        value: str = ''.join(
            [c.most_common()[0][0] for c in self.bit_counters]
        )
        return int(value, base=2)

    @property
    def gamma(self) -> int:
        value: str = ''.join(
            [c.most_common()[-1][0] for c in self.bit_counters]
        )
        return int(value, base=2)

    @property
    def power_consumption(self) -> int:

        value: int = self.epsilon * self.gamma
        return value

    @property
    def oxygen_generator_rating(self) -> int:

        data: list[str] = list(self.data)
        bit_length: int = len(data[0])
        default_bit: Bit = '1'

        for bit_index in range(bit_length):

            bit_counter: Counter = Counter((i[bit_index] for i in data))

            most_common_bit: str = self._get_most_common_bit(
                bit_counter,
                default_bit=default_bit,
            )

            data: list[str] = list(  # type: ignore
                filter(lambda x: x[bit_index] != most_common_bit, data)
            )
            if len(data) == 1:
                return int(data[0], base=2)

        if len(data) == 1:
            return int(data[0], base=2)
        else:
            raise ValueError(
                f'No oxygen generator rating found: {len(data)=}.'
            )

    @property
    def co2_scrubber_rating(self) -> int:

        data: list[str] = list(self.data)
        bit_length: int = len(data[0])
        default_bit: Bit = '0'

        for bit_index in range(bit_length):

            bit_counter: Counter = Counter((i[bit_index] for i in data))

            least_common_bit: str = self._get_least_common_bit(
                bit_counter,
                default_bit=default_bit,
            )

            data: list[str] = list(  # type: ignore
                filter(lambda x: x[bit_index] != least_common_bit, data)
            )
            if len(data) == 1:
                return int(data[0], base=2)

        if len(data) == 1:
            return int(data[0], base=2)
        else:
            raise ValueError(f'No CO2 Scrubber Rating found: {len(data)=}.')

    @property
    def life_support_rating(self) -> int:
        value: int = self.oxygen_generator_rating * self.co2_scrubber_rating
        return value


if __name__ == '__main__':

    data_path: Path = Path(config.get('paths', 'data'))
    data_file: Path = data_path / 'input_3.txt'

    puzzle: IPuzzle = Puzzle(data_file=data_file)
    solution: int = puzzle.solve()
    # 10683072 - Too High
    assert solution < 10683072, f'Answer is too hight: {solution}'

    print(f'{solution=}')
