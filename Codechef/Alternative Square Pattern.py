# Q = https://www.codechef.com/CCSTART2/problems/SQALPAT

for i in range(int(input())):
    if i%2==0:
        x = 5*i + 1
        list1 = [x+i for i in range(5)]
        print(*list1)
    else:
        x = 5*(i+1)
        list1 = [x-i for i in range(5)]
        print(*list1)