# Q = https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import itertools
for test in range(int(input())):
    n,k = map(int,input().split())
    s = str(input())
    list2 = list1[:k]
    count = 0
    ans = [p for p in itertools.product(list2, repeat=n)]
    for i in ans:
        j = "".join(i)
        if j[::-1] == j and j<s: 
            count=count+1
    count = count%1000000007
    print('Case #{0}: {1}'.format(test+1,count))