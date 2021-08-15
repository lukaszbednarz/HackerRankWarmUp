#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the freqQuery function below.
def freqQuery(queries):
    a = Counter()
    b = Counter()

    ans = []

    for q in queries:
        c = q[0]
        v = q[1]
        if c == 1:
            if b[a[v]]:
                b[a[v]] -= 1
            a[v] += 1
            b[a[v]] += 1
        elif c == 2:
            if b[a[v]]:
                b[a[v]] -= 1
            a[v] -= 1
            b[a[v]] += 1
        elif b[a[v]] > 0:
            ans.append(1)
        else:
            ans.append(0)
    return (ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
