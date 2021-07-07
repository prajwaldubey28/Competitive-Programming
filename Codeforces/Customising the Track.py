# Q = https://codeforces.com/contest/1543/problem/B
for _ in range(int(input())):
    l = []
    n = int(input())
    l1 = list(map(int,input().split()))
    x = sum(l1)
    y = n - x%n
    a = x//n
    l = [a]*y + [a +1]*(n-y)
    b = l.count(a)
    c = n-b
    final = b*c
    print(final)