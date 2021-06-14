# Q = https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        flag = True
        ans = []
        inp = [i for i in range(left,right+1)]
        for i in ranges:
            a = i[0]
            b = i[1]
            for i in range(a,b+1):
                ans.append(i)
        ans = set(ans)
        ans = list(ans)
        for i in inp:
            if i not in ans:
                flag = False
        return flag