# Q = https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    set1 = set(ar)
    count = 0
    for i in set1:
        if ar.count(i)>=2:
            count= count+ int(ar.count(i)/2)
        else:
            continue
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
