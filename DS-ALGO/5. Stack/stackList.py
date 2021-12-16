class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(value) for value in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self,value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None
        
customStack  = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("----****----")
print(customStack.pop())
print("----****----")
print(customStack)
print("----****----")
print(customStack.peek())
print("----****----")
print(customStack.delete())
print("----****----")
