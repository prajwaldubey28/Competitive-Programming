# Q = https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        list1 = [0,1]
        for i in range(n):
            s = a+b
            a = b
            b = s
            list1.append(s)
        return list1[n]