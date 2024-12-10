import sys
sys.path.append("../helpers.py")
from helpers import *

# sys.set_int_max_str_digits(0)

################################################################################
# Notes
################################################################################
'''
Requirements
------------
• Final result is to calculate checksum by
    • multiplying each blocks position and id
    • adding them all together
• 

Ideas
-----
• 
• 
'''

################################################################################
# Functional logic
################################################################################

class Block:
    def __init__(self, id, data, location):
        self.id = id
        self.value = data
        self.location = location

    def __str__(self):
        return f"Block(id={self.id}, value={self.value}, location={self.location})\n\r"
    def __repr__(self):
        return f"Block(id={self.id}, value={self.value}, location={self.location})\n\r"

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
                map.append(Block(fileid, int(i/2), location))
                #map.append(Block(fileid, input[i], location))
            else:
                #print(fileid, '', location)
                map.append(Block('', '', location))
            j += 1
            location += 1
        if is_even(i):
            fileid += 1
        i += 1

    #print(map)
    return map

def sort_space_map(map):
    map_pointer = 0 # forward pointer
    rmap_pointer = len(map)-1 # backwards pointer

    while map_pointer < len(map) and map_pointer < rmap_pointer-5:
        #print_map(map)
        # skip any blocks already filled
        if map[map_pointer].value != '':
            map_pointer += 1
            continue

        while rmap_pointer >= 0:
            #print ('pointer:', map_pointer, 'rpointer:', rmap_pointer)
            # reverse the blocks (empty block goes to end, non-empty block comes forward
            if map[rmap_pointer].value != '':
                # note the order of pop/inserts to not mess up index / pointer references
                #print('swap1', map_pointer, map[map_pointer].location, map[map_pointer].value)
                #print('swap2', rmap_pointer, map[rmap_pointer].location, map[rmap_pointer].value)
                rblock = map.pop(rmap_pointer)
                rblock.location = map_pointer

                block = map.pop(map_pointer)
                block.location = rmap_pointer

                map.insert(map_pointer, rblock)
                map.insert(rmap_pointer, block)
                break

            rmap_pointer -= 1
        map_pointer += 1

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
# 6337367227720 - Too high
# 6337367222422 - Correct
def solve(input):
    map = build_space_map(input)
    map = sort_space_map(map)
    print_map(map)

    return calculate_result(map)


################################################################################
# Main
################################################################################

# input_data = load_input(9, InputType.MAIN)
input_data = load_input(9, InputType.EXAMPLE)


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

