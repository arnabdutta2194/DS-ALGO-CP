class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(node) for node in self.linkedList]
        return " ".join(values)
    
    def enqueue(self,value):
        node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next= node
            self.linkedList.tail = node
        return "Element has been successfully inserted"
    
    def isEmpty(self):
        return self.linkedList.head == None
    
    def peek(self):
        if self.isEmpty(): return "Queue is Empty"
        return self.linkedList.head.value

    def dequeue(self):
        if self.isEmpty(): return "Queue is Empty"
        elif self.linkedList.head == self.linkedList.tail:
            value = self.linkedList.head
            self.linkedList.head = None
            self.linkedList.tail = None
        else:
            value = self.linkedList.head
            self.linkedList.head = self.linkedList.head.next
        # return "Element has been successfully removed"
        return value
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


customQueue = Queue()
print(customQueue.isEmpty())
print("---***---")
print(customQueue.enqueue(10))
print(customQueue.enqueue(20))
print(customQueue.enqueue(3))
print(customQueue)
print("---***---")
print(customQueue.peek())
print("---***---")
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())