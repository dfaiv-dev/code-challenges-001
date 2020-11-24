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
    equal length
    children must be in order
    string length is 5000, so n^2 may be on the table
    does it matter which string is used as the root?

    brute force -probably n!, need find all ordered substrings of a and b, see which match is longest

    **idea 1**
    find indexes of same letters in a -> b, find longest ascending sequence of b indexes.
    ...
    doesn't handle duplicate letters, would always pick first instance of X in b: ie:
      a: AAA, b: AAA
      0:0, 1:0, 2:0
    need index of y occurrence of letter
    also don't need to track as map from a -> b, just found index of b

    * idea 1.1 *
    find longest ascending sequence
    brute force: n^2, for x:1-n, for y:x+1-n, pfff, I can't even think of it. Might be more than n^2???

    keep lowest val for each index of seq?
    0,7,8,9,6,1,2,5,3,4
      0
      7 > 0 ? add to i + 1 -> 0,7
      8 > 7 ? add to i + 1 ... -> 0,7,8,9
      6 > 9 ? > 8 ? > 7 ? > 0 ? set i + 1 -> 0,6,8,9
      1 > 9 ? > 8 ? > 6 ? > 0 ? -> 0,1,8,9
      2 > 9 ? > 8 ? > 1 -> 0,1,2,9
      5 > 9 ? > 8 ? > 2 -> 0,1,2,5
      3 > 5 ? > 2 -> 0,1,2,3
      4 > 3 ? -> 0,1,2,3,4

    basically n^2? worst case? probably could use a sorted insert. but at 5k item max, probably OK.

    * idea 1.2 *
    can do a single pass of of b first to get a dict of letter -> [indexes] so
      we don't need to traverse the entire string to find instance N of letter_x

    :param s1:
    :param s2:
    :return:
    '''

    # map of each char in s2 to all of its (ordered) indexes in the str
    s2_char_indexes_map = {}
    idx = 0
    for char in s2:
        indexes = s2_char_indexes_map.setdefault(char, [])
        indexes.append(idx)
        idx = idx + 1

    # for each char instance of s1, find the corresponding index of s2
    s1_char_counts_map = {}
    s2_seq = []
    for char in s1:
        count = s1_char_counts_map.setdefault(char, 0)

        s2_chars = s2_char_indexes_map.get(char)
        if s2_chars and len(s2_chars) > count:
            s2_seq.append(s2_chars[count])

        s1_char_counts_map[char] = count + 1

    if len(s2_seq) == 0:
        return 0

    # find longest asc sequence of s2_seq
    seq_vals = s2_seq[0:1]
    for i in s2_seq[1:]:
        # the seq_vals will always be sorted
        # use sorted insert to find insertion point, but replace instead
        #   unless insertion is beyond end of array, then add

        insertion_idx = bisect.bisect(seq_vals, i)
        if insertion_idx == len(seq_vals):
            seq_vals.append(i)
        else:
            seq_vals[insertion_idx] = i

    return len(seq_vals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
