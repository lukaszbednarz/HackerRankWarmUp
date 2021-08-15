#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from collections import deque


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    l = len(c)
    a = Counter()

    q = deque()
    q.extend(range(k))

    c1 = c[:l - k]
    c2 = c[l - k:]

    while q:


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
