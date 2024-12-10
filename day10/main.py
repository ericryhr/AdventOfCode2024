"""
Author: Èric Ryhr Mateu
Day: 10
GitHub: https://github.com/ericryhr
"""

from copy import deepcopy


def search_trailheads(topographic_map):
    n = len(topographic_map)
    m = len(topographic_map[0])
    trailheads = []

    for i in range(n):
        for j in range(m):
            if topographic_map[i][j] == 0:
                trailheads.append((i, j))

    return trailheads


def is_valid_pos(pos, n):
    return 0 <= pos[0] < n and 0 <= pos[1] < n


def trailhead_score(current_pos, previous_value, destinations_found, topographic_map):
    if not is_valid_pos(current_pos, len(topographic_map)): return

    i, j = current_pos
    current_value = topographic_map[i][j]
    if current_value != previous_value + 1: return

    if current_value == 9 and (i, j) not in destinations_found:
        destinations_found.append((i, j))
        return

    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)
    
    trailhead_score(up, current_value, destinations_found, topographic_map)
    trailhead_score(down, current_value, destinations_found, topographic_map)
    trailhead_score(left, current_value, destinations_found, topographic_map)
    trailhead_score(right, current_value, destinations_found, topographic_map)

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    topographic_map = list(map(lambda line: list(map(lambda x: int(x), line.strip())), lines))
    trailheads = search_trailheads(topographic_map)
    
    result = 0
    for trailhead in trailheads:
        destinations_found = []
        trailhead_score(trailhead, -1, destinations_found, topographic_map)
        result += len(destinations_found)

    if result != -1:
        print("The solution to part one is: " + str(result))


def trailhead_score_v2(current_pos, previous_value, destinations_found, topographic_map):
    if not is_valid_pos(current_pos, len(topographic_map)): return

    i, j = current_pos
    current_value = topographic_map[i][j]
    if current_value != previous_value + 1: return

    if current_value == 9 and (i, j):
        destinations_found.append((i, j))
        return

    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)
    
    trailhead_score_v2(up, current_value, destinations_found, topographic_map)
    trailhead_score_v2(down, current_value, destinations_found, topographic_map)
    trailhead_score_v2(left, current_value, destinations_found, topographic_map)
    trailhead_score_v2(right, current_value, destinations_found, topographic_map)


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    topographic_map = list(map(lambda line: list(map(lambda x: int(x), line.strip())), lines))
    trailheads = search_trailheads(topographic_map)
    
    result = 0
    for trailhead in trailheads:
        destinations_found = []
        trailhead_score_v2(trailhead, -1, destinations_found, topographic_map)
        result += len(destinations_found)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day10/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
