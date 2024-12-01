from puzzle01 import part1, part2
from aocd.models import Puzzle


example = Puzzle(year=2024, day=1).examples[0]

print(example)
SAMPLE_INPUT = example.input_data


PART1_EXPECTED = int(example.answer_a)
PART2_EXPECTED = int(example.answer_b)


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED
