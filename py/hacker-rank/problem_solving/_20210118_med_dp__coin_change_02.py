#!/bin/python3

import math
import os
import random
import re
import sys

# Given an amount and the denominations of coins available, determine how many ways change can be made for amount.
# There is a limitless supply of each coin type.

# attempt 2
# cache previous values somehow, getting timeouts

# ex 1
# amount:   4
# coins:    1 2 3
# results:   {1,1,1,1},   {1,1,2},   {2,2},   {1,3}
#
# =
# (1) -> 3, [1,2,3] = 3 +
# (2) -> 2, [2,3] = 1 +
# (3) -> 1, [3] = 0

# 3, [1,2,3] = 3
# (1) -> 2, [1,2,3] = 2 +
# (2) -> 1, [2,3] = 0 +
# (3) -> 0, [3] = 1

# 2, [1,2,3] = 2
# (1) -> 1, [1,2,3] = 1 +
# (2) -> 0, [2,3] = 1 +
# (3) -> -1, [3] = 0

# 1, [1,2,3] = 1
# (1) -> 0, [1,2,3] = 1 +
# (2) -> -1, [2,3] = 0 +
# (3) -> -2, [3] = 0

# 1, [2,3] = 0
# (2) -> -1, [2,3] = 0
# (3) -> *-2, [3] = 0

# 2, [2,3] = 1
# (2) -> 0, [2,3] = 1
# (3) -> -1, [3] = 0


# a: 10, cs: 2,3,5,6
# ({2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}, {5,5})
#
# =
# (2) -> 8, [2,3,5,6] = 3 +
# (3) -> 7, [3,5,6] = 0 +
# (5) -> 5, [5,6] = 1 +
# (6) -> 4, [6] = 0

# 8, [2,..] = 3
# (2) -> 6, [2,..] = 2 +
# (3) -> 5, [3,..] = 1 +
# (5) -> 3, [5..] = 0
# (6) -> 2, [6] = 0

# 6, [2,..] = 2
# (2) -> 4, [2,..] = 1 +
# (3) -> 3, [3,..] = 1 +
# (5) -> 1, [5..] = 0 +
# (6) -> 0, [6] = 1

# 4, [2,..] = 1
# (2) -> 2, [2,..] = 1 +
# (3) -> 1, [3,..] = 0 +
# (5) -> -1, [5,..] = 0
# (6) -> -2, [6] = 0

# 2, [2,...] = 1
# (2) -> 0, [2,...] = 1 +
# (3) -> -1 XXXX = 0

# 1, [3,..] = 0

# 3, [3,..] = 1

# 5, [3,..] = 1
# (3) -> 2, [3,..] = 0
# (5) -> 0, [5...] = 1
# X

# 7, [3,..] = 0
# (3) -> 4, [3,..] = 0
# (5) -> 2, [5,..] = 0
# (6) -> 2, [6] = 0

# 4, [3,...] = 0
# (3): 1, [3,..] = 0
# (5): -1 XXXX

# 5, [5,..] = 1
# (5): 0, [5,...] = 1
# XXX
#

# cache by remainder:smallest_coin -> num_ways

def getWays(n, c):
    coins_sorted = sorted(c)

    return getWaysInteral(n, coins_sorted)


ways_count = {}
def getWaysInteral(amount, coins_sorted):
    if len(coins_sorted) == 0:
        return 0

    # if smallest coin is larger than amount, then no way
    if coins_sorted[0] > amount:
        return 0

    amount_cache = ways_count.get(amount)
    if not amount_cache:
        amount_cache = {}

    smallest_coin = coins_sorted[0]
    coin_cache = amount_cache.get(smallest_coin)
    if not coin_cache:
        coin_cache = {}

    if smallest_coin in coin_cache:
        return coin_cache.get(smallest_coin)

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
