# Q= https://www.codechef.com/TCQL2021/problems/TCQL21E/

try:    
    n = int(input())
    while n>0:
        x = int(input())
        s = input()
        i = 0
        list1 = []
        list2= []
        ans = ""
        while i<len(s):
            if s[i].isdigit()==True:
                j = i
                if j==len(s)-1:
                    list1.append(int(s[j]))
                    break
                else:
                    while s[j].isdigit()==True:
                        ans = ans + s[j]
                        if j==len(s)-1:
                            break
                        else:
                            j = j+1
                list1.append(int(ans))
            else:
                if s[i].isdigit()==False:
                    j = i
                    if j==len(s)-1:
                        list2.append(s[j])
                        break
                    else:
                        while s[j].isdigit()==False:
                            ans = ans + s[j]
                            if j==len(s)-1:
                                break
                            else:
                                j = j+1
                    list2.append(ans)
            ans = ""
            i = j
        print(max(list2,key=len),max(list1))
        n = n-1
except:
    pass