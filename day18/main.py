"""
Author: Èric Ryhr Mateu
Day: 18
GitHub: https://github.com/ericryhr
"""

from networkx import NetworkXNoPath, astar_path, grid_graph


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    coordinates = list(map(lambda line: (int(line.strip().split(',')[1]), int(line.strip().split(',')[0])), lines))
    n = 71
    memory = [[0 for _ in range(n)] for _ in range(n)] 

    for index, (i, j) in enumerate(coordinates):
        if index >= 1024:
            break

        memory[i][j] = -1


    memory_graph = grid_graph(dim=[n, n])
    result = len(astar_path(memory_graph, (0, 0), (n-1, n-1), \
            lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]), \
            lambda p1, p2, d: None if memory[p1[0]][p1[1]] == -1 or memory[p2[0]][p2[1]] == -1 else 1)) - 1

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    coordinates = list(map(lambda line: (int(line.strip().split(',')[1]), int(line.strip().split(',')[0])), lines))
    n = 71
    memory = [[0 for _ in range(n)] for _ in range(n)] 

    for index, (i, j) in enumerate(coordinates):
        memory[i][j] = -1

        if index < 1024:
            continue

        memory_graph = grid_graph(dim=[n, n])
        try:
            astar_path(memory_graph, (0, 0), (n-1, n-1), \
                    lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]), \
                    lambda p1, p2, d: None if memory[p1[0]][p1[1]] == -1 or memory[p2[0]][p2[1]] == -1 else 1)
        except NetworkXNoPath: 
            result = f'{j},{i}'
            break

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day18/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
