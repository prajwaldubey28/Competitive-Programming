# Q = https://www.codechef.com/COOK130B/problems/WAV2

import bisect
[n,q]=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
for i in range(q):
    x=int(input())
    l=bisect.bisect_left(arr,x)
    if l<n and arr[l]==x:
        print(0)
    elif l%2==0:
        print('POSITIVE')
    else:
        print('NEGATIVE')