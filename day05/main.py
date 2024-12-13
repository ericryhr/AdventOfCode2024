"""
Author: Èric Ryhr Mateu
Day: 5
GitHub: https://github.com/ericryhr
"""

from functools import cmp_to_key


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    rules = lines[:lines.index('\n')]
    updates = lines[lines.index('\n')+1:]

    rules = list(map(lambda line: list(map(lambda x: int(x), line.strip().split('|'))), rules))
    updates = list(map(lambda line: list(map(lambda x: int(x), line.strip().split(','))), updates))

    result = 0
    for update in updates:
        valid = True
        applied_rules = list(filter(lambda rule: rule[0] in update or rule[1] in update, rules))
        for i, value in enumerate(update):
            other_values = update[i+1:]
            if len(list(filter(lambda rule: rule[0] in other_values and rule[1] == value, applied_rules))) > 0:
                valid = False
                break
        
        if valid:
            result += update[len(update)//2]

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    rules = lines[:lines.index('\n')]
    updates = lines[lines.index('\n')+1:]

    rules = list(map(lambda line: list(map(lambda x: int(x), line.strip().split('|'))), rules))
    updates = list(map(lambda line: list(map(lambda x: int(x), line.strip().split(','))), updates))

    result = 0
    for update in updates:
        valid = True
        applied_rules = list(filter(lambda rule: rule[0] in update or rule[1] in update, rules))
        for i, value in enumerate(update):
            other_values = update[i+1:]
            if len(list(filter(lambda rule: rule[0] in other_values and rule[1] == value, applied_rules))) > 0:
                valid = False
                break
        
        if not valid:
            new_update = sorted(update, key=cmp_to_key(lambda x, y: 0 if x == y else
                                                +1 if len(list(filter(lambda rule: rule[0] == x and rule[1] == y, applied_rules))) > 0
                                                else -1))
            result += new_update[len(new_update)//2]

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day5/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
