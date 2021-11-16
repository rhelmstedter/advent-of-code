from pyperclip import copy

def group_answer_counts(group):
    answers = set()
    for individual in group:
        answers.update(individual)
    return len(answers)


with open("inputs/day_6_input.txt", 'r') as input:
    group_answers = [line.strip("\n").split() for line in input.readlines()] 

total = sum([group_answer_counts(group) for group in group_answers])
print(total)
copy(total)

# Part 2
from collections import Counter

def group_counts(group):
    response_counts = Counter()
    for individual in group:
        response_counts.update(Counter(individual))
    return response_counts


def count_if_everyone_ansered(group_counts, group_length):
    return len([count for count in group_counts.values() if count == group_length])


with open("inputs/day_6_input.txt", 'r') as input:
    group_answers = [line.strip("\n").split() for line in input.readlines()] 

total = sum([count_if_everyone_ansered(group_counts(group), len(group))for group in group_answers])
print(total)
copy(total)
