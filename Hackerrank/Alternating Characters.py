# Q = https://www.hackerrank.com/challenges/alternating-characters/problem?h_r=profile


import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    i = 0
    c = 0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            c += 1
        i = i+1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()