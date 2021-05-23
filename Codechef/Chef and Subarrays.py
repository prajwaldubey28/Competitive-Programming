# Q = https://www.codechef.com/COOK129B/problems/CSUBS

try:    
    for _ in range(int(input())):
        n,k = map(int,input().split())
        list1 = list(map(int,input().split()))
        dict1 = {}
        ans = 0
        for i in range(k):
            if list1[i] in dict1.keys():
                dict1[list1[i]] +=1
            else:
                dict1[list1[i]] = 1     
            count = 1
            j = i+k
            while j<n:
                if list1[j] in dict1.keys():
                    dict1[list1[j]] +=1
                else:
                    dict1[list1[j]] = 1   
                count+=1
                j=j+k
            final = 0
            for i,j in dict1.items():
                final = max(final,j)
            dict1 = {}
            ans+=(count-final)
        print(ans)
except:
    pass