# Q = https://codeforces.com/contest/1579/problem/A

for _ in range(int(input())):
    s = str(input())
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    if (a==b) and (c==0):
        print('YES')
    elif (b==c) and (a==0):
        print('YES')
    elif (b-a == c):
        print("YES")
    else:
        print('NO')