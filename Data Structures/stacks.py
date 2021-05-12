class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return  self.container[-1]
    def isempty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
s.push(10)
s.peek()
s.pop()
s.isempty()
s.size()

# Reversing the string

string = str(input())
for i in string:
    s.push(i)
for i in range(len(string)):
    ans = ans + s.pop()
print(ans)