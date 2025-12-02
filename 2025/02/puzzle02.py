import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then optionally splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


def _parse_input(data: str) -> list[tuple[int, int]]:
    """Turns a string into a list of tuples consisting of the start and end of a range."""
    ranges = []
    for r in data.split(","):
        start, end = r.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def part1(data: str) -> int:
    """Takes the data a returns the sum of the invalid IDs."""
    total = 0
    ranges = _parse_input(data)
    for start, end in ranges:
        for id in range(start, end + 1):
            id_str = str(id)
            len_id = len(id_str)
            if len_id % 2 == 0:
                if id_str[: len_id // 2] == id_str[len_id // 2 :]:
                    total += id
    return total


def _repeats(id_str: str) -> bool:
    """Checks if an ID consists of repeating substrings."""
    len_id = len(id_str)
    for i in range(1, len_id // 2 + 1):
        chunks = set(id_str[n : i + n] for n in range(0, len_id, i))
        if len(chunks) == 1:
            return True
    return False


def part2(data: str) -> int:
    """Takes the data a returns the sum of the invalid IDs. Where IDs consist of repeating substrings of any length."""
    total = 0
    ranges = _parse_input(data)
    for start, end in ranges:
        for id in range(start, end + 1):
            if _repeats(str(id)):
                total += id
    return total


if __name__ == "__main__":
    day = 2
    data = get_data(2, lines=False)
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    # aocd.submit(part2(data), part="b", day=day, year=2025)
