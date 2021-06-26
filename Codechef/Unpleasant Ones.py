# Q = https://www.codechef.com/LTIME97C/problems/UNONE

from collections import deque
for _ in range(int(input())):
    n = int(input())
    even = deque()
    odd = deque()
    a=0
    b=0
    list1 = list(map(int,input().split()))
    for i in list1:
        if i%2==0:
            even.appendleft(i)
        else:
            odd.appendleft(i)
    if n==1:
        print(list1[0])
    elif n==2:
        if list1[0]%2==0:
            print(list1[0],list1[1])
        else:
            print(list1[1],list1[0])
        
    else:
        print(*even , end=" ")
        print(*odd , end=" ")
    print()