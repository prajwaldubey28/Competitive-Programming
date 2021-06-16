# Q = https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = [str(i) for i in digits]
        x = "".join(digit)
        x = int(x)
        y = x+1
        y = str(y)
        return list(y)