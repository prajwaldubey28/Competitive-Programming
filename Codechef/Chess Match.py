# Q = https://www.codechef.com/START5B/problems/BLITZ3_2

for _ in range(int(input())):
    N,A,B = map(int,input().split())
    time = 2*(180+N)
    x = A+B
    ans = time-x
    print(ans)