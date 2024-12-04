# Ideas
# • Move through the matrix one by one. If an M or S is spotted, do a X-MAS check on it.
#   • Always check from the top left corner (to avoid duplicates)
#   • Count the positive hits

import sys, re
sys.path.append("../helpers.py")
from helpers import *

input_data = load_input(4, InputType.MAIN).splitlines()
#input_data = load_input(4, InputType.EXAMPLE).splitlines()


def check_mas(input, v, h):
    width = len(input[0])
    height = len(input)

    if (v > height - 3 or h > width - 3):
        # too close to the edge of the matrix
        #print ('out of bounds', v, h)
        return False

    #print(v, h, input[v][h+2], 'checking')
    #Top right
    if  input[v][h+2] != "M" and input[v][h+2] != "S":
        return False
    # print (v, h, input[v][h+2], 'Top right hit')

    #Middle
    if input[v+1][h+1] != "A":
        return False
    #print (v, h, input[v+1][h+1], 'Middle hit')

    #Bottom Left
    if input[v+2][h] != "M" and input[v+2][h] != "S":
        return False
    #print (v, h, input[v+2][h], 'Bottom left hit')

    #Bottom Right
    if input[v+2][h+2] != "M" and input[v+2][h+2] != "S":
        return False
    # print (v, h, input[v+2][h+2], 'Bottom right hit')

    # Now check to make sure the two words are actually "MAS" or "SAM"
    w1 = input[v][h] + input[v+1][h+1] + input[v+2][h+2]
    w2 = input[v][h+2] + input[v + 1][h + 1] + input[v + 2][h]
    if not (w1 == "SAM" or w1 == "MAS") or not (w2 == "SAM" or w2 == "MAS"):
        return False

    #print (v,h, w1, w2, 'found')
    return True


def solve (input, word):
    width = len(input[0])
    height = len(input)

    count = 0
    vpos = 0
    hpos = 0

    while vpos < height:
        while hpos < width:
            if (input[vpos][hpos] == "M" or input[vpos][hpos] == "S"):
                #print (vpos, hpos, input[vpos][hpos])
                if (check_mas(input, vpos, hpos)):
                    count += 1
            hpos += 1

        hpos = 0
        vpos += 1

    print(count)


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