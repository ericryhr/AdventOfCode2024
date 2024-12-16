"""
Author: Èric Ryhr Mateu
Day: 14
GitHub: https://github.com/ericryhr
"""

import re


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    n = 103
    m = 101

    quadrants = [0, 0, 0, 0]

    for line in lines:
        info = re.findall("p=(\d*),(\d*) v=(-?\d*),(-?\d*)", line.strip())[0]
        p_j, p_i, v_j, v_i = int(info[0]), int(info[1]), int(info[2]), int(info[3])

        f_i = (p_i + 100*v_i) % n
        f_j = (p_j + 100*v_j) % m

        if f_i == n//2 or f_j == m//2: continue # Middle points

        quadrant_index = 0
        quadrant_index += 2 if f_i > n//2 else 0
        quadrant_index += 1 if f_j > m//2 else 0

        quadrants[quadrant_index] += 1

    result = 1
    for q in quadrants:
        result *= q

    if result != -1:
        print("The solution to part one is: " + str(result))


def check_repeated_spaces(robot_map):
    n = len(robot_map)
    m = len(robot_map[0])
    for i in range(n):
        for j in range(m):
            if robot_map[i][j] > 1:
                return True
    return False


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    n = 103
    m = 101

    robot_map = [[0 for _ in range(m)] for _ in range(n)]
    robots = []

    for line in lines:
        info = re.findall("p=(\d*),(\d*) v=(-?\d*),(-?\d*)", line.strip())[0]
        p_j, p_i, v_j, v_i = int(info[0]), int(info[1]), int(info[2]), int(info[3])

        robots.append((p_i, p_j, v_i, v_j))
        robot_map[p_i][p_j] += 1

    result = 0
    while check_repeated_spaces(robot_map):
        for robot_index, robot in enumerate(robots):
            p_i, p_j, v_i, v_j = robot
            new_i = (p_i + v_i) % n
            new_j = (p_j + v_j) % m
            robot_map[p_i][p_j] -= 1
            robot_map[new_i][new_j] += 1
            robots[robot_index] = (new_i, new_j, v_i, v_j)
        result += 1

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day14/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
