# Q = https://www.codechef.com/LTIME96B/problems/CHARGES

try:
    t = int(input())
    while t>0:
        n, k = map(int, input().split())
        ss = str(input())
        s = list(ss)  
        list1 = list(map(int, input().split()))

        if n == 1:
            print("0")
            continue

        sums=0
        for i in range(1, n):
            if s[i - 1] == s[i]:
                sums += 2
            else:
                sums += 1

        for i in range(k):
            final = list1[i] - 1
            if final == 0 and n > 1:
                if s[final] == s[final + 1]:
                    sums -= 1
                else:
                    sums += 1  
                print(sums)

                if s[final] == "0":
                    s[final] = "1"
                else:
                    s[final] = "0"
                continue

            if final == n - 1 and n > 1:

                if s[final] == s[final - 1]:
                    sums -= 1
                else:
                    sums += 1
                print(sums)

                if s[final] == "0":
                    s[final] = "1"
                else:
                    s[final] = "0"
                continue

            if s[final] == s[final + 1]:
                sums -= 1
            else:
                sums += 1

            if s[final] == s[final - 1]:
                sums -= 1
            else:
                sums += 1

            if s[final] == "0":
                s[final] = "1"
            else:
                s[final] = "0"

            print(sums)
        t = t-1
except:
    pass
