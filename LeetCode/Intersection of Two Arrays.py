# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set3 = set(nums1).intersection(set(nums2))
        return list(set3)