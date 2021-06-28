# Q = https://www.codechef.com/START5B/problems/SLPCYCLE

for _ in range(int(input())):
    L,H = map(int,input().split())
    s = str(input())
    count = 0 
    if '0'*H in s:
        print('YES')
        continue
    for k in s:
        if k== '0':
            count = count+1
            if count==H:
                print('YES')
                break
        else:
            if count!=0:
                H = 2*(H-count)
                count=0
    else:
        print('NO')