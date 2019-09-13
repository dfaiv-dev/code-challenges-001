#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    q_len = len(q)
    bribes_max = 2
    bribes_total = 0

    q_idx = q_len
    while q_idx > 0:
        bribes = 0
        q_val = q[q_idx - 1]
        while q_val != q_idx and bribes < bribes_max:
            bribes += 1
            q_val = q[q_idx - bribes - 1]

        if q_val != q_idx:
            print("Too chaotic")
            return

        del q[q_idx - bribes - 1]
        bribes_total += bribes
        q_idx -= 1

    print(bribes_total)


def __minimumBribes__sorting(q):
    queue_len = len(q)
    bribe_count_max = 2
    bribe_count_total = 0

    # queue numbering is 1 based
    queue_idx = queue_len
    while queue_idx > 0:
        queue_val = q[queue_idx - 1]

        swap_val = queue_val
        bribe_count = 0

        while swap_val != queue_idx and bribe_count < bribe_count_max:
            bribe_count += 1
            swap_val = q[queue_idx - bribe_count - 1]

        if swap_val != queue_idx:
            print("Too chaotic")
            return

        # swap vals
        q[queue_idx - 1] = swap_val
        q[queue_idx - bribe_count - 1] = queue_val
        bribe_count_total += bribe_count
        queue_idx -= 1

    print(bribe_count_total)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
