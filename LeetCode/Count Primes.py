# Q = https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        elif n==2:
            return 0
        else:
            list1 = []
            prime = [True for i in range(n + 1)]
            p = 2
            while (p * p <=n):
                if (prime[p] == True):
                    for i in range(p * 2, n + 1, p):
                        prime[i] = False
                p += 1
            prime[0]= False
            prime[1]= False
            for p in range(n):
                if prime[p]:
                    list1.append(p)
            return len(list1)