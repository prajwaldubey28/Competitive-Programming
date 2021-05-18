# Q = https://www.codechef.com/MAY21C/problems/XOREQUAL/

try:    
    n = int(input())
    def ans(a,b,p):
        count = 1
        while b>0:
            if b & 1:
                count = (count*a)%p
            b = b>>1
            a = (a*a)%p
        return count
    while n>0:
        p = 10**9 + 7
        x = int(input())
        a = 2
        b = x-1
        p = 1000000007
        final = ans(a,b,p)
        print(final)
        n = n-1
except:
    pass