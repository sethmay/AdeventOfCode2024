import sys, copy
sys.path.append("../helpers.py")
from helpers import *
from functools import cache


################################################################################
# Functional logic
################################################################################
class Plot:
    def __init__(self, row, col, crop):
        self.row = row
        self.col = col
        self.crop = crop
        self.region = -1
        self.checked = False
        self.n = 0
        self.e = 0
        self.s = 0
        self.w = 0

    def __str__(self):
        return f"Block(pos=({self.row}, {self.col}), crop={self.crop}, region={self.region}), n={self.n}), s={self.s}), e={self.e}), w={self.w})\n\r"
    def __repr__(self):
        return f"Block(pos=({self.row}, {self.col}), crop={self.crop}, region={self.region}), n={self.n}), s={self.s}), e={self.e}), w={self.w})\n\r"

class Region:
    def __init__(self, crop):
        self.crop = crop
        self.plots = {}
        self.area = 0
        self.perimeter = 0
        self.price = 0

    def __str__(self):
        return f"Block(crop={self.crop}, plot count={len(self.plots)}), area={self.area}), perimeter={self.perimeter})\n\r"
    def __repr__(self):
        return f"Block(crop={self.crop}, plot count={len(self.plots)}), area={self.area}), perimeter={self.perimeter})\n\r"


def print_map(map):
    print()
    current_row = 0
    line = ''
    for pos, plot in map.items():
        row = plot.row
        if row == current_row:
            line += plot.crop
        else:
            print(line)
            line = plot.crop
            current_row = plot.row
    print(line)

@cache
def is_inbounds(max_row, max_col, row, col):
    if 0 <= row < max_row and 0 <= col < max_col:
        return True
    return False


def build_map(input):
    map = {}
    row = 0
    while row < len(input):
        col = 0
        while col < len(input[0]):
            if is_inbounds(len(input), len(input[1]), row, col):
                #print (len(input), len(input[1]), row, col, input[row][col])
                map[(row, col)] = Plot(row, col, input[row][col])
            col += 1
        row += 1
    return map

def map_fences(input, map):
    max_rows = len(input)
    max_col = len(input[1])

    for pos, plot in map.items():
        # check north
        if not is_inbounds(max_rows, max_col, plot.row-1, plot.col):
            plot.n = 1 # fence outer perimeter
        elif plot.crop != map[(plot.row-1, plot.col)].crop:
            plot.n = 1

        # check south
        #print (plot.row, plot.col, plot.crop, map[(plot.row+1, plot.col)].crop)
        if not is_inbounds(max_rows, max_col, plot.row+1, plot.col):
            plot.s = 1 # fence outer perimeter
        elif plot.crop != map[(plot.row+1, plot.col)].crop:
            plot.s = 1

        # check east
        if not is_inbounds(max_rows, max_col, plot.row, plot.col+1):
            plot.e = 1  # fence outer perimeter
        elif plot.crop != map[(plot.row, plot.col+1)].crop:
            plot.e = 1

        # check west
        if not is_inbounds(max_rows, max_col, plot.row, plot.col-1):
            plot.w = 1  # fence outer perimeter
        elif plot.crop != map[(plot.row, plot.col-1)].crop:
            plot.w = 1

def flood(map, plot, plots):
    #print (plot.row, plot.col)
    plots[(plot.row, plot.col)] = plot
    del map[(plot.row, plot.col)] # don't check this spot again

    if plot.n == 0:
        check_pos = (plot.row-1, plot.col)
        if check_pos in map:
            flood(map, map[check_pos], plots)
    if plot.s == 0:
        check_pos = (plot.row+1, plot.col)
        if check_pos in map:
            flood(map, map[check_pos], plots)
    if plot.e == 0:
        check_pos = (plot.row, plot.col+1)
        if check_pos in map:
            flood(map, map[check_pos], plots)
    if plot.w == 0:
        check_pos = (plot.row, plot.col-1)
        if check_pos in map:
            flood(map, map[check_pos], plots)
    #return plots

def count_perimeter(plots):
    count = 0
    for plot in plots.values():
        count += plot.n + plot.e + plot.w + plot.s
    return count

def build_regions(input, map):
    regions = []
    test_map = copy.deepcopy(map)
    remaining_map = copy.deepcopy(map)

    for pos, plot in test_map.items():
        if not plot.checked:
            plot = map[(pos[0], pos[1])]
            region = Region(plot.crop)

            plots = {}
            # print()
            flood(remaining_map, plot, plots)
            region.plots = plots
            region.area = len(region.plots)
            region.perimeter = count_perimeter(region.plots)
            region.price = region.area * region.perimeter
            #print(region.plots)
            for key in region.plots:
                test_map[key].checked = True # remove used plots so we don't search them again

            regions.append(region)
    return regions


# guesses:
# 1363484 - Correct
#
def solve(input_data):
    map = build_map(input_data)
    #print_map(map)

    map_fences(input_data, map)
    #print(map)

    regions = build_regions(input_data, map)
    # print(regions)

    total_price = 0
    for region in regions:
        total_price += region.price

    return total_price


################################################################################
# Main
################################################################################

input_data = make_2d_list(load_input(12, InputType.MAIN).splitlines())
# input_data = make_2d_list(load_input(12, InputType.EXAMPLE).splitlines())


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

