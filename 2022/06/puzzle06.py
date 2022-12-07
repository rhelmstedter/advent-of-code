from aocd import get_data, submit
from collections import deque


def get_lines(day: int) -> list:
    """Uses aocd to get the input then splits it into data."""
    return get_data(day=day, year=2022).splitlines()


def _sliding_window(data, window_size):
    """Return the number of characters processed until a window with all
    unique chars.
    """
    window = deque(data[:window_size], maxlen=window_size)
    for chars_processed, c in enumerate(data[window_size:], window_size):
        if len(set(window)) == len(window):
            break
        else:
            window.append(c)
    return chars_processed


def part1(data):
    """Use a sliding window of width 4."""
    return _sliding_window(data, 4)


def part2(data):
    """Use a sliding window of width 14."""
    return _sliding_window(data, 14)


if __name__ == "__main__":

    day = 6
    data = get_data(day=day, year=2022)
    # submit(part1(data), part="a", day=day, year=2022)
    # submit(part2(data), part="b", day=day, year=2022)
