n = int(input())
dp = [[-1 for i in range(100)] for j in range(101)]
def knapsack(wt,val,cap,n1):
    if (n1==0) or (cap==0):
        return 0
    if dp[cap][n1]!=-1:
        return dp[cap][n1]
    if wt[n1-1]>cap:
        dp[cap][n1] =  knapsack(wt,val,cap,n1-1)
        return knapsack(wt,val,cap,n1-1)
    elif wt[n1-1]<=cap:
        dp[cap][n1] = max( val[n1-1] +  knapsack(wt,val,cap-wt[n1-1],n1-1) ,knapsack(wt,val,cap,n1-1))
        return max( val[n1-1] +  knapsack(wt,val,cap-wt[n1-1],n1-1) ,knapsack(wt,val,cap,n1-1))
        
while n>0:
    n1 = int(input())
    wt = list(map(int,input().split()))
    val = list(map(int,input().split()))
    cap = int(input())
    ans = knapsack(wt,val,cap,n1)
    print(ans)
    n = n-1