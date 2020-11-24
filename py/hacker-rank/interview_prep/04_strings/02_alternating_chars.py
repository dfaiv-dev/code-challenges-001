#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # probably should just be able to count number of duplicates?

    curr_char = None
    dup_count = 0
    for c in s:
        # if the character changed (from A/B), then we aren't a duplicate
        #   set it as current and continue
        if c != curr_char:
            curr_char = c
            continue

        # else, it's the same character, mark it as a dupe
        dup_count = dup_count + 1

    return dup_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
