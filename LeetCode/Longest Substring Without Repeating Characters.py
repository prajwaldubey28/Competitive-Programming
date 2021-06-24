# Q = https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0 
        elif len(s)==1:
            return 1
        elif len(set(list(s)))==1:
            return 1
        else:
            maxs =0
            for i in range(len(s)):
                list1 = [s[i]]
                j = i+1
                while j<len(s):
                    if s[j] in list1:
                        break
                    else:
                        list1.append(s[j])
                        j = j+1
                if len(list1)>maxs:
                    maxs = len(list1)
            return maxs