# Q = https://www.codechef.com/MISC2021/problems/MCQ2

list1 =[]
for i in range(int(input())):
    list1.append(int(input()))
n = len(list1)

final = [1]

for i in range(1, n):
    if list1[i] > list1[i-1]:
        final.append(final[-1]+1)
    else:
        final.append(1)

for i in range(n-1, 0, -1):
    if list1[i-1] >list1[i] and final[i] >= final[i-1]:
        final[i-1] = final[i]+1
print(sum(final))
