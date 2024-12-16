"""
Author: Èric Ryhr Mateu
Day: 16
GitHub: https://github.com/ericryhr
"""
import numpy as np
import sys
sys.setrecursionlimit(10000)


def get_pos(char, maze):
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == char:
                return (i, j)
    return (-1, -1)


directions = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1),
}

possible_turns = {
    0: [2, 3],
    1: [2, 3],
    2: [0, 1],
    3: [0, 1],
}


def gen_best_route(i, j, direction, current_score, maze, route_scores):
    if maze[i][j] == '#': return
    if route_scores[i, j, direction//2] < current_score: return

    route_scores[i, j, direction//2] = current_score
    if maze[i][j] == 'E': return

    s_i, s_j = directions[direction]
    new_i, new_j = i + s_i, j + s_j

    # Forward
    gen_best_route(new_i, new_j, direction, current_score+1, maze, route_scores)

    # Turns
    gen_best_route(i, j, possible_turns[direction][0], current_score+1000, maze, route_scores)
    gen_best_route(i, j, possible_turns[direction][1], current_score+1000, maze, route_scores)


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    maze = list(map(lambda line: list(line.strip()), lines))
    n = len(maze)
    m = len(maze[0])

    i, j = get_pos('S', maze)
    route_scores = np.full((n, m, 2), 100000000)

    gen_best_route(i, j, 3, 0, maze, route_scores)

    end_i, end_j = get_pos('E', maze)
    result = min(route_scores[end_i, end_j])
    
    if result != -1:
        print("The solution to part one is: " + str(result))


iterations = 0


def gen_best_route_v2(i, j, direction, current_score, current_route: list, maze, route_scores, routes_that_reached_the_end):
    if maze[i][j] == '#': return
    if route_scores[i, j, direction//2] < current_score: return

    route_scores[i, j, direction//2] = current_score
    if maze[i][j] == 'E':
        routes_that_reached_the_end.append((current_score, current_route.copy()))
        return

    global iterations
    iterations += 1
    if iterations % 1000000 == 0:
        print(f'Iterations: {iterations}')

    s_i, s_j = directions[direction]
    new_i, new_j = i + s_i, j + s_j

    # Forward
    current_route.append((new_i, new_j))
    gen_best_route_v2(new_i, new_j, direction, current_score+1, current_route, maze, route_scores, routes_that_reached_the_end)
    del current_route[-1]

    # Turns
    gen_best_route_v2(i, j, possible_turns[direction][0], current_score+1000, current_route, maze, route_scores, routes_that_reached_the_end)
    gen_best_route_v2(i, j, possible_turns[direction][1], current_score+1000, current_route, maze, route_scores, routes_that_reached_the_end)


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    maze = list(map(lambda line: list(line.strip()), lines))
    n = len(maze)
    m = len(maze[0])

    i, j = get_pos('S', maze)
    route_scores = np.full((n, m, 2), 100000000)
    routes_that_reached_the_end = []

    gen_best_route_v2(i, j, 3, 0, [], maze, route_scores, routes_that_reached_the_end)

    min_score = min(list(map(lambda r: r[0], routes_that_reached_the_end)))
    filtered_routes = list(filter(lambda r: r[0] == min_score, routes_that_reached_the_end))

    result = 1
    best_tiles = np.zeros((n, m), dtype=int)
    for _, route in filtered_routes:
        for i, j in route:
            maze[i][j] = 'O'
            if best_tiles[i, j] == 0:
                result += 1
                best_tiles[i, j] = 1

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day16/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    # part1(lines)
    part2(lines)
