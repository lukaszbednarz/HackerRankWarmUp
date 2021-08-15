#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left, insort
from collections import deque

def rolling_median(iterable, k):
    # taking iterator so it works on sequences and generators
    it = iter(iterable)

    # a deque has optimized access from its endpoints
    # we consume and store the first K values
    deq = deque(next(it) for _ in range(k))

    # initialize the sorted array
    sor = sorted(deq)

    # index of median in sorted list
    i = (k + 1) // 2 - 1
    if k%2:
        yield sor[i]
    else:
        yield (sor[i] + sor[i+i])/2

    for r in it:
        # `deq` keeps track of chronological order
        out = deq.popleft()
        deq.append(r)
        # `sor` keeps track of sortedness
        sor.pop(bisect_left(sor, out))
        insort(sor, r)
        if k % 2:
            yield sor[i]
        else:
            yield (sor[i] + sor[i + i]) / 2
#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    l = len(expenditure)
    m = rolling_median(expenditure, d)
    alerts = 0
    for i in range(d, l):
        med = next(m)
        if expenditure[i] >= 2 * med:
            alerts += 1

    return alerts


if __name__ == '__main__':

    d = 4

    expenditure = [1, 2, 3, 4, 4]

    result = activityNotifications(expenditure, d)

    print(result)
