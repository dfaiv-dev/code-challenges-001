# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    # find max number of toys mark can buy using k dollars

    # sln 1 - sort prices, take until we run out of money
    # n log n to sort, + n to find how many we can buy
    # (n log n) + n == O(n log n)?

    prices.sort()
    total_spent = 0
    toy_count = 0

    while toy_count < len(prices):
        total_spent += prices[toy_count]
        if total_spent > k:
            break

        toy_count += 1

    return toy_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
