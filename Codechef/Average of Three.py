# Q = https://www.codechef.com/START23B/problems/AVGOF3

def final(s1):
    for i in range(1,1001):
        for j in range(i+1,1001):
            for k in range(j+1,1001):
                if i+j+k==s1:
                    return [i,j,k]
    

for _ in range(int(input())):
    s = int(input())
    s1 = s*3
    ans = final(s1)    
    print(*ans)
