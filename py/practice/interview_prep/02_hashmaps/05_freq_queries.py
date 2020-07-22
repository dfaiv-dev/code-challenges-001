#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Complete the freqQuery function below.
def freqQuery(queries):
    # query format
    # x(1):i -> add an instance i to list
    # y(2):i -> remove an instance of i from list
    # z(3):n -> return 1 if there is any instance of i that has frequency n

    # solution 1, brute force with two dictionaries
    # i-freq: {i:freq} -- frequency of i in list. inc/dec based on x/y queries
    # freq-counts: {freq:count} -- count of frequency occurrences for all i's

    i_freq = dict()
    freq_counts = dict()
    q_results = list()

    for q in queries:
        op_code = q[0]
        op_input = q[1]
        freq_curr = None
        freq_next = None

        if op_code == 1:
            # x, add op input to "list"

            # get current freq, so we can decr
            freq_curr = i_freq.get(op_input)
            if not freq_curr:
                i_freq[op_input] = 0
                freq_curr = 0

            freq_next = freq_curr + 1
            i_freq[op_input] = freq_next

            # updates - could be a func
            if freq_counts.get(freq_curr):
                freq_counts[freq_curr] = freq_counts[freq_curr] - 1

            if not freq_counts.get(freq_next):
                freq_counts[freq_next] = 0
            freq_counts[freq_next] = freq_counts[freq_next] + 1
        elif op_code == 2:
            # y, remove op input from "list"

            freq_curr = i_freq.get(op_input)
            if freq_curr:
                freq_next = freq_curr - 1
                i_freq[op_input] = freq_next

            # update counts -- could be a func
            if freq_counts.get(freq_curr):
                    freq_counts[freq_curr] = freq_counts[freq_curr] - 1

            if not freq_counts.get(freq_next):
                freq_counts[freq_next] = 0
            freq_counts[freq_next] = freq_counts[freq_next] + 1
        elif op_code == 3:
            # do we have any i freqs of length n (op_input)
            if freq_counts.get(op_input):
                q_results.append(1)
            else:
                q_results.append(0)

    return q_results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
