"""
Author: Èric Ryhr Mateu
Day: 15
GitHub: https://github.com/ericryhr
"""


def print_map(robot_map):
    for m in robot_map:
        print(m)


def find_robot(robot_map):
    n = len(robot_map)
    m = len(robot_map[0])
    for i in range(n):
        for j in range(m):
            if robot_map[i][j] == '@':
                return (i, j)
            
    return (-1, -1)


def calculate_score(robot_map):
    result = 0
    n = len(robot_map)
    m = len(robot_map[0])
    for i in range(n):
        for j in range(m):
            if robot_map[i][j] == 'O':
                result += 100*i + j

    return result


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }

    robot_map = list(map(lambda line: list(line.strip()), lines[:lines.index('\n')]))
    movements = "".join(list(map(lambda line: line.strip(), lines[lines.index('\n')+1:])))

    r_i, r_j = find_robot(robot_map)

    for movement in movements:
        s_i, s_j = directions[movement]
        new_i, new_j = r_i + s_i, r_j + s_j

        if robot_map[new_i][new_j] == '.':
            robot_map[new_i][new_j] = '@'
            robot_map[r_i][r_j] = '.'
            r_i = new_i
            r_j = new_j
        elif robot_map[new_i][new_j] == '#':
            continue
        elif robot_map[new_i][new_j] == 'O':
            next_i, next_j = new_i + s_i, new_j + s_j
            while True:
                if robot_map[next_i][next_j] == '.':
                    robot_map[r_i][r_j] = '.'
                    robot_map[new_i][new_j] = '@'
                    robot_map[next_i][next_j] = 'O'
                    r_i = new_i
                    r_j = new_j
                    break
                elif robot_map[next_i][next_j] == '#':
                    break
                elif robot_map[new_i][new_j] == 'O':
                    next_i, next_j = next_i + s_i, next_j + s_j
                else:
                    print('Something went wrong (again)')
        else:
            print('Something went wrong!')

    result = calculate_score(robot_map)

    if result != -1:
        print("The solution to part one is: " + str(result))


def widen_row(robot_map_row):
    new_row = []
    for r in robot_map_row:
        if r == '#':
            new_row.append('#')
            new_row.append('#')
        elif r == 'O':
            new_row.append('[')
            new_row.append(']')
        elif r == '.':
            new_row.append('.')
            new_row.append('.')
        elif r == '@':
            new_row.append('@')
            new_row.append('.')

    return new_row


def calculate_box_movement_horizontal(new_i, new_j, s_i, s_j, robot_map):
    next_i, next_j = new_i + s_i*2, new_j + s_j*2
    bracket = '[' if s_j == 1 else ']'
    other_bracket = ']' if s_j == 1 else '['

    if robot_map[next_i][next_j] == '.':
        robot_map[next_i][next_j] = other_bracket
        robot_map[new_i+s_i][new_j+s_j] = bracket
        return True
    elif robot_map[next_i][next_j] == '#':
        return False
    elif robot_map[new_i][new_j] == bracket:
        if calculate_box_movement_horizontal(next_i, next_j, s_i, s_j, robot_map):
            robot_map[next_i][next_j] = other_bracket
            robot_map[new_i+s_i][new_j+s_j] = bracket
            return True
    else:
        print('Something went wrong (again)')


def check_box_movement_vertical(new_i, new_j, s_i, s_j, robot_map):
    if robot_map[new_i][new_j] == '.':
        return True
    elif robot_map[new_i][new_j] == '#':
        return False
    elif robot_map[new_i][new_j] == '[':
        next_i = new_i + s_i
        if check_box_movement_vertical(next_i, new_j, s_i, s_j, robot_map) and check_box_movement_vertical(next_i, new_j+1, s_i, s_j, robot_map):
            return True
        else: 
            return False
    elif robot_map[new_i][new_j] == ']':
        next_i = new_i + s_i
        if check_box_movement_vertical(next_i, new_j-1, s_i, s_j, robot_map) and check_box_movement_vertical(next_i, new_j, s_i, s_j, robot_map):
            return True
        else: 
            return False
    else:
        print('Something went wrong (again)')


