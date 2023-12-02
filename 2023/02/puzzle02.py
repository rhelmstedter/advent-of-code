from functools import reduce
from operator import mul

import aocd

ACTUAL = {"red": 12, "green": 13, "blue": 14}


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines if lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


def part1(data):
    """ """
    valid_ids = []
    for line in data:
        valid = True
        game, subsets = line.split(":")
        for subset in subsets.split(";"):
            for element in subset.split(","):
                count, color = element.split()
                if int(count) > ACTUAL[color]:
                    valid = False
                    break
        if valid:
            game_id = int(game.split()[-1])
            valid_ids.append(game_id)
    return sum(valid_ids)


def part2(data):
    """ """
    powers = []
    for line in data:
        max_counts = {"red": 0, "green": 0, "blue": 0}
        _, subsets = line.split(":")
        for subset in subsets.split(";"):
            for element in subset.split(","):
                count, color = element.split()
                if int(count) > max_counts[color]:
                    max_counts[color] = int(count)
        powers.append(reduce(mul, max_counts.values()))

    return sum(powers)


if __name__ == "__main__":
    day = 2
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    aocd.submit(part2(data), part="b", day=day, year=2023)
