# Q = https://www.codechef.com/TCQL2021/problems/TCQL21D

try:    
    from itertools import groupby
    import collections
    n = int(input())
    def ans(x):
      return list(dict.fromkeys(x))
    
    
    while n>0:
        count = 0
        count1 = 0
        row = []
        column=[]
        x,y = map(int,input().split())
        for i in range(0,x):
            row.append([int(i) for i in input().split()])
        for i in range(0,x):
            res = [i[0] for i in groupby(row[i])]
            counter = collections.Counter(res)
            for i in counter.keys():
                if i==0:
                    count = count + counter[i]
                elif i==1:
                    count1 = count1 + counter[i]
            
        if count<=count1:
            print("CHEF")
        else:
            print("APOLLO")
        n = n-1
except:
    pass