# Q = https://leetcode.com/problems/find-the-difference/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = sorted(s)
        y = sorted(t)
        for i,j in enumerate(x):
    	    if j != y[i]: 
                return y[i]
        return y[-1]