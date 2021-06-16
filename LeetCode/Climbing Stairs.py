# Q = https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        else:
            a = 0
            b = 1
            for i in range(n):
                s = a+b
                a = b
                b = s
            return b