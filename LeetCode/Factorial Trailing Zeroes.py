# Q = https://leetcode.com/problems/factorial-trailing-zeroes/

import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        x = math.factorial(n)
        while x%10==0:
            c+=1
            x = x//10
        return c