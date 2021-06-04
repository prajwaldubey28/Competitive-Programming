# Q = https://codeforces.com/contest/1535/problem/B

from itertools import permutations
import math
for _ in range(int(input())):
    n = int(input())
    c = 0
    list1 = list(map(int,input().split()))
    list1.sort()
    for i in range(0,len(list1)+1):
        for j in range(i+1,len(list1)):
            if math.gcd(list1[i],2*list1[j])>1 or math.gcd(list1[j],2*list1[i])>1:
                c+=1
    print(c)