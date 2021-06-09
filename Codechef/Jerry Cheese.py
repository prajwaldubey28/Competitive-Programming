# Q = https://www.codechef.com/REC92019/problems/REC09A

N,k = map(int,input().split())
list1 = list(map(int,input().split()))
flag = False
if sum(list1)==k:
    print('YES')
elif sum(list1)>k:
    print('NO')
else:
    x = sum(list1)
    for i in range(min(list1),max(list1)):
        if i not in list1:
            if x+i==k:
                flag = True
                print('YES')
                break
    if flag==False:
        print('NO')