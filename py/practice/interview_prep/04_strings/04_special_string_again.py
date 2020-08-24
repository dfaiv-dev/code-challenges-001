#!/bin/python3

import math
import os
import collections
import random
import re
import sys

# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Complete the substrCount function below.
def substrCount(n, s):
    # valid substrings:
    # - single characters (len)
    # - same characters in a row (combinations, ie: aaaa -> aa, aa, aa, aaa, aaa, aaaa)
    # - same characters with single other character in between (aabaa)
    #
    # single character and same character in a row simple, just keep track walking the string
    # balanced characters, harder?
    # ababa -> aba, bab, aba
    # aabaabab -> aabaa, aba, aba, bab
    # need to keep track of the potential first half of a match (letter and max length?)
    #   same as current character set?
    # track if we have a potential match situation:
    #   if next character set is a single, and the next after is the same character:
    #   track n2, n1, and n current matches
    #   if n1 is single AND n and n2 and n are the same char, then mirror match length is min(len(n2), len(n))
    #
    # track 3 character sets

    # character sets counts: { len: count }
    char_set_counts = {}

    # number of mirror sets: { max_len : count }, aabaa -> len 2
    mirror_set_counts = {}

    # track last three char sets, (n, n-1, n-2) --> n: (char, len)
    char_set_cache = collections.deque([None, None, None])

    # append None, so we can do a final count of the last character set.
    chars = list(s)
    chars.append(None)
    curr_char = chars[0]
    curr_len = 1

    for c in chars[1:]:
        # if diff char, then:
        # - log char set
        # - check if we have a mirror set, log
        # abab
        # curr_char = a (, bab)
        # curr_len = 1
        # c(har) = b (, ab)
        # a != b, long char set, check mirrors, then update state
        #   state: curr_char, len, char_set_cache
        # char_sets: { 1: 1 }
        # mirrors - not a complete set
        # -- state
        # curr_char = b,
        # curr_len = 1
        # cache = [(a, 1), None, None]
        # ...
        # cache = [(b, 1), (a, 1), None]
        # ...
        # cache = [(a, 1), (b, 1), (a, 1)]

        # ERROR 1: for the last character, nothing gets counted
        #   either character is different, and we count for the last character set OR
        #   character is same and we just "continue"
        #   Adding None to end of string to allow final counting
        #   BUT could have just found all character sets first, put in list (single pass)
        #   then count in a second pass.


        if curr_char == c:
            # don't count or modify state until we move to a new character set
            curr_len += 1
            continue

        # else, new character set, add to char set counts, update state (curr char, curr len, mirror cache), count mirrors
        # count mirrors last after state, since the cache is part of the state and we need to log the last character set first.
        char_set_counts[curr_len] = char_set_counts.setdefault(curr_len, 0) + 1

        char_set_cache.appendleft((curr_char, curr_len))
        char_set_cache.pop()
        curr_char = c
        curr_len = 1

        # count mirrors
        # we only have a potential complete mirror set if all cached values are not None, check last value
        if char_set_cache[2]:
            # (char, len),
            [start, middle, end] = char_set_cache
            if not end:
                # no potential mirror, continue
                continue

            # mirror if start, end char same and middle char is length 1
            if start[0] == end[0] and middle[1] == 1:
                # have a mirror, length is min of start/end
                mirror_len = min(start[1], end[1])
                mirror_set_counts[mirror_len] = mirror_set_counts.setdefault(mirror_len, 0) + 1

    # total strings:
    #   combinations of all character sets: [aaaa] => [a, a, a, a, aa, aa, aa, aaa, aaa, aaaa]
    #       4 + 3 + 2 + 1
    #       combinations of odd number [aaaaa] => [a,a,a,a,a,aa,aa,aa,aa,aaa,aaa,aaa,aaaa,aaaa,aaaaa]
    #       5 + 4 + 3 + 2 + 1
    #       so, sum first n natural number
    #       (took way to long to google)
    #           == (n (n + 1)) / 2
    #   mirror sets, just max_len of mirror:
    #   aaabaaa -> aba, aabaa, aaabaaa

    total = 0
    for (len, count) in char_set_counts.items():
        combinations = (len * (len + 1)) / 2
        total += (combinations * count)
    for (len, count) in mirror_set_counts.items():
        combinations = len
        total += (combinations * count)

    return int(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
