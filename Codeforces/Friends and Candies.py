# Q = https://codeforces.com/contest/1538/problem/B

for _ in range(int(input())):
    n = int(input())
    list1 = list(map(int,input().split()))
    s = sum(list1)
    c =0
    if s%n==0:
        list2 = [i for i in list1 if i > s/n]
        print(len(list2))
    else:
        print(-1)