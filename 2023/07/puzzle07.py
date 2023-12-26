import aocd
from dataclasses import dataclass
from collections import Counter
from enum import IntEnum


def get_data(day: int, lines: bool = True) -> str | list:
    """Use aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


class HandType(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


@dataclass(order=True)
class Hand:
    hand_type: HandType
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


def get_hand_type(cards, with_joker=False):
    count = Counter(cards)
    if with_joker:
        if "J" in cards and len(set(cards)) > 1:
            if count.most_common()[0][0] == "J":
                count[count.most_common()[1][0]] += count["J"]
            else:
                count[count.most_common()[0][0]] += count["J"]
            del count["J"]
    mc = count.most_common()
    if mc[0][1] == 5:
        return HandType.FIVE_OF_A_KIND
    elif mc[0][1] == 4:
        return HandType.FOUR_OF_A_KIND
    elif mc[0][1] == 3 and mc[1][1] == 2:
        return HandType.FULL_HOUSE
    elif mc[0][1] == 3:
        return HandType.THREE_OF_A_KIND
    elif mc[0][1] == 2 and mc[1][1] == 2:
        return HandType.TWO_PAIRS
    elif mc[0][1] == 2:
        return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD


def part1(data):
    """ """
    hands = []
    for line in data:
        cards, bid = line.split()
        hand_type = get_hand_type(cards)
        card_values = tuple([CARD_VALUES_PART1[card] for card in cards])
        hands.append(
            Hand(
                cards=cards, bid=int(bid), hand_type=hand_type, card_values=card_values,
            )
        )
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), 1))


def part2(data):
    """ """
    hands = []
    for line in data:
        cards, bid = line.split()
        hand_type = get_hand_type(cards, True)
        card_values = tuple([CARD_VALUES_PART2[card] for card in cards])
        hands.append(
            Hand(
                cards=cards, bid=int(bid), hand_type=hand_type, card_values=card_values,
            )
        )
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), 1))


if __name__ == "__main__":
    day = 7
    data = get_data(day)
    print(part2(data))
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
