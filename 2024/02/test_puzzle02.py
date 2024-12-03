from puzzle02 import part1, part2

SAMPLE_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

SAMPLE_INPUT2 = """2 5 6 8 6
87 89 90 93 96 99 99
13 14 15 18 19 23
67 69 71 72 73 76 82
29 32 30 31 34 35 37
54 56 54 57 54
70 73 75 74 77 79 81 81
53 55 56 59 62 61 65
90 93 95 92 99
58 61 61 64 67
36 37 37 39 42 39
32 35 38 40 40 40
17 19 19 21 22 23 25 29
"""

PART1_EXPECTED = 2
PART2_EXPECTED = 4


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED
