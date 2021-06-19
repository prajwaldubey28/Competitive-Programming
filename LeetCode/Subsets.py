# Q = https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerset(nums):
            if len(nums) <= 0:
                yield []
            else:
                for i in powerset(nums[1:]):
                    yield [nums[0]]+i
                    yield i
        return list(powerset(nums))