# Q = https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6

n = int(input())

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

for test in range(n):
    list2 = []
    x = int(input())
    final = SieveOfEratosthenes(100000)
    for i in range(0,len(final)-1):
        j = i+1
        if final[i]*final[j]<=x:
            list2.append(final[i]*final[j])
    ans = max(list2)
    print('Case #{0}: {1}'.format(test+1,ans))