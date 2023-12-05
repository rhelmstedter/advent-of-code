import aocd

from dataclasses import dataclass


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


@dataclass
class Scratchcard:
    id: int
    winning_nums: set[int]
    your_nums: set[int]

    def count_wins(self) -> int:
        matches = self.winning_nums & self.your_nums
        return len(matches)

    def calc_points(self) -> int:
        wins = self.count_wins()
        if wins:
            return 2 ** (wins - 1)
        else:
            return 0


def scratchcard_from(line: str) -> Scratchcard:
    card_id, nums = line.split(":")
    id = int(card_id.split()[-1])
    winning_nums, your_nums = nums.split("|")
    return Scratchcard(
        id,
        {int(n) for n in winning_nums.split()},
        {int(n) for n in your_nums.split()},
    )


def part1(data):
    """ """
    return sum(scratchcard_from(line).calc_points() for line in data)


def part2(data):
    """ """
    card_counts = {i: 1 for i in range(1, len(data) + 1)}
    for line in data:
        card = scratchcard_from(line)
        for copy in range(card.id + 1, card.id + card.count_wins() + 1):
            card_counts[copy] += card_counts[card.id]
    return sum(card_counts.values())


if __name__ == "__main__":
    day = 4
    data = get_data(day)
    # part2(data)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
