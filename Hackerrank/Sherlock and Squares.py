# Q = https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import math
import os
import random
import re
import sys
import math

def squares(a, b):
    x1 = math.sqrt(a)
    x2 = int(math.sqrt(b))
    if int(x1)!=x1:
        x1 = x1+1 
    x1 = int(x1)  
    ans = len([i for i in range(x1,x2+1)])
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()