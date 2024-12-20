"""
Author: Èric Ryhr Mateu
Day: 20
GitHub: https://github.com/ericryhr
"""

import sys
sys.setrecursionlimit(10000)


def search_path(i, j, current_path, cpu):
    if cpu[i][j] == '#':
        return
    
    current_path.append((i, j))
    if cpu[i][j] == 'E':
        return

    cpu[i][j] = '#'
    
    search_path(i-1, j, current_path, cpu)
    search_path(i+1, j, current_path, cpu)
    search_path(i, j-1, current_path, cpu)
    search_path(i, j+1, current_path, cpu)


def search_pos(pos, cpu):
    n = len(cpu)
    for i in range(n):
        for j in range(n):
            if cpu[i][j] == pos:
                return (i, j)


def look_for_cheats_over_n(path, n=100):
    allowed_cheat_jumps = 2
    possible_cheats = 0
    
    for index_1 in range(len(path) - 4):
        for index_2 in range(index_1 + 4, len(path)):
            i_1, j_1 = path[index_1]
            i_2, j_2 = path[index_2]

            if i_1 == i_2 and abs(j_1 - j_2) <= allowed_cheat_jumps:
                cheat_size = index_2 - index_1 - 2
                if cheat_size >= n:
                    possible_cheats += 1
            if j_1 == j_2 and abs(i_1 - i_2) <= allowed_cheat_jumps:
                cheat_size = index_2 - index_1 - 2
                if cheat_size >= n:
                    possible_cheats += 1

    return possible_cheats
        
    
def part1(lines):
    result = -1
    # PART 1 SOLUTION

    cpu = list(map(lambda line: list(line.strip()), lines))
    path = []
    s_i, s_j = search_pos('S', cpu)

    search_path(s_i, s_j, path, cpu)
    result = look_for_cheats_over_n(path, 100)

    if result != -1:
        print("The solution to part one is: " + str(result))


# def look_for_cheats_over_n_v2(path, n=100):
#     allowed_cheat_jumps = 20
#     possible_cheats = 0
    
#     for index_1 in range(len(path) - 4):
#         for index_2 in range(index_1 + 4, len(path)):
#             i_1, j_1 = path[index_1]
#             i_2, j_2 = path[index_2]

#             if i_1 == i_2 and abs(j_1 - j_2) <= allowed_cheat_jumps:
#                 cheat_size = index_2 - index_1 - 2
#                 if cheat_size >= n:
#                     possible_cheats += 1
#             if j_1 == j_2 and abs(i_1 - i_2) <= allowed_cheat_jumps:
#                 cheat_size = index_2 - index_1 - 2
#                 if cheat_size >= n:
#                     possible_cheats += 1

#     return possible_cheats

def look_for_cheats_over_n_v2(path, n=50):
    allowed_cheat_jumps = 20
    possible_cheats = 0
    
    for index_1 in range(len(path) - 4):
        for index_2 in range(index_1 + 4, len(path)):
            i_1, j_1 = path[index_1]
            i_2, j_2 = path[index_2]

            cheat_jump = abs(i_1 - i_2) + abs(j_1 - j_2)
            if cheat_jump <= allowed_cheat_jumps:
                cheat_size = index_2 - index_1 - cheat_jump
                if cheat_size >= n:
                    possible_cheats += 1

    return possible_cheats


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    cpu = list(map(lambda line: list(line.strip()), lines))
    path = []
    s_i, s_j = search_pos('S', cpu)

    search_path(s_i, s_j, path, cpu)
    result = look_for_cheats_over_n_v2(path, 100)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day20/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
