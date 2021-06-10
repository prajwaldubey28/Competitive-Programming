def InsertionSort(n,list1):
    for i in range(1,n):
        key = list1[i]
        j = i-1
        while j>=0 and key<list1[j]:
            list1[j+1] = list1[j]
            j -=1
        list1[j+1] = key
    return list1

n = int(input())
list1 = list(map(int,input().split()))
print(InsertionSort(n,list1))