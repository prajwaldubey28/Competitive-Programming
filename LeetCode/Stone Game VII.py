# Q = https://leetcode.com/problems/stone-game-vii/

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp1, dp2 = [0] * len(stones), [0] * len(stones)
        for i in range(len(stones) - 2, -1, -1):
            final = stones[i]
            dp2, dp1 = dp1, dp2
            for j in range(i + 1, len(stones)):
                final += stones[j]
                dp1[j] = max(final - stones[i] - dp2[j], final - stones[j] - dp1[j-1])
        return dp1[-1]