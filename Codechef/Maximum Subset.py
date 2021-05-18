# Q = https://www.codechef.com/CQM2021/problems/CQM82A

try:
    n = int(input())
    list1 = list(map(int,input().split()))
    list2 = []
    for i in list1:
        if i>=0:
            list2.append(i)
    if len(list2)>0:
        print(sum(list2))
    else:
        print(max(list1))

except:
    pass