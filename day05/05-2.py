import sys
from collections import namedtuple

sys.path.append("../helpers.py")
from helpers import *

input_data = load_input(5, InputType.MAIN).splitlines()
#input_data = load_input(5, InputType.EXAMPLE).splitlines()


def buildRuleset (rule_input):
    rules = {}

    for item in rule_input:
        if item[0] in rules:
            rules[item[0]].append(item[1])
        else:
            rules[item[0]] = [item[1]]
    return rules


def check_rule (rules, page1, page2):
    if page1 in rules and page2 in rules[page1]:
        return True
    return False


def check_update (rules, update):
    pages = len(update)
    i = 0
    while i < pages:
        if i+1 < pages and not(check_rule(rules, update[i], update[i+1])):
            return False
        i += 1
    return True

def get_first (rules, page_list):
    first = page_list[0]
    i = 0
    while i < len(page_list):
        page = page_list[i]

        if (page_list[i] in rules and first in rules[page_list[i]]):
            first = page_list[i]
        i += 1
    return first

def correct_order(rules, update):
    reorder = []

    while len(update) > 0:
        first = get_first(rules, update)
        reorder.append(first)
        update.remove(first)

    return reorder


def solve (input_data):
    rules_input = []
    updates = []
    part1 = True
    for line in input_data:
        if line == '':
            part1 = False
            continue

        if part1:
            rules_input.append(line.split('|'))
        else:
            updates.append(line.split(','))

    rules = buildRuleset(rules_input)

    passing = []
    corrected = []
    for update in updates:
        if (check_update(rules, update)):
            passing.append(update)
        else:
            corrected.append(correct_order(rules, update.copy()))

    #print(rules)
    #print(updates)
    #print(passing)
    #print(corrected)

    score = 0
    for item in corrected:
        page_count = len(item)
        middle_index = int((page_count+1)/2)-1 #+1 to account from indexes starting at 0
        score += int(item[middle_index])

    print(score)


solve(input_data)
