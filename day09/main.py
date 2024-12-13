"""
Author: Èric Ryhr Mateu
Day: 9
GitHub: https://github.com/ericryhr
"""

from dataclasses import dataclass, replace


def get_disk(disk_map):
    disk = []
    current_id = 0
    current_is_free_space = False
    for disk_pos in disk_map:
        if current_is_free_space:
            for _ in range(disk_pos):
                disk.append(-1)
        else:
            for _ in range(disk_pos):
                disk.append(current_id)
            current_id += 1
        current_is_free_space = not current_is_free_space
    return disk


def rearrange_disk(disk):
    rearranged_disk = disk.copy()
    free_space_pointer = rearranged_disk.index(-1)
    data_pointer = len(rearranged_disk)-1
    while(rearranged_disk[data_pointer] == -1): data_pointer -= 1

    while free_space_pointer < data_pointer:
        rearranged_disk[free_space_pointer] = rearranged_disk[data_pointer]
        rearranged_disk[data_pointer] = -1

        # Update pointers
        while(rearranged_disk[free_space_pointer] != -1): free_space_pointer += 1
        while(rearranged_disk[data_pointer] == -1): data_pointer -= 1

    return rearranged_disk


def compute_checksum(disk):
    result = 0
    for i, data in enumerate(disk):
        if data == -1: return result
        result += i * data

    return result


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    disk_map = list(map(lambda x: int(x), lines[0].strip()))

    disk = get_disk(disk_map)
    rearranged_disk = rearrange_disk(disk)
    result = compute_checksum(rearranged_disk)

    if result != -1:
        print("The solution to part one is: " + str(result))


@dataclass
class disk_item:
    id: int
    is_free_space: bool
    size: int


def get_disk_v2(disk_map):
    disk = []
    current_id = 0
    for i, disk_pos in enumerate(disk_map):
        if i % 2 == 1:
            disk.append(disk_item(-1, True, disk_pos))
        else:
            disk.append(disk_item(current_id, False, disk_pos))
            current_id += 1
    return disk


def rearrange_disk_v2(disk: list):
    rearranged_disk = disk.copy()
    data_pointer = len(disk) - 1
    if data_pointer % 2 == 1: data_pointer -= 1

    while data_pointer > 0:
        # Look for free space
        for i, data in enumerate(rearranged_disk):
            if i > data_pointer: break

            item = rearranged_disk[data_pointer]
            if data.is_free_space and data.size >= item.size:
                new_item = replace(item)
                item.id = -1
                item.is_free_space = True
                rearranged_disk.insert(i, new_item)
                data.size -= item.size
                break
        
        data_pointer -= 1
        while rearranged_disk[data_pointer].is_free_space: data_pointer -= 1

    return rearranged_disk


def compute_checksum_v2(disk):
    result = 0
    i = 0
    for item in disk:
        for j in range(item.size):
            if not item.is_free_space:
                result += item.id * i
            i += 1

    return result


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    disk_map = list(map(lambda x: int(x), lines[0].strip()))
    
    disk = get_disk_v2(disk_map)
    rearranged_disk = rearrange_disk_v2(disk)
    result = compute_checksum_v2(rearranged_disk)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day9/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
