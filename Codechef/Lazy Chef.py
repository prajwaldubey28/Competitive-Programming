# Q = https://www.codechef.com/START4B/problems/LAZYCHF

for _ in range(int(input())):
    x,m,d = map(int,input().split())
    ans = m*x
    if ans<=(x+d):
        print(ans)
    else:
        print(min(ans,x+d))
