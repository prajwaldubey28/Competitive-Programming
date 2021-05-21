# Q = https://codeforces.com/problemset/problem/263/A
mat = []
for i in range(5):
	list1 = list(map(int,input().split()))
	mat.append(list1)
for i in range(5):
    for j in range(5):
        if mat[i][j]==1:
            a = i
            b = j
print(abs(2-a)+abs(2-b))