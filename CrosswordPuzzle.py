#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect


#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words

def matchWord(s, word, k):
    l = len(s)

    i = 0
    k = 1

    for k in [1, 10]
        for a in word:
            if a != s[i] or s[i] != "-":
                break
            i += k

    return True


def crosswordPuzzle(crossword, words):
    # Write your code here

    s = "".join(crossword)

    stack = s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
