import sys
from functools import cache

sys.path.append("../helpers.py")
from helpers import *


################################################################################
# Functional logic
################################################################################


@cache
def count_stones(value, depth=75):
    if depth == 0:
        return 1

    if value == 0:
        return count_stones(1, depth - 1)

    str_etch = str(value)
    digits = len(str_etch)
    if digits % 2 == 0:
        mid = digits // 2
        left =  int(str_etch[:mid])
        right = int(str_etch[mid:])
        return count_stones(left, depth - 1) + count_stones(right, depth - 1)

    else:
        return count_stones(int(value)*2024, depth - 1)


# guesses:
# 64 - Not right
# 277154 - Not right
# 182081
# 306060414185968 - Too high
# 65601038650482 - Too high
# 208485527159331 - Too high
# 216318908621637 - Correct

def solve(input_data):
    blinks = 75

    stone_count = 0
    for stone in input_data:
         stone_count += count_stones(int(stone), blinks)


    return stone_count



################################################################################
# Main
################################################################################

input_data = load_input(11, InputType.MAIN).split(' ')
# input_data = load_input(11, InputType.EXAMPLE).split(' ')


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

