# Q = https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a,2)
        n2 = int(b,2)
        ans = n1 + n2
        final = bin(ans)
        final = final.replace('0b','')
        return final