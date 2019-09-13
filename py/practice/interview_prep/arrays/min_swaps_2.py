#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0
    for i in range(len(arr)):
        val = arr[i]

        while val != (i + 1):
            swap_val = arr[val - 1]
            arr[val - 1] = val
            arr[i] = swap_val
            swap_count += 1

            val = swap_val

    return swap_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
