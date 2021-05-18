# Q = https://www.codechef.com/SHAK2021/problems/KRAFT

try:
    n = int(input())
    while n>0:
        l,b = map(int,input().split())
        x = int(l/2)
        y = int(b/x)
        print(2*y)
        
        n = n-1
except:
    pass