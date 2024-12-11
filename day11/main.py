"""
Author: Èric Ryhr Mateu
Day: 11
GitHub: https://github.com/ericryhr
"""

from functools import cache


@cache
def calculate_number_steps(stone, n_steps):
    if n_steps == 0:
        return 1
    
    stone_str = str(stone)
    n_digits = len(stone_str)
    if stone == 0:
        return calculate_number_steps(1, n_steps-1)
    elif n_digits % 2 == 0:
        left = stone
        for _ in range(n_digits//2):
            left = left // 10

        right = stone - left * pow(10, n_digits//2)

        return calculate_number_steps(left, n_steps-1) + calculate_number_steps(right, n_steps-1)
    else:
        return calculate_number_steps(stone * 2024, n_steps-1)


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    stones = list(map(lambda stone: int(stone), lines[0].strip().split()))

    result = 0
    for stone in stones:
        result += calculate_number_steps(stone, 25)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    stones = list(map(lambda stone: int(stone), lines[0].strip().split()))

    result = 0
    for stone in stones:
        result += calculate_number_steps(stone, 75)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day11/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
