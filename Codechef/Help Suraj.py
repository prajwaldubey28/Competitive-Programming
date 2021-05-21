# Q = https://www.codechef.com/LETS2021/problems/LETSC001

try:
    def SieveOfEratosthenes(n):
        list1 = []
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0]= False
        prime[1]= False
        for p in range(n + 1):
            if prime[p]:
                list1.append(p)
        return list1


    list2 = []
    x = int(input())
    final = SieveOfEratosthenes(x)
    print(len(final))
except:
    pass
