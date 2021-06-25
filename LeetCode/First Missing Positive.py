# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        p = 1
        for i in nums:
            if i == p:
                p += 1
        return p
