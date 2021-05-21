# Q = https://codeforces.com/problemset/problem/231/A

n = int(input())
sums = 0
for i in range(n):
	list1 = list(map(int,input().split()))
	if list1.count(1)>=2:
		sums = sums+1
print(sums)