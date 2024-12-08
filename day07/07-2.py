import sys, math
from collections import namedtuple

sys.path.append("../helpers.py")
from helpers import *

input_data = load_input(7, InputType.MAIN).splitlines()
# input_data = load_input(7, InputType.EXAMPLE).splitlines()
input_results = []
input_parts = []

for line in input_data:
    results, parts = line.split(":")
    input_results.append(results)
    input_parts.append(parts.split())


# print(input_results, input_parts)


# Build the binary map of operators
def get_binary_iterations(num_count):
    digitcount = num_count - 1
    op_count = 2 ** (num_count - 1)
    bperms = []
    j = 0
    while j <= op_count - 1:
        f = "0" + str(digitcount) + "b"
        bperms.append(format(j, f))
        j += 1

    # print('bperms', bperms)
    return bperms

def convert_to_base_3(n):
    """Converts a decimal number to base 3."""
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 3) + result
        n //= 3
    return result

# Build the binary map of operators
def get_trinary_iterations(num_count):
    digitcount = num_count - 1
    op_count = 3 ** (num_count - 1)
    bperms = []
    j = 0
    while j <= op_count - 1:
        num = convert_to_base_3(j)
        formatted_num = str(num).zfill(digitcount)
        bperms.append(formatted_num)

        j += 1
    # print('bperms', bperms)
    return bperms


def get_result(equation, test_result):
    # result = eval(''.join(equation))
    num1 = equation[0]
    op = equation[1]
    num2 = equation[2]
    #print(''.join(equation), num1, op, num2)
    if (op == '|'):
        result = num1 + num2
    else:
        result = eval(num1 + op + num2)
    i = 3

    while i < len(equation):
        op = equation[i]
        num2 = equation[i + 1]
        #print(''.join(equation), result, op, num2)
        if (op == '|'):
            result = str(result) + num2
        else:
            result = eval(str(result) + op + num2)
        i += 2

    if (int(result) == int(test_result)):
        print(Colors.yellow(str(test_result)+':'), Colors.yellow(''.join(equation)), Colors.yellow(str(result)), Colors.yellow(str(test_result)))
    # else:
    #     print(str(test_result) + ':', ''.join(equation), result, test_result)
    return int(result)


# guesses:
# 333027885676693 - Correct
def solve(input_results, input_parts):
    loop_eq = 0
    solvable_results = 0
    sum_of_results = 0
    while loop_eq < len(input_results):
        iterations = []
        needed_iterations = 3 ** (len(input_parts[loop_eq]) - 1)  # 2^len-1
        numbers = input_parts[loop_eq]
        #print(needed_iterations, numbers, len(numbers))
        perms = get_trinary_iterations(len(numbers))

        loop_op = 0
        while loop_op < len(perms):
            perm = perms[loop_op]
            #print (perm)
            equation = []

            loop_number = 0
            while loop_number < len(numbers)-1:
                number = numbers[loop_number]
                equation.append(number)

                operator = perm[loop_number]
                #print (number, operator, perm, len(numbers))

                if operator == '0':
                    equation.append('+')
                elif operator == '1':
                    equation.append('*')
                else:
                    equation.append('|')
                loop_number += 1

                # add on the last number at the end
                if loop_number == len(numbers) - 1:
                    equation.append(numbers[loop_number])
            #print(equation)
            iterations.append(equation)
            loop_op += 1

        # print(iterations)

        for equation in iterations:
            result = get_result(equation, int(input_results[loop_eq]))
            if (result == int(input_results[loop_eq])):
                solvable_results += 1
                sum_of_results += result
                break

        loop_eq += 1

    print('num solvable:', solvable_results)
    print('sum of all solvable:', sum_of_results)


result = time_solution(solve, input_results, input_parts)
#solve(input_results, input_parts)


