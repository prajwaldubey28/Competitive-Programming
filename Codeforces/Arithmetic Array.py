# Q = https://codeforces.com/contest/1537/problem/A

for _ in range(int(input())):
    n = int(input())
    c= 0 
    list1 = list(map(int,input().split()))
    if sum(list1)/n ==1:
        print(0)
    else:
        if sum(list1)>=n:
            x = sum(list1)-n
            print(x)
        else:
            print(1)