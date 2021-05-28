# Q = https://www.codechef.com/MISC2021/problems/MCQ7

try:    
    for _ in range(int(input())):
        Q = int(input())
        count = 0
        list1 = list(map(int,input().split()))
        for i in range(0,len(list1)):
            for j in range(i+1,len(list1)):
                    if list1[i]|list1[j]<=max(list1[i],list1[j]):
                        count+=1
        print(count)
except:
    pass