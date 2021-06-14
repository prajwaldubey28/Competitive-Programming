# Q = https://www.codechef.com/JUNE21B/problems/COCONUT

for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    ans = int(c/a)+ int(d/b)
    print(ans)