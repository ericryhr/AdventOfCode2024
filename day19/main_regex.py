"""
Author: Èric Ryhr Mateu
Day: 19
GitHub: https://github.com/ericryhr
"""

from tqdm.auto import tqdm
import regexy


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    towels = lines[0].strip().split(', ')
    towel_patterns = list(map(lambda line: line.strip(), lines[2:]))

    towels = '|'.join(towels)
    pattern_matcher = f"^({towels})*$"
    nfa = regexy.compile(pattern_matcher)

    result = 0
    for towel_pattern in tqdm(towel_patterns):
        if regexy.match(nfa, towel_pattern) != None:
            result += 1

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION


    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day19/input.test"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    # part1(lines)
    part2(lines)