def move_boxes_vertical(new_i, new_j, s_i, s_j, robot_map):
    if robot_map[new_i][new_j] == '[':
        next_i = new_i + s_i
        move_boxes_vertical(next_i, new_j, s_i, s_j, robot_map)
        move_boxes_vertical(next_i, new_j+1, s_i, s_j, robot_map)
        robot_map[next_i][new_j] = '['
        robot_map[next_i][new_j+1] = ']'
        robot_map[new_i][new_j] = '.'
        robot_map[new_i][new_j+1] = '.'
    elif robot_map[new_i][new_j] == ']':
        next_i = new_i + s_i
        move_boxes_vertical(next_i, new_j-1, s_i, s_j, robot_map)
        move_boxes_vertical(next_i, new_j, s_i, s_j, robot_map)
        robot_map[next_i][new_j-1] = '['
        robot_map[next_i][new_j] = ']'
        robot_map[new_i][new_j-1] = '.'
        robot_map[new_i][new_j] = '.'


def calculate_score_v2(robot_map):
    result = 0
    n = len(robot_map)
    m = len(robot_map[0])
    for i in range(n):
        for j in range(m):
            if robot_map[i][j] == '[':
                result += 100*i + j

    return result


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }

    robot_map = list(map(lambda line: widen_row(list(line.strip())), lines[:lines.index('\n')]))
    movements = "".join(list(map(lambda line: line.strip(), lines[lines.index('\n')+1:])))

    r_i, r_j = find_robot(robot_map)

    for movement in movements:
        s_i, s_j = directions[movement]
        new_i, new_j = r_i + s_i, r_j + s_j

        if robot_map[new_i][new_j] == '.':
            robot_map[new_i][new_j] = '@'
            robot_map[r_i][r_j] = '.'
            r_i = new_i
            r_j = new_j
        elif robot_map[new_i][new_j] == '#':
            continue
        # Horizontal push
        elif (robot_map[new_i][new_j] == '[' or robot_map[new_i][new_j] == ']') and s_i == 0:
            if calculate_box_movement_horizontal(new_i, new_j, s_i, s_j, robot_map):
                    robot_map[new_i][new_j] = '@'
                    robot_map[r_i][r_j] = '.'
                    r_i = new_i
                    r_j = new_j
        # Vertical push
        else:
            next_i = new_i + s_i
            if robot_map[new_i][new_j] == '[':
                if check_box_movement_vertical(next_i, new_j, s_i, s_j, robot_map) and check_box_movement_vertical(next_i, new_j+1, s_i, s_j, robot_map):
                    move_boxes_vertical(next_i, new_j, s_i, s_j, robot_map)
                    move_boxes_vertical(next_i, new_j+1, s_i, s_j, robot_map)
                    robot_map[r_i][r_j] = '.'
                    robot_map[new_i][new_j] = '@'
                    robot_map[new_i][new_j+1] = '.'
                    robot_map[next_i][new_j] = '['
                    robot_map[next_i][new_j+1] = ']'
                    r_i = new_i
                    r_j = new_j
            elif robot_map[new_i][new_j] == ']':
                if check_box_movement_vertical(next_i, new_j-1, s_i, s_j, robot_map) and check_box_movement_vertical(next_i, new_j, s_i, s_j, robot_map):
                    move_boxes_vertical(next_i, new_j-1, s_i, s_j, robot_map)
                    move_boxes_vertical(next_i, new_j, s_i, s_j, robot_map)
                    robot_map[r_i][r_j] = '.'
                    robot_map[new_i][new_j-1] = '.'
                    robot_map[new_i][new_j] = '@'
                    robot_map[next_i][new_j-1] = '['
                    robot_map[next_i][new_j] = ']'
                    r_i = new_i
                    r_j = new_j

    result = calculate_score_v2(robot_map)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day15/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
