from random import randint

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None
    #--- To Invoke Str Class In an Object ---#
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #-- To Make Linked List Iterable --#
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
    
    def __str__(self):
        values = [str(node.value) for node in self]
        return ' --> ' . join(values)
    
    #-- Returns the Length of the Linked List --#
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result+=1
            node=node.next
        return result
    
    #-- Addition Of Node --#
    def add(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head =  newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    #-- Generate Linked List Based On Random Numbers
    def generate(self,n, min_value,max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self


# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))


