""" Get the episilon and gamma values """
from collections import Counter
from pathlib import Path
from typing import Iterator


def get_input_data() -> Iterator[str]:

    data_file: Path = Path(__file__).parent / 'input.txt'

    with open(data_file, 'r') as fin:
        for line in fin:
            yield line.strip()


def update_counters(counters: list[Counter], line: str) -> None:
    """Update the counters"""
    for index, char in enumerate(line):
        counters[index].update(char)


def get_epsilon_and_gamma(counters: list[Counter]) -> tuple[int, int]:
    """Get the epsilon and gamma values"""
    epsilon: str = ''.join([c.most_common()[0][0] for c in counters])
    gamma: str = ''.join([c.most_common()[-1][0] for c in counters])

    return int(epsilon, base=2), int(gamma, base=2)


if __name__ == '__main__':

    input_lines: Iterator[str] = get_input_data()

    first_line: str = next(input_lines)
    counters: list[Counter] = [Counter() for _ in range(len(first_line))]
    for report in input_lines:
        update_counters(counters, report)

    epsilon, gamma = get_epsilon_and_gamma(counters)
    power_consumption: int = epsilon * gamma

    print(f'ANSWER: {power_consumption}')
