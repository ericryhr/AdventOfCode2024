"""
Author: Èric Ryhr Mateu
Day: 2
GitHub: https://github.com/ericryhr
"""


def check_report(report):
    level0 = report[0]
    level1 = report[1]
    increasing = level1 > level0
    safe = True

    for i in range(len(report) - 1):
        level = report[i]
        level_next = report[i+1]

        if increasing and level_next < level:
            safe = False
            break

        if not increasing and level < level_next:
            safe = False
            break

        diff = abs(level - level_next)
        if diff < 1 or diff > 3:
            safe = False
            break

    return safe


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    reports = list(map(lambda line: list(map(lambda level: int(level), line.strip().split())), lines))

    result = 0
    for report in reports:
        if check_report(report):
            result += 1
            
    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    reports = list(map(lambda line: list(map(lambda level: int(level), line.strip().split())), lines))

    result = 0
    for report in reports:
        if check_report(report):
            result += 1
        else:
            for i in range(len(report)):
                new_rep = report.copy()
                new_rep.pop(i)
                if check_report(new_rep):
                    result += 1
                    break

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day2/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
