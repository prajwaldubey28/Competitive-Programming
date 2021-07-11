# Q = https://codeforces.com/contest/1547/problem/A

for _ in range(int(input())):
    s = str(input())
    A1,A2 = map(int,input().split())
    B1,B2 = map(int,input().split())
    F1,F2 = map(int,input().split())
    ans = abs(A1-B1) + abs(A2-B2)
    if A1==F1 and B1==F1:
        m1 = max(A2,B2)
        m2 = min(A2,B2)
        if F2>m2 and F2<m1:
            ans = ans+2
    elif A2==F2 and B2==F2:
        m3 = max(A1,B1)
        m4 = min(A1,B1)
        if F1>m4 and F1<m3:
            ans = ans+2
    print(ans)
