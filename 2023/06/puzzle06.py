import aocd
import math


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


def _get_wins(time, distance):
    return [s for s in range(time) if s * (time - s) > distance]


def part1(data):
    """ """
    times = [int(t) for t in data[0].split(":")[-1].split()]
    distances = [int(d) for d in data[1].split(":")[-1].split()]
    num_wins = 1
    for time, distance in zip(times, distances):
        num_wins *= len(_get_wins(time, distance))
    return num_wins


def part2(data):
    """ """
    time = int("".join([t for t in data[0].split(":")[-1].split()]))
    distance = int("".join([d for d in data[1].split(":")[-1].split()]))

    # # my original solution
    # return len(_get_wins(time, distance))

    # with math
    a = 1
    b = time
    c = distance
    x_pos = math.floor((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a))
    x_min = math.ceil((-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a))
    return x_pos - x_min + 1


if __name__ == "__main__":
    day = 6
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
