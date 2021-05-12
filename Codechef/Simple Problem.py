# Q = https://www.codechef.com/TCQL2021/problems/TCQL21A

try:    
    n = int(input())
    while n>0:
        list1 = []
        ans = 0
        row = []
        column=[]
        x,y = map(int,input().split())
        for i in range(0,x):
            row.append([int(i) for i in input().split()])
        middle = row[int(x/2)][int(y/2)]
        a = int(x/2)
        b = int(y/2)
        if middle == 0:
            print("YES 0")
        else:
            for i in range(0,x):
                for j in range(0,y):
                    if row[i][j]==0:
                        ans = abs(i-a)+abs(j-b)
                        list1.append(ans)
            if ans>0:
                print("YES",min(list1))
            else:
                print("NO -1")
    
        n = n-1
except:
    pass