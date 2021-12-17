class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(item) for item in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == [] : return True
        return False
    
    def enqueue(self,value):
        self.items.append(value)
        return "Element is inserted at end of Queue"
    
    def dequeue(self):
        if self.isEmpty(): return "Queue is empty"
        self.items.pop(0)
        return "Element has been successfully removed"
    
    def peek(self):
        if self.isEmpty(): return "Queue is empty"
        return self.items[0]
        
    
    def delete(self):
        self.items = None


customQueue = Queue()
print(customQueue.isEmpty())
print("--****--")
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print("--****--")
customQueue.dequeue()
print(customQueue)
print("--****--")
customQueue.enqueue(10)
print(customQueue)
print("--****--")
customQueue.dequeue()
customQueue.dequeue()
print(customQueue)
print("--****--")
print(customQueue.peek())
