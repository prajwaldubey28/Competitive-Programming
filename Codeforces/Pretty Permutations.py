# Q = https://codeforces.com/contest/1541/problem/A

for _ in range(int(input())):
    n = int(input())
    list1 = [i for i in range(1,n+1)]
    n = len(list1)
    if len(list1)%2==0:
        for i in range(0,len(list1)-1,2):
            list1[i] ,list1[i+1] = list1[i+1],list1[i]
    else:
        for i in range(0,len(list1)-1,2):
            list1[i] ,list1[i+1] = list1[i+1],list1[i]
        list1[n-1],list1[n-2] = list1[n-2],list1[n-1]
    print(*list1)