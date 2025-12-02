import aocd

ZERO = 0
UPPER = 100


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


def parse_move(direction):
    return int(direction.replace("L", "-").replace("R", "+"))


def part1(data):
    """ """
    password = 0
    current = 50
    for direction in data:
        move = parse_move(direction)
        current = (current + move) % UPPER
        if current == ZERO:
            password += 1
    return password


def part2(data):
    """ """
    password = 0
    current = 50
    for direction in data:
        move = parse_move(direction)
        if move < 0:
            rotations, move = divmod(move, -UPPER)
            password += rotations
            if current != ZERO and current + move < ZERO:
                password += 1
        else:
            rotations, move = divmod(move, UPPER)
            password += rotations
            if current + move > UPPER:
                password += 1
        current = (current + move) % UPPER
        if current == ZERO:
            password += 1
    return password


if __name__ == "__main__":
    day = 1
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    # aocd.submit(part2(data), part="b", day=day, year=2025)
