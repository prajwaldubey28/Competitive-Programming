# Q = https://www.codechef.com/MISC2021/problems/MCQ4

try:
    n,k = map(int,input().split())
    col = list(map(int,input().split()))
    fav = list(map(int,input().split()))
    happ = list(map(int,input().split()))
    sums = 0
    for i in fav:
        if i in col:
            x = col.count(i)
            if x>k:
                sums = sums+ happ[k-1]
                for p in range(k):
                    col.remove(i)
            else:
                sums = sums+ happ[x-1]
                for p in range(x):
                    col.remove(i)
    print(sums)
except:
    pass