"""
Author: Èric Ryhr Mateu
Day: 13
GitHub: https://github.com/ericryhr
"""

import re
from sympy import solve, Eq
from sympy.abc import x, y


def solve_system(a1, b1, c1, a2, b2, c2):
    result = solve([Eq(a1*x + b1*y, c1), Eq(a2*x + b2*y, c2)], [x, y])

    if result[x] - int(result[x]) != 0:
        return (0, 0)
    else:
        return (result[x], result[y])


# It doesn't work for part 2 for some reason (probably float precision)
# def solve_system(a1, b1, c1, a2, b2, c2):
#     x = (b2*c1 - b1*c2) / (a1*b2 - a2*b1)
#     y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)

#     if x - int(x) != 0 and y - int(y) != 0:
#         return (0, 0)
#     else:
#         return (int(x), int(y))


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    for i in range(0, len(lines), 4):
        a1 = int(re.search("X\+(\d*)", lines[i]).group(1))
        b1 = int(re.search("X\+(\d*)", lines[i+1]).group(1))
        c1 = int(re.search("X=(\d*)", lines[i+2]).group(1))
        
        a2 = int(re.search("Y\+(\d*)", lines[i]).group(1))
        b2 = int(re.search("Y\+(\d*)", lines[i+1]).group(1))
        c2 = int(re.search("Y=(\d*)", lines[i+2]).group(1))

        (x, y) = solve_system(a1, b1, c1, a2, b2, c2)

        result += 3*x + y

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    for i in range(0, len(lines), 4):
        a1 = int(re.search("X\+(\d*)", lines[i]).group(1))
        b1 = int(re.search("X\+(\d*)", lines[i+1]).group(1))
        c1 = int(re.search("X=(\d*)", lines[i+2]).group(1)) + 10000000000000
        
        a2 = int(re.search("Y\+(\d*)", lines[i]).group(1))
        b2 = int(re.search("Y\+(\d*)", lines[i+1]).group(1))
        c2 = int(re.search("Y=(\d*)", lines[i+2]).group(1)) + 10000000000000

        (x, y) = solve_system(a1, b1, c1, a2, b2, c2)

        result += 3*x + y

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day13/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
