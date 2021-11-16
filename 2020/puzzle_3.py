import pyperclip

with open("inputs/day_3_input.txt", "r") as input:
    lines = [line.strip('\n') for line in input.readlines()]
    trees = 0
    value = 0
    for level in range(1, len(lines)):
        value += 3
        value = value % len(lines[0]) 
        trees += lines[level][value] == "#"


print(trees)
pyperclip.copy(trees)

# Part 2
slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]

with open("inputs/day_3_input.txt", "r") as input:
    lines = [line.strip('\n') for line in input.readlines()]
    trees_list = []
    for right, down in slopes:
        trees = 0
        value = 0
        
        for level in range(down, len(lines), down):
            value += right
            value = value % len(lines[0]) 
            trees += lines[level][value] == "#"

        trees_list.append(trees)


    # Matt Harrison uses this in his solution.
    product = reduce(lambda x,y:x*y, trees_list)

    # product = 1
    # for tree_count in trees_list:
    #     product *= tree_count

print(product)
pyperclip.copy(product)
