# Q = https://leetcode.com/contest/biweekly-contest-56/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        ans = [i**2 for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                x = i**2 + j**2
                if x in ans:
                    c = c+1
        return c    