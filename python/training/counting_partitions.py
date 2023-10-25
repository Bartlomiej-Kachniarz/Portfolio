import os
import sys

# This is a bypass to import a decorator from another module:

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from decorators.decorators import time_this_func  # noqa: E402


def get_biggest_power(nmbr):  # 67
    if nmbr == 0:
        return 0
    current_power = 0
    while True:
        if 2 ** (current_power + 1) > nmbr >= 2 ** (current_power):  # 128 > 67 > 64 = 2^6
            return current_power  # 6
        current_power += 1  # 6


def find_binary_repr(nmbr):  # 67
    if nmbr == 0:
        return [0]
    turn_zero_to_one = get_biggest_power(nmbr)  # 6
    table = [0 for _ in range(turn_zero_to_one + 1)]  # [0] x 7
    table[-(turn_zero_to_one + 1)] = 1  # [1, 0, 0, 0, 0, 0, 0]
    new_nmbr = nmbr - 2 ** (turn_zero_to_one)  # 67 - 64 = 3
    while new_nmbr != 0:
        turn_zero_to_one = get_biggest_power(new_nmbr)  # 1    # 0
        table[-(turn_zero_to_one + 1)] = 1  # [1, 0, 0, 0, 0, 1, 0]    # [1, 0, 0, 0, 0, 1, 1]
        new_nmbr = new_nmbr - 2 ** (turn_zero_to_one)  # 3 - 2 = 1    # 1 - 1 = 0
    return table


@time_this_func
def count_partitions(nmbr):
    partitions = 1
    binary_repr = find_binary_repr(nmbr)
    for number in range(len(binary_repr)):
        if number == len(binary_repr) - 1:
            break
        if binary_repr[number] != binary_repr[number + 1]:
            partitions += 1
    return f"No of partitions: {partitions}\n"


if __name__ == "__main__":
    print(find_binary_repr(340))
    print(count_partitions(340))

    print(find_binary_repr(67))
    print(count_partitions(67))

    print(find_binary_repr(245))
    print(count_partitions(245))

    print(find_binary_repr(928050254646230))
    print(count_partitions(928050254646230))

    print(find_binary_repr(102))
    print(count_partitions(102))

    print(find_binary_repr(20024))
    print(count_partitions(20024))
