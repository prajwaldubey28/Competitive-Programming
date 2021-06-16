# Q = https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        list1 = [0,1,1]
        for i in range(n):
            s = a+b+c
            a = b
            b = c
            c = s
            list1.append(s)
        return list1[n]