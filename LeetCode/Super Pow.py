# Q = https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        c = int(''.join(map(str,b)))
        return int(pow(a,c,1337))