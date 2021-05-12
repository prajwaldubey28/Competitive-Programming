def selection(list1):
    length = len(list1)
    for i in range(length-1):
        mins = i 
        for j in range(i+1,length):
            if list1[j]<list1[mins]:
                mins = j
        if i!=mins:
            list1[i],list1[mins] = list1[mins],list1[i] 
    return list1
ans = selection([78,12,67,99])
print(ans)    