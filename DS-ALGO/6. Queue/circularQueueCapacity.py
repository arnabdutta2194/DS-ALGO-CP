class Queue:
    def __init__(self,maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.top = -1
        self.start = -1
    
    def __str__(self):
        values = [str(value) for value in self.items]
        return " ".join(values)
    
    def isFull(self):
        if self.top + 1 == self.top: return True
        elif self.start == 0 and self.top+1 == self.maxSize: return True
        else: return False 
    
    def isEmpty(self):
        if self.top == -1: return True
        else: return False
    
    def enqueue(self,value):
        if self.isFull(): return "Queue is Full"
        else: 
            if self.top + 1 ==self.maxSize :
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "Element has been Inserted at the end of Queue"
    def dequeue(self):
        firstElement = self.items[self.start]
        start = self.start
        if self.start + 1 == self.maxSize:
            self.start = 0
        elif self.start == self.top:
            self.start = -1
            self.top = -1
        else:
            self.start += 1
        self.items[start] = None
        return firstElement
    
    def peek(self):
        if self.isEmpty(): return "Queue is Empty"
        return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue(6)
print(customQueue)
print(customQueue.isFull())
print(customQueue.isEmpty())
print("---***---")
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)
customQueue.enqueue(50)
print("---***---")
print(customQueue)
print("---***---")
print(customQueue.isEmpty())
print("---***---")
customQueue.enqueue(5)
print(customQueue)
print(customQueue.isFull())
print("---***---")
# print(customQueue.enqueue(22))
print(customQueue.dequeue())
print(customQueue.start)
print(customQueue.top)
print(customQueue)
print("---***---")
print(customQueue.peek())