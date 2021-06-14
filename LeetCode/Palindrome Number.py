# Q = https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s1 = s[::-1]
        if s1 == s:
            return 'true'

