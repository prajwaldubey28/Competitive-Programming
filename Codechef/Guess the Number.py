# Q = https://www.codechef.com/problems/GUESSIT

try:
    n = int(input())
    while n>0:
        x = 1
        while True:
            print(x**2)
            t = int(input())
            if t==1:
                break
            x +=1
        n = n-1
except:
    pass