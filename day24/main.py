"""
Author: Èric Ryhr Mateu
Day: 24
GitHub: https://github.com/ericryhr
"""

from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Operation:
    left: str
    right: str
    result: str
    operator: str

    def __str__(self):
        return f'{self.left} {self.operator} {self.right} -> {self.result}'


def get_init_variables(init_variables):
    variables = {}

    for line in init_variables:
        name, value = line.strip().split(': ')
        variables[name] = int(value)

    return variables


def get_sorted_operations(init_operations, variables):
    operations = []

    for line in init_operations:
        left, operator, right, _, result = line.strip().split()
        operation = Operation(left, right, result, operator)
        operations.append(operation)

    # Sort operations
    sorted_operations = []

    while len(operations) > 0:
        operations_to_remove = []
        for operation in operations:
            if operation.left in variables and operation.right in variables:
                variables[operation.result] = -1
                operations_to_remove.append(operation)
                sorted_operations.append(operation)

        for operation in operations_to_remove:
            operations.remove(operation)

    return sorted_operations


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    init_variables = lines[:lines.index('\n')]
    init_operations = lines[lines.index('\n')+1:]

    variables = get_init_variables(init_variables)
    operations = get_sorted_operations(init_operations, variables)

    for operation in operations:
        if operation.left == -1 or operation.right == -1:
            print('ERROR')

        match operation.operator:
            case 'AND':
                variables[operation.result] = variables[operation.left] & variables[operation.right]
            case 'OR':
                variables[operation.result] = variables[operation.left] | variables[operation.right]
            case 'XOR':
                variables[operation.result] = variables[operation.left] ^ variables[operation.right]

    sorted_zs = sorted(list(filter(lambda key: key[0] == 'z', variables.keys())))

    result = 0
    for i, z in enumerate(sorted_zs):
        result += variables[z] * (1 << i)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    init_variables = lines[:lines.index('\n')]
    init_operations = lines[lines.index('\n')+1:]

    variables = get_init_variables(init_variables)
    operations = get_sorted_operations(init_operations, variables)

    # Find largest digit
    digit_size = len(list(filter(lambda key: key[0] == 'z', variables.keys())))
    previous_carry = ''
    for d in range(digit_size-1):
        char_d = '0' + str(d) if d < 10 else str(d)
        if d == 0:
            xor_rule = list(filter(lambda o: o.operator == 'XOR' and (o.left[1:] == char_d or o.right[1:] == char_d), operations))[0]
            and_rule = list(filter(lambda o: o.operator == 'AND' and (o.left[1:] == char_d or o.right[1:] == char_d), operations))[0]
            previous_carry = and_rule.result
            print(xor_rule)
            print(and_rule)
        else:
            xor_rule_1 = list(filter(lambda o: o.operator == 'XOR' and (o.left[1:] == char_d or o.right[1:] == char_d), operations))[0]
            and_rule_1 = list(filter(lambda o: o.operator == 'AND' and (o.left[1:] == char_d or o.right[1:] == char_d), operations))[0]
            print(xor_rule_1)
            print(and_rule_1)

            xor_rule_2 = list(filter(lambda o: o.operator == 'XOR' and (o.left == previous_carry or o.right == previous_carry), operations))
            if len(xor_rule_2) == 0:
                print(f'XOR break on {char_d}')
                break
            else:
                xor_rule_2 = xor_rule_2[0]
                print(xor_rule_2)

            and_rule_2 = list(filter(
                lambda o: o.operator == 'AND' and \
                    ((o.left == xor_rule_1.result and o.right == previous_carry) or \
                    (o.left == previous_carry and o.right == xor_rule_1.result)),
                operations
            ))

            if len(and_rule_2) == 0:
                print(f'AND break on {char_d}')
                break
            else:
                and_rule_2 = and_rule_2[0]
                print(and_rule_2)

            or_rule = list(filter(
                lambda o: o.operator == 'OR' and \
                    ((o.left == and_rule_2.result and o.right == and_rule_1.result) or \
                    (o.left == and_rule_1.result and o.right == and_rule_2.result)),
                operations
            ))

            if len(or_rule) == 0:
                print(f'OR break on {char_d}')
                break
            else:
                or_rule = or_rule[0]
                print(or_rule)
                previous_carry = or_rule.result

        print()

    result = ','.join(sorted(['z07', 'vmv', 'z20', 'kfm', 'z28', 'hnv', 'hth', 'tqr']))

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day24/input.fixed"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
