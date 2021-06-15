# Q = https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxs = 0
        i = 0
        j = len(height)-1
        while i<j:
            ans = (j-i)*(min(height[i],height[j]))
            if ans>maxs:
                maxs = ans
            if height[i]>height[j]:
                j = j-1
            elif height[i]<height[j]:
                i = i+1
            else:
                if height[i+1]>height[j-1]:
                    j = j-1
                else:
                    i = i+1
        return maxs