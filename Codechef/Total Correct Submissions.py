# Q = https://www.codechef.com/START5B/problems/TOTCRT

for _ in range(int(input())):
    N = int(input())
    dict1 = {}
    for i in range(N*3):
        x,y = map(str,input().split())
        if x in dict1:
            dict1[x] = dict1[x]+int(y)
        else:
            dict1[x]= int(y)

    x = list(dict1.values())
    x.sort()
    print(*x)