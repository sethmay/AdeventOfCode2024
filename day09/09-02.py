import sys
sys.path.append("../helpers.py")
from helpers import *


################################################################################
# Notes
################################################################################


################################################################################
# Functional logic
################################################################################

class Block:
    def __init__(self, id, data, length, location):
        self.id = id
        self.value = data
        self.length = length
        self.location = location

    def __str__(self):
        return f"Block(id={self.id}, value={self.value}, length={self.length}, location={self.location})\n\r"
    def __repr__(self):
        return f"Block(id={self.id}, value={self.value}, length={self.length}, location={self.location})\n\r"

def print_map (map):
    map_string = ''
    for block in map:
        if block.value == '':
            map_string += '.'
        else:
            map_string += str(block.value)
    print(map_string)

def build_space_map(input):
    map = []
    i = 0
    fileid = 0
    location = 0
    while i < len(input):
        # even holds the count of file blocks
        # odd holds the count of free space blocks
        # value = input[i]
        length = int(input[i])
        # print(value)
        # print(length)
        # exit()

        j = 0
        while j < length:
            if is_even(i):
                #print (fileid, int(input[i]), location)
                map.append(Block(fileid, int(i/2), length, location))
                #map.append(Block(fileid, input[i], location))
            else:
                #print(fileid, '', location)
                map.append(Block('', '', 0, location))
            j += 1
            location += 1
        if is_even(i):
            fileid += 1
        i += 1

    #print(map)
    return map


def find_first_open_space(map, length, block_start):
    spaces_open = 0
    space_open_index = 0
    i = 0
    while i < len(map) and i < block_start:
        if (map[i].value == ''):
            spaces_open += 1
            #print(spaces_open, length)
            if (space_open_index == 0):
                space_open_index = i
            if (spaces_open == length):

                return space_open_index

        else:
            spaces_open = 0
            space_open_index = 0
        i += 1
    return 0

def defrag(map):
    rmap_pointer = len(map)-1 # backwards pointer

    while rmap_pointer > 0:
        #print_map(map)
        # skip any blocks already filled
        if map[rmap_pointer].value == '':
            rmap_pointer -= 1
            continue

        length = map[rmap_pointer].length
        first_open_space = find_first_open_space(map, length, rmap_pointer - length)
        #print_map(map)
        #print(map[rmap_pointer], first_open_space)

        if (first_open_space != 0):
            j = 0
            while j < length:
                # do the swap
                #print(rmap_pointer - j, len(map))
                rblock = map.pop(rmap_pointer - j)
                block = map.pop(first_open_space + j)

                rblock.location = first_open_space + j
                block.location = rmap_pointer - j

                map.insert(first_open_space + j, rblock)
                map.insert(rmap_pointer - j, block)

                j += 1

        rmap_pointer -= length
    return map

def calculate_result(map):
    # • Final result is to calculate checksum by
    #     • multiplying each blocks position and id
    #     • adding them all together
    result = 0
    for block in map:
        if (block.value != ''):
            #print(int(block.location), '*', int(block.value), '=', int(block.value) * int(block.location) )
            result += int(block.value) * int(block.location)
    return result


# guesses:
# 6361381088795 - Too high
#
def solve(input):
    map = build_space_map(input)
    map = defrag(map)

    print_map(map)
    print(map)


    return calculate_result(map)


################################################################################
# Main
################################################################################

input_data = load_input(9, InputType.MAIN)
# input_data = load_input(9, InputType.EXAMPLE)


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

