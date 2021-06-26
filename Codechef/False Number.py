# Q = https://www.codechef.com/LTIME97C/problems/FALSNUM

for _ in range(int(input())):
    s = str(input())
    a = int(s)
    ans = ''
    if s[0]=='1':
        ans = s[0] + '0' + s[1:]
    else:
        ans = '1' + s
    print(ans)