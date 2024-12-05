import sys, re
sys.path.append("../helpers.py")
from helpers import *

#input_data = load_input(5, InputType.MAIN).splitlines()
input_data = load_input(5, InputType.EXAMPLE).splitlines()



def solve (input, word):
   print('solve')


input = []
for line in input_data:
    input.append(list(line))

solve(input, 'XMAS')

