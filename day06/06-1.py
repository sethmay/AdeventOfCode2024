import sys
from collections import namedtuple

sys.path.append("../helpers.py")
from helpers import *

input_data = make_2d_list(load_input(6, InputType.MAIN).splitlines())
#input_data = make_2d_list(load_input(6, InputType.EXAMPLE).splitlines())



def search_map (map, item):
    row_count = len(map)
    col_count = len(map[0])

    row = 0
    col = 0

    while row < row_count:
        while col < col_count:
            #print (col, row, map[row][col])
            if map[row][col] == item:
                return (row, col)
            col += 1
        row += 1
        col = 0
    return (False, False)

def in_inbounds (map, row, col):
    return 0 <= row < len(map) and 0 <= col < len(map[row])

def get_next_pos (direction, row, col):
    if direction == 'n':
        #print (row, col, row-1, col, direction)
        return [row-1, col]
    if direction == 'e':
        #print(row, col, row, col+1, direction)
        return [row, col+1]
    if direction == 's':
        #print(row, col, row+1, col, direction)
        return [row+1, col]
    if direction == 'w':
        #print(row, col, row, col-1, direction)
        return [row, col-1]

def is_next_inbounds (map, direction, row, col):
    row_count = len(map)
    col_count = len(map[0])

    next_row, next_col = get_next_pos(direction, row, col)

    if 0 <= next_row < row_count and 0 <= next_col < col_count:
        return True
    return False

def has_obstacle (map, direction, row, col):
    if is_next_inbounds(map, direction, row, col):
        next_row, next_col = get_next_pos(direction, row, col)
        if map[next_row][next_col] == '#':
            return True
        else:
            return False

    return -1 # out of bounds

def turn_90_degrees(directions, person_dir):
    if (person_dir == 'n'):
        return ['e', '>']
    if (person_dir == 'e'):
        return ['s', 'v']
    if (person_dir == 's'):
        return ['w', '<']
    if (person_dir == 'w'):
        return ['n', '^']

def move_forward(map, direction, start_row, start_col, icon):
    #print ('move forward', direction, start_row, start_col)
    pos = get_next_pos(direction, start_row, start_col)
    #print ('pos:', pos)
    next_row = pos[0]
    next_col = pos[1]
    map[start_row][start_col] = 'X'
    map[next_row][next_col] = icon
    return [map, next_row, next_col]

def path_count(map):
    traversed = 0
    row = 0
    col = 0
    while row < len(map):
        while col < len(map[row]):
            if map[row][col] == 'X':
                traversed += 1
            col += 1
        row += 1
        col = 0
    return traversed

def print_map(map):
    for row in map:
        print("".join(row))

def solve (input_data):
    map = input_data.copy()
    person_row, person_col = search_map(map, '^')
    person_dir = 'n'
    person_icon = '^'


    while is_next_inbounds(map, person_dir, person_row, person_col):
        if (has_obstacle(map, person_dir, person_row, person_col)):
            output = turn_90_degrees(person_dir, person_dir)
            person_dir = output[0]
            person_icon = output[1]
        map, person_row, person_col = move_forward(map, person_dir, person_row, person_col, person_icon)

    traversed = path_count(map) + 1 #(count the final position)
    #print()
    print_map(map)
    print(traversed)



solve(input_data)
