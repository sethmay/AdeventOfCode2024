import sys
sys.path.append("../helpers.py")
from helpers import *


################################################################################
# Functional logic
################################################################################



# guesses:
#
def solve(input_data):
    result = 0
    return result


################################################################################
# Main
################################################################################

# input_data = load_input(8, InputType.MAIN).splitlines()
input_data = load_input(7, InputType.EXAMPLE).splitlines()


result = time_solution(solve, input_data)
print(Colors.yellow('Result:'))
print(f"    {result}")

