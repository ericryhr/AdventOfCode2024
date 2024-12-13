"""
Author: Èric Ryhr Mateu
Day: 4
GitHub: https://github.com/ericryhr
"""

import numpy as np


def is_valid(i, j, n):
    return i >= 0 and i < n and j >= 0 and j < n


def search_in_lines(lines, word):
    word_backwards = word[::-1]
    count = 0

    for line in lines:
        count += line.count(word)
        count += line.count(word_backwards)

    return count


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    lines = list(map(lambda line: line.strip(), lines))
    word = 'XMAS'
    result = 0
    n = len(lines)

    # Horizontal
    result += search_in_lines(lines, word)

    # Vertical
    vertical_lines = [''.join(line) for line in zip(*lines)]
    result += search_in_lines(vertical_lines, word)

    # Diagonal left
    diag_left_lines = [""] * (n*2)
    for line in range(0, n*2 - 1):
        j = max(0, line - n + 1) 
        i = min(line, n - 1)

        while is_valid(i, j, n):
            diag_left_lines[line] += lines[i][j]
            i -= 1
            j += 1
    result += search_in_lines(diag_left_lines, word)

    # Diagonal right
    diag_right_lines = [""] * (n*2)
    for line in range(0, n*2 - 1):
        j = max(0, n - line - 1)
        i = max(0, line - n + 1)

        while is_valid(i, j, n):
            diag_right_lines[line] += lines[i][j]
            i += 1
            j += 1
    result += search_in_lines(diag_right_lines, word)

    if result != -1:
        print("The solution to part one is: " + str(result))


def check_MAS(chunk):
    word = 'MAS'
    word_backwards = 'SAM'
    diag1 = chunk[0, 0] + chunk[1, 1] + chunk[2, 2]
    diag2 = chunk[0, 2] + chunk[1, 1] + chunk[2, 0]
    if (diag1 == word or diag1 == word_backwards) and (diag2 == word or diag2 == word_backwards):
        return True
    else:
        return False

def part2(lines):
    result = -1
    # PART 2 SOLUTION

    n = len(lines)
    lines = np.array(list(map(lambda line: list(line.strip()), lines)))
    
    result = 0
    for i in range(n-2):
        for j in range(n-2):
            result += check_MAS(lines[i:i+3, j:j+3])

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day4/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
