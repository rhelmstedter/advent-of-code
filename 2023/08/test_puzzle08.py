import pytest
from puzzle08 import part1, part2, _parser

SAMPLE_INPUT1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

SAMPLE_INPUT2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

PART1_EXPECTED = ...
PART2_EXPECTED = ...


def test_parser():
    actual = _parser(SAMPLE_INPUT2.splitlines())
    expected = (
        "LLR",
        {
            "AAA": {"L": "BBB", "R": "BBB"},
            "BBB": {"L": "AAA", "R": "ZZZ"},
            "ZZZ": {"L": "ZZZ", "R": "ZZZ"},
        },
    )
    assert actual == expected


@pytest.mark.parametrize("input, expected", [(SAMPLE_INPUT1, 2), (SAMPLE_INPUT2, 6)])
def test_part1(input, expected):
    actual = part1(input.splitlines())
    assert actual == expected


def test_part2():
    actual = part2(SAMPLE_INPUT1.splitlines())
    assert actual == 2
