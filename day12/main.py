"""
Author: Èric Ryhr Mateu
Day: 12
GitHub: https://github.com/ericryhr
"""

from dataclasses import dataclass


global_plots_explored_1 = set()
global_plots_explored_2 = set()


def is_valid_index(i, j, n):
    return 0 <= i < n and 0 <= j < n


def calculate_region_info(i, j, region_type, local_plots_explored, farm):
    if not is_valid_index(i, j, len(farm)):
        return (0, 1)   # +1 perimeter

    if farm[i][j] != region_type:
        return (0, 1)   # +1 perimeter
    
    if (i, j) in local_plots_explored:
        return (0, 0)
    else:
        local_plots_explored.add((i, j))
        global_plots_explored_1.add((i, j))
        
    # Up
    i_up, j_up = i-1, j
    area_up, perimeter_up = calculate_region_info(i_up, j_up, region_type, local_plots_explored, farm)

    # Down
    i_down, j_down = i+1, j
    area_down, perimeter_down = calculate_region_info(i_down, j_down, region_type, local_plots_explored, farm)

    # Left
    i_left, j_left = i, j-1
    area_left, perimeter_left = calculate_region_info(i_left, j_left, region_type, local_plots_explored, farm)

    # Right
    i_right, j_right = i, j+1
    area_right, perimeter_right = calculate_region_info(i_right, j_right, region_type, local_plots_explored, farm)

    return (1 + area_up + area_down + area_left + area_right, perimeter_up + perimeter_down + perimeter_left + perimeter_right)


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    farm = list(map(lambda line: list(line.strip()), lines))
    n = len(farm)
    
    result = 0
    for i in range(n):
        for j in range(n):
            if (i, j) in global_plots_explored_1:
                continue
            
            area, perimeter = calculate_region_info(i, j, farm[i][j], set(), farm)
            result += area*perimeter

    if result != -1:
        print("The solution to part one is: " + str(result))


@dataclass
class Perimeter:
    out_i: int
    out_j: int
    in_i: int
    in_j: int


def calculate_region_info_v2(i, j, region_type, local_plots_explored, farm, prev_i=-1, prev_j=-1):
    if not is_valid_index(i, j, len(farm)):
        return (0, [Perimeter(i, j, prev_i, prev_j)])   # +1 perimeter

    if farm[i][j] != region_type:
        return (0, [Perimeter(i, j, prev_i, prev_j)])   # +1 perimeter
    
    if (i, j) in local_plots_explored:
        return (0, [])
    else:
        local_plots_explored.add((i, j))
        global_plots_explored_2.add((i, j))
        
    # Up
    i_up, j_up = i-1, j
    area_up, perimeter_up = calculate_region_info_v2(i_up, j_up, region_type, local_plots_explored, farm, i, j)

    # Down
    i_down, j_down = i+1, j
    area_down, perimeter_down = calculate_region_info_v2(i_down, j_down, region_type, local_plots_explored, farm, i, j)

    # Left
    i_left, j_left = i, j-1
    area_left, perimeter_left = calculate_region_info_v2(i_left, j_left, region_type, local_plots_explored, farm, i, j)

    # Right
    i_right, j_right = i, j+1
    area_right, perimeter_right = calculate_region_info_v2(i_right, j_right, region_type, local_plots_explored, farm, i, j)

    area = 1 + area_up + area_down + area_left + area_right
    perimeters = perimeter_up + perimeter_down + perimeter_left + perimeter_right
    return (area, perimeters)


# Spaguetti code
def calculate_perimeter_set(perimeters: list[Perimeter], farm):
    p: Perimeter = perimeters.pop()
    perimeter_set = [[p]]
    perimeter_index = 0

    while len(perimeters) > 0:
        # Check horizontal
        possible_horizontal = [index for index, p2 in enumerate(perimeters) 
                                if p.out_i == p2.out_i and p.in_i == p2.in_i and
                                abs(p.out_j - p2.out_j) == 1 and abs(p.in_j - p2.in_j) == 1]
        if len(possible_horizontal) > 0:
            p = perimeters.pop(possible_horizontal[0])
            perimeter_set[perimeter_index].append(p)
            continue

        # Check vertical
        possible_vertical = [index for index, p2 in enumerate(perimeters) 
                                if p.out_j == p2.out_j and p.in_j == p2.in_j and
                                abs(p.out_i - p2.out_i) == 1 and abs(p.in_i - p2.in_i) == 1]
        if len(possible_vertical) > 0:
            p = perimeters.pop(possible_vertical[0])
            perimeter_set[perimeter_index].append(p)
            continue

        # Check diagonal
        possible_diagonal = [index for index, p2 in enumerate(perimeters) 
                                if (p.in_i == p2.in_i and p.in_j == p2.in_j and
                                abs(p.out_i - p2.out_i) == 1 and abs(p.out_j - p2.out_j) == 1) or
                                (p.out_i == p2.out_i and p.out_j == p2.out_j and
                                abs(p.in_i - p2.in_i) == 1 and abs(p.in_j - p2.in_j) == 1)]
        if len(possible_diagonal) > 0:
            current_type = farm[p.in_i][p.in_j]
            for diagonal_index in possible_diagonal:
                p2 = perimeters[diagonal_index]
                i = p.in_i if p.in_i != p.out_i else p2.in_i
                j = p.in_j if p.in_j != p.out_j else p2.in_j
                if p.out_i == p2.out_i and farm[i][j] != current_type:
                    continue
                else:
                    p = perimeters.pop(diagonal_index)
                    perimeter_set[perimeter_index].append(p)
                    break
        else:
            p = perimeters.pop()
            perimeter_index += 1
            perimeter_set.append([p])
    
    return perimeter_set


def calculate_perimeter_score(perimeters: list[Perimeter]):
    result = 0

    for perimeter in perimeters:
        p = perimeter[-1]

        for p2 in perimeter:
            # Same row
            if p.in_i == p2.in_i and p.out_i == p2.out_i:
                pass
            # Same col
            elif p.in_j == p2.in_j and p.out_j == p2.out_j:
                pass
            else:
                result += 1
            
            p = p2

    return result


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    farm = list(map(lambda line: list(line.strip()), lines))
    n = len(farm)
    
    result = 0
    for i in range(n):
        for j in range(n):
            if (i, j) in global_plots_explored_2:
                continue
            
            area, perimeters = calculate_region_info_v2(i, j, farm[i][j], set(), farm)
            perimeter_set = calculate_perimeter_set(perimeters, farm)
            perimeter_score = calculate_perimeter_score(perimeter_set)

            result += area * perimeter_score

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day12/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
