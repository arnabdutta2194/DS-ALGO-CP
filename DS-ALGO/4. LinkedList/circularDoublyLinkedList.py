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
    
    def insertNodeCircularDLL(self,value,position):
        if self.head is None:
            print("Circular DLL is empty")
        else:
            newNode = Node(value)
            if position == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
            elif position == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
                
            else:
                index = 0
                currNode = self.head
                while index < position - 1:
                    if currNode.next == self.head: break
                    currNode = currNode.next
                    index += 1
                nextNode = currNode.next
                newNode.next = nextNode
                newNode.prev = currNode
                currNode.next = newNode
                nextNode.prev = newNode
    
    def traverseCDLL(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            if tempNode ==  self.tail: break
            tempNode = tempNode.next
    
    def reverseTraverseCDLL(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            if tempNode ==  self.head: break
            tempNode = tempNode.prev
    
    def searchCDLL(self,value):
        tempNode = self.head
        while tempNode:
            if tempNode.value == value:
                return "Value found in CDLL"
            if tempNode == self.tail: break
            tempNode = tempNode.next
        return "Value not found in CDLL"
    
    def deleteNodeCDLL(self,position):
        if position == 0:
            if self.head.next == self.head:
                self.head.next = None
                self.tail.next = None
                self.head = None
                self.head = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
                self.head.prev = self.tail
        elif position == 1:
            if self.head.next == self.head:
                self.head.next = None
                self.tail.next = None
                self.head = None
                self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
        else:
            currNode = self.head
            index = 0
            while index < position-1:
                if currNode == self.tail: break
                currNode = currNode.next
                index += 1
            nextNode = currNode.next
            currNode.next = nextNode.next
            nextNode.next.prev = currNode
   
    def deleteEntireCDLL(self):
        if self.head is None:
            print("Circular CDLL is empty")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None  
            print("The CDLL has been successfully deleted")



            
newNodeCDLL = CircularDLL()
newNodeCDLL.createCircularDLL(1)
newNodeCDLL.insertNodeCircularDLL(2,1)
newNodeCDLL.insertNodeCircularDLL(3,1)
newNodeCDLL.insertNodeCircularDLL(4,1)
newNodeCDLL.insertNodeCircularDLL(5,1)
newNodeCDLL.insertNodeCircularDLL(6,0)
print([node.value for node in newNodeCDLL])
newNodeCDLL.insertNodeCircularDLL(11,2)
print([node.value for node in newNodeCDLL])
newNodeCDLL.insertNodeCircularDLL(5,1)
print([node.value for node in newNodeCDLL])
newNodeCDLL.traverseCDLL()
print("***********")
newNodeCDLL.reverseTraverseCDLL()
print("***********")
print(newNodeCDLL.searchCDLL(2))
print(newNodeCDLL.searchCDLL(22))
print("***********")
print([node.value for node in newNodeCDLL])
newNodeCDLL.deleteNodeCDLL(0)
print([node.value for node in newNodeCDLL])
newNodeCDLL.deleteNodeCDLL(1)
print([node.value for node in newNodeCDLL])
newNodeCDLL.deleteNodeCDLL(2)
print([node.value for node in newNodeCDLL])
newNodeCDLL.deleteNodeCDLL(1)
print([node.value for node in newNodeCDLL])
newNodeCDLL.deleteEntireCDLL()
print([node.value for node in newNodeCDLL])
