"""
Author: Èric Ryhr Mateu
Day: 19
GitHub: https://github.com/ericryhr
"""

from functools import cache


class TowelTree:
    def __init__(self, value: str):
        self.value = value
        self.children = {}
    
    def add_child(self, node, node_type: str):
        if node_type in self.children:
            if node.value != '':
                self.children[node_type].value = node.value
        else: 
            self.children[node_type] = node

    def __str__(self):
        def recurse(node, indent=0):
            result = "--" * indent + f"{node.value}\n"
            for node_type, child in node.children.items():
                result += recurse(child, indent + 2)
            return result
        
        return recurse(self)


def build_towel_tree(towels):
    towel_tree = TowelTree('')

    for towel in towels:
        previous_node = towel_tree
        for i, char in enumerate(towel):
            if i == len(towel) - 1:
                child = TowelTree(towel)
            else:
                child = TowelTree('')

            previous_node.add_child(child, char)
            previous_node = previous_node.children[char]

    return towel_tree

@cache
def check_pattern(index, pattern, towel_tree):
    n = len(pattern)
    if index == n:
        return True
    
    current_node = towel_tree
    for i in range(index, n):
        char = pattern[i]
        if not char in current_node.children:
            return False
        
        current_node = current_node.children[char]

        if current_node.value != '':
            if check_pattern(i+1, pattern, towel_tree):
                return True

    return False


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    towels = lines[0].strip().split(', ')
    towel_tree = build_towel_tree(towels)
    patterns = lines[2:]

    result = 0
    for i, pattern in enumerate(patterns):
        pattern = pattern.strip()
        result += check_pattern(0, pattern, towel_tree)

    if result != -1:
        print("The solution to part one is: " + str(result))


@cache
def check_pattern_v2(index, pattern, towel_tree):
    n = len(pattern)
    if index == n:
        return 1
    
    possible_patterns = 0
    
    current_node = towel_tree
    for i in range(index, n):
        char = pattern[i]
        if not char in current_node.children:
            return possible_patterns
        
        current_node = current_node.children[char]

        if current_node.value != '':
            possible_patterns += check_pattern_v2(i+1, pattern, towel_tree)

    return possible_patterns


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    towels = lines[0].strip().split(', ')
    towel_tree = build_towel_tree(towels)
    patterns = lines[2:]

    result = 0
    for i, pattern in enumerate(patterns):
        pattern = pattern.strip()
        num_patterns = check_pattern_v2(0, pattern, towel_tree)
        result += num_patterns

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day19/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
