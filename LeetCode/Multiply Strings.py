# Q = https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x = int(num1)
        y = int(num2)
        ans = x*y
        return str(ans)