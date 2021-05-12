##Q - https://www.codechef.com/TCQL2021/problems/TCQL21B
try:
    n = int(input())
    import math
    from math import sqrt
    from itertools import count, islice

    def is_prime(n):
        return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

    while n>0:
        N,Q = map(int,input().split())
        list1 = list(map(int,input().split()))
        for i in range(1,Q+1):
            x,y= map(int,input().split())
            list2 = []
            i = 0
            while len(list2)<=x:
                if i not in list1:
                    list2.append(i)
                    i = i+1
                else:
                    i = i+1
                    continue
            prime = []
            for i in list2:
                if is_prime(i)==True:
                    prime.append(i)
                else:
                    continue
            if y==1:
                if len(prime)==0:
                    print("NO")
                else:
                    c = prime[0]
                    ans = list2.index(c)
                    if ans<=x:
                        print(c)
                    else:
                        print("NO")
            elif y==2:
                if len(prime)==0:
                    print("NO")
                else:
                    final = 0
                    for c in prime:
                        ans = list2.index(c)
                        if ans<=x:
                            final = c
                        
                    if final==0:
                        print("NO")
                    else:
                        print(final)

            else:
                if len(prime)==0:
                    print("NO")
                else:
                    final = 0
                    c = prime[0]
                    ans = list2.index(c)
                    for d in prime:
                        ans1 = list2.index(d)
                        if ans1<=x:
                            final= d
                    if final==0:
                        d = "NO"
                    else:
                        d=final
                    if ans<=x:
                        print(c,d)
                    else:
                        print("NO")
        n = n-1    

except:
    pass