# Q = https://www.codechef.com/COOK129B/problems/TLAPM

for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    a =1
    b=1
    c=1
    for i in range(1,y1):
        a+=i
        b+=i
    for i in range(y1+1,y1+x1):
        a+=i
    for i in range(y1+1,y1+x2):
        b+=i
    for i in range(1,y2):
        c+=i
    for i in range(y2+1,y2+x2):
        c+=i
    ans = 0
    pos= a
    while pos!=b:
        ans+=pos
        pos+=x1+y1
        x1 = x1+1
    while pos!=c:
        ans+=pos
        pos+=x1+y1-1
        y1=y1+1
    ans+=c
    print(ans)