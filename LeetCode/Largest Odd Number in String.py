# Q = https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num)&1==1:
            return str(num)
        else:
            flag = True
            x = int(num)
            while x>0:
                x = x//10
                if x&1==1:
                    return str(x)
            return "" 