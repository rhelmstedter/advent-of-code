import re
from string import punctuation

import aocd

SYMBOLS = punctuation.replace(".", "")

SAMPLE_INPUT = """467..114..
...*......
..35..633.
......#...
617*2.....
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


def _is_part_number(data: list[str], row_number: int, start: int, match: str) -> bool:
    length = len(match)
    for row in range(row_number - 1, row_number + 2):
        if row < 0:
            continue
        for col in range(start - 1, start + length + 1):
            if col < 0:
                continue
            try:
                if data[row][col] in SYMBOLS:
                    return True
            except IndexError:
                continue
    return False


def part1(data: list[str]):
    """ """
    pattern = r"\d+"
    part_numbers = []
    for r, row in enumerate(data):
        for part_number in re.finditer(pattern, row):
            start, match = part_number.start(), part_number.group()
            if _is_part_number(data, r, start, match):
                part_numbers.append(int(match))
    return sum(part_numbers)


def part2(data: list[str]):
    """ """
    part_pattern = r"\d+"
    gear_pattern = r"\*"
    gear_ratios = []
    for r, row in enumerate(data):
        if r == 0:
            adjacent_rows = (row, data[r + 1])
        elif r == len(data) - 1:
            adjacent_rows = (data[r - 1], row)
        else:
            adjacent_rows = (data[r - 1], row, data[r + 1])
        for gear in re.finditer(gear_pattern, row):
            gear_position = gear.start()
            parts = []
            for _row in adjacent_rows:
                for part_number in re.finditer(part_pattern, _row):
                    start, match = part_number.start(), part_number.group()
                    end = start + len(match)
                    if any(
                        abs(gear_position - part_position) <= 1
                        for part_position in range(start, end)
                    ):
                        parts.append(match)
            if len(parts) == 2:
                part1, part2 = parts
                gear_ratios.append(int(part1) * int(part2))
    return sum(gear_ratios)


if __name__ == "__main__":
    day = 3
    data = get_data(day, True)
    # answer = part2(data)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    aocd.submit(part2(data), part="b", day=day, year=2023)
