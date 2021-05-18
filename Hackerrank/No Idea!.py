# Q = https://www.hackerrank.com/challenges/no-idea/problem

n,m= map(int,input().split())
list1 = list(map(int,input().split()))
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))
ans = sum((i in A) - (i in B) for i in list1 )
print(ans)  