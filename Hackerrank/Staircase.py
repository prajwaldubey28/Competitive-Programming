# Q = https://www.hackerrank.com/challenges/staircase/problem?h_r=profile

n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("#",end="")
        if k==i:
            print()