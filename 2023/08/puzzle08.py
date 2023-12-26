import aocd
import re
from math import lcm


def get_data(day: int, lines: bool = True) -> str | list:
    """Use aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


def _parser(data):
    directions = data[0]
    pattern = r"[A-Z]{3}"
    map = {}
    for line in data[1:]:
        if line:
            location, left, right = re.findall(pattern, line)
            map[location] = {"L": left, "R": right}
    return directions, map


def part1(data):
    """ """
    directions, map = _parser(data)
    step = 0
    location = "AAA"
    while location != "ZZZ":
        direction = directions[step % len(directions)]
        location = map[location][direction]
        step += 1
    return step


def part2(data):
    """ """
    directions, map = _parser(data)
    locations = [location for location in map if location.endswith("A")]
    steps = []
    for location in locations:
        step = 0
        while not location.endswith("Z"):
            direction = directions[step % len(directions)]
            location = map[location][direction]
            step += 1
        steps.append(step)
    return lcm(*steps)


if __name__ == "__main__":
    day = 8
    data = get_data(day)
    # part2(data)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    aocd.submit(part2(data), part="b", day=day, year=2023)
