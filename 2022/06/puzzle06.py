from aocd import get_data, submit
from collections import deque


# def get_lines(day: int) -> list:
#     """Uses aocd to get the input then splits it into lines."""
#     return get_data(day=day, year=2022).splitlines()

def _sliding_window(lines, window_size):
    window = deque(lines[:window_size], maxlen=window_size)
    for chars_processed, c in enumerate(lines[window_size:], window_size):
        if len(set(window)) == len(window):
            break
        else:
            window.append(c)
    return chars_processed


def part1(lines):
    """ """
    return _sliding_window(lines, 4)


def part2(lines):
    """ """
    return _sliding_window(lines, 14)


if __name__ == "__main__":

    day = 6
    # lines = get_lines(day)
    with open("./input.txt", "r") as input_file:
        lines = input_file.read()
    print(part2(lines))
    # submit(part1(lines), part="a", day=day, year=2022)
    # submit(part2(lines), part="b", day=day, year=2022)
