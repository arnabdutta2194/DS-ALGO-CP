class MultiStack:
    def __init__(self,stackSize):
        self.numberStacks = 3
        self.custList = [0] * (stackSize * self.numberStacks)
        self.sizes = [0] * self.numberStacks
        self.stackSize = stackSize

    def isFull(self,stackNum):
        if self.sizes[stackNum] == self.stackSize: return True
        return False
    
    def isEmpty(self,stackNum):
        if self.sizes[stackNum] == 0: return True
        return False

    def indexOfTop(self,stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1
    
    def push(self,item,stackNum):
        if self.isFull(stackNum): return "Stack is Full"
        else:
            self.sizes[stackNum] += 1
            self.custList[self.indexOfTop(stackNum)] = item

    def pop(self,stackNum):
        if self.isEmpty(stackNum) :  return "Stack is Empty"
        else:
            value = self.custList[self.indexOfTop(stackNum)]
            self.custList[self.indexOfTop(stackNum)] = 0
            self.sizes[stackNum] -= 1
            return value
    
    def peek(self,stackNum):
        if self.isEmpty(stackNum) :  return "Stack is Empty"
        else: 
            value = self.custList[self.indexOfTop(stackNum)]
            return value
    
    
stack = MultiStack(3)
print(stack.custList)
print(stack.sizes)
print(stack.isFull(2))
print(stack.indexOfTop(1))
stack.push(2,2)
stack.push(3,2)
stack.push(1,0)
print(stack.custList)
print(stack.peek(0))
print(stack.peek(2))
stack.pop(1)
stack.pop(1)
stack.pop(2)
print(stack.custList)
