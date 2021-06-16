# Q = https://www.codechef.com/NCCW2021/problems/AKSPSTR

for _ in range(int(input())):
    flag = 'YES'
    n = int(input())
    s = str(input())
    s1 = str(input())
    x = ord(s1[0])- ord(s[0])
    for i,j in zip(s1,s):
        if ord(i)-ord(j)!=x:
            flag = 'NO'
    print(flag)