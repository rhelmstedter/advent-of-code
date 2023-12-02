import aocd
import pandas as pd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2022).splitlines()
    else:
        return aocd.get_data(day=day, year=2022)


def part1(data):
    """ """
    ...


def part2(data):
    """ """
    ...


if __name__ == "__main__":

    day = 8
    data = get_data(day)
    # submit(part1(lines), part="a", day=day, year=2022)
    # submit(part2(lines), part="b", day=day, year=2022)
