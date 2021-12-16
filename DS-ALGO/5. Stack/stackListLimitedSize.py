class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(value) for value in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == [] :  return True
        return False

    def isFull(self):
        if len(self.list) == self.maxSize: return True
        return False
    
    def push(self,value):
        if self.isFull() : return "Stack is Full"
        self.list.append(value)
        return "Element has been successfully pushed in Stack"
    
    def pop(self):
        if self.isEmpty() : return "Stack is Empty"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty() : return "Stack is Empty"
        return self.list[len(self.list[len(self.list)-1])]
    
    def delete(self):
        self.list = None

customStack = Stack(5)
print(customStack.isEmpty())
print("--****--")
print(customStack.push(2))
print(customStack.push(3))
print(customStack.push(4))
print(customStack.push(5))
print(customStack.push(2))
print("--****--")
print(customStack.isEmpty())
print("--****--")
print(customStack)
print("--****--")
print(customStack.push(2))
print("--****--")
print(customStack)
print("--****--")
print(customStack.pop())
print("--****--")
print(customStack)


    

    
