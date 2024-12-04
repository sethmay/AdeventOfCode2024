# Ideas
# • Flatten the matrix into a single massive string
#    • horizontal + vertical + LR diagonal + RL diagonal
#    • search for forward & backwards variants of the work
#    • this should ensure uniqueness (no word counted twice
# • Build into a 2D array
#    • Use a second array to track matches
#    • Have a function to verify matches are not duplicates

import sys, re
sys.path.append("../helpers.py")
from helpers import *

input_data = load_input(4, InputType.MAIN).splitlines()
#input_data = load_input(4, InputType.EXAMPLE).splitlines()


class Direction(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    DIAGONAL_RL = "diagonal_rl"
    DIAGONAL_LR = "diagonal_lr"

def buildString (input, direction: Direction):
    width = len(input_data[0])
    height = len(input_data)
    outputString = ''

    if direction == Direction.HORIZONTAL:
        for line in input:
            outputString += "".join(line)
            outputString += ","
        return outputString

    if direction == Direction.VERTICAL:
        pos_hor = 0
        while pos_hor < width:
            pos_vert = 0
            while pos_vert < height:
                outputString += input[pos_vert][pos_hor]
                pos_vert += 1
            pos_hor += 1
            outputString += ","
        return outputString

    if direction == Direction.DIAGONAL_RL:
        start_hor_pos = 0
        start_vert_pos = 0
        pos_hor = 0
        pos_vert = 0

        while start_vert_pos < height :
            #print()
            while pos_hor >= 0 and pos_vert < height:
                #print (pos_vert, pos_hor, input[pos_vert][pos_hor])
                outputString += input[pos_vert][pos_hor]
                pos_hor -= 1
                pos_vert += 1

            start_hor_pos += 1
            if (start_hor_pos == width):
                start_hor_pos = width - 1
                start_vert_pos += 1

            pos_vert = start_vert_pos
            pos_hor = start_hor_pos
            outputString += ","
            #print (start_vert_pos, start_hor_pos)
        return outputString


    if direction == Direction.DIAGONAL_LR:
        start_hor_pos = width - 1
        start_vert_pos = 0
        pos_hor = start_hor_pos
        pos_vert = start_vert_pos

        while start_vert_pos < height :
            #print()
            while pos_hor < width and pos_vert < height:
                #print (pos_vert, pos_hor)
                outputString += input[pos_vert][pos_hor]
                pos_hor += 1
                pos_vert += 1

            start_hor_pos -= 1
            if (start_hor_pos < 0):
                start_hor_pos = 0
                start_vert_pos += 1

            pos_vert = start_vert_pos
            pos_hor = start_hor_pos
            outputString += ","
            #print (start_vert_pos, start_hor_pos)
        return outputString



def solve (input, word):
    hor = buildString(input, Direction.HORIZONTAL)
    vert = buildString(input, Direction.VERTICAL)
    diag_rl = buildString(input, Direction.DIAGONAL_RL)
    diag_lr = buildString(input, Direction.DIAGONAL_LR)

    teststring = hor + ";" + vert + ";" + diag_rl + ";" + diag_lr
    patterns = ['XMAS', 'SAMX']
    counts = 0
    for pattern in patterns:
        counts += teststring.count(pattern)

    print(counts)


input = []

for line in input_data:
    input.append(list(line))

solve(input, 'XMAS')



# [0,0]
# [0,1],[1,0]
# [0,2],[1,1][2,0]
# [0,3],[1,2][2,1][3,0]
#
# go until x = 0
# increment start pos by 0,1 each time
#  if y = width