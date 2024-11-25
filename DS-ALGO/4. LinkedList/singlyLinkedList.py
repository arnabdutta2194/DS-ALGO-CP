class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SLinkedList:
    #Initialize Linked List with empty values
    def __init__(self):
        self.head = None
        self.tail = None

    #Function to Print Nodes in Singly Linked List
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #Insertion Method in Singly Linked List
    def insertSLL(self,value,location):
        newNode = Node(value) #Create a new node and assign value
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #Insert at beginning
                newNode.next = self.head
                self.head = newNode
            elif location == 1: #Insert at end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else: #Insert anywhere in middle
                tempNode = self.head
                index = 0
                #If given location is 5, it will be inserted at 6
                while index < location - 1: #Iterate untill Location 5
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next #Store value of 6
                tempNode.next = newNode #Point 5 to newNode
                newNode.next = nextNode #Point newly created 6 to existing 6

    #  Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            return "Singly Linked List Does Not Exists"
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    # Search For a Value in Singly Linked List
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "Singly Linked List Does Not Exists"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The Value does not exist in the List"
     
    # Delete a Specific Node in Singly Linked List
    def deleteNodeSLL(self,location):
        if self.head is None:
            return "Single Linked List Does Not Exists"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if self.tail == node.next:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while (index < location -1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next #--- Node to Be Deleted
                tempNode.next = nextNode.next
    
    def deleteAllNodesSLL(self):
        if self.head is None:
            return "Single Linked List Does Not Exists"
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
# node1 =Node(1)
# node2 =Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

singlyLinkedList.insertSLL(2,0)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,1)
singlyLinkedList.insertSLL(6,1)
singlyLinkedList.insertSLL(20,4)

print([node.value for node in singlyLinkedList])

# singlyLinkedList.traverseSLL()
# print(singlyLinkedList.searchSLL(7))
# print(singlyLinkedList.searchSLL(3))

singlyLinkedList.deleteNodeSLL(2)
singlyLinkedList.traverseSLL()
print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteAllNodesSLL()
print([node.value for node in singlyLinkedList])
