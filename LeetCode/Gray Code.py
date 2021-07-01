# Q = https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3799/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==1:
            return [0,1]
        elif n==2:
            return [0,1,3,2]
        else:
            l1 = [ i^(i>>1) for i in range(0, 2**n) ]
            return l1