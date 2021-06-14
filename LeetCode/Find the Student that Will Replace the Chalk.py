# Q = https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        x = sum(chalk)
        if x-k==0:
            return 0
        else:
            a = k//x
            k = k-x*a
            for i in range(len(chalk)):
                k = k- chalk[i]
                if k==0:
                    return i+1
                elif k<0:
                    return i 
