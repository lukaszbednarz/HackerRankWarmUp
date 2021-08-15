#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    l = len(s)
    mi = l - 1
    pairs = 0
    # Write your code here
    for i in range(l):
        for j in range(mi, mi - i - 1, -1):
            for k in range(l - i):
                if s[i:] == s[l - 1:i - 1:-1]:
                    pairs += 1
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
