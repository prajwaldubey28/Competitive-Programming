# Q = https://www.codechef.com/FEST2021/problems/TCOMPUTE

try:    
    sums,xors= map(int,input().split())
    And = (sums - xors)//2
    def ans(sums, xors,And):
        x = 0
        y = 0
        for i in range(64):
            A = (And & (1 << i))
            X = (xors & (1 << i))
            if (X == 0 and A == 0):
                pass
            elif (X == 0 and A > 0):
                x = ((1 << i) | x) 
                y = ((1 << i) | y) 
            elif (X > 0 and A == 0):
                x = ((1 << i) | x) 
            else:
                print(-1)
                return
        print((x*y)%1000000007)
            
        
    
    ans(sums,xors,And)
except:
    pass