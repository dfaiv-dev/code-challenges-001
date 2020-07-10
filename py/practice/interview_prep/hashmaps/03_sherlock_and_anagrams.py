#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(substr):
    # get all sub strings
    # dict of substrings -> (instanceCount:number, letters:dict{letter -> count})
    #   instanceCount - for anagrams that are identical (pairs would be count - 1)
    #   letters - must have same letter/count pairs as other substrings of same length

    # substrings
    substrings = [
        substr[i: j]
        for i in range(len(substr))
        for j in range(i + 1, len(substr) + 1)
    ]

    # note, I made my own substring combination before in 02_two_strings.py:
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

    # get dict of instance counts and letter counts
    stats = {}
    for substr in substrings:
        if not stats.get(substr):
            letters = {}
            for char in substr:
                if not letters.get(char):
                    letters[char] = 1
                else:
                    letters[char] = letters[char] + 1

            stats[substr] = {
                'instance_count': 1,
                'length': len(substr),
                'letters': letters
            }
        else:
            substr_stats = stats[substr]
            substr_stats['instance_count'] = substr_stats['instance_count'] + 1

    # print(stats)

    # for each substring (stats key), look for other substrings of same length that have same letter counts

    # for substr, substr_stats in stats.items():

    ##
    # ugg, nested loop is not elegant, and no way its going to pass perf

    ##
    # solution 2: sub strings, with characters sorted

    substr_counts = {}
    for substr in substrings:
        substr_sorted = ''.join(sorted(substr))
        if not substr_counts.get(substr_sorted):
            substr_counts[substr_sorted] = 1
        else:
            substr_counts[substr_sorted] = substr_counts[substr_sorted] + 1

    # anagrams_count = 0
    # for counts in substr_counts.values():
    #     anagrams_count += (counts - 1)

    # return anagrams_count

    ##
    # oops, they want all combinations, need to factorial?
    # anagrams_count = 0
    # for counts in substr_counts.values():
    #     if counts == 1:
    #         continue
    #
    #     anagrams_count += math.factorial(counts - 1)

    ##
    # oops, factorial is not how you calculate combinations
    # n choose r (where r = 2) since we want pairs
    anagrams_count = 0
    for counts in substr_counts.values():
        # math.comb only works in py 3.8?
        # anagrams_count += math.comb(counts, 2)

        if counts <= 1:
            continue

        # nCr = (n!) / (r!(n - r)!)
        anagrams_count += int(
            math.factorial(counts) /
            (2 * math.factorial(counts - 2)))

    # return substr_counts
    return anagrams_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
