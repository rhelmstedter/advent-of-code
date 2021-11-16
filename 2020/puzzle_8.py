from pyperclip import copy
test = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

def instruction_parser(line):
    """
    >>> instruction_parser('acc +1')
    ('acc', 1)
    >>> instruction_parser('acc -21')
    ('acc', -21)
    """
    instruction, operation = line.split()
    operation = int(operation.strip('+\n'))
    return instruction, operation

def accumulator(instructions):
    """
    >>> accumulator(['nop +0','acc +1','jmp +4','acc +3','jmp -3','acc -99','acc +1','jmp -4','acc +6'])
    5
    """
    index = 0
    seen = []
    accumulator = 0
    while True:
        for _ in range(len(instructions)):
            instruction, operation = instruction_parser(instructions[index])
            if instruction == 'acc':
                accumulator += operation
                seen.append(index)
                index += 1
            elif instruction == 'jmp':
                seen.append(index)
                index += operation
            else:
                seen.append(index)
                index +=1
            if index in seen:
                break
        return accumulator


def part_1():
    with open("inputs/day_8_input.txt", "r") as input:
        lines = input.readlines()
        final_value = accumulator(lines)

        print(final_value)
        copy(final_value)


def part_2():
    with open("inputs/day_8_input.txt", "r") as input:

        print(total)
        copy(total)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    part_1()
    # part_2()
