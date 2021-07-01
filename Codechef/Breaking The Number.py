# Q = https://www.codechef.com/CSRK2021/problems/SPARK001

try:
    n = int(input())
    c = 0
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if i+j+k==n:
                    c = c+1
    print(c)
except:
    pass