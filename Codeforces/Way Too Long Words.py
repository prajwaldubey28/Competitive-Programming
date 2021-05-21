# Q = https://codeforces.com/problemset/problem/71/A

n = int(input())
while n>0:
	s = str(input())
	x = len(s)
	if x<=10:
		print(s)
	else:
		print(s[0]+str(len(s)-2) + s[-1])
	n = n-1