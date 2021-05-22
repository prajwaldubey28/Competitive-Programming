# Q = https://www.codechef.com/CDIG2021/problems/RJ1

s = str(input())
s=s.replace(" ",'')
s=s.replace('S',"")
s=s.replace('=',"")

x = str(input())
x=x.replace(" ",'')
x=x.replace('X',"")
x=x.replace('=',"")

y = str(input())
y=y.replace(" ",'')
y=y.replace('Y',"")
y=y.replace('=',"")

c = 0
a=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
for i in a:
    if i.count(x)==int(y):
        c = c + 1
print(c)