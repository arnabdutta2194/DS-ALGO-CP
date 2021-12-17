class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode : return None
        else: return self.minNode.value
    
    def push(self,item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.top = Node(value=item,next=self.top)
    
    def pop(self):
        if not self.top: return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item
customStack = Stack()
customStack.push(10)
customStack.push(4)
customStack.push(44)
customStack.push(2)
print(customStack.min())
customStack.pop()
print(customStack.min())
customStack.pop()
print(customStack.min())
customStack.pop()
print(customStack.min())
