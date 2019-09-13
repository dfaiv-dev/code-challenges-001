#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cloudCount = len(c)
    jumps = 0
    pos = 0

    while pos < cloudCount - 1:
        if pos == cloudCount - 2:
            # last pos is always safe, jump, and done
            jumps += 1
            break

        pos2 = c[pos + 2]
        if pos2 == 0:
            pos += 2
        else:
            pos += 1

        jumps +=1

    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
