# Q = https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.split() == []:
            return 0 
        else:
            list1 = s.split()
            return len(list1[-1])