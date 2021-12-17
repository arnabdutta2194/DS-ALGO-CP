# --- Initialize Node Class --- #
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# --- Initialize Linked List --- #
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(node.value) for node in self.LinkedList]
        return "\n".join(values)

    def isEmpty(self):
        if self.LinkedList.head == None : return True
        return False
    
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty(): return "Stack is Empty"
        nodeValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return nodeValue
    
    def peek(self):
        if self.isEmpty(): return "Stack is Empty"
        nodeValue = self.LinkedList.head.value
        return nodeValue
    
    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print("--****--")
customStack.pop()
print("--****--")
print(customStack)
print("--****--")
print(customStack.peek())