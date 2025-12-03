import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


def part1(data):
    """ """
    total = 0
    for bank in data:
        max_value = -1
        for i in range(len(bank)):
            first = bank[i]
            for j in range(i + 1, len(bank)):
                second = bank[j]
                current_value = int(first + second)
                if current_value > max_value:
                    max_value = current_value
        total += max_value
    return total


def part2(data):
    """ """
    ...


if __name__ == "__main__":
    day = 3
    data = get_data(day)
    # print(part1(data))
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    # aocd.submit(part2(data), part="b", day=day, year=2025)
