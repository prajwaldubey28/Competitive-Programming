# Q = https://leetcode.com/problems/permutations-ii/

from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = list(permutations(nums,len(nums)))
        ans = set(ans)
        ans = list(ans)
        return ans