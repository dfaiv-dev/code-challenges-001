#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Complete the repeatedString function below.
def repeatedString(s, n):
    sLen = len(s)
    wholeStrRepeats = math.floor(n / sLen)
    trailingStrLen = n % sLen
    trailingStr = s[0:trailingStrLen]

    aCount = (s.count('a') * wholeStrRepeats) + trailingStr.count('a')

    return aCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
