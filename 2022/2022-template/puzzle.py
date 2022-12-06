from aocd import get_data, submit


def get_lines(day: int) -> list:
    """Uses aocd to get the input then splits it into lines."""
    return get_data(day=day, year=2022).splitlines()


def part1(lines):
    """ """
    ...


def part2(lines):
    """ """
    ...


if __name__ == "__main__":

    day = ...
    lines = get_lines(day)
    # submit(part1(lines), part="a", day=day, year=2022)
    # submit(part2(lines), part="b", day=day, year=2022)
