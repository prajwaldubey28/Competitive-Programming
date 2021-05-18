# Q = https://www.hackerrank.com/challenges/drawing-book/problem?h_r=profile

n = int(input())
f = int(input())
front = int(f/2)
if (n%2!=0) and (n-f)<=1:
    back = 0
elif (n%2!=0) and (n-f)>1:
    back = int((n-f)/2) 
elif (n%2==0):
    if (n-f)==1:
        back = 1
    else:
        back = int((n-f)/2)
print(min(front,back))
