# Q = https://www.hackerrank.com/challenges/save-the-prisoner/problem

n1 = int(input().strip())
while n1>0:
    n,m,s = map(int,input().split())
    s = s-1
    m = m-1
    ans = (s+m)%n
    print(ans+1)
    n1 = n1-1