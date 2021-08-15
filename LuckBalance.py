#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    if k == 0:
        return 0

    count = Counter()
    luck = 0
    for c in contests:
        i = c[1]
        l = c[0]

        if i == 0:
            luck += l
        else:
            count[l] += 1

    for l in reversed(sorted(count.keys())):
        if k == 0:
            break
        m = min(k, count[l])
        luck += m * l
        k -= m

    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
