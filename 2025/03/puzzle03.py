import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


def part1(data):
    """This works because we are finding the largest value in the list of integers as long
    as its not in the final position. Then, using list.index(), we find us the first occurance
     the max, and only search from that point on."""
    total = 0
    banks = [[int(b) for b in line] for line in data]
    for bank in banks:
        tens = max(bank[:-1])
        ones = max(bank[bank.index(tens) + 1:])
        total += tens * 10 + ones
    return total


def part2(data):
    """This leverages the same logic as the first, but instead of finding two digits, we iterate
    up to 11 digits. Then we take care of the 12th outside of the loop. If we iterated all 12
    inside the loop, we would end up with list[:0] which is the empty list."""
    total = 0
    banks = [[int(b) for b in line] for line in data]
    for bank in banks:
        jolts = 0
        for i in range(11):
            digit = max(bank[:i - 11])
            bank = bank[bank.index(digit) + 1:]
            jolts = jolts * 10 + digit
        jolts = jolts * 10 + max(bank)
        print(jolts)
        total += jolts
    return total


if __name__ == "__main__":
    day = 3
    data = get_data(day)
    # print(part1(data))
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    # aocd.submit(part2(data), part="b", day=day, year=2025)
