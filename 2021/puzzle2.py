<<<<<<< HEAD
with open("./inputs/day2.txt") as input:
    course = input.readlines()

print(course)
=======
from pyperclip import copy

with open("inputs/day2.txt", "r") as input:
    course = input.read().split("\n")


def final_destination_simple(course):
    range = 0
    depth = 0
    parsed_course = [direction.split() for direction in course]

    for bearing, board in parsed_course:
        if bearing == "forward":
            range += int(board)
        elif bearing == "up":
            depth -= int(board)
        elif bearing == "down":
            depth += int(board)

    return range, depth


def final_destination_with_aim(course):
    range = 0
    depth = 0
    aim = 0
    parsed_course = [direction.split() for direction in course]

    for bearing, board in parsed_course:
        if bearing == "forward":
            range += int(board)
            depth += aim * int(board)
        elif bearing == "up":
            aim -= int(board)
        elif bearing == "down":
            aim += int(board)

    return range, depth


def part_1():
    range, depth = final_destination_simple(course)
    print(range * depth)
    copy(range * depth)


def part_2():
    range, depth = final_destination_with_aim(course)
    print(range * depth)
    copy(range * depth)


if __name__ == "__main__":
    # part_1()
    part_2()
>>>>>>> 442fe14be1849c24db0e1a6841f30a8fa1ff469e
