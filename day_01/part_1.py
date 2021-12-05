""" Find the number of times that the depth increased. """
import itertools
from pathlib import Path
from typing import Iterable
from typing import Iterator


def pairwise(iterable: Iterable) -> Iterator[tuple]:
    # From Python itertools documentation
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def get_input_data() -> Iterator[str]:

    data_file: Path = Path(__file__).parent / 'input.txt'

    with open(data_file, 'r') as fin:
        for line in fin:
            yield line.strip()


if __name__ == '__main__':

    input_lines: Iterator[str] = get_input_data()

    increase_count: int = 0
    for depths in pairwise(input_lines):

        depth_1, depth_2 = map(int, depths)

        if depth_1 < depth_2:
            increase_count += 1

    print(f'ANSWER: {increase_count}')
