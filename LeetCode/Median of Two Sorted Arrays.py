# Q = https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = nums1 + nums2
        final.sort()
        n = len(final)
        if len(final)==0:
            ans = "{:.5f}".format(0)
            return float(ans)
        elif len(final)==1:
            ans = "{:.5f}".format(final[0])
            return float(ans)
        else:
            if len(final)%2!=0:
                p = final[int(n/2)]
                ans = "{:.5f}".format(p)
                return float(ans)
            else:
                p1 = int(n/2) - 1
                p2 = int(n/2)
                ans = (final[p1]+final[p2])/2
                ans1 = "{:.5f}".format(ans)
                return float(ans1)