# Q = https://www.codechef.com/problems/CM164364


try:
    for _ in range(int(input())):
        n,x = map(int,input().split())
        list1 = list(map(int,input().split()))
        c = n-x
        set1 = set(list1) 
        b = len(set1)
        if c>=b:
            print(b)
        else:
            print(c)
except:
    pass