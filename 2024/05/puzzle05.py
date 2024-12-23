import aocd
from collections import defaultdict


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2024).splitlines()
    else:
        return aocd.get_data(day=day, year=2024)


def build_order_stacks(orders) -> None:
    order_stacks = defaultdict(list)
    for line in orders.splitlines():
        page, rule = map(int, line.split("|"))
        order_stacks[page].append(rule)
    return order_stacks, page


def fix_bad_lines(line, order_stacks, page) -> None:
    bad = False
    for i, page in enumerate(line):
        pages_in_rule = set(line) & set(order_stacks[page])
        if pages_in_rule and not all(
            line.index(page) < line.index(p) for p in pages_in_rule
        ):
            bad = True
            line = sorted(
                line,
                key=lambda x: len(line) if x in order_stacks[page] else line.index(x),
            )
    return bad, line


def is_bad(line, order_stacks, page) -> None:
    for i, page in enumerate(line):
        pages_in_rule = set(line) & set(order_stacks[page])
        if pages_in_rule and not all(
            line.index(page) < line.index(p) for p in pages_in_rule
        ):
            return True
    return False


def part1(data):
    """ """
    orders, reports = data.split("\n\n")
    order_stacks, page = build_order_stacks(orders)

    total = 0
    for line in reports.splitlines():
        line = [int(x) for x in line.split(",")]
        bad = is_bad(line, order_stacks, page)
        if not bad:
            total += line[len(line) // 2]
    return total


def part2(data):
    """ """
    orders, reports = data.split("\n\n")
    order_stacks, page = build_order_stacks(orders)

    total = 0
    for line in reports.splitlines():
        line = [int(x) for x in line.split(",")]
        bad, line = fix_bad_lines(line, order_stacks, page)
        if bad:
            total += line[len(line) // 2]
    return total


if __name__ == "__main__":
    day = 5
    data = get_data(day, lines=False)
    print(part2(data))
    # aocd.submit(part1(data), part="a", day=day, year=2024)
    # aocd.submit(part2(data), part="b", day=day, year=2024)
