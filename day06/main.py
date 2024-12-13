"""
Author: Èric Ryhr Mateu
Day: 6
GitHub: https://github.com/ericryhr
"""

import copy
from tqdm.auto import tqdm


def get_starting_pos(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] == '^':
                return i, j


def is_valid_pos(i, j, n):
    return i >= 0 and i < n and j >= 0 and j < n


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    M = list(map(lambda line: list(line.strip()), lines))
    n = len(M)

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    new_directions = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up"
    }

    i, j = get_starting_pos(M)
    current_direction = "up"

    result = 1
    while True:
        new_i = i + directions[current_direction][0]
        new_j = j + directions[current_direction][1]

        # Sortir del mapa
        if not is_valid_pos(new_i, new_j, n):
            if M[i][j] == '.':
                result += 1
                M[i][j] = 'X'
            break
        
        # Girar
        if M[new_i][new_j] == '#':
            current_direction = new_directions[current_direction]
            continue
        
        # Avançar
        if M[i][j] == '.':
            result += 1
            M[i][j] = 'X'
        
        i = new_i
        j = new_j

    # for m in M:
    #     print(m)

    if result != -1:
        print("The solution to part one is: " + str(result))


def print_map(M):
    for m in M:
        print("".join(m))
    print()


def timeloop(starting_i, starting_j, M):
    n = len(M)
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }
    new_directions = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^"
    }
    current_direction = "^"

    i = starting_i
    j = starting_j
    
    while True:
        new_i = i + directions[current_direction][0]
        new_j = j + directions[current_direction][1]

        # Sortir del mapa
        if not is_valid_pos(new_i, new_j, n):
            return False
        
        # TIMELOOP
        if M[i][j] == current_direction and i != starting_i and j != starting_j:
            return True
        
        # Girar
        if M[new_i][new_j] == '#' or M[new_i][new_j] == 'O':
            current_direction = new_directions[current_direction]
        # Avançar
        else:
            M[i][j] = current_direction
            i = new_i
            j = new_j        


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    M = list(map(lambda line: list(line.strip()), lines))
    n = len(M)

    i, j = get_starting_pos(M)

    result = 0
    for a in tqdm(range(n*n)):
        x = a // n
        y = a % n
        if M[x][y] == '.':
            new_M = copy.deepcopy(M)
            new_M[x][y] = 'O'
            result += timeloop(i, j, new_M)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day6/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
