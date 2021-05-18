# Q = https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_r=profile

from collections import Counter
import math
import os
import random
import re
import sys


def makeAnagram(a, b):
    c1 = Counter(a)
    c2 = Counter(b)
    c1.subtract(c2)
    sums = 0
    for i in c1.values():
        sums += abs(i)
    return sums


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
