import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


ZERO = 0


def part1(data):
    """ """
    password = 0
    current = 50
    for row in data:
        move = int(row.replace("L", "-").replace("R", "+"))
        current = (current + move) % 100
        if current == ZERO:
            password += 1
    return password


def part2(data):
    """Doesn't work yet."""
    password = 0
    current = 50
    for row in data:
        move = int(row.replace("L", "-").replace("R", "+"))
        if move < 0:
            rotations, move = divmod(move, -100)
            password += rotations
            if current != ZERO and current + move < ZERO:
                password += 1
        else:
            rotations, move = divmod(move, 100)
            password += rotations
            if current + move > 100:
                password += 1
        current = (current + move) % 100
        if current == ZERO:
            password += 1
    return password


if __name__ == "__main__":
    day = 1
    data = get_data(day)
    print(part2(data))
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    aocd.submit(part2(data), part="b", day=day, year=2025)
