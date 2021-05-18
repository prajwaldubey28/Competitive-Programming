# Q = https://www.codechef.com/JSSC2021/problems/POWSOC

try:
    x,y = map(int,input().split())
    count = 0
    ans = x
    final = 0
    if y<=x:
        print(1)
    else:
        while final<y:
            final = (ans-1)+x
            ans = final
            count =  count+1
        print(count+1)
except:
    pass