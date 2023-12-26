import aocd
from pprint import pprint


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


def recursive_prediction(history: list[int]) -> int:
    if all(d == 0 for d in history):
        return 0
    diffs = [next - cur for cur, next in zip(history, history[1:])]
    return history[-1] + recursive_prediction(diffs)


def part1(data):
    """ """
    predictions = []
    for line in data:
        history = [int(n) for n in line.split()]
        predictions.append(recursive_prediction(history))
    return sum(predictions)


def prediction(history) -> int:
    prediction = history[-1]
    while True:
        diffs = [next - cur for cur, next in zip(history, history[1:])]
        prediction += diffs[-1]
        if all(d == 0 for d in diffs):
            break
        history = diffs
    return prediction


def part2(data):
    """ """
    predictions = []
    for line in data:
        history = list(reversed([int(n) for n in line.split()]))
        predictions.append(recursive_prediction(history))
    return sum(predictions)


if __name__ == "__main__":
    day = 9
    data = get_data(day)
    print(part2(data))
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
