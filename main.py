#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the triplets function below.
def triplets(a, b, c):
    i = j = k = 0
    la = len(a)
    lb = len(b)
    lc = len(c)

    a.sort()
    b.sort()
    c.sort()
    ans = 0

    while i < la and j < lb and k < lc:
        p = a[i]
        q = b[j]
        r = c[k]

        if p <= q:
            i += 1
        elif r <= q:
            k += 1
        else:
            j += 1
            ans += i * k

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
