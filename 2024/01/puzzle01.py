import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2024).splitlines()
    else:
        return aocd.get_data(day=day, year=2024)


def build_lists(data):
    llist = []
    rlist = []
    for line in data:
        left, right = line.strip().split()
        llist.append(int(left))
        rlist.append(int(right))
    return llist, rlist


def part1(data):
    """ """
    left, right = build_lists(data)
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


def part2(data):
    """ """
    left, right = build_lists(data)
    return sum(i * right.count(i) for i in left)


if __name__ == "__main__":
    day = 1
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2024)
    # aocd.submit(part2(data), part="b", day=day, year=2024)
