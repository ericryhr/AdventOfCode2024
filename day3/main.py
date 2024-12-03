"""
Author: Èric Ryhr Mateu
Day: 3
GitHub: https://github.com/ericryhr
"""

import re


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    program = "".join(lines)
    matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)", program)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    program = "".join(lines)
    matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", program)
    result = 0
    active = True
    for match in matches:
        if match[2] == "do":
            active = True
        elif match[3] == "don't":
            active = False
        elif active:
            result += int(match[0]) * int(match[1])

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day3/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
