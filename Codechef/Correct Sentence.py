# Q = https://www.codechef.com/START4B/problems/CORTSENT

for _ in range(int(input())):
    list1 = list(map(str,input().split()))
    k = int(list1[0])
    list2 = list1[1:]
    count=0
    for i in list2:
        lang1 = 0
        lang2=0
        for j in i:
            if 'a'<= j and j<='m':
                lang1+=1
            elif 'N'<= j and j<='Z':
                lang2+=1
                
        if lang1==len(i):
            count+=1
        elif lang2==len(i):
            count+=1
    if count==k:
        print('YES')
    else:
        print('NO')
             