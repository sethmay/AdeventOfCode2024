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


class RuleTest(Enum):
    NO_RULE = "no rule"
    PASS = "page1 and page 2 in correct order"
    FAIL = "page2 goes before page1"

def check_rule (rules, page1, page2):
    if page1 in rules and page2 in rules[page1]:
        return RuleTest.PASS
    if page2 in rules and page1 in rules[page2]:
        return RuleTest.FAIL
    return RuleTest.NO_RULE


def check_update (rules, update):
    check = True

    pages = len(update)
    i = 0
    while i < pages:
        if i+1 < pages:
            test = check_rule(rules, update[i], update[i+1])
            if test == RuleTest.FAIL:
                check = False
        i += 1
    return check



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
    for update in updates:
        if (check_update(rules, update)):
            passing.append(update)

    #print(rules)
    #print(updates)
    #print(passing)

    score = 0
    for item in passing:
        page_count = len(item)
        middle_index = int((page_count+1)/2)-1 #+1 to account from indexes starting at 0
        score += int(item[middle_index])

    print(score)


solve(input_data)
