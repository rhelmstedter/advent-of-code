import aocd
from operator import add, mul
from functools import reduce


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


def _parse_ops(data):
    return [op for op in data[-1].split()]


def part1(data):
    """ """
    values = list(zip(*[list(map(int, line.split())) for line in data[:-1]]))
    ops = _parse_ops(data)
    return sum(reduce(mul if op == "*" else add, nums) for nums, op in zip(values, ops))


def part2(data):
    """ """
    ops = _parse_ops(data)
    cols = []
    nums = []
    for chars in zip(*data[:-1]):
        try:
            num = int("".join(chars))
            nums.append(num)
        except ValueError:
            cols.append(nums)
            nums = []
    cols.append(nums)

    return sum(reduce(mul if op == "*" else add, nums) for nums, op in zip(cols, ops))


if __name__ == "__main__":
    day = 6
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    # aocd.submit(part2(data), part="b", day=day, year=2025)
