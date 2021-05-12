# Q = https://www.codechef.com/APRIL21C/problems/SDICE/

try:
    n = int(input())
    while n>0:
        x = int(input())
        if x==1:
            print(20)
        elif x==2:
            print(36)
        elif x==3:
            print(51)
        elif x==4:
            print(60)
        else:
            a = int(x/4)
            b = x%4
            if b==0:
                ans = 44*a + 16
            elif b==1:
                ans = 44*a + 32
            elif b ==2:
                ans = 44*a + 44
            elif b==3:
                ans = 44*a + 55
            print(ans)
        n = n-1
except:
    pass