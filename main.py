#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from collections import Counter


# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries


class Node:

    def __init__(self, value, depth=None, left=None, right=None):
        self.value = value
        self.trav = None
        self.left = left
        self.right = right
        self.depth = depth

    def swapChildren(self):
        tmp = self.left
        self.left = self.right
        self.right = tmp


    def swapNodes(self, query, max_depth):

        levels = []
        tmp = query
        while tmp <= max_depth:
            levels.append(tmp)
            tmp += query

        q = deque()
        s = deque()
        q.append(self)
        s.extend(levels)
        d = 0

        while q:
            n = q.popleft()
            sd = n.depth
            if s and d < sd:
                d = s.popleft()
            if d == sd:
                n.swapChildren()

            if s or d > sd:
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)

        print()


    def traverse(self):
        vals = []

        if self.left is not None:
            vals.extend(self.left.traverse())
        vals.append(self.value)
        if self.right is not None:
            vals.extend(self.right.traverse())

        return vals





def generateTree(indexes):

    root = Node(1, 1)

    ii = iter(indexes)
    q = deque()
    q.append(root)

    max_depth = 0
    while q and ii:
        lr = next(ii)
        n = q.popleft()
        depth = n.depth

        if depth > max_depth:
            max_depth = depth

        depth += 1

        left = lr[0]
        if left != -1:
            n.left = Node(left, depth)
            q.append(n.left)

        right = lr[1]
        if right != -1:
            n.right = Node(right, depth)
            q.append(n.right)

    return root, max_depth





def swapNodes(indexes, queries):
    # Write your code here

    root, max_depth = generateTree(indexes)

    print(root.traverse())
    ans = []

    for q in queries:
        root.swapNodes(q, max_depth)
        ans.append(root.traverse())

    return ans





if __name__ == '__main__':
    fptr = open('./tests/SwapNodes0.txt', 'r')

    n = int(fptr.readline().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, fptr.readline().rstrip().split())))

    queries_count = int(fptr.readline().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(fptr.readline().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    for r in result:
        print(r)
