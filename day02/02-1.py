import sys
sys.path.append("../helpers.py")
from helpers import *


input_data = load_input(2, InputType.MAIN).splitlines()
#input_data = load_input(2, InputType.EXAMPLE).splitlines()


def is_safe(report):
    if not (is_increasing2(report) or is_decreasing2(report)):
        #print (report, '- unsafe - not sorted')
        return False

    prev_num = report[0]
    for num in report[1:]:
        distance = find_distance(prev_num, num)
        if not 0 < distance <= 3:
            #print (report, 'unsafe - distance', prev_num, num, find_distance(prev_num, num))
            return False
        prev_num = num
    print(report)
    return True

safe_count = 0
for line in input_data:
    if is_safe(line.split(' ')):
        safe_count += 1

print('safe: ', safe_count)
