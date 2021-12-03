""" Find the number of times that the depth increased. """
import configparser
import itertools
from pathlib import Path
from typing import Final
from typing import Iterator


CONFIG_FILE: Final[Path] = Path(__file__).parent / 'config.ini'
config: configparser.ConfigParser = configparser.ConfigParser()
config.read(CONFIG_FILE)


def pairwise(iterable) -> Iterator[tuple]:
    # From Python itertools documentation
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def get_input_data() -> Iterator[str]:

    data_path: Path = Path(config.get('paths', 'data'))
    data_file: Path = data_path / 'puzzle_1.txt'

    if not data_path.exists():
        data_path.mkdir()

    with open(data_file, 'r') as fin:
        for line in fin:
            yield line.strip()


if __name__ == '__main__':

    input_lines: Iterator[str] = get_input_data()

    increase_count: int = 0
    for depth_1, depth_2 in pairwise(input_lines):
        if int(depth_1) < int(depth_2):
            increase_count += 1

    print(f'ANSWER: {increase_count}')
