# Q = https://codeforces.com/contest/1579/problem/E1

from collections import deque 
for _ in range(int(input())):
    ans = deque()
    n = int(input())
    l1 = list(map(int,input().split()))
    ans.append(l1[0])
    for i in range(1,len(l1)):
        if l1[i]>=ans[0]:
            ans.append(l1[i])
        else:
            ans.appendleft(l1[i])
    print(*ans)