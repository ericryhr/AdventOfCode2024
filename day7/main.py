"""
Author: Èric Ryhr Mateu
Day: 7
GitHub: https://github.com/ericryhr
"""

def check_calibration(current, target, numbers):
    if current == target and len(numbers) == 0:
        return True
    elif current > target or len(numbers) == 0:
        return False
    
    sum_calib = check_calibration(current + numbers[0], target, numbers[1:])
    mul_calib = check_calibration(current * numbers[0], target, numbers[1:])
    return sum_calib or mul_calib


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    calibrations = list(map(lambda line: line.strip(), lines))
    result = 0
    for calibration in calibrations:
        equation = calibration.split(':')
        target = int(equation[0])
        numbers = list(map(lambda number: int(number), equation[1].split()))
        if check_calibration(0, target, numbers):
            result += target

    if result != -1:
        print("The solution to part one is: " + str(result))


def concat(n1, n2):
    return int(str(n1) + str(n2))

def check_calibration_v2(current, target, numbers):
    if current == target and len(numbers) == 0:
        return True
    elif current > target or len(numbers) == 0:
        return False
    
    sum_calib = check_calibration_v2(current + numbers[0], target, numbers[1:])
    mul_calib = check_calibration_v2(current * numbers[0], target, numbers[1:])
    concat_calib = check_calibration_v2(concat(current, numbers[0]), target, numbers[1:])
    return sum_calib or mul_calib or concat_calib


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    calibrations = list(map(lambda line: line.strip(), lines))
    result = 0
    for calibration in calibrations:
        equation = calibration.split(':')
        target = int(equation[0])
        numbers = list(map(lambda number: int(number), equation[1].split()))
        if check_calibration_v2(0, target, numbers):
            result += target

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day7/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
