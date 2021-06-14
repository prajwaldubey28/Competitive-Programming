# Q = https://www.codechef.com/JUNE21B/problems/CHFHEIST

for _ in range(int(input())):
    D,d,P,Q = map(int,input().split())
    x = D%d
    y = int(D/d)
    ans = D*P + (y*(y-1)//2)*Q*d + x*(y)*Q
    print(ans)