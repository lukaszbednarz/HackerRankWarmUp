#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect
from collections import deque

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words

def matchH(s, word, k = 0):

    if s[k - 1] != "+":
        k -= 1

    l = 10
    max_i = (k//10 + 1) * 10

    i = k
    for a in word:
        if i >= max_i or (a != s[i] and s[i] != "-"):
            return False, None, None
        else:
            s[i] = a
            i += 1

    if i < max_i and s[i] != "+":
        return False, None, None

    i = nextIndex(s, i)
    return True, s, i


def matchV(s, word, k = 0):
    max_i = len(s)

    if k >= 10 and s[k - 10] != "+":
        k -= 10

    i = k
    for a in word:
        if i >= max_i or (a != s[i] and s[i] != "-"):
            return False, None, None
        else:
            s[i] = a
            i += 10
    if i < max_i and s[i] != "+":
        return False, None, None

    i = nextIndex(s, k)
    return True, s, i

def crosswordPuzzle(crossword, words):
    # Write your code here

    s = [item for elem in crossword for item in list(elem)]
    l = len(s)
    q = deque()
    q.extend(words)
    i = nextIndex(s, 0)

    stack = []

    q_size = len(q)
    max_iter = q_size * (q_size + 1) // 2
    count = 0

    while q and i < l:
        q_size = len(q)
        max_iter = q_size * (q_size + 1) // 2

        w = q.popleft()
        matchh, tmp, next_i = matchH(s.copy(), w, i)
        if matchh:
            stack.append((s, i, w))
            i = next_i
            s = tmp
            count = 0
            continue
        matchv, tmp, next_i = matchV(s.copy(), w, i)
        if matchv:
            stack.append((s, i, w))
            i = next_i
            s = tmp
            count = 0
            continue

        q.append(w)

        if count > max_iter:
            s, i, w = stack.pop()
            q.append(w)

            count = 0
        else:
            count += 1


    ans = listToGrid(stack[-1][0])

    return ans

def nextIndex(s, i, c = "-"):
    l = len(s)
    while i < l and s[i] != c:
        i += 1
    return i

def listToGrid(s):
    ans = []
    for i in range(0, 100, 10):
        ans.append("".join(s[i:i + 10]))
    return(ans)

def printGrid(s):

    for r in listToGrid(s):
        print(r)




if __name__ == '__main__':
    fptr = open('./tests/CrosswordPuzzle6.txt', 'r')

    crossword = []

    for _ in range(10):
        crossword_item = fptr.readline().strip()
        crossword.append(crossword_item)

    words = fptr.readline().split(";")

    result = crosswordPuzzle(crossword, words)

    for r in result:
        print(r)
