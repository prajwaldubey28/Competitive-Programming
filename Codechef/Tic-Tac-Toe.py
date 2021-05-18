# Q = https://www.codechef.com/MAY21C/problems/TCTCTOE


try:    
    n = int(input())
    def check(ch,list1):
        for i in range(3):
            if list1[i][0]==ch and (list1[i][0]==list1[i][1]==list1[i][2]!='_'):
                return 1
            if list1[0][i]==ch and (list1[0][i]==list1[1][i]==list1[2][i]!='_'):
                return 1
        if list1[0][0]==ch and (list1[0][0]==list1[1][1]==list1[2][2]!='_'):
            return 1
        if list1[0][2] == ch and (list1[0][2]==list1[1][1]==list1[2][0]!='_'):
            return 1
    while n>0:
        counth=0
        countv=0
        countd=0
        row = 3
        column = 3
        list1 = []
        for i in range(row):
            list1.append(input())
        a=0
        b=0
        c=0
        for i in list1:
            a= a+ i.count('X')
            b= b+ i.count('O')
            c = c+i.count('_')

        if b>a or abs(a-b)>1 :
            print(3)
        else:
            X = check('X',list1)
            O = check('O',list1)
            if X and O:
                print(3)
            elif (X and a == b):
                print(3)
            elif (O and a > b):
                print(3)
            elif (X or O):
                print(1)
            elif c==0:
                print(1)
            else:
                print(2)
                    
        n = n-1
except:
    pass