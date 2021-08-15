#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    l = len(s1)
    ans = 0
    for i in range(l, 0, -1):
        comb1 = combinations(s1, i)
        for c1 in comb1:
            comb2 = combinations(s2, i)
            for c2 in comb2:
                if c1 == c2:
                    return i
    return 0


def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result


if __name__ == '__main__':

    s1 = "HARRY"

    s2 = "SALLY"

    result = commonChild(s1, s2)

    print(result)

    result = lcs(s1, s2)

    print(result)
