import sys, re
sys.path.append("../helpers.py")
from helpers import *

input_data = load_input(3, InputType.MAIN)
#input_data = load_input(3, InputType.EXAMPLE).replace("\n", '')


do_donts = input_data.split('do()')

do_calcs = []
for item in do_donts:
    pos = item.find("don't()")
    if (pos != -1):
        do_calcs.append(item[:item.find("don't()")])
    else:
        do_calcs.append(item)

data = "".join(do_calcs)
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
matches = re.findall(pattern, data)

mult_pattern = r"[0-9]{1,3}"
total = 0
for expression in matches:
    items = re.findall(mult_pattern, expression)
    total += int(items[0]) * int(items[1])

print(total)
