from pyperclip import copy

test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def instruction_parser(line):
    """
    >>> instruction_parser('acc +1')
    ('acc', 1)
    >>> instruction_parser('acc -21')
    ('acc', -21)
    """
    instruction, operation = line.split()
    operation = int(operation.strip("+\n"))
    return instruction, operation


def accumulator(instructions):
    """
    >>> accumulator(['nop +0','acc +1','jmp +4','acc +3','jmp -3','acc -99','acc +1','jmp -4','acc +6'])
    (5, 1)
    """
    index = 0
    seen = []
    accumulator = 0
    while True:
        instruction, operation = instruction_parser(instructions[index])
        if index in seen:
            break
        seen.append(index)
        if instruction == "acc":
            accumulator += operation
            index += 1
        elif instruction == "jmp":
            index += operation
        elif instruction == "nop":
            index += 1
    return accumulator, index


def fixer(instructions):
    print(instructions)
    for i, instruction in enumerate(instructions):
        original = instruction
        if original.startswith('jmp'):
            instructions[i] = original.replace('jmp', 'nop')
            result, final_index = accumulator(instructions)
            if final_index == len(instructions):
                return result
            instructions[i] = original
        elif original.startswith('acc'):
            continue
        elif original.startswith('nop'):
            instructions[i] = original.replace('nop', 'jmp')
            result, final_index = accumulator(instructions)
            if final_index == len(instructions):
                return result
            instructions[i] = original


def part_1():
    with open("inputs/day_8_input.txt", "r") as input:
        lines = input.readlines()
        final_value = accumulator(lines)
        print(final_value)
        copy(final_value)


def part_2():
    with open("inputs/day_8_input.txt", "r") as input:
        lines = input.readlines()
        final_value = fixer(lines)
        print(final_value)
        copy(final_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # part_1()
    part_2()
