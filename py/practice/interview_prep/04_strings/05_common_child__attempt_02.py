#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Complete the commonChild function below.
def commonChild(s1, s2):
    '''
    (see also ***__attempt_01)
    equal length
    children must be in order
    string length is 5000, so n^2 may be on the table
    does it matter which string is used as the root?

    still not sure how to exploit equal lengths, or if it matters which string is the "root"

    # idea 2 #
    sudo brute force, hoping that the 5k limit lets us...

    for chars in root string (s1):
        find longest common string in s2
    '''

    # map of each char in s2 to all of its (ordered) indexes in the str
    # use to see if there is a instance of letter after the current index of substr_b
    s2_char_indexes_map = {}
    idx = 0
    for char in s2:
        indexes = s2_char_indexes_map.setdefault(char, [])
        indexes.append(idx)
        idx = idx + 1

    max_len = 0
    start_idx = 0
    while start_idx < len(s1):
        start_char = s1[start_idx]
        if not s2_char_indexes_map.get(start_char):
            start_idx += 1
            continue

        s2_substr_idx = s2_char_indexes_map.get(start_char)[0]
        sub_str_len = 1
        char_instance_count = {start_char: 1}
        for c in s1[start_idx + 1:]:
            count = char_instance_count.setdefault(c, 0) + 1
            char_instance_count[c] = count

            s2_indexes = s2_char_indexes_map.get(c)
            if not s2_indexes:
                continue
            if len(s2_indexes) < count:
                continue

            s2_char_index = s2_indexes[count - 1]
            if s2_char_index > s2_substr_idx:
                s2_substr_idx = s2_char_index
                sub_str_len += 1

        if sub_str_len > max_len:
            max_len = sub_str_len

        start_idx += 1

    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
