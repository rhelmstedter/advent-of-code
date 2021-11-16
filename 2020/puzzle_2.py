from collections import Counter
import pyperclip


def password_validator(line):
    """
    >>> password_validator('1-13 r: gqdrspndrpsrjfjx')
    True
    """
    line = line.split()
    lower_bound = int(line[0].split("-")[0])
    upper_bound = int(line[0].split("-")[1])
    criteria = line[1].strip(":")
    password = line[2]

    counts = Counter(password)

    if criteria not in password:
        return False
    elif (counts[criteria] < lower_bound) or (counts[criteria] > upper_bound):
        return False
    return True

def password_validator2(line):
    first_position = int(line[0].split("-")[0])
    second_position = int(line[0].split("-")[1])

    criteria = line[1].strip(":")
    password = line[2]

    if (
        password[first_position - 1] == criteria
        and password[second_position - 1] == criteria
    ):
        return False
    elif (
        password[first_position - 1] == criteria
        or password[second_position - 1] == criteria
    ):
        return True
    return False


with open("inputs/puzzle_2_input.txt", "r") as input:
    num_valid_password = 0
    for line in input:
        line = line.split()
        if password_validator(line):
            num_valid_password += 1

print("Part 1")
print(num_valid_password)
pyperclip.copy(num_valid_password)


with open("inputs/day_2_input.txt", "r") as input:
    num_valid_password = 0
    for line in input:
        if password_validator(line):
            num_valid_password += 1
print("Part 2")
print(num_valid_password)
pyperclip.copy(num_valid_password)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
