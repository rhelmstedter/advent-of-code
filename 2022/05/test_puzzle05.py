from puzzle05 import part1, part2, _parse_diagram, _parse_move, _parse_move_part2

SAMPLE_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

EXAMPLE_LINES = [line.strip("\n") for line in SAMPLE_INPUT.split()]
PART1_EXPECTED = "CMZ"
PART2_EXPECTED = "MCD"

SAMPLE_STACKS = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}

SAMPLE_MOVE1 = "move 1 from 2 to 1"
AFTER_MOVE1 = {1: ["Z", "N", "D"], 2: ["M", "C"], 3: ["P"]}

SAMPLE_MOVE2 = "move 3 from 1 to 3"
AFTER_MOVE2 = {1: [], 2: ["M", "C"], 3: ["P", "D", "N", "Z"]}

SAMPLE_MOVE3 = "move 2 from 2 to 1"
AFTER_MOVE3 = {1: ["C", "M"], 2: [], 3: ["P", "D", "N", "Z"]}

SAMPLE_MOVE4 = "move 1 from 1 to 2"
AFTER_MOVE4 = {1: ["C"], 2: ["M"], 3: ["P", "D", "N", "Z"]}


def test_parse_diagram():
    sample_diagram, _ = SAMPLE_INPUT.split("\n\n")
    actual = _parse_diagram(sample_diagram)
    assert actual == SAMPLE_STACKS


def test_parse_move1():
    actual = _parse_move(SAMPLE_STACKS, SAMPLE_MOVE1)
    assert actual == AFTER_MOVE1


def test_parse_move2():
    actual = _parse_move(AFTER_MOVE1, SAMPLE_MOVE2)
    assert actual == AFTER_MOVE2


def test_parse_move3():
    actual = _parse_move(AFTER_MOVE2, SAMPLE_MOVE3)
    assert actual == AFTER_MOVE3


def test_parse_move_part2():
    actual = _parse_move_part2(AFTER_MOVE1, SAMPLE_MOVE2)
    assert actual == {1: [], 2: ["M", "C"], 3: ["P", "Z", "N", "D"]}


def test_part1():
    actual = part1(SAMPLE_INPUT)
    print(actual)
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT)
    assert actual == PART2_EXPECTED
