# Q = https://www.codechef.com/YTPP001/problems/ISGOODNM



import math
n = int(input())
ans = 1
i = 2
while i * i <= n:
    if n % i == 0:
        ans = ans + i + n/i
    i += 1
    if ans>n:
        break

if ans==n:
    print('YES')
else:
    print('NO')
