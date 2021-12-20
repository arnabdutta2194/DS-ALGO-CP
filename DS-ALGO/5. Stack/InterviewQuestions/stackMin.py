class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += "," + str(self.next)
        return string

class Stack:
    def __init__(self):
        self.mainNode = None
        self.minNode = None
    
    def min(self):
        if not self.minNode : return None
        else: return self.minNode.value
    
    #-- To Check MinNode LinkedList
    def __iter__(self):
        node = self.minNode
        while node:
            yield node
            node = node.next

    #-- Uncomment this - To Check mainNode LinkedList
    # def __iter__(self):
    #     node = self.mainNode
    #     while node:
    #         yield node
    #         node = node.next
    
    def push(self,item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.mainNode = Node(value=item,next=self.mainNode)
    
    def pop(self):
        if not self.mainNode: return None
        self.minNode = self.minNode.next
        item = self.mainNode.value
        self.mainNode = self.mainNode.next
        return item
        
customStack = Stack()
customStack.push(10)
customStack.push(4)
customStack.push(44)
customStack.push(21)
customStack.push(3)
print(customStack.min())
print([node.value for node in customStack])
customStack.pop()
print(customStack.min())
customStack.pop()
print(customStack.min())
customStack.pop()
print(customStack.min())
customStack.pop()
print(customStack.min())