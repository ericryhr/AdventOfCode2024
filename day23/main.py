"""
Author: Èric Ryhr Mateu
Day: 23
GitHub: https://github.com/ericryhr
"""


def construct_graph(edge_list):
    graph = {}

    # Construct graph
    for l, r in edge_list:
        if not l in graph:
            graph[l] = [r]
        else:
            graph[l].append(r)

        if not r in graph:
            graph[r] = [l]
        else:
            graph[r].append(l)

    return graph


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    edge_list = list(map(lambda line: line.strip().split('-'), lines))
    graph = construct_graph(edge_list)

    # Find groups of 3 with a starting t
    result = 0
    for l, r in edge_list:
        l_list = graph[l]
        r_list = graph[r]
        intersection = [node for node in l_list if node in r_list]

        for node in intersection:
            if l[0] == 't' or r[0] == 't' or node[0] == 't':
                result += 1

    result //= 3

    if result != -1:
        print("The solution to part one is: " + str(result))


def find_fully_connected_set(node, current_set_index, connected_sets, graph):
    if node in connected_sets[current_set_index]:
        return
    
    for connected_node in connected_sets[current_set_index]:
        if connected_node not in graph[node]:
            return

    connected_sets[current_set_index].add(node)

    for other_node in graph[node]:
        find_fully_connected_set(other_node, current_set_index, connected_sets, graph)


def is_in_any_connected_set(node, connected_sets):
    for connected_set in connected_sets:
        if node in connected_set:
            return True
        
    return False


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    edge_list = list(map(lambda line: line.strip().split('-'), lines))
    graph = construct_graph(edge_list)

    connected_sets = [set()]
    current_set_index = 0
    for l, r in edge_list:
        if not is_in_any_connected_set(l, connected_sets):
            find_fully_connected_set(l, current_set_index, connected_sets, graph)
            current_set_index += 1
            connected_sets.append(set())

    # Find largest set
    largest_size = 0
    largest_index = -1
    for i, connected_set in enumerate(connected_sets):
        if len(connected_set) > largest_size:
            largest_size = len(connected_set)
            largest_index = i

    result = ','.join(sorted(list(connected_sets[largest_index])))

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day23/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
