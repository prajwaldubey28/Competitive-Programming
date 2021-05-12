# Q = https://www.codechef.com/TCQL2021/problems/TCQL21C

try:
    import math
    n1 = int(input())
    while n1>0:
        m,n = map(int,input().split())
        if m==0:
            print(n)
        elif n==0:
            print(m)
        else:
            print(2*math.gcd(m,n))
        n1 = n1-1
except:
    pass