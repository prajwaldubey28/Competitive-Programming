# Q = https://www.codechef.com/LTIME97C/problems/HTMLTAGS

for _ in range(int(input())):
    s = str(input()).strip()
    if s[0]=='<' and s[1]=='/':
        if s[-1]=='>':
            x = s[2:-1]
            if x.isalnum()==True:
                flag = True
                for i in x:
                    if i.isdigit()==False:
                        if i.islower()==True:
                            continue
                        else:
                            print('Error')
                            flag = False
                            break
                if flag==True:
                    print('Success')
            else:
                print('Error')
        else:
            print('Error')
    else:
        print('Error')