import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Use aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
"""
- no diagonal checks in part one.
- direction matters: i.e. going west to east in - can only connect to -, J, or 7. whereas E to W - connects to -, L, F.  
"""


def part1(data):
    """ """
    ...


def part2(data):
    """ """
    ...


if __name__ == "__main__":
    day = 10
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
