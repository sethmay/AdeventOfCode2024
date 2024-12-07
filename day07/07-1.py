import sys
from collections import namedtuple

sys.path.append("../helpers.py")
from helpers import *

#input_data = load_input(7, InputType.MAIN).splitlines()
input_data = load_input(7, InputType.EXAMPLE).splitlines()
input_results = []
input_parts = []

for line in input_data:
    results, parts = line.split(":")
    input_results.append(results)
    input_parts.append(parts.split())
#print(input_results, input_parts)


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l:
            return self._find(val, node.l)
        elif val > node.v and node.r:
            return self._find(val, node.r)

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.l)
            print(node.v, end = " ")
            self._view_tree(node.r)

    def allPaths(self):
        if self.root:
            return self._allPaths(self.root)

    # def _allPaths(self, node):
    #     if node:
    #         if not node.l and not node.r:  # Leaf
    #             yield [node.v]
    #         else:
    #             yield from ([node.v] + arr for arr in self._allPaths(node.l))
    #             yield from ([node.v] + arr for arr in self._allPaths(node.r))

    # def _allPaths(self, node, partial_res, res):
    #     if not node:
    #         return
    #     if not node.l and not node.r:
    #         res.append(partial_res[:] + [node.v])
    #         return
    #     partial_res.append(node.v)
    #     self._allPaths(node.l, partial_res, res)
    #     self._allPaths(node.r, partial_res, res)
    #     partial_res.pop()

    # def _allPaths(self, node, path=[]):
    #     if not node: return  # no node, do nothing
    #     fullPath = path + [node.v]
    #     if node.l or node.r:  # node is not a leaf, recurse down
    #         yield from self._allPaths(node.l, fullPath)  # left leaves if any
    #         yield from self._allPaths(node.r, fullPath)  # right leaves if any
    #     else:
    #         yield fullPath  # leaf node, return final path

    def _allPaths(self, node, path=[]):
        tmp = []
        if node.l:
            tmp.extend(self._allPaths(node.l, path + [node.v]))
        if node.r:
            tmp.extend(self._allPaths(node.r, path + [node.v]))
        if not node.l and not node.r:
            tmp.append(path + [node.v])
        return tmp

    # def _allPaths(self, node):
    #     if node:
    #         if not node.l and not node.r: # Leaf
    #             yield [node.v]
    #         else:
    #             yield from ([node.v] + arr for arr in self._allPaths(node.l))
    #             yield from ([node.v] + arr for arr in self._allPaths(node.r))


def build_premutations (parts):
    round = 1
    tree = Tree()
    for part in parts:
        i = 0
        while i < round:
            #print (part)
            tree.add(part)
            i += 1
        round += 1

    #tree.view_tree()
    print()

    g = tree.allPaths()

    print (g)
    # exit()


def solve (input_results, input_parts):

    i = 0
    solvable_results = []
    while i < len(input_results):
        permutations = build_premutations(input_parts[i])
        i += 1

    print(Colors.purple('foo'))



solve(input_results, input_parts)


