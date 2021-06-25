# Q = https://codeforces.com/contest/1541/problem/C

for _ in range(int(input())):
    n = int(input())
    list1 = list(map(int,input().split()))
    list1.sort()
    ans = 0
    sums = 0
    p = 2
    while p<n:
        sums = sums + list1[p-2]
        ans = ans - (list1[p]*(p-1))
        ans = ans + sums
        p = p+1
    print(ans)