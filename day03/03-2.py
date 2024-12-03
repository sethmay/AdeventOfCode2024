import sys, re
sys.path.append("../helpers.py")
from helpers import *

#input_data = load_input(3, InputType.MAIN)
input_data = load_input(3, InputType.EXAMPLE)


do_donts = input_data.split('do()')
#print(do_donts)

test = []
for item in do_donts:
    match = re.search(r"don\'t\(\)", item)
    print(match)
    if (match):
        test.append(item[match.end():])

#print(do_donts)

#print(test)

# pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
# matches = re.findall(pattern, input_data)
#
# mult_pattern = r"[0-9]{1,3}"
# total = 0
# for expression in matches:
#     items = re.findall(mult_pattern, expression)
#     total += int(items[0]) * int(items[1])
#
# print(total)



#https://stackoverflow.com/questions/3475251/split-a-string-by-a-delimiter-in-python
#https://stackoverflow.com/questions/46766530/python-split-a-string-by-the-position-of-a-character