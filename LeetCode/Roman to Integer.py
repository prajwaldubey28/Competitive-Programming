# Q = https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        su=0
        list1 = list(s)
        i = 0
        while i<len(s):
            if "".join(list1[i:i+2]) in dict1.keys():
                x = "".join(list1[i:i+2])
                su = su + dict1[x]
                i = i+2
            else:
                su = su+ dict1[list1[i]]
                i = i+1
        return su
        