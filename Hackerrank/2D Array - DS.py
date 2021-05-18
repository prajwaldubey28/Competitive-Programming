# Q = https://www.hackerrank.com/challenges/2d-array/problem?h_r=profile

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    list1 = []
    sums ,sums1= 0,0
    for i in range(4):
        for j in range(4):
            sums = arr[i][j]+arr[i][j+1]+arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

            list1.append(sums)
        
    
    return max(list1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
