#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # sln 1 (brute force):
    # d - trailing days
    # d_exp: List - expenditures of trailing days, ordered
    # median(list): func - sort list, find median
    #
    # there may be a way to optimize the number of sorts we need to do,
    # since it is just a single add and remove
    # python may have a data structure that uses some efficiencies when adding/removing from sorted list

    # def median(items):
    #     # sort a copy
    #     items_sorted = sorted(items)
    #     # length so we know where the median value will be
    #     item_count = len(items)
    #
    #     # odd count, return middle value
    #     if item_count % 2 == 1:
    #         return items_sorted[int(item_count / 2)]
    #     else:
    #         return (items_sorted[int(item_count / 2)] + items_sorted[int(item_count / 2) - 1]) / 2

    # alert_count = 0
    # exp_d = list()
    # for i in range(len(expenditure)):
    #     if len(exp_d) == d:
    #         exp_median = median(exp_d)
    #         if expenditure[i] >= exp_median * 2:
    #             alert_count += 1
    #
    #         exp_d.pop(0)
    #
    #     exp_d.append(expenditure[i])

    # as expected, timeout
    # trying using bisect for the trailing days (maintain a sorted list)
    #
    # time complexity
    # n = len(expenditures)
    # window: 1-n == n (worst case)
    # insert/delete sorted window - bisect - log(n) * 2 == O(log(n))
    # == n*log(n)


    def median_sorted(items_sorted):
        # length so we know where the median value will be
        item_count = len(items_sorted)

        # odd count, return middle value
        if item_count % 2 == 1:
            return items_sorted[int(item_count / 2)]
        else:
            return (items_sorted[int(item_count / 2)] + items_sorted[int(item_count / 2) - 1]) / 2

    alert_count = 0
    trailing_exp = []
    trailing_exp_sorted = []
    for i in range(len(expenditure)):
        # i is current day
        # trailing needs d days
        # compare to i

        exp_curr = expenditure[i]
        if i < d:
            # don't have enough days yet
            trailing_exp.append(exp_curr)
            bisect.insort(trailing_exp_sorted, exp_curr)
            continue

        # enough days, check if notification, then update trialing
        exp_median = median_sorted(trailing_exp_sorted)
        if exp_curr >= exp_median * 2:
            alert_count += 1

        # add curr expense to trailing, remove oldest
        trailing_exp.append(exp_curr)
        exp_expired = trailing_exp.pop(0)

        # remove the expired from the sorted list, add the new expense sorted
        exp_expired_idx = bisect.bisect(trailing_exp_sorted, exp_expired) - 1
        trailing_exp_sorted.pop(exp_expired_idx)
        bisect.insort(trailing_exp_sorted, exp_curr)

    return alert_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
