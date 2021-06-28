# Q = https://www.codechef.com/START5B/problems/CYCLICQD

for _ in range(int(input())):
    A,B,C,D = map(int,input().split())
    if B+D==180 and A+C==180:
        print('YES')
    else:
        print('NO')