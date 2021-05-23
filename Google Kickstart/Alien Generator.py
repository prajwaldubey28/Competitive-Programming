# Q = https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec1cb

for test in range(int(input())):
    g = int(input())
    sums = 0
    ans = []
    for i in range(1,g):
        sums = 0
        k = i
        while sums!=g:
            sums = sums+k
            if sums==g:
                ans.append(i)
                break
            elif sums>g:
                break
            else:
                k = k+1
                continue
    print('Case #{0}: {1}'.format(test+1,len(ans)+1))