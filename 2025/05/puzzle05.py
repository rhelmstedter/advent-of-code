from webbrowser import get
from operator import ge
from turtledemo.chaos import g
import aocd
from 2025.02.puzzle02 import timeit


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


def _parse_input(data):
    _ranges, ingredients = data.split("\n\n")
    ranges = []
    for r in _ranges.split():
        start, end = r.split("-")
        ranges.append((int(start), int(end)))
    return ranges, [int(i) for i in ingredients.split()]


def part1(data):
    """ """
    ranges, ingredients = _parse_input(data)
    return len([i for i in ingredients if any(low <= i <= high for low, high in ranges)])


def part2(data):
    """ """
    ranges, _ = _parse_input(data)
    last = None
    count = 0
    for low, high in sorted(ranges):
        if last is None:
            last = (low, high)
        elif last[1] < low:
            count += last[1] - last[0] + 1
            last = (low, high)
        else:
            last = (last[0], max(last[1], high))
    count += last[1] - last[0] + 1
    return count


if __name__ == "__main__":
    day = 5
    data = get_data(day, False)
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    # aocd.submit(part2(data), part="b", day=day, year=2025)
