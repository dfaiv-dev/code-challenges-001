#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_word_len = len(magazine)
    note_word_len = len(note)

    if (note_word_len > magazine_word_len):
        print("No")
        return

    def get_word_dict(words):
        word_dict = {}
        for w in words:
            if (word_dict.get(w) is not None):
                word_dict[w] = word_dict[w] + 1
            else:
                word_dict[w] = 1
        return word_dict

    note_words = get_word_dict(note)
    magazine_words = get_word_dict(magazine)

    for k, v in note_words.items():
        if magazine_words.get(k) is None:
            print("No")
            return

        if (magazine_words[k] < v):
            print("No")
            return

    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
