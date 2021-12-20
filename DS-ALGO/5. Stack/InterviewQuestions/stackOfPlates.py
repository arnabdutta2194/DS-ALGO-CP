class stackOfPlates:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        return str(self.stacks)
    
    def push(self,item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item]) #-- When Capacity of Stack is reached we are creating a new stack and adding elements to it
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0: #-- Clear the empty Stack
            self.stacks.pop()
        if len(self.stacks) == 0: return None
        else: return self.stacks[-1].pop() #-- Delete from Last Stack
    
    def popAt(self,stackNumber): #--- Pop at a specific Stack Number
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else: return None

customStack = stackOfPlates(3)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
customStack.push(4)
print(customStack)
customStack.pop()
customStack.pop()
print(customStack)
customStack.popAt(0)
print(customStack)


