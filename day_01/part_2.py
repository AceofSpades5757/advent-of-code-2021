""" Find the number of times that the depth increased, with a window of 3
(summed). """
import itertools
from pathlib import Path
from typing import Iterable
from typing import Iterator
from typing import Union


def pairwise(iterable: Iterable) -> Iterator[tuple]:
    # From Python itertools documentation
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def triplewise(iterable: Iterable) -> Iterator[tuple]:
    # triplewise('ABCDEFG') --> ABC BCD CDE DEF EFG FGH
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


def get_input_data() -> Iterator[str]:

    data_file: Path = Path(__file__).parent / 'input.txt'

    with open(data_file, 'r') as fin:
        for line in fin:
            yield line.strip()


def get_windowed_depth_data(
    depth_data: Iterator[Union[str, int]],
) -> Iterator[int]:
    """Get the depth data, with a window of 3 (summed)."""
    for depths in triplewise(depth_data):

        sum_: int = sum(map(int, depths))
        yield sum_


if __name__ == '__main__':

    input_lines: Iterator[str] = get_input_data()
    windowed_depths: Iterator[int] = get_windowed_depth_data(input_lines)

    increase_count: int = 0
    for depths in pairwise(windowed_depths):

        depth_1, depth_2 = map(int, depths)

        if depth_1 < depth_2:
            increase_count += 1

    print(f'ANSWER: {increase_count}')
