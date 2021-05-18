# Q = https://www.codechef.com/SHAK2021/problems/KRAFT

try:
    import math
    n = int(input())
    while n>0:
        l,b = map(int,input().split())
        ans = math.gcd(l,b)**2
        final = (l*b)//ans
        print(final)
        
        n = n-1
except:
    pass
