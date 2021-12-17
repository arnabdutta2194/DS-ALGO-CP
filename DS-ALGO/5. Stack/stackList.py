class Stack:
    # --- Initialize Empty List --- #
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(value) for value in self.list]
        return "\n".join(values)
    
    # --- Check if Stack is Empty --- #
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    # --- Add Elements To Stack --- #
    def push(self,value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    # --- Remove Elements From Stack --- #
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.list.pop()

    # --- Check Last Element --- #
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.list[len(self.list)-1]
    
    # --- Delete Entire Stack --- #
    def delete(self):
        self.list = None
        
customStack  = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack)
print("----****----")
print(customStack.pop())
print("----****----")
print(customStack)
print("----****----")
print(customStack.peek())
print("----****----")
print(customStack.delete())
print("----****----")
