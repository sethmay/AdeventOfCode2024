import sys, copy
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

def is_inbounds (map, row, col):
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

def is_next_step_inbounds (map, direction, row, col):
    next_row, next_col = get_next_pos(direction, row, col)

    if is_inbounds(map, next_row, next_col):
        return True
    return False

def has_obstacle (map, direction, row, col):
    if is_next_step_inbounds(map, direction, row, col):
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
    print()
    for row in map:
        print("".join(row))

def has_walked_this_path(path, person_row, person_col, person_dir):
    test = [person_row, person_col, person_dir]
    for spot in path:
        if test == spot:
            return True
    return False


def solve (input_data):
    path_map = copy.deepcopy(input_data)
    person_row, person_col = search_map(path_map, '^')
    person_dir = 'n'
    person_icon = '^'
    rows = len(path_map)
    cols = len(path_map[0])

    # Run the initial path so I know which positions should be in my test set
    while is_next_step_inbounds(path_map, person_dir, person_row, person_col):
        if (has_obstacle(path_map, person_dir, person_row, person_col)):
            person_dir, person_icon = turn_90_degrees(person_dir, person_dir)

        path_map, person_row, person_col = move_forward(path_map, person_dir, person_row, person_col, person_icon)
    path_map[person_row][person_col] = 'X'


    # Now build a list only of the positions that should be tested (only those traversed by the guard)
    blocker_spots = []
    row = 0
    col = 0
    start_row, start_col = search_map(input_data, '^')
    path_map[start_row][start_col] == 'X' # ensure the starting position is included

    while row < rows:
        while col < cols:
            #blocker_spots.append([row, col])
            if path_map[row][col] == 'X':
                blocker_spots.append([row, col])
            col += 1
        row += 1
        col = 0



    #Answers: 1700, too small
    # 1701 - wrong
    # 1702 - wrong
    # 1703 - wrong - someone elses number
    # 1704 - wrong

    #
    looping_path_count = 0
    blocker_spot_count = len(blocker_spots)
    attempt = 1

    # Build a new map for each spot to test
    for pos_row, pos_col in blocker_spots:
        # if attempt % 1000 == 0:
        #     print ('attempt:', attempt, 'of', blocker_spot_count)
        test_path_map = copy.deepcopy(input_data) # generate a clean map
        test_path_map[pos_row][pos_col] = '#' # mark the new obstacle
        step_counter = 0
        person_row = start_row  # these are static for all maps, so use them recorded above
        person_col = start_col  # these are static for all maps, so use them recorded above
        person_dir = 'n'
        person_icon = '^'
        path = [] # used to track the coord/direction of each step taken

        # follow the guard until they go out of bounds OR they start looping
        while is_next_step_inbounds(test_path_map, person_dir, person_row, person_col):
            if has_walked_this_path(path, person_row, person_col, person_dir):
                looping_path_count += 1
                #print_map(test_path_map)
                print('attempt:', attempt, '/', blocker_spot_count, '- loop', looping_path_count, 'found, steps:', step_counter)
                break

            # track the path before taking next step
            path.append([person_row, person_col, person_dir])

            # If they are blocked, turn
            if (has_obstacle(test_path_map, person_dir, person_row, person_col)):
                person_dir, person_icon = turn_90_degrees(person_dir, person_dir)


            # move forward one step
            test_path_map, person_row, person_col = move_forward(test_path_map, person_dir, person_row, person_col, person_icon)
            step_counter += 1

        attempt += 1

   #print_map(map)
    print(looping_path_count)



solve(input_data)
