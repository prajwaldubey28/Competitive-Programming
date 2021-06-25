# Q = https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        elif len(nums)==0:
            return [-1,-1]
        
        else:
            if nums.count(target)==1:
                ans = nums.index(target)
                return [ans,ans]
            else:
                new = nums[::-1]
                mins = nums.index(target)
                ind = new.index(target)
                maxs = len(nums)-1-ind
                return [mins,maxs]