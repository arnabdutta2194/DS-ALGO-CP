class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self) -> str:
        return str(self.list)
    
    def __len__(self):
        return len(self.list)
    
    def push(self,item):
        self.list.append(item)
        return "Item Has Been Addedd Successfully"
    
    def pop(self):
        if len(self.list) == 0: return "Queue is Empty"
        else:
            return self.list.pop()
        
class QueueviaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    
    def __str__(self) -> str:
        return str(self.inStack)
    
    def enqueue(self,item):
        self.inStack.push(item)
    
    def deque(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        
        return result

customQueue = QueueviaStack()
customQueue.enqueue(2)
customQueue.enqueue(4)
customQueue.enqueue(12)
customQueue.enqueue(99)
customQueue.enqueue(212)
print(customQueue)
print(customQueue.deque())
print(customQueue)
print(customQueue.deque())
print(customQueue)


