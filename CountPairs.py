#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right


#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    arr.sort()

    l = len(arr)
    i = 0
    n = 1

    ans = 0

    while i < l - 1:
        a = arr[i + 1]
        if arr[i + 1] == a:
            i += 1
            n += 1

        if k == 0:
            ans += n * (n + 1) // 2
        else:
            j = i + 1
            while j < l:
                b = arr[j] - a
                if b < k:
                    j += 1
                elif b == k:
                    j += 1
                    ans += n
                else:
                    break
        i += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
