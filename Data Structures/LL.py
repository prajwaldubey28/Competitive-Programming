class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
        
        
    def print(self):
        if self.head is None:
            print("Empty")
            return
        
        i = self.head
        ans = ''
        while i:
            ans += str(i.data)+ ' --> ' if i.next else str(i.data)
            i = i.next
        print(ans)
            
    def length(self):
        count=0
        i = self.head
        while i:
            count = count+1
            i=i.next
        return count
            
    
    def insert_begin(self,data):
        node = Node(data,self.head)
        self.head = node 
        
        
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        i = self.head
        while i.next:
            i = i.next
        i.next = Node(data,None)
            
    def insert(self,index,data):
        count = 0
        i = self.head
        if index==0:
            self.insert_begin(data)
        elif index<0 or index>= self.length():
            print("Invalid")
        while i:
            if count == index-1:
                node = Node(data,i.next)
                i.next = node
                break
            count = count+1
            i = i.next
                
    def remove(self,index):
        count = 0
        i = self.head
        if index==0:
            self.head = self.head.next
            return 
        elif index<0 or index>= self.length():
            print("Invalid")
        while i:
            if count == index-1:
                i.next = i.next.next
                break
            
            count = count+1
            i = i.next
                
    def insert_values(self,datalist):
        self.head = None
        for k in datalist:
            self.insert_end(k)

ll = Linkedlist()
ll.insert_values(["banana","mango","grapes","orange"])
ll.insert(1,"blueberry")
ll.remove(2)
ll.print()

ll.insert_values([45,7,12,567,99])
ll.insert_end(67)
ll.print()     