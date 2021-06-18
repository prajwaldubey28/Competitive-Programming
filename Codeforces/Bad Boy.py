# Q = https://codeforces.com/contest/1537/problem/B

for _ in range(int(input())):
    n,m,i,j = map(int,input().split())
    list1 = []
    list1.append(1)
    list1.append(1)
    list1.append(n)
    list1.append(m)
    print(*list1)