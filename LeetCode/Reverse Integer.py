# Q = https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            s = str(x)
            s1 = int(s[::-1])
            if abs(s1) < 2**31 and s1 != 2**31 - 1:
                return int(s1)
            else:
                return 0
        else:
            s = str(x)
            s = s.replace('-','')
            s1 = s[::-1]
            s2 = '-' + s1
            if abs(int(s2)) < 2**31 and int(s2) != 2**31 - 1:
                return int(s2)
            else:
                return 0
