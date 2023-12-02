import re

import aocd

WORDS_TO_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


def part1(data):
    """ """
    digits = list("0123456789")
    filter = ["".join(c for c in line if c in digits) for line in data if line]
    return sum(int(cal[0] + cal[-1]) for cal in filter)


def part2(data):
    """ """
    pattern = r"""(?=
        (
            \d
            | one
            | two
            | three
            | four
            | five
            | six
            | seven
            | eight
            | nine
        )
    )
    """
    calibrations = []
    for line in data:
        matches = re.finditer(pattern, line, flags=re.VERBOSE)
        digits = [match.group(1) for match in matches]
        converted = []
        for d in digits:
            if d in WORDS_TO_DIGITS:
                d = WORDS_TO_DIGITS[d]
            converted.append(d)
        calibrations.append(int(converted[0] + converted[-1]))
    return sum(calibrations)


if __name__ == "__main__":
    day = 1
    data = get_data(day, True)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
