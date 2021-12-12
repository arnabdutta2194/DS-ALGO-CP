from contextlib import nullcontext


class Node:
    def __init__(self,value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def CreateDLL(self,nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        return "DLL is created Successfully"
    
    def InsertDLL(self,nodeValue,position):
        newNode = Node(nodeValue)
        if self.head is None:
            return "Doubly Linked List Does Not Exists"
        else:
            if position == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif position == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                currNode = self.head
                index = 0
                while index < position-1:
                    if currNode.next is None: break
                    currNode = currNode.next
                    index +=1
                newNode.next = currNode.next
                newNode.prev = currNode
                currNode.next.prev = newNode
                currNode.next = newNode
            return "Node is Inserted Successfully in DLL"

    def traverseDLL(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
    
    def reverseTraverseDLL(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def searchDLL(self,value):
        if self.head is None:
            return "DLL is Empty"
        node = self.head
        while node:
            if node.value == value:
                return f"{node.value} Exists in DLL"
            node = node.next
        return f"{value} Does Not Exists in DLL"
    
    def deleteNodeDLL(self,position):
        if self.head is None:
            print("DLL is Empty")
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif position == 1:
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                index = 0
                currNode = self.head
                while index < position-1:
                    if currNode.next == None:
                        break
                    currNode = currNode.next
                    index += 1
                nextNode = currNode.next
                currNode.next = nextNode.next
                nextNode.prev = currNode
                print("Node has been Deleted")
    def deleteEntireDLL(self):
        if self.head is None:
            print("DLL is Empty")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been deleted Successfully")
        
newNode = DoublyLinkedList()
newNode.CreateDLL(1)
print([node.value for node in newNode])
newNode.InsertDLL(2,1)
newNode.InsertDLL(3,1)
newNode.InsertDLL(4,1)
newNode.InsertDLL(5,1)
newNode.InsertDLL(6,1)
print([node.value for node in newNode])
newNode.InsertDLL(20,0)
print([node.value for node in newNode])
newNode.InsertDLL(25,3)
print([node.value for node in newNode])
# newNode.traverseDLL()
newNode.reverseTraverseDLL()

print(newNode.searchDLL(2))
print(newNode.searchDLL(22))
print([node.value for node in newNode])
newNode.deleteNodeDLL(0)
print([node.value for node in newNode])
newNode.deleteNodeDLL(1)
print([node.value for node in newNode])
newNode.deleteNodeDLL(4)
print([node.value for node in newNode])

newNode.deleteEntireDLL()
print([node.value for node in newNode])

