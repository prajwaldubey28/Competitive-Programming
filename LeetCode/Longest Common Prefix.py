# Q = https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in zip(*strs):
            if len(set(i))>1:
                return ans
            else:
                ans = ans + i[0]
        return ans