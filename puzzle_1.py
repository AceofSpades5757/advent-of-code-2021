import configparser
from pathlib import Path
from typing import Iterator


CONFIG_FILE = Path(__file__).parent / 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE)


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

    for line in input_lines:
        print(line)
