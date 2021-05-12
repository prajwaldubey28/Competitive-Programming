# Q = https://www.codechef.com/APRIL21C/problems/KAVGMAT/


def worthy():


    testcases = int(input())
    while(testcases):
        (m,n,k) = map(int,input().strip().split(' '))
        matrix = [[0 for x in range(n)] for y in range(m)]
        
        matrix = []
        for i in range(m):
            r = list(map(int,input().strip().split(' ')))
            matrix.append(r)
            
        
                
        auxillary = [[0 for x in range(n+1)] for y in range(m+1)] 
        
        for i in range(m+1):
            auxillary[i][0] = 0
            
        for j in range(n+1):
            auxillary[0][j] = 0
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                auxillary[i][j] = matrix[i-1][j-1]
                
        
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                auxillary[i][j] += auxillary[i][j-1]
                
        for j in range(1,n+1):
            for i in range(1,m+1):
                auxillary[i][j] += auxillary[i-1][j]
                
        
        
                
        result = 0
        
        for p in range(1,m+1):
            for i in range(1,m-p+2):
                l = 1 
                h = n-p+1 
                mid = 0
                q = 0
                flag = 0
                while(l <= h):
                    mid = int((l+h)/2)
                    out = auxillary[i+p-1][mid+p-1]-auxillary[i+p-1][mid-1]-auxillary[i-1][mid+p-1]+auxillary[i-1][mid-1]
                    if (out >= k*p*p):
                        h = mid-1 
                        q = mid 
                        flag = 1 
                    else:
                        l = mid+1 
                        
                if flag == 1: 
                    result += (n-p-q+2)
                    
        
        print(result)
        testcases -= 1