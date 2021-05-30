# Q = https://www.codechef.com/START4B/problems/CTIME

import collections
for _ in range(int(input())):
    dee = collections.deque()
    n,k,f = map(int,input().split())
    ans = 0
    for i in range(n):
        a,b = map(int,input().split())
        dee.appendleft([a,b])
    de = sorted(dee)
    x = de[0][0]
    y = de[0][1]
    ans = ans+de[0][0]
    for i in range(1,n):
        if de[i][0]>y:
            ans += de[i][0]-y
            y = max(y,de[i][1])
        else:
            y = max(y,de[i][1])
    ans+=f-y
    if (ans)>=k:
        print('YES')
    else:
        print('NO')