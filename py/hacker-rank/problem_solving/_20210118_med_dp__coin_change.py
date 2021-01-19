#!/bin/python3

import math
import os
import random
import re
import sys

# Given an amount and the denominations of coins available, determine how many ways change can be made for amount.
# There is a limitless supply of each coin type.

# ex 1
# amount:   4
# coins:    1 2 3
# results:
#   {1,1,1,1}
#   {1,1,2}
#   {2,2}
#   {1,3}

# *** attempt 1 ***
# use largest coins to smallest
# - available coins {3,2,1}
# - {3} - complete (no)
# - {3,3} X
# - {3,2} X
# - {3,1} Y
# - no more "3" options, remove
# - available coins {2,1}
# - {2}
# - {2,2} Y
# - {2,1}
# - {2,1,1} Y
# - available coins  {1}
# - {1}
# - {1,1}
# - {1,1,1}
# - {1,1,1,1}
#
#

# a: 10, cs: 2,3,5,6
# ({2,2,2,2,2}, {2,2,3,3}, {2,3,5}, {5,5})
#
# {2}
# {2,2}
# {2,2,2}
# {2,2,2,2}
# {2,2,2,2,2} Y (X 3,5,6)
# {2,2,2,3}
# {2,2,2,3,3} X
# {2,2,2,5} X
# {2,2,3}
# {2,2,3,3} Y
# {2,2,5}
# {2,2,5,5} X
# {2,2,6} Y
# {2,3}
# {2,3,3}
# {2,3,3,3} X
# {2,3,5} Y
# {2,5}
# {2,5,5} X
# {2,6}
# {2,6,6} X
# {3}
# {3,3}
# {3,3,3} X
# {3,5}
# {3,5,5} X
# {3,6}
# {3,6,6} X
# {5}
# {5,5} Y
# {6}
# {6,6} x
# {}

# - sort coins lowest to highest (so we can use ascending order to not overlap coin sets?)
# - for lowest coin, find all combinations
# - for next lowest, find all combinations, excluding prev coin
# - etc
# -- find all combos for coin set {X} --
# remainder = amount
# coin = lowest
# max coin count = floor(remainder / coin)
# if remainder = 0: log combo
# update remainder, next coin

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#


def getWays(n, c):
    coins_sorted = sorted(c)

    return getWaysInteral(n, coins_sorted)


def getWaysInteral(amount, coins_sorted):
    if amount <= 0:
        return 0

    if len(coins_sorted) == 0:
        return 0

    # if smallest coin is larger than amount, then no way
    if coins_sorted[0] > amount:
        return 0

    ways = 0
    for i in range(0, len(coins_sorted)):
        val = coins_sorted[i]

        if val > amount:
            break

        if val == amount:
            ways += 1
            break

        remainder_val = amount - val
        remainder_coins = coins_sorted[i:]

        ways += getWaysInteral(remainder_val, remainder_coins)

    return ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
