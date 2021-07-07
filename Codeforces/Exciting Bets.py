# Q = https://codeforces.com/contest/1543/problem/A
import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    flag = True
    if a==b:
        flag = 'Red'
    else:
        if a<b:
            ans = b-a
            x = a%ans
            y = ans - a%ans
            c = min(x,y)
        else:
            ans = a-b
            x = b%ans
            y = ans- b%ans
            c = min(x,y)
                
    if flag== 'Red':
        print(0,0)
    else:
        print(ans,c)