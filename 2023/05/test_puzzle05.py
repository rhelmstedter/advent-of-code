from puzzle05 import part1, part2, _parser, _mapper
from rich import print

SAMPLE_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

seeds, maps = _parser(SAMPLE_INPUT.splitlines())

PART1_EXPECTED = 35
PART2_EXPECTED = 46


def test_mapper():
    assert _mapper(79, maps["seed-to-soil map"]) == 81
    assert _mapper(14, maps["seed-to-soil map"]) == 14
    assert _mapper(55, maps["seed-to-soil map"]) == 57
    assert _mapper(13, maps["seed-to-soil map"]) == 13
    assert _mapper(81, maps["water-to-light map"]) == 74


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED
