import time
import math
from enum import Enum
from pathlib import Path

def find_distance(item1, item2):
    return abs(int(item1) - int(item2))


class InputType(Enum):
    EXAMPLE = "example"
    MAIN = "main"

def load_input(day: int, input_type: InputType = InputType.MAIN) -> str:
    if(input_type == InputType.MAIN):
        input_file = Path(f"../../AdventOfCode2024_Inputs/day{day:02}/input.txt")
    else:
        input_file = Path(f"../../AdventOfCode2024_Inputs/day{day:02}/example.txt")

    if input_file.exists():
        with open(input_file, "r") as f:
            return f.read().strip()
    else:
        raise FileNotFoundError(f"Input file for day {day:02} not found!")


# If the list is equal to the reverse sort, it is all decreasing
def is_decreasing(numlist):
    #print(numlist)
    return numlist == sorted(numlist, reverse=True)

def is_decreasing2(numlist):
    i = 0
    while i < len(numlist):
        if (i > 0):
            if (int(numlist[i - 1]) < int(numlist[i])):
                return False
        i += 1

    return True


# If the list is equal to the list normally sorted, it is all increasing
def is_increasing(numlist):
    #print(numlist)
    return numlist == sorted(numlist)


def is_increasing2(numlist):
    i = 0
    while i < len(numlist):
        if (i > 0):
            if (int(numlist[i - 1]) > int(numlist[i])):
                return False
        i += 1

    return True

def make_2d_list (input):
    output = []
    for line in input:
        output.append(list(line))
    return output

class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def blue(text):
        return Colors.BLUE + text + Colors.ENDC
    def cyan(text):
        return Colors.CYAN + text + Colors.ENDC
    def green(text):
        return Colors.GREEN + text + Colors.ENDC
    def purple(text):
        return Colors.PURPLE + text + Colors.ENDC
    def red(text):
        return Colors.RED + text + Colors.ENDC
    def yellow(text):
        return Colors.YELLOW + text + Colors.ENDC
    def bold(text):
        return Colors.BOLD + text + Colors.ENDC
    def underline(text):
        return Colors.UNDERLINE + text + Colors.ENDC
    # print (Colors.BLUE + "Blue" + Colors.ENDC)
    # print (Colors.CYAN + "Cyan" + Colors.ENDC)
    # print (Colors.GREEN + "Green" + Colors.ENDC)
    # print (Colors.RED + "Red" + Colors.ENDC)
    # print (Colors.PURPLE + "Purple" + Colors.ENDC)
    # print (Colors.YELLOW + "Yellow" + Colors.ENDC)
    # print (Colors.BOLD + "Bold" + Colors.ENDC)
    # print (Colors.UNDERLINE + "Underline" + Colors.ENDC)


def time_solution(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    execution_time_sec = (end_time - start_time)
    execution_time_ms = execution_time_sec * 1_000
    execution_time_us = execution_time_sec * 1_000_000

    print()
    print(Colors.green("Execution time:"))
    print(f"  - {execution_time_sec:.3f} sec")
    print(f"  - {execution_time_ms:.2f} ms")
    print(f"  - {math.ceil(execution_time_us)} µs")
    return result