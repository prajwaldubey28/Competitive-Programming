# Q = https://codeforces.com/contest/1529/problem/A

from collections import Counter
for _ in range(int(input())):
    n = int(input())
    list1 = list(map(int,input().split()))
    print(n-(list1.count(min(list1))))