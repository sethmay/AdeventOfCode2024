import sys
sys.path.append("../helpers.py")
from helpers import *


input_data = load_input(2, InputType.MAIN).splitlines()
#input_data = load_input(2, InputType.EXAMPLE).splitlines()

def find_problem_index(report):
    prev_num = int(report[0])
    increasing = prev_num <= int(report[1])

    if (increasing):
        i = 1
        while i < len(report):
            if not (0 < int(report[i]) - prev_num <= 3):
                print("\t", report, int(report[i]), prev_num, (int(report[i]) - prev_num))
                return i
            prev_num = int(report[i])
            i += 1

    else:
        i = 1
        while i < len(report):
            if not (0 < prev_num - int(report[i]) <= 3):
                print("\t", report, prev_num, int(report[i]), (prev_num - int(report[i])))
                return i
            prev_num = int(report[i])
            i += 1
    return -1


def is_safe(report):
    print()
    print(report)
    index = find_problem_index(report)

    # Brute force, try removing each index and try again
    if not (index == -1):
        i = 0
        while i < len(report):
            reportA = report.copy()
            del reportA[i]
            print('\tretry ', i)
            index = find_problem_index(reportA)
            if (index == -1):
                break
            i += 1

    if (index == -1):
        print('\tsafe')
        print()
        return True

    else:
        print('\tfailed')
    return False


safe_count = 0
for line in input_data:
    report = line.split(' ')
    if is_safe(report):
        safe_count += 1

print('safe: ', safe_count)
