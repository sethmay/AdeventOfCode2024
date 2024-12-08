import sys, math
from collections import namedtuple

sys.path.append("../helpers.py")
from helpers import *

# input_data = load_input(7, InputType.MAIN).splitlines()
input_data = load_input(7, InputType.EXAMPLE).splitlines()
input_results = []
input_parts = []

for line in input_data:
    results, parts = line.split(":")
    input_results.append(results)
    input_parts.append(parts.split())
#print(input_results, input_parts)


# Build the binary map of operators
def get_binary_iterations(num_count):
    digitcount = num_count -1
    op_count = 2 ** (num_count - 1)
    bperms = []
    j = 0
    while j <= op_count-1:
        f = "0" + str(digitcount) + "b"
        bperms.append(format(j, f))
        j += 1

    #print('bperms', bperms)
    return bperms


def get_result(equation, test_result):
    #result = eval(''.join(equation))
    num1 = equation[0]
    op = equation[1]
    num2 = equation[2]
    result = eval(num1 + op + num2)
    i = 3
    while i < len(equation):
        op = equation[i]
        num2 = equation[i + 1]
        result = eval(str(result) + op + num2)
        i += 2

    if (result == test_result):
        print (Colors.yellow(''.join(equation)), Colors.yellow(str(result)), Colors.yellow(str(test_result)))
    # else:
    #     print(''.join(equation), result, test_result)
    return result

# guesses:
# 274 - too low
# 6231007345478 - sum of all solvable - CORRECT!
def solve (input_results, input_parts):

    i = 0
    solvable_results = 0
    sum_of_results = 0
    while i < len(input_results):
        iterations = []
        needed_iterations = 2 ** (len(input_parts[i]) - 1) # 2^len-1

        bperms = get_binary_iterations(len(input_parts[i]))
        #print (bperms)

        # cycle through every number in the set
        k = 0
        while k < needed_iterations:
            # for each number, add the
            equation = []
            m = 0
            while m < len(input_parts[i])-1:
                equation.append(input_parts[i][m])

                #print (k, m, input_parts[i][m], bperms[k][m])
                if bperms[k][m] == '0':
                    equation.append('+')
                else:
                    equation.append('*')
                m += 1

                # add on the last number at the end
                if (m == len(input_parts[i])-1):
                    equation.append(input_parts[i][m])

            iterations.append(equation)
            k += 1

        #print(iterations)

        for equation in iterations:
            result = get_result(equation, int(input_results[i]))
            if (result == int(input_results[i])):
                solvable_results += 1
                sum_of_results += result
                break

        i += 1

    print('num solvable:', solvable_results)
    print('sum of all solvable:', sum_of_results)



result = time_solution(solve, input_results, input_parts)
