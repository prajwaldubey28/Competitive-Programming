# Q = https://www.codechef.com/JUNE21B/problems/BITTUP/

def anss(x,m):
    ans = 1
    if m==0:
        return 1
    if m==1:
        return x
    
    if (m%2==0):
        ans = anss(x,m/2)
        return (ans*ans)%1000000007
    else:
        ans = anss(x,((m-1)/2))
        return ((x*ans)%1000000007*ans)%1000000007

for _ in range(int(input())):
    n,m = map(int,input().split())
    x = anss(2,n)-1
    final = anss(x,m)
    print(final)