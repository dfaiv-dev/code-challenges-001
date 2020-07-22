#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    s1_chars = set(s1)
    s2_chars = set(s2)

    if s1_chars.intersection(s2_chars):
        return 'YES'
    else:
        return 'NO'

    #
    # Below is wrong -- was trying to find ALL substrings. Single character substrings are fine.
    #

    # foo
    # f, o, o, fo, oo, foo
    # 0:1, 1:2, 2:3, 0:2, 1:3, 0:3
    # 0:1, 0:2, 0:3, 1:2, 1:3, 2:3

    # def get_substrings(s):
    #     substrings = set()
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             substr = s[i:j]
    #             substrings.add(substr)
    #
    #     return substrings
    #
    # s1_substrings = get_substrings(s1)
    # s2_substring = get_substrings(s2)
    #
    # if (s1_substrings.intersection(s2_substring)):
    #     return 'YES'
    # else:
    #     return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
