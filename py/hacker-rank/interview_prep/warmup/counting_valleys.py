#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount = 0
    elevationPos = 0 #sea level
    inValley = False

    for step in s:
        elevDir = 1 if step == 'U' else -1

        if elevationPos == 0 and elevDir < 0:
            # entering valley
            valleyCount += 1

        elevationPos += elevDir

    return valleyCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
