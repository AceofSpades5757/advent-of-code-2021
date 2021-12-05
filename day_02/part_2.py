""" Given list of commands, what is your final depth times your final
horizontal position.

Includes Aim
Commands mean different things.
"""
from pathlib import Path
from typing import Iterator


def get_input_data() -> Iterator[str]:

    data_file: Path = Path(__file__).parent / 'input.txt'

    with open(data_file, 'r') as fin:
        for line in fin:
            yield line.strip()


if __name__ == '__main__':

    input_lines: Iterator[str] = get_input_data()

    horizontal_position: int = 0
    depth:               int = 0
    aim:                 int = 0

    for command in input_lines:
        match command.split():
            case 'forward', value:
                horizontal_position += int(value)
                depth += aim * int(value)
            case 'up', value:
                aim -= int(value)
            case 'down', value:
                aim += int(value)
            case _:
                raise ValueError(f'Unknown command: {command.split()}')

    print(f'ANSWER: {horizontal_position * depth}')
