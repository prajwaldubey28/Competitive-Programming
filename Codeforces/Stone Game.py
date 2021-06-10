# Q = https://codeforces.com/contest/1538/problem/A

for _ in range(int(input())):
    n = int(input())
    list1 = list(map(int, input().split()))
    ma = 0
    mi = 0
    for i in range(n):
        if list1[i] == 1:
            mi = i+1
        elif list1[i] == n:
            ma = i+1      
    mins = min(mi, (n + 1) - mi)
    maxs = min(ma, (n + 1) - ma)
    d = abs(mi - ma)   
    print(min({d + mins, d + maxs, mins + maxs}))