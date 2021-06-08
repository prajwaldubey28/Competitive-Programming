BUBBLE SORT


def bubblesort(n,list1):    
    for i in range(n):
        c = 0
        for j in range(n-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]= list1[j+1],list1[j]
        if c==0:
            break
    return list1

n = int(input())
list1 = list(map(int,input().split()))
print(bubblesort(n,list1))  