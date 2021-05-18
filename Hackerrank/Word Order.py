# Q = https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter
n = int(input())
list1 =[input() for _ in range(n)]
ans = Counter(list1)
print(len(ans))
for i in ans.values():
    print(i,end = " ")