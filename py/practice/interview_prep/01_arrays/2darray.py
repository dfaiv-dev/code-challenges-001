#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def hourglassSum(arr):
    hourGlassRelativeIndcies = [
        (0,0), (1,0), (2,0),
        (1,1),
        (0,2), (1,2), (2,2)
    ]

    hourGlassSumResults = []
    hourGlassOriginX = 0
    while hourGlassOriginX + 2 < 6:
        hourGlassOriginY = 0
        while hourGlassOriginY + 2 < 6:
            print('origin: ' + str(hourGlassOriginX) + ', ' + str(hourGlassOriginY))
            sum = 0
            for idx in hourGlassRelativeIndcies:
                x = hourGlassOriginX + idx[0]
                y = hourGlassOriginY + idx[1]
                print(str(x) + "," + str(y))
                sum += arr[y][x]

            hourGlassSumResults.append(sum)
            hourGlassOriginY += 1

        hourGlassOriginX += 1


    return max(hourGlassSumResults)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
