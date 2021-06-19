# Q = https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        for k in range(2,len(nums)):
            nums[k] = nums[k] + max(nums[:k-1])
        return max(nums)