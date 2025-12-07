import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


neighbors = [
    (-1, -1),  # top left
    (-1, 0),  # top
    (-1, 1),  # top right
    (0, -1),  # left
    (0, 1),  # right
    (1, -1),  # bottom left
    (1, 0),  # bottom
    (1, 1),  # bottom right
]


def part1(data):
    """ """
    good = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "@":
                rolls = 0
                for n in neighbors:
                    try:
                        if (data[r + n[0]][c + n[1]] == "@" and (r + n[0] >= 0 and c + n[1] >= 0)):
                            rolls += 1
                    except IndexError:
                        pass
                if rolls < 4:
                    good += 1
    return good


def part2(data):
    """ """
    removed = 0
    while True:
        data = [list(line) for line in data]
        about_to_remove = []
        for r in range(len(data)):
            for c in range(len(data[r])):
                if data[r][c] == "@":
                    rolls = 0
                    for n in neighbors:
                        try:
                            if data[r + n[0]][c + n[1]] == "@" and (r + n[0] >= 0 and c + n[1] >= 0):
                                rolls += 1
                        except IndexError:
                            pass
                    if rolls < 4:
                        about_to_remove.append((r, c))
        for r, c in about_to_remove:
            data[r][c] = "x"
        exes = sum(line.count("x") for line in data)
        if exes != removed:
            removed = exes
        else:
            return removed


if __name__ == "__main__":
    day = 4
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    aocd.submit(part2(data), part="b", day=day, year=2025)
