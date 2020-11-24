#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # can we just count occurrences, then compare?
    # or could keep a running count of the diff?

    char_cache = {}
    for c in a:
        count = char_cache.get(c)
        count = count if count else 0
        char_cache[c] = count + 1

    for c in b:
        count = char_cache.get(c)
        count = count if count else 0
        char_cache[c] = count - 1

    diff = 0
    for (c, count) in char_cache.items():
        diff = diff + abs(count)

    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
