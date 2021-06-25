# Q = https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        final = [i for i in range(len(nums)+1)]
        for p in final:
            if p not in nums:
                return p 
