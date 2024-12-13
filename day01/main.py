"""
Author: Èric Ryhr Mateu
Day: 1
GitHub: https://github.com/ericryhr
"""
import numpy as np


def part1(lines):
    result = -1
    # PART 1 SOLUTION
    pairs = list(map(lambda line: line.strip().split('   '), lines))
    left_ids = [int(left) for left, right in pairs]
    right_ids = [int(right) for left, right in pairs]

    left_ids.sort()
    right_ids.sort()

    result = 0
    for i, left in enumerate(left_ids):
        right = right_ids[i]
        result += abs(right - left)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION
    pairs = list(map(lambda line: line.strip().split('   '), lines))
    left_ids = [int(left) for left, right in pairs]
    right_ids = [int(right) for left, right in pairs]

    left_unique, left_counts = np.unique(left_ids, return_counts=True)
    right_unique, right_counts = np.unique(right_ids, return_counts=True)
    left_ids = list(zip(left_unique, left_counts))
    right_ids = dict(zip(right_unique, right_counts))

    result = 0
    for location, count in left_ids:
        if not location in right_ids:
            continue
        right_count = right_ids[location]
        result += (location * count * right_count)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day1/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
