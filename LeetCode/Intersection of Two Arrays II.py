# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set1.intersection(set2)
        for i in set3:
            x = min(nums1.count(i),nums2.count(i))
            for k in range(x):
                ans.append(i)
        return ans