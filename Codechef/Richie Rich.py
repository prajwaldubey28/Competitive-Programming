# Q = https://www.codechef.com/LTIME97C/problems/CHFRICH

for _ in range(int(input())):
    A,B,X = map(int,input().split())
    y = B-A
    ans = int((B-A)/X)
    print(ans)