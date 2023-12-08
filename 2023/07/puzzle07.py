import aocd
from rich import print
from dataclasses import dataclass
from collections import Counter


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


@dataclass(order=True)
class Hand:
    _type: int
    card_values: tuple
    cards: str
    bid: int


CARD_VALUES_PART1 = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}

CARD_VALUES_PART2 = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}


def get_hand_type(cards):
    count = Counter(cards)
    mc = count.most_common()
    if mc[0][1] == 5:
        return 6
    elif mc[0][1] == 4:
        return 5
    elif mc[0][1] == 3 and mc[1][1] == 2:
        return 4
    elif mc[0][1] == 3:
        return 3
    elif mc[0][1] == 2 and mc[1][1] == 2:
        return 2
    elif mc[0][1] == 2:
        return 1
    else:
        return 0


def get_hand_type_part2(cards):
    count = Counter(cards)
    if "J" in cards and len(set(cards)) > 1:
        if count.most_common()[0][0] == "J":
            count[count.most_common()[1][0]] += count["J"]
        else:
            count[count.most_common()[0][0]] += count["J"]
        del count["J"]
    mc = count.most_common()
    if mc[0][1] == 5:
        return 6
    elif mc[0][1] == 4:
        return 5
    elif mc[0][1] == 3 and mc[1][1] == 2:
        return 4
    elif mc[0][1] == 3:
        return 3
    elif mc[0][1] == 2 and mc[1][1] == 2:
        return 2
    elif mc[0][1] == 2:
        return 1
    else:
        return 0


def tie_breaker_score(hand):
    return sum(CARD_VALUES_PART1[card] for card in hand.cards)


def part1(data):
    """ """
    hands = []
    for line in data:
        cards, bid = line.split()
        hand_type = get_hand_type(cards)
        card_values = tuple([CARD_VALUES_PART1[card] for card in cards])
        hands.append(
            Hand(cards=cards, bid=int(bid), _type=hand_type, card_values=card_values)
        )
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), 1))


def part2(data):
    """ """
    hands = []
    for line in data:
        cards, bid = line.split()
        hand_type = get_hand_type_part2(cards)
        card_values = tuple([CARD_VALUES_PART2[card] for card in cards])
        hands.append(
            Hand(cards=cards, bid=int(bid), _type=hand_type, card_values=card_values)
        )
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), 1))


if __name__ == "__main__":
    day = 7
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
