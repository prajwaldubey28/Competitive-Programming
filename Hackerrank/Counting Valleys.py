# Q = https://www.hackerrank.com/challenges/counting-valleys/submissions

#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    sums = 0
    count = 0
    for i in path:
        if i=="U":
            sums = sums +1
        else:
            sums = sums-1
        if i=="U" and sums==0:
            count = count+1
  
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
