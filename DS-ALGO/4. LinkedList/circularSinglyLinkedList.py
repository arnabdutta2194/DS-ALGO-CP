class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head: #This condition will satisfy because, last node references head
                break
            node = node.next
    
    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "CSLL has been created"

circularSLL = CircularSLL()
circularSLL.createCSLL(1)

print([node.value for node in circularSLL])
