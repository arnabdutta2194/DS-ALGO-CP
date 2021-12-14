class Node:
    def __init__(self,value = None):
        self.value = value
        self.prev = None
        self.next = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCircularDLL(self,nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
        print("Circular DLL Created")
    
newNodeCDLL = CircularDLL()
newNodeCDLL.createCircularDLL(1)
print([node.value for node in newNodeCDLL])