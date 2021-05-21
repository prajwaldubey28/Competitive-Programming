# Q = https://codeforces.com/problemset/problem/282/A

n = int(input())
x = 0
while n>0:
	s = str(input())
	if s[0]=='+' or s[1]=='+':
		x += 1
	elif s[0]=='-' or s[1]=='-':
		x = x-1
	n = n-1
print(x)