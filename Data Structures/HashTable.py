class hashtable():
    def __init__(self):
        self.max = 100
        self.list1 = [[] for i in range(self.max)]
    def hash(self,key):
        ans = 0
        for char in key:
            ans = ans + ord(char)
        return ans%100
    
    def __setitem__(self,key,value):
        final = self.hash(key)
        F = False
        for index,element in enumerate(self.list1[final]):
            if element[0]==key and len(element)==2:
                self.list1[index] = (key,value)
                F = True
        if F==False:
            self.list1[final].append((key,value))

    
    def __getitem__(self,key):
        final = self.hash(key)
        for item in self.list1[final]:
            if item[0] == key:
                return item[1]

            

    
    def __delitem__(self,key):
        final = self.hash(key)
        for index,element in enumerate(self.list1[final]):
            if element[0]==key:
                del self.list1[final][index]