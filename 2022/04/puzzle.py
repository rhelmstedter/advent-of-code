from aocd import get_data, submit


def get_lines(day: int) -> list:
    """Uses aocd to get the input then splits it into lines."""
    return get_data(day=day, year=2022).splitlines()


def _expand_sections(first: str, last: str) -> set:
    return set(range(int(first), int(last) + 1))


def _get_assignments(line: str) -> tuple[set]:
    elf1, elf2 = line.split(",")
    return _expand_sections(*elf1.split("-")), _expand_sections(*elf2.split("-"))


def part1(lines) -> int:
    """Number of pairs of elves that contain duplicate assigments."""
    match = []
    for line in lines:
        elf1_assignment, elf2_assignment = _get_assignments(line)
        intersection = elf1_assignment & elf2_assignment
        match.append(intersection == elf1_assignment or intersection == elf2_assignment)
    return sum(match)


def part2(lines) -> int:
    """Number of pairs of elves that are assigned duplicate sections."""
    match = []
    for line in lines:
        elf1_assignment, elf2_assignment = _get_assignments(line)
        if elf1_assignment & elf2_assignment:
            match.append(1)
    return sum(match)


if __name__ == "__main__":

    day = 4
    lines = get_lines(day)
    # submit(part1(lines), part="a", day=day, year=2022)
    # submit(part2(lines), part="b", day=day, year=2022)
