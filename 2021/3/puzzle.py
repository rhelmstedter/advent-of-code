from pyperclip import copy

with open("inputs/day3.txt", "r", encoding="uft-8") as p_input:
    diagnostics = p_input.readlines()


position_sums = [0 for bit in range(len(diagnostics[0].strip()))]
for number in diagnostics:
    for i, bit in enumerate(number.strip()):
        position_sums[i] += int(bit)


def construct_rates(position_sums):
    gamma = ""
    epsilon = ""
    for position in position_sums:
        if position > len(diagnostics) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2), int(epsilon, 2)


def part_1():
    gamma, epsilon = construct_rates(position_sums)
    print(gamma * epsilon)
    copy(gamma * epsilon)


if __name__ == "__main__":
    part_1()
