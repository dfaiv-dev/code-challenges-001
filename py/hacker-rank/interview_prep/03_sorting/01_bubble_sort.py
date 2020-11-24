#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    # print numswaps, first elem, last elem
    # ugh, this seems like a waste of time, but I'll do them all.
    # sudo code
    # for (int i = 0; i < n; i++) {
    # for (int j = 0; j < n - 1; j++) {
    # // Swap adjacent elements if they are in decreasing order
    # if (a[j] > a[j + 1]) {
    # swap(a[j], a[j + 1]);
    # }
    # }
    # }

    swapCount = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                swapCount += 1
                swap = a[j+1]
                a[j+1] = a[j]
                a[j] = swap

    print(f"Array is sorted in {swapCount} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
