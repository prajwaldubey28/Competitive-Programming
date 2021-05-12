# Q = https://www.codechef.com/APRIL21C/problems/SSCRIPT

try:
    n = int(input())
    while(n>0):
        n1,n2 = map(int,input().split())
        s = str(input())
        count = 0
        for i in range(0,n1):
            if s[i]=="*":
                count = count +1
                if count==n2:
                    print("YES")
                    break
            else:
                count = 0 
        if count!=n2:
            print("NO")
        

        n = n-1
except:
    pass
