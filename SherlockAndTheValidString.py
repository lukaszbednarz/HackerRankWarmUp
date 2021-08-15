#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    a = Counter(s)
    b = Counter(a.values())

    if len(b) == 1:
        return True
    elif len(b) == 2:
        keys = sorted(b.keys)
        if keys[0] == 1 and b[keys[0]] == 1:  # any  character
            return True
        elif keys[0] == 1 and b[keys[0]] - b[keys[1]] == 1:
            return True
    else:
        return False

    return False

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
