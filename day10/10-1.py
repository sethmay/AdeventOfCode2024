import sys
sys.path.append("../helpers.py")
from helpers import *


################################################################################
# Functional logic
################################################################################

def build_map(input):
    map = {}
    rows = len(input)
    cols = len(input[0])
    row = 0
    while row < rows:
        col = 0
        while col < cols:
            #print (input[row][col])
            map[(row, col)] = int(input[row][col])
            col += 1
        row += 1
    #print(map)
    return map

def find_trail_heads(map):
    paths = {}
    for key, value in map.items():
        #print (key, value)
        if value == 0:
            paths[key] = []
    return paths

def print_paths(paths):
    for path_key in paths:
        #print(path_key)
        path = f"trialhead: {path_key}, trail: "

        for step in paths[path_key]:
            for pos, level in step.items():
                #print(pos, level)
                path = path + f' {level}:{pos}, '
        print(path)

def build_path(map, startpath, current_level, path):
    start_row = startpath[0]
    start_col = startpath[1]

    if current_level == 9:
        return path

    #try north
    check_row = start_row-1
    check_col = start_col
    if (check_row, check_col) in map:
        if map[(check_row, check_col)] == current_level + 1:
            path.append({(check_row, check_col): map[(check_row, check_col)]})
            path = build_path(map, (check_row, check_col), current_level+1, path)

    # try east
    check_row = start_row
    check_col = start_col + 1
    if (check_row, check_col) in map:
        if map[(check_row, check_col)] == current_level + 1:
            path.append({(check_row, check_col): map[(check_row, check_col)]})
            path = build_path(map, (check_row, check_col), current_level + 1, path)

    # try south
    check_row = start_row + 1
    check_col = start_col
    if (check_row, check_col) in map:
        if map[(check_row, check_col)] == current_level + 1:
            path.append({(check_row, check_col): map[(check_row, check_col)]})
            path = build_path(map, (check_row, check_col), current_level + 1, path)

    # try south
    check_row = start_row
    check_col = start_col - 1
    if (check_row, check_col) in map:
        if map[(check_row, check_col)] == current_level + 1:
            path.append({(check_row, check_col): map[(check_row, check_col)]})
            path = build_path(map, (check_row, check_col), current_level + 1, path)

    return path


def count_reachable_peaks(paths):
    reachable_peaks = {}
    trail_heads = {}

    for path_key in paths:
        trail_heads[path_key] = {}
        for step in paths[path_key]:
            for pos, level in step.items():
                if level == 9:
                    trail_heads[path_key][pos] = True
                    reachable_peaks[pos] = True

    #print (trail_heads)
    total_score = 0
    for trail in trail_heads:
        #print(len(trail_heads[trail]))
        total_score += len(trail_heads[trail])

    return total_score


# guesses:
# 629 - correct
def solve(input_data):
    map = build_map(input_data)
    paths = find_trail_heads(map)
    for key in paths:
        paths[key] = build_path(map, key, map[key], paths[key])

    #print_paths(paths)
    result = count_reachable_peaks(paths)

    return result


################################################################################
# Main
################################################################################

input_data = make_2d_list(load_input(10, InputType.MAIN).splitlines())
# input_data = make_2d_list(load_input(10, InputType.EXAMPLE).splitlines())


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

