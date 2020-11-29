#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

# Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady.
# Right now, he is examining a gene represented as a string `gene`. It is not necessarily steady. Fortunately, Limak can
# choose one (maybe empty) substring of `gene` and replace it with any string of the same length.
#
# Modifying a large substring of bear genes can be dangerous. Given a string `gene`,
# can you help Limak find the length of the smallest possible substring that he can replace to make `gene` a steady gene?
#
# Note: A substring of a string `s` is a subsequence made up of zero or more contiguous characters of `s`.
#
# Complete the steadyGene function below.

# DEBRIEF
# - took about 30-45 minutes
# - main point was to realize that the valid window substring was based on the overage gene character counts
# - initial plan worked

def steadyGene(gene):
    '''
    return an integer that represents the length of the smallest substring to replace.

    n = |gene|
    4 <= n <= 500,000
    n % 4 == 0
    gene[i] in [CGAT]

    --- sample
    GAAATAAA
    replace AATAA => TTCCG => GATTCCGA
    ---

    ---
    - initial thought is that some sort of window function may work
    - also wonder if n % 4 == 0 will help?
    ... 5 minutes
    - there needs to be an equal amount of ALL 4 letters
    - can count each letter, find delta D needed to to get to n/4
    - foreach letter > n/4, find substring that contains >= D of each letter
    -       ^ use window function
    - if window is smallest, record
    ---

    --- algo
    - n = len(gene)
    - steady_gene_count = n / 4
    - count instances of each letter (single pass n) - { 'LETTER': 'COUNT' }
    - gene_delta = { 'LETTER': 'COUNT' - steady_gene_count >> where gene_delta > 0 }
    - window_start = 0
    - window_end = 0
    - window_char_counts: { G : COUNT }
    - window_size_min = n
    - while window_end < len(n)
    -   add_char to counts
    -
    -   while window_start <= window_end:
    -       if is_valid_substring(window_char_count):
    -           # smaller than smallest? record new smallest size
    -           sub_string_len = (window_start - window_end) + 1
    -           if window_size_min > sub_string_len:
                    window_size_min = sub_string_len

                # either way shrink the window by one

                #remove the char from substring and window start
    -           remove_char (gene, window_start, window_char_counts)

                # update start index
    -           window_start += 1
    -       else
    -           break
    -
    -   window_end += 1
    '''

    # get length gene
    n = len(gene)
    # how many of each letter do we expect? guaranteed n % 4 == 0
    steady_char_count = n / 4

    # get string instance count
    char_instance_count = {}
    for c in gene:
        if c in char_instance_count:
            char_instance_count[c] += 1
        else:
            char_instance_count[c] = 1

    # get deltas that are >0
    deltas = {}
    for c in char_instance_count:
        count = char_instance_count[c]
        if count > steady_char_count:
            deltas[c] = count - steady_char_count

    # special case, no deltas, then already steady
    if len(deltas) == 0:
        return 0

    window_start = 0
    window_end = 0
    window_char_counts = {}
    # min window size will never be more than the entire gene
    window_size_min = n

    while window_end < n:
        # expand window substring char counts to end
        c = gene[window_end]
        if c in window_char_counts:
            window_char_counts[c] += 1
        else:
            window_char_counts[c] = 1

        # shrink window until substring not valid
        # (window_start = window_end is valid, since it is len=1)
        while window_start <= window_end:
            is_valid_substring = True
            for k in deltas:
                k_delta = deltas[k]
                if k not in window_char_counts or \
                        window_char_counts[k] < k_delta:
                    is_valid_substring = False
                    break

            if is_valid_substring:
                # if current window is new shortest, record
                sub_string_len = (window_end - window_start) + 1
                if sub_string_len < window_size_min:
                    window_size_min = sub_string_len

                # either way, reduce window
                window_start_char = gene[window_start]
                window_char_counts[window_start_char] -=1
                window_start += 1
            else:
                # not valid substring, stop shrinking window and keep expanding window
                break

        window_end += 1

    return window_size_min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
