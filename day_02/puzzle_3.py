""" Given list of commands, what is your final depth times your final
horizontal position. """
import configparser
from pathlib import Path
from typing import Final
from typing import Iterator


CONFIG_FILE: Final[Path] = Path(__file__).parent / 'config.ini'
config: configparser.ConfigParser = configparser.ConfigParser()
config.read(CONFIG_FILE)


def get_input_data() -> Iterator[str]:

    data_path: Path = Path(config.get('paths', 'data'))
    data_file: Path = data_path / 'input_2.txt'

    if not data_path.exists():
        data_path.mkdir()

    with open(data_file, 'r') as fin:
        for line in fin:
            yield line.strip()


if __name__ == '__main__':

    input_lines: Iterator[str] = get_input_data()

    horizontal_position, depth = 0, 0
    for command in input_lines:
        match command.split():
            case 'forward', value:
                horizontal_position += int(value)
            case 'up', value:
                depth -= int(value)
            case 'down', value:
                depth += int(value)
            case _:
                raise ValueError(f'Unknown command: {command.split()}')

    print(f'ANSWER: {horizontal_position * depth}')
