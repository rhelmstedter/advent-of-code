import string
import aocd
from itertools import pairwise


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2018).splitlines()
    else:
        return aocd.get_data(day=day, year=2018)


def remove_match_stack(data: str) -> int:
    stack = []
    for unit in data:
        if stack and unit == stack[-1].swapcase():
            stack.pop()
        else:
            stack.append(unit)
    return "".join(stack)


def remove_match(data: str) -> str:
    out = []
    gen = pairwise(data)
    for a, b in gen:
        if a == b.swapcase():
            try:
                next(gen)
            except StopIteration:
                return "".join(out)
        else:
            out.append(a)
    out.append(data[-1])  # Append the last character
    return "".join(out)


def solve_part1(data: str) -> int:
    old_length = len(data)
    while True:
        data = remove_match(data)
        new_length = len(data)
        if new_length == old_length:
            return new_length
        old_length = new_length
    return -1


def solve_part2(data):
    """ """
    units = string.ascii_lowercase
    result = []
    for unit in units:
        new_data = data.replace(unit, "").replace(unit.upper(), "")
        result.append(solve_part1(new_data))
    return min(result)


def part1(data):
    """ """
    return len(remove_match_stack(data))


def part2(data):
    """ """
    units = string.ascii_lowercase
    result = []
    for unit in units:
        new_data = data.replace(unit, "").replace(unit.upper(), "")
        result.append(part1(new_data))
    return min(result)


if __name__ == "__main__":
    day = 5
    data = get_data(day, lines=False)
    # aocd.submit(part1(data), part="a", day=day, year=2018)
    # aocd.submit(part2(data), part="b", day=day, year=2018)
