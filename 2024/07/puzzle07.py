import aocd
from itertools import product
from operator import add, mul
from functools import reduce


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2024).splitlines()
    else:
        return aocd.get_data(day=day, year=2024)


def double_pipe(a: int, b: int):
    return int(str(a) + str(b))


def part1(data):
    """ """
    good = 0
    for line in data:
        test_value, terms = line.split(":")
        terms = [int(x) for x in terms.split()]
        for c in product([mul, add], repeat=len(terms) - 1):
            v = terms[0]
            for i in range(len(terms) - 1):
                v = reduce(c[i], (v, terms[i + 1]))
            print(v)
            if v == int(test_value):
                good += int(test_value)
                break
    return good


def part2(data):
    """ """
    good = 0
    for line in data:
        test_value, terms = line.split(":")
        terms = [int(x) for x in terms.split()]
        for c in product([add, mul, double_pipe], repeat=len(terms) - 1):
            v = terms[0]
            for i in range(len(terms) - 1):
                v = reduce(c[i], (v, terms[i + 1]))
            if v == int(test_value):
                good += int(test_value)
                break
    return good


if __name__ == "__main__":
    day = 7
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2024)
    # aocd.submit(part2(data), part="b", day=day, year=2024)
