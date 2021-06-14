# Q = https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split(' ')
        x = list1.count('')
        for i in range(x): 
            list1.remove('')
        list2 = list1[::-1]
        ans = " ".join(list2)
        return ans