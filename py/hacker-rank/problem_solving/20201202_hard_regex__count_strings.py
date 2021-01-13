#!/bin/python3

import os
import sys


# https://www.hackerrank.com/challenges/count-strings/problem
# start date: 2020-12-02 2:50PM
# abandoned: 2021-01-13 -- there seems to be a way to do this using a finite state machine...?
#   still think it could be done with the right recursive logic though

# given a regex and a length of a string, count the number of strings length <= L that could match the regex
# regex language:
# R is a valid regex if:
# 1) R is "a" or "b".
# 2) R is of the form "(R1R2)", where R1 and R2 are regular expressions.
# 3) R is of the form "(R1|R2)" where R1 and R2 are regular expressions.
# 4) R is of the form "(R1*)" where R1 is a regular expression.
#       (the strings recognized are the empty string
#           and the concatenation of an arbitrary number of copies of any string recognized by R1).
#
# Regular expressions can be nested and will always have have two elements in
# the parentheses (* is an element, | is not);
# * will always be the second element of a pair
#
# UPDATE UNDERSTANDING 2020-12-02
# Regular expression must match the ENTIRE string (see Test Case 3)
#   (aa), l = 3 -> 0 matches, since no l=3 string == 'aa'
#
# UPDATE UNDERSTANDING 2020-12-02
#   R1* -> empty string OR any number of R1s
#       a* => a, aa, aaa
#       NOT a* => a, ab, aa,
# ---
# Test Cases
# ((ab)|(ba)) 2
# ((a|b)*) 5
# ((a*)(b(a*))) 100
# Output
# 2
# 32
# 100
#
# *** output value should be (total strings) % (10^9 + 7)
#
# TODO [dmf]: handle 'mod' of length, eg: ((ab)*) - L must be %2 = 0?
# work through
# test case 1: ((ab)|(ba)), length 2
#   ab, length 2 = 1
#   ba, length 2 = 1
#   total = 2
#
# test case 2: ((a|b)*), l=5
#   R = ((a|b)*)
#       = (c2:l1*)
#       = (
#   R1_1 = a; range [1:1], P = c^r = 1
#   R1_2 = b; range [1:1], P = c^r = 1
#   R1
#

# test case 3: ((a*)(b(a*))), l=100
#   R1 = (a*)
#       a*, min/max = 0/L, P = 1^L
#
#   R2 = (b(a*))
#   R2_1 = a*, min/max = 0/L, P = 1
#   R2_2 = b, min/max = 1/1, P = 1
#   R2 min = R2_1_min + R2_2_min = 1
#   R2 max = ''_max + ''_max = L
#   R2 P ??? = R2_1_p ?* R2_2_p = 1?
#
#   l = 100
#   R1 = 0/L;p:1, R2 = 1/L;p:1
#   find possible "layouts" of R1R2
#   ?for each layout, multiply permutations?
#
#   0-99 (inclusive?) = 100
#   100 * r1_p = 100
#   for each of r1, how many ways can we add r2?
#       1
#   r1_p * 1 = 100

#   r1_range_max = r2
#   r1_l = 0, r2_l = 3
#   r1_l = 1, r2_l = 2
#   r1_l = 2, r2_l = 1
#
# test case 4: (((a(ba))|(bb))*), l=5
#   R = ((a|b)*)
#       = (c2:l1*)
#       = (
#   R1_1 = a; range [1:1], P = c^r = 1
#   R1_2 = b; range [1:1], P = c^r = 1
#   R1
#
#
# general ideas?
#   - n choose k, permutations, combinations, etc?
#   - R1* = 2 ^ (l-1) ?
#       ** = n^r = 2^l (ab choices = 2, r repetitions = l)
#       a* = xxx = 2^l
#           = aaa, aab, aba, abb, baa, bab, bba, bbb
#       a* = b* = (a|b)*
#       ((aa)*)?
#           = aaa, aab, aba ... = 2^3
#       * basically allows all characters to be anything?
#
#

def countStrings(r, l):
    #
    # Write your code here.
    #
    print(f"r: {r}")
    print(f"l: {l}")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        rl = input().split()

        r = rl[0]

        l = int(rl[1])

        result = countStrings(r, l)

        fptr.write(str(result) + '\n')

    fptr.close()
