# Q = https://www.codechef.com/MAY21C/problems/MODEQ

try:
    n = int(input())
    while n>0:
        count = 0
        N,M = map(int,input().split())
        count = 0
        list1 = [1]*(N+1)
        for i in range(2,N+1):
            mo = M%i
            count = count+list1[mo]
            for j in range(mo,N+1,i):
                list1[j]+=1
        print(count)
        n = n-1
except:
    pass