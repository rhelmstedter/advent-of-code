import pandas as pd

day = 2

with open(f"../inputs/{day}.txt") as input:
    lines = [line.strip("\n") for line in input.readlines()]


def part1(lines):
    """total score where strategy represents the preferred choice."""
    df = pd.read_csv("./rps.csv", index_col="my_move")
    my_score = 0
    for line in lines:
        opponent_move, my_move = line.split()
        if my_move == "X":
            my_score += 1
        elif my_move == "Y":
            my_score += 2
        elif my_move == "Z":
            my_score += 3

        if df.loc[my_move, opponent_move] == "win":
            my_score += 6
        elif df.loc[my_move, opponent_move] == "tie":
            my_score += 3
        elif df.loc[my_move, opponent_move] == "loss":
            my_score += 0
    return my_score


def part2(lines):
    """total score where second character represents the outcome."""
    df = pd.read_csv("./new_rules.csv", index_col="my_move")
    my_score = 0
    for line in lines:
        opponent_move, my_move = line.split()
        if my_move == "X":
            my_score += 0
        elif my_move == "Y":
            my_score += 3
        elif my_move == "Z":
            my_score += 6

        if df.loc[my_move, opponent_move] == "A":
            my_score += 1
        elif df.loc[my_move, opponent_move] == "B":
            my_score += 2
        elif df.loc[my_move, opponent_move] == "C":
            my_score += 3
    return my_score


if __name__ == "__main__":
    from pyperclip import copy

    # copy(part1(lines))
    copy(part2(lines))
