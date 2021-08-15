#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    l = len(arr)
    resp = 0
    r2 = r * r
    cube = set()
    square = set()

    for i in range(l):
        a = arr[i]
        a2 = a * r
        if a in square:
            resp += 1
        if a2 in cube:
            square.add(a2)
        cube.add(a * r2)

    return resp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
