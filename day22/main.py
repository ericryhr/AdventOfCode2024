"""
Author: Èric Ryhr Mateu
Day: 22
GitHub: https://github.com/ericryhr
"""

from numba import njit
from numba.typed import List
from tqdm.auto import tqdm


@njit
def get_next_number(number):
    secret = ((number*64) ^ number) % 16777216
    secret = ((secret//32) ^ secret) % 16777216
    secret = ((secret*2048) ^ secret) % 16777216
    return secret


@njit
def get_number_after_iterations(number, iterations=2000):
    for _ in range(iterations):
        number = get_next_number(number)

    return number


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    numbers = list(map(lambda line: int(line.strip()), lines))

    result = 0
    for number in tqdm(numbers):
        result += get_number_after_iterations(number, 2000)

    if result != -1:
        print("The solution to part one is: " + str(result))


def generate_sequences():
    sequences = []

    for n1 in range(10):
        for n2 in range(10):
            for n3 in range(10):
                for n4 in range(10):
                    for n5 in range(10):
                        i1 = n2-n1
                        i2 = n3-n2
                        i3 = n4-n3
                        i4 = n5-n4
                        sequence = [i1, i2, i3, i4]
                        sequences.append(sequence)

    return sequences


@njit
def get_prices_iterations(number, iterations=2000):
    prices = [number%10]

    for _ in range(iterations):
        number = get_next_number(number)
        prices.append(number%10)

    return prices


@njit
def find_first_occurrence_of_sequence(prices, sequence):
    i1, i2, i3, i4 = sequence

    for i in range(4, len(prices)):
        n1 = prices[i-4]
        n2 = prices[i-3]
        n3 = prices[i-2]
        n4 = prices[i-1]
        n5 = prices[i]

        if n2-n1 == i1 and n3-n2 == i2 and n4-n3 == i3 and n5-n4 == i4:
            return n5
    
    return 0


@njit
def check_sequence(sequence, prices_for_numbers):
    current_result = 0
    for prices in prices_for_numbers:
        first_occurrence = find_first_occurrence_of_sequence(prices, sequence)
        current_result += first_occurrence

    return current_result


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    numbers = list(map(lambda line: int(line.strip()), lines))
    sequences = generate_sequences()
    prices_for_numbers = List(map(lambda number: List(get_prices_iterations(number, 2000)), numbers))
    
    result = 0
    for sequence in tqdm(sequences):
        sequence_score = check_sequence(sequence, prices_for_numbers)
        result = max(sequence_score, result)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day22/input.test2"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    # part1(lines)
    part2(lines)
