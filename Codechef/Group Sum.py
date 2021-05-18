# Q = https://www.codechef.com/JSSC2021/problems/GRPSUM

try:
    n = int(input())
    while n>0:
        list1 = []
        k = int(input())
        final = 0
        x = k-1
        sums = int(((x)**2+(x))/2)
        for i in range(1,k+1):
            final = final + 2*(sums+i)
        print(final)    
            
        n = n-1
except:
    pass