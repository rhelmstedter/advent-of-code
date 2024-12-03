import aocd
from itertools import pairwise
from functools import wraps
from time import perf_counter_ns


def perf(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()

        time_taken = (end - start) / 1_000_000
        took = f"{time_taken:0.4f} ms"
        if time_taken > 1_000:
            seconds = time_taken / 1_000
            took = f"{seconds:0.4f} s"
        if time_taken > 1_000 * 60:
            mins = time_taken / (1_000 * 60)
            took = f"{mins:0.4f} min"
        print(f"{func.__name__} took {took}")
        return result

    return wrapper


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2024).splitlines()
    else:
        return aocd.get_data(day=day, year=2024)


def check_report(report: tuple[int]) -> bool:
    if report[0] < report[1]:
        increasing = True
    else:
        increasing = False
    for a, b in pairwise(report):
        if (increasing and a > b) or (not increasing and a < b):
            return False
        if not 1 <= abs(a - b) <= 3:
            return False
    return True


def check_report_with_all(report):
    increasing = all(a < b and 0 < b - a <= 3 for a, b in pairwise(report))
    decreasing = all(a > b and 0 < a - b <= 3 for a, b in pairwise(report))
    return increasing or decreasing


def check_report_with_damper_all(report: tuple[int]) -> bool:
    return any(
        check_report_with_all(report[:i] + report[i + 1:])
        for i in range(len(report) + 1)
    )


def check_report_with_damper(report: tuple[int]) -> bool:
    return any(
        check_report(report[:i] + report[i + 1:]) for i in range(len(report) + 1)
    )


@perf
def part1(data) -> int:
    """Solved."""
    reports = [tuple(map(int, report.split())) for report in data]
    return sum(check_report_with_all(report) for report in reports)


@perf
def part1_with_for_loop(data) -> int:
    """Solved."""
    reports = [tuple(map(int, report.split())) for report in data]
    return sum(check_report(report) for report in reports)


@perf
def part2(data) -> int:
    """Need to work on this, but too tired. Going to bed."""
    reports = [tuple(map(int, report.split())) for report in data]
    return sum(check_report_with_damper_all(report) for report in reports)


@perf
def part2_with_for_loop(data) -> int:
    """Need to work on this, but too tired. Going to bed."""
    reports = [tuple(map(int, report.split())) for report in data]
    return sum(check_report_with_damper(report) for report in reports)


if __name__ == "__main__":
    day = 2
    data = get_data(day)
    print(part1(data))
    print(part1_with_for_loop(data))
    print(part2(data))
    print(part2_with_for_loop(data))
    # aocd.submit(part1(data), part="a", day=day, year=2024)
    # aocd.submit(part2(data), part="b", day=day, year=2024)
