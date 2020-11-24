#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Complete the isValid function below.
def isValid(s):
    # count char instances
    # count total instances of distinct char counts
    # distinct counts == 1 || distinct counts == 2 and diff == 1 -- else false

    char_counts = {}
    for c in s:
        count = char_counts.get(c)
        count = 0 if not count else count
        char_counts[c] = count + 1

    # char_count_instances = {} # char_count : instances
    # for (_, count) in char_counts.items():
    #     instances = char_count_instances.get(count)
    #     instances = 0 if not instances else instances
    #     char_count_instances[count] = instances + 1
    #
    # if len(char_count_instances) > 2:
    #     return 'NO'
    # if len(char_count_instances) == 1:
    #     return 'YES'

    # distinct char counts == 2, see if total counts diff by 1
    # instance_counts = list(char_count_instances.values())
    # return 'YES' if 1 in instance_counts else 'NO'

    # OOPS - we can only have ONE letter with a difference instance count, and that instance needs to be 1 diff than the other instance.
    # this is a really bad comment, sorry.

    # instance_counts = list(char_count_instances.values())
    # distinct_instances = list(char_count_instances.keys())
    # if 1 in instance_counts and abs(distinct_instances[0] - distinct_instances[1]) == 1:
    #     return 'YES'
    # else:
    #     return 'NO'

    # FAILED
    # that's what I get for not understanding the comment I was writing to explain the logic
    # -- reset
    # we have two difference instance counts
    # ugh
    # what if we just iterate ALL the instance counts, and if one is diff, check if it is diff by 1?
    # counts = list(char_counts.keys())
    # current_count = counts[0]
    # distinct_counts = 1
    # for count in counts[1:]:
    #     if current_count == count:
    #         continue
    #
    #     distinct_counts += 1
    #     if distinct_counts > 2:
    #         return 'NO'
    #
    #     diff = abs(current_count - count)
    #     if diff > 1:
    #         return 'NO'

    # won't work either, since if the one diff count is first, then everything breaks. need count of count still.
    # really seems like it should be working, probably should take a break and come back, but feels so close.

    # ahh, crap. 'aabcc' returns True, because it was using absolute diff
    # need to check that the char count of the single instance is 1 MORE than the multi instance

    char_count_instances = {}  # char_count : instances
    for (_, count) in char_counts.items():
        instances = char_count_instances.get(count)
        instances = 0 if not instances else instances
        char_count_instances[count] = instances + 1

    if len(char_count_instances) > 2:
        return 'NO'
    if len(char_count_instances) == 1:
        return 'YES'

    has_single_instance = 1 in char_count_instances.values()
    if not has_single_instance:
        return 'NO'

    single_instance_count = 0
    multi_instance_count = 0
    for (k,v) in char_count_instances.items():
        if v == 1:
            single_instance_count = k
        else:
            multi_instance_count = k

    # return 'YES' if single_instance_count - multi_instance_count == 1 else 'NO'
    # pfff, either the single_instance_count drops to 0, or to the multi instance count
    return 'YES' if single_instance_count == 1 or single_instance_count - multi_instance_count == 1 else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
