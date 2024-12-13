"""
Author: Èric Ryhr Mateu
Day: 8
GitHub: https://github.com/ericryhr
"""


def is_valid_pos(i, j, n):
    return 0 <= i < n and 0 <= j < n


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    antena_locations = {}

    signal_map = list(map(lambda line: list(line.strip()), lines))
    n = len(signal_map)

    # Construct antena map
    for i in range(n):
        for j in range(n):
            antena = signal_map[i][j]
            if antena != '.':
                if antena not in antena_locations:
                    antena_locations[antena] = [(i, j)]
                else: 
                    antena_locations[antena].append((i, j))

    # Look for antipodes
    result = 0
    for antena, locations in antena_locations.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                x_1, y_1 = locations[i]
                x_2, y_2 = locations[j]

                dist_x = x_2 - x_1
                dist_y = y_2 - y_1

                ax_1, ay_1 = x_1 - dist_x, y_1 - dist_y
                ax_2, ay_2 = x_2 + dist_x, y_2 + dist_y

                if is_valid_pos(ax_1, ay_1, n):
                    if signal_map[ax_1][ay_1] != '#':
                        signal_map[ax_1][ay_1] = '#'
                        result += 1
                if is_valid_pos(ax_2, ay_2, n):
                    if signal_map[ax_2][ay_2] != '#':
                        signal_map[ax_2][ay_2] = '#'
                        result += 1

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    antena_locations = {}

    signal_map = list(map(lambda line: list(line.strip()), lines))
    n = len(signal_map)

    # Construct antena map
    for i in range(n):
        for j in range(n):
            antena = signal_map[i][j]
            if antena != '.':
                if antena not in antena_locations:
                    antena_locations[antena] = [(i, j)]
                else: 
                    antena_locations[antena].append((i, j))

    # Look for antipodes
    result = 0
    for antena, locations in antena_locations.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                x_1, y_1 = locations[i]
                x_2, y_2 = locations[j]

                dist_x = x_2 - x_1
                dist_y = y_2 - y_1

                # Start at each antena
                ax_1, ay_1 = x_1, y_1
                ax_2, ay_2 = x_2, y_2

                while is_valid_pos(ax_1, ay_1, n):
                    if signal_map[ax_1][ay_1] != '#':
                        signal_map[ax_1][ay_1] = '#'
                        result += 1
                    ax_1, ay_1 = ax_1 - dist_x, ay_1 - dist_y

                while is_valid_pos(ax_2, ay_2, n):
                    if signal_map[ax_2][ay_2] != '#':
                        signal_map[ax_2][ay_2] = '#'
                        result += 1
                    ax_2, ay_2 = ax_2 + dist_x, ay_2 + dist_y

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day8/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
