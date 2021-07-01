# Q = https://www.codechef.com/problems/SPARK002

try:
    s = str(input())
    l1 = []
    k = 0
    for i in s:
        if i=='(':
            k = k+1
            l1.append(k)
        elif i==')':
            l1.append(k)
    print(*l1)
except:
    pass