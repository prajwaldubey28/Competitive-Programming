# Q = https://codeforces.com/contest/1535/problem/A

for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    list1.sort(reverse=True)
    x = max(a,b)
    y = max(c,d)
    if x in list1[:2] and y in list1[:2]:
        print("YES")
    else:
        print('NO')