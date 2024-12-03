import aocd
from itertools import pairwise


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2024).splitlines()
    else:
        return aocd.get_data(day=day, year=2024)


def check_report(report: tuple[int]) -> bool:
    if len(report) != len(set(report)):
        return False
    elif report[0] < report[1]:
        increasing = True
    else:
        increasing = False
    for a, b in pairwise(report):
        if (increasing and a > b) or (not increasing and a < b):
            return False
        if abs(a - b) > 3:
            return False
    return True


def check_report_original(report):
    if len(report) != len(set(report)):
        return False
    increasing = all(a < b and b - a <= 3 for a, b in pairwise(report))
    decreasing = all(a > b and a - b <= 3 for a, b in pairwise(report))
    return increasing or decreasing


def check_report_with_damper(report: tuple[int]) -> int:
    for i in range(len(report) + 1):
        dampened = report[:i] + report[i + 1:]
        if check_report_original(dampened):
            return 1
    return 0


def part1(data) -> int:
    """Solved."""
    reports = [tuple(map(int, report.split())) for report in data]
    return sum(check_report_original(report) for report in reports)


def part2(data) -> int:
    """Need to work on this, but too tired. Going to bed."""
    reports = [tuple(map(int, report.split())) for report in data]
    good = 0
    for report in reports:
        if check_report_original(report):
            good += 1
        else:
            good += check_report_with_damper(report)
    return good


if __name__ == "__main__":
    day = 2
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2024)
    # aocd.submit(part2(data), part="b", day=day, year=2024)
