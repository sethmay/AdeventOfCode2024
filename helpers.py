import time
import math
from enum import Enum
from pathlib import Path

class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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