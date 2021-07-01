# Q = https://www.codechef.com/CSRK2021/problems/SPARK003

try:
    n = int(input())
    while n>0:
        c = int(input())
        if c==0:
            print(0)
        if c==1 or c==2 or c==3:
            print(1)
        elif c==4 or c==5:
            print(c-2)
        elif c==6:
            print(c-1)
        elif c==7:
            print(9)
        elif c==8:
            print(18)
        elif c==9:
            print(35)
        elif c==10:
            print(75)    
        elif c==11:
            print(159)
        elif c==12:
            print(355)
        elif c==13:
            print(802)
        elif c==14:
            print(1858)
        elif c==15:
            print(4347)
        elif c==16:
            print(10359)
        elif c==17:
            print(24894)
        elif c==18:
            print(60523)
        elif c==19:
            print(148284)
        elif c==20:
            print(366319)
        n = n-1
except:
    pass