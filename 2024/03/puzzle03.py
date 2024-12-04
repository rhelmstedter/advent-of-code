import aocd
import re


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2024).splitlines()
    else:
        return aocd.get_data(day=day, year=2024)


def part1(data):
    """ """
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    return sum(int(a) * int(b) for a, b in matches)


def part2(data):
    """ """
    pattern = r"""
    (don\'t)\(\) |
    (do)\(\) |
    mul\((\d+,\d+)\)
    """
    matches = re.findall(pattern, data, flags=re.VERBOSE)
    flattened = [match for sub in matches for match in sub if match]
    multiply = True
    total = 0
    for match in flattened:
        if match == "don't":
            multiply = False
            continue
        elif match == "do":
            multiply = True
            continue
        if multiply:
            a, b = map(int, match.split(","))
            total += a * b
    return total


if __name__ == "__main__":
    day = 3
    data = get_data(day, lines=False)
    # aocd.submit(part1(data), part="a", day=day, year=2024)
    # aocd.submit(part2(data), part="b", day=day, year=2024)
