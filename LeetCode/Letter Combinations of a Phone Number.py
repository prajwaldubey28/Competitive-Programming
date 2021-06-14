# Q = https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        list1 = []
        dict1= {'1':'','2':'abc','3':'def','4':'ghi','5': 'jkl' , '6':'mno', '7':'pqrs', '8':'tuv' , '9':'wxyz'}
        ans = []
        if len(digits)==1:
            ans = [i for i in dict1[digits]]
        elif len(digits)==2:
            x = dict1[digits[0]]
            y = dict1[digits[1]]
            for i in x:
                for j in y:
                    ans.append(i+j)
        elif len(digits)==3:
            x = dict1[digits[0]] 
            y = dict1[digits[1]]
            z = dict1[digits[2]]
            for i in x:
                for j in y:
                    for k in z:
                        ans.append(i+j+k)
                    
        elif len(digits)==4:
            x = dict1[digits[0]] 
            y = dict1[digits[1]]
            z = dict1[digits[2]]
            a = dict1[digits[3]]
            for i in x:
                for j in y:
                    for k in z:
                        for l in a:
                            ans.append(i+j+k+l)
        
        return ans