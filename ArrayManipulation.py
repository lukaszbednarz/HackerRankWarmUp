#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    sets = []

    for i in range(len(queries)):
        q = queries[i]
        if q[2] == 0:
            continue

        for j in range(len(sets)):
            s = sets[j]
            if hasOverlap(s, q):
                sets[j] = intersection(s, q)
        sets.append(q)
    res = 0

    for s in sets:
        res = max(res, s[2])

    return res

def hasOverlap(x, y):

    return max(x[0], y[0]) <= min(x[1], y[1])

def intersection(x, y):
    x[0] = max(x[0], y[0])
    x[1] = min(x[1], y[1])
    if(x[1] >= x [0]):
        x[2] += y[2]
    return x


if __name__ == '__main__':
    fptr = open('./tests/MinimumSwaps2.txt', 'r')

    first_multiple_input = fptr.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, fptr.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

