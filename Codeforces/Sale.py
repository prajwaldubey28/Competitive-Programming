# Q = https://codeforces.com/contest/34/problem/B

n,m = map(int,input().split())
list1 = list(map(int,input().split()))
list2  = []
list1.sort()
for i in list1:
    if i>0:
        break
    else:
        list2.append(abs(i))
if len(list2)==0:
    print(0)
elif len(list2)>m:
    final = sum(list2[:m])
    print(final)
else:
    final = sum(list2)
    print(final)