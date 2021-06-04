# Q = https://www.codechef.com/LTIME96B/problems/TANDJ1

for _ in range(int(input())):
    a,b,c,d,k = map(int,input().split())
    ans = abs(c-a)+ abs(d-b)
    if ans>k:
        print('NO')
    else:
        if (k-ans)%2==0:
            print('YES')
        else:
            print('NO')