import aocd
import time
from functools import wraps


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then optionally splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2025).splitlines()
    else:
        return aocd.get_data(day=day, year=2025)


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def _parse_input(data: str) -> None:
    """Turns a string into a list of tuples consisting of the start and end of a range."""
    for r in data.split(","):
        start, end = r.split("-")
        yield int(start), int(end)


def _repeats(id_str: str) -> bool:
    """Checks if an ID consists of repeating substrings."""
    # Solution using stack overflow algorithm
    return (id_str + id_str).find(id_str, 1) != len(id_str)
    # My original solution
    # len_id = len(id_str)
    # for i in range(1, len_id // 2 + 1):
    #     if not len_id % i == 0:
    #         continue
    #     chunks = set(id_str[n : i + n] for n in range(0, len_id, i))
    #     if len(chunks) == 1:
    #         return True
    # return False


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


@timeit
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
    part2(data)
    # aocd.submit(part1(data), part="a", day=day, year=2025)
    # aocd.submit(part2(data), part="b", day=day, year=2025)
