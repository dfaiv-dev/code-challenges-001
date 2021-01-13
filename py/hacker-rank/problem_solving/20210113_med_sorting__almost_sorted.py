#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/almost-sorted/problem
# can an array be sorted by either: a) swapping two elements, or b) reversing a subsegment of the array?

# sample 2
# 3
# 3 1 2
# no

# sample 3
# 6
# 1 5 4 3 2 6
# yes
# reverse 2 5

#
# *** implementation notes 1 ***
#
# - find "segments" that are not in ascending order
#       - for each i
#       - if i + 1 < i, then in unsorted segment
#       - extend segment  (i+n) until i+n >= i
# - if no unsorted segments, yes
# - if >1 unsorted segments, no
# - else - 1 unsorted segment, check if we can sort it with one of our ops

# - if segment length == 2 ? yes, swap
# - else
#       - reverse segment
#       - sorted? yes, else no

#
# UPDATE 1
# swapping can be any two elements, don't need to be next to each other
#
# - multiple segments == no should still be valid
# - if reverse is sorted - still valid
# - swap two in the unsorted segment
#       can only be first and last element?
#       [1,2,6,4,5,3,7] - [6,4,5,3] -> [3,5,4,6] X
#

# UPDATE 2
# [43, 65, 1, 98, 99, 101]
# unsorted segment can be sorted/swapped, but the segment itself does not fit in the array
# [65,1] -> [1,65] -> [43,1,65,98,99,101] -> X

# Complete the almostSorted function below.
def almostSorted(arr):
    # arr of index tuples
    unsorted_segments = []

    sorted_index = 0
    min_sorted = 0
    while sorted_index < len(arr):
        x = arr[sorted_index]
        if x >= min_sorted:
            min_sorted = x
            sorted_index += 1
            continue

        # else we are in an unsorted segment
        # expand the segment until we get back to a sorted
        last_sorted = arr[min(0, sorted_index - 2)]
        unsorted_index_start = sorted_index - 1
        unsorted_index_end = sorted_index
        unsorted_start_val = arr[sorted_index - 1]
        if x < last_sorted:
            print('no')
            return

        while unsorted_index_end + 1 < len(arr):
            unsorted_candidate = arr[unsorted_index_end + 1]
            if unsorted_candidate < last_sorted:
                print('no')
                return

            if unsorted_candidate < unsorted_start_val:
                unsorted_index_end += 1
                continue
            else:
                break

        unsorted_segments.append([unsorted_index_start, unsorted_index_end])
        sorted_index = unsorted_index_end + 1

    unsorted_segments_count = len(unsorted_segments)
    if unsorted_segments_count == 0:
        print('yes')
        return
    if unsorted_segments_count > 1:
        print('no')
        return

    unsorted_seg = unsorted_segments[0]
    unsorted = arr[unsorted_seg[0]:unsorted_seg[1] + 1]

    min_sorted = arr[max(0, unsorted_seg[0] - 1)]
    # check if swapping the works first, since that "wins"
    seg_first = unsorted[0]
    seg_last = unsorted[-1]
    unsorted[0] = seg_last
    unsorted[-1] = seg_first

    if all(unsorted[i] <= unsorted[i+1] for i in range(len(unsorted)-1)):
        print('yes')
        print(f'swap {unsorted_seg[0] + 1} {unsorted_seg[1] + 1}')
        return

    # else, restore, and check if we can reverse
    unsorted[0] = seg_first
    unsorted[-1] = seg_last
    unsorted_reversed = list(reversed(unsorted))
    if all(unsorted_reversed[i] <= unsorted_reversed[i+1] for i in range(len(unsorted_reversed)-1)):
        print('yes')
        print(f'reverse {unsorted_seg[0] + 1} {unsorted_seg[1] + 1}')
        return

    print('no')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
