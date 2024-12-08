import sys, copy
sys.path.append("../helpers.py")
from helpers import *


################################################################################
# Functional logic
################################################################################

def find_frequencies(map, frequencies):
    row = 0
    while row < len(map):
        col = 0
        while col < len(map[0]):
            if not map[row][col] == '.':
                freq = map[row][col]
                pos = [row, col]
                if freq in frequencies:
                    frequencies[freq].append(pos)
                else:
                    frequencies[freq] = [pos]
            col += 1
        row += 1
    return frequencies

def is_node_inbounds (map, node):
    row_max = len(map)
    col_max = len(map[0])
    if (0 <= node[0] < row_max) and (0 <= node[1] < col_max):
        #print ('bound pass:', node[0], node[1])
        return True
    #print('bound fail:', node[0], node[1])
    return False

def calculate_antinode(node1, node2):

    distance_row = abs(node1[0] - node2[0])
    distance_col = abs(node1[1] - node2[1])
    antinode_row = 0
    antinode_col = 0
    if (node1[0] < node2[0]):
        antinode_row = node1[0] - distance_row
    else:
        antinode_row = node1[0] + distance_row

    if (node1[1] < node2[1]):
        antinode_col = node1[1] - distance_col
    else:
        antinode_col = node1[1] + distance_col


    antinode = [antinode_row, antinode_col]
    print(node1, node2, 'antinode:', antinode, distance_row, distance_col)
    return antinode

def find_antinodes (map, nodes):
    row_max = len(map)
    col_max = len(map[0])
    temp_nodes = copy.deepcopy(nodes)
    antinodes = []


    while len(temp_nodes) > 0:
        node = temp_nodes.pop(0)
        j = 0
        while j < len(temp_nodes):
            temp_node = temp_nodes[j]
            #print(node, temp_nodes[j])
            antinode1 = calculate_antinode(node, temp_node)
            antinode2 = calculate_antinode(temp_node, node)

            if (is_node_inbounds(map, antinode1)):
                antinodes.append(antinode1)
            if (is_node_inbounds(map, antinode2)):
                antinodes.append(antinode2)

            j += 1

    return antinodes

def remove_antinode_collisions (map, antinodes_list):
    temp_map = copy.deepcopy(map)
    antinode_result = []

    for antinodes in antinodes_list.values():
        for antinode in antinodes:
            if temp_map[antinode[0]][antinode[1]] != '#':
                antinode_result.append(antinode)
            temp_map[antinode[0]][antinode[1]] = '#'

    print_map(temp_map)
    return antinode_result


def print_map(map):
    print()
    for row in map:
        print("".join(row))


# guesses:
# 379 - Too high (someone elses right answer)
# 369 - Correct!
def solve(map):
    print_map(map)
    result = 0
    frequencies = {}
    antinodes = {}
    frequencies = find_frequencies(map, frequencies)
    print (frequencies)

    for key in frequencies:
        antinodes[key] = find_antinodes(map, frequencies[key])


    print (antinodes)
    antinode_result = remove_antinode_collisions(map, antinodes)

    antinode_count = len(antinode_result)
    # for key in antinodes:
    #     antinode_count += len(antinodes[key])
    print(antinode_count)

    return result


################################################################################
# Main
################################################################################

input_data = make_2d_list(load_input(8, InputType.MAIN).splitlines())
# input_data = make_2d_list(load_input(8, InputType.EXAMPLE).splitlines())



result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")


