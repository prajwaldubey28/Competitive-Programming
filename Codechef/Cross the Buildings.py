# Q = https://www.codechef.com/MISC2021/problems/MCQ3

n,m = map(int,input().split())
list1 = list(map(int,input().split()))
count = 0
for i in range(len(list1)-1):
    if list1[i]==list1[i+1]:
        count+=1
        continue
    elif list1[i]>list1[i+1]:
        m = m+ list1[i]-list1[i+1]
        count+=1
    else:
        if m>= list1[i+1]-list1[i]:
            m = m-(list1[i+1]-list1[i])
            count+=1
        else:
            print('NO')
if count==len(list1)-1:
    print('YES')