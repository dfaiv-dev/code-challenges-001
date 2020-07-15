#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Complete the countTriplets function below.
def countTriplets(arr, r):
    '''
    Function Description

    Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given
    as an integer.

    countTriplets has the following parameter(s):
    arr: an array of integers
    r: an integer, the common ratio

    :param arr:
    :param r:
    :return:
    '''

    # probably need to use some combination/permutation calculation?
    #   if we can get an ordered array of only integers with multiples then we can count triplets
    #       add extra triplets if multiple occurs > 1 -- this is where we'd need combination/permutation

    # Combination/Permutation Logic
    # ex: triplets [1,4,4,16] ->
    #       {1:1, 4:2, 16:1}
    # is this 4c3? - combination because, once we have the triplet and number of occurrences, I don't care about order?
    # (n!) / (r!(n - r)!)
    #   4! / (3!(1)!) = 24 / 6 = 4 -- so no?
    # ugh
    #
    # 1 * 2 * 1 = 2?
    # ex: triplets [1,1,1,4,4,16,16] ->
    #        {1:3, 4:2, 16:2}
    #   1(1),4(1),16(1);
    #   1(1),4(2),16(1);
    #   1(1),4(2),16(2);
    #   1(1),4(1),16(2);
    #   ...again for 1(2), 1(3) = 12
    # OK!?


    # multiples = [i for i in arr if i == 1 or i % r == 0]

    # whoops, mod is not how we get a geometric progression
    #   that would be log...
    # multiples = []
    # # sorry, don't know how to do a list comprehension for this.
    # for i in arr:
    #     if i < 1:
    #         continue
    #
    #     log_i_r = math.log(i, r)
    #     if round(log_i_r, 5) == round(log_i_r):
    #         multiples.append(i)
    #
    # # sort, since triplets need to be i < j < k
    # multiples = sorted(multiples)
    #
    # # turn into instance count
    # # ugh, probably a better way, but brute force for now
    # i_counts = []
    # i_current = 0
    # for i in multiples:
    #     if i_current != i:
    #         i_current = i
    #         i_counts.append(1)
    #     else:
    #         # duplicate, increment count
    #         i_counts[-1] = i_counts[-1] + 1
    #
    # triplets_count = 0
    # # for each triplet sequence (j, j + 3, while j + 3 < i_counts.length), find total combinations
    # for i in range(0, len(i_counts) - 2):
    #     j = i+1
    #     k = i+2
    #
    #     triplets_count = triplets_count + (i_counts[i] * i_counts[j] * i_counts[k])

    #    return triplets_count

    # print to make comment collapse work...  wonder if I should just use ''' comments?

    print('attempt 1 wrong')

    # ATTEMPT 2
    #
    # index of triplets in ORIGINAL array need to be in asc order (i < j < k)
    #   I was looking for ALL triplets, should have read clearer. need to learn to slow down.
    # SO
    # ...
    # reading some MORE - geometric progression implies a*r, a*r^2, a*r^3, not just ascending powers
    # ... I need to learn to slow down (again, pff)
    # Read some of the discussion, didn't fully grok it, but thought I should confess

    # Proposal 2 #
    # Track number of incomplete triplets, keyed on what the next number the incomplete set needs to continue
    #   (or complete) the triplet.
    # EX
    # (1,2,3,4,5)
    # [1,2,1,4,8] ; r=2
    # expected: (1,2,4), (2,4,5)
    #
    # triplet_count - total
    # tripX(potential triplets, length X): { N(number needed to continue triplet): COUNT }

    # step1 (i=1, x=1):
    # triplet_next = 1*2 = 2
    # trip1 = { 2:1 }

    # step2 (i=2, x=2):
    # triplet_next = 2*2 = 4
    # trip2 = { 4:1 } // trip1 was waiting for a 2, now it is 1,2, waiting for a 4
    # trip1 = { 2:1; 4:1}

    # step3 (i=3, x=1):
    # triplet_next = 1*2 = 2
    # trip2 = {4:1} // no trip1 waiting for a 1
    # trip1 = {2:2, 4:1}

    # step4 (i=4, x=4)
    # triplet_next = 4*2 = 8
    # triplet_count += trip2[x=4] = 1 == 1 // trip2 had 1 set waiting for a 4, add it to complete
    # trip2 = {4:1, 8:1} // trip1 had 1 set waiting for a 4, add to trip 2
    # trip1 = {2:2, 4:1, 8:1}

    # etc

    print('attempt 2')

    # valid geometric triplets found
    triplet_count = 0
    # potential triplets of length N: {next_X_needed:count}
    triplets_n1 = {}
    triplets_n2 = {}

    for x in arr:
        # REMOVING ROUNDING - seems that the inputs are a geometric progression
        #   with rounding check, one case fails, and I don't want to figure out the issue...

        # make sure it's a multiple
        # if r != 1:
        #     log_x_r = math.log(x, r)
        #     if round(log_x_r, 5) != round(log_x_r):
        #         continue

        # next geometric progression val
        xr = x * r

        # do we have any sub-triplets of length 2 that this x can complete?
        n2_x_count = triplets_n2.get(x)
        if n2_x_count:
            triplet_count += n2_x_count

        # any sub-triplets of length 1 waiting for next_x = x?
        n1_x_count = triplets_n1.get(x)
        if n1_x_count:
            n2_xr_count = triplets_n2.get(xr)
            if not n2_xr_count:
                n2_xr_count = 0

            n2_xr_count += n1_x_count
            triplets_n2[xr] = n2_xr_count

        # add to length 1
        n1_xr_count = triplets_n1.get(xr)
        if not n1_xr_count:
            n1_xr_count = 0
        n1_xr_count += 1
        triplets_n1[xr] =n1_xr_count

    return triplet_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
