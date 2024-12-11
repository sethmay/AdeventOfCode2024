import sys
from functools import cached_property

sys.path.append("../helpers.py")
from helpers import *


################################################################################
# Functional logic
################################################################################
def split_stones(stones, index, cache, do_print):
    value = str(stones[index])
    val_len = int(len(value)/2)

    left_val = int(value[:val_len])
    right_val = int(value[val_len:])
    stones[index] = left_val
    stones.insert(index+1, right_val)

    cache[value] = [left_val, right_val]

    if do_print:
        print('rule #2:', value, '->', left_val, ',', right_val)

    return stones

def remove_duplicates (stones, stone_dups):
    print (stones)
    unique_list = list(set(stones))
    for item in unique_list:
        dup_count = stones.count(item)
        print ('dup_count:', item, dup_count)

        if item in stone_dups:
            stone_dups[item] += dup_count - 1
        else:
            stone_dups[item] = dup_count - 1
    return unique_list, stone_dups


def blink(stones, cache, stone_dups, do_print=False):
    i = 0
    stones, stone_dups = remove_duplicates(stones, stone_dups)

    while i < len(stones):
        # first try to pull the value from cache
        etch = stones[i]
        if etch in cache:
            cached_value = cache[etch]
            if isinstance(cached_value, list):
                stones[i] = cached_value[0]
                stones.insert(i + 1, cached_value[2])
                if do_print:
                    print('rule #2 (cached):', etch, '->', cached_value[0], ',', cached_value[2])
                i += 1  # because we added a stone
            else:
                if do_print:
                    print('rule #3 (cached):', stones[i], '->', cached_value)
                stones[i] = cached_value
        else:
            # rule 1 - if stone = 0, replace with stone = 1
            # if stones[i] == 0:
            #     # if do_print:
            #     #     print('rule #1: 0 -> 1')
            #     stones[i] = 1
            #     cache[etch] = 1

            # rule 2 - If stone is even, split
            if is_even(len(str(stones[i]))):
                stones = split_stones(stones, i, cache, do_print)
                i += 1 #because we added a stone

            # rule 3 - If all else fails, multiply by 2024
            else:
                if do_print:
                    print('rule #3:', stones[i], '->', int(stones[i]) * 2024)
                stones[i] = int(stones[i]) * 2024
                cache[etch] = stones[i]
        i += 1
    return stones


def calc_result(stones, stone_dups):
    stone_count = 0
    for stone in stones:
        if stone in stone_dups:
            print (stone, stone_dups[stone])
            stone_count += stone_dups[stone] + 1
        else:
            stone_count += 1

    return stone_count


# guesses:
# 64 - Not right
# 277154 - Not right
# 182081
def solve(input_data):
    # make a list of duplicate numbers
    # run the blink process for only one instance of those numbers
    # track a count of duplicates
    #

    stone_cache = {0: 1, 1:2024}
    stone_dups = {}
    stones = []
    for item in input_data:
        stones.append(item)

    blinks = 25
    blink_count = 1
    print_start = 6
    print_end = 6

    while blink_count <= blinks:
        print(Colors.yellow('blink count:'), blink_count)
        do_print = False
        if print_start <= blink_count <= print_end:
            do_print = True

        time_start = time.time()
        stones = blink(stones, stone_cache, stone_dups, do_print)

        time_end = time.time()
        time_sec = time_end - time_start
        print(f"  blink time: {time_sec:.3f} sec")

        blink_count += 1

    print(stone_dups)
    result = calc_result(stones, stone_dups)
    # result = len(stones)
    return result


################################################################################
# Main
################################################################################

# input_data = load_input(11, InputType.MAIN).split(' ')
input_data = load_input(11, InputType.EXAMPLE).split(' ')


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

