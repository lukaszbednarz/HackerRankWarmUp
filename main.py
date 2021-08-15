#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the triplets function below.
def triplets(a, b, c):
    ai = bi = ci = 0

    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    la = len(a)
    lb = len(b)
    lc = len(c)

    ans = 0

    # p = a[i]
    # q = b[j]
    # r = c[k]

    while bi < lb:
        while ai < la and a[ai] <= b[bi]:
            ai += 1
        while ci < lc and c[ci] <= b[bi]:
            ci += 1

        ans += ai * ci

        bi += 1

    return ans



    return ans


if __name__ == '__main__':
    fptr = open('./tests/TripleSum0.txt', 'r')

    lenaLenbLenc = fptr.readline().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, fptr.readline().rstrip().split()))

    arrb = list(map(int, fptr.readline().rstrip().split()))

    arrc = list(map(int, fptr.readline().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    print(ans)
