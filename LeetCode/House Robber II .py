# Q = https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        p1=0
        p2=0
        x=0
        x1=0
        for k in range(0,len(nums)-1):
            x = max(p1,p2+nums[k])
            p2 =p1
            p1= x
        p1 = 0
        p2 = 0
        for k in range(1,len(nums)):
            x1 = max(p1,p2+nums[k])
            p2 =p1
            p1= x1
        
        return max(x,x1)