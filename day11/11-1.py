import sys
sys.path.append("../helpers.py")
from helpers import *


################################################################################
# Functional logic
################################################################################

def split_stones(stones, index, do_print):
    value = str(stones[index])
    val_len = int(len(value)/2)

    left_val = int(value[:val_len])
    right_val = int(value[val_len:])
    stones[index] = left_val
    stones.insert(index+1, right_val)

    if do_print:
        print('rule #2:', value, '->', left_val, ',', right_val)

    return stones


def blink(stones, do_print=False):
    i = 0
    while i < len(stones):

        # rule 1 - if stone = 0, replace with stone = 1
        if stones[i] == 0:
            if do_print:
                print('rule #1: 0 -> 1')
            stones[i] = 1

        # rule 2 - If stone is even, split
        elif is_even(len(str(stones[i]))):
            stones = split_stones(stones, i, do_print)
            i += 1 #because we added a stone

        # rule 3 - If all else fails, multiply by 2024
        else:
            if do_print:
                print('rule #3:', stones[i], '->', int(stones[i]) * 2024)
            stones[i] = int(stones[i]) * 2024
        i += 1
    return stones


# guesses:
# 64 - Not right
# 277154 - Not right
# 182081
def solve(input_data):
    stones = []
    for item in input_data:
        stones.append(item)

    blinks = 6
    blink_count = 1
    print_start = 0
    print_end = 6

    while blink_count <= blinks:
        print(Colors.yellow('blink count:'), blink_count)
        do_print = False
        if print_start <= blink_count <= print_end:
            do_print = True
        stones = blink(stones, do_print)
        blink_count += 1



    result = len(stones)
    return result


################################################################################
# Main
################################################################################

# input_data = load_input(11, InputType.MAIN).split(' ')
input_data = load_input(11, InputType.EXAMPLE).split(' ')


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

