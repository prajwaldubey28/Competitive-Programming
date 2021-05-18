# Q = https://www.codechef.com/SHAK2021/problems/GUESIT99

try:
    n = int(input())
    list1 = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while n>0:
        n1 = int(input())
        x = n1%7
        print(list1[x-1])
        
        n = n-1
except:
    pass
