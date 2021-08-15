#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here

    jumps = 0
    shift = 1
    for i in range(len(q)):
        tmp = q[i] - shift - i
        if tmp > 0:
            jumps += tmp
            for j in range(i + 1, i + tmp, 1):
                q[j] += 1
        if tmp > 2:
            return "Too chaotic"
    return str(jumps)


if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]

    print(minimumBribes(q))
