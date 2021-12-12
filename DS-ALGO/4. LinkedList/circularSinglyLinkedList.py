from typing import MutableSequence


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
        self.head = node
        self.tail = node
        node.next = node
        return "CSLL has been created"

    def insertCSLL(self,nodeValue,position):
        if self.head is None:
            return "Circular Singly Linked List Does Not Exist"
        else:
            newNode = Node(nodeValue)
            if position == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif position == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                tempNode = self.head
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "Node Has been successfully created"
    def traverseCSLL(self):
        if self.head is None:
            return "Circular Singly Linked List Does Not Exist"
        
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCSLL(self,value):
        if self.head is None:
            return "Circular Singly Linked List Does Not Exist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "Value Does not Exist in Circular SLL"
    def deleteCSLL(self,position):
        if self.head is None:
            return "Circular Singly Linked List Does Not Exist"
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next =self.head
            elif position == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    self.tail = node
                    node.next = self.head
            else:
                index = 0
                tempNode =  self.head
                while index < position - 1:
                    if tempNode.next == self.tail:
                        break
                    tempNode = tempNode.next
                    index += 1

                    nextNode = tempNode.next
                    tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


circularSLL = CircularSLL()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(2,0)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(4,1)
circularSLL.insertCSLL(5,1)
circularSLL.insertCSLL(22,4)
print([node.value for node in circularSLL])
circularSLL.traverseCSLL()
# print(circularSLL.searchCSLL())
circularSLL.deleteCSLL(0)
print([node.value for node in circularSLL])
circularSLL.deleteCSLL(0)
print([node.value for node in circularSLL])
circularSLL.deleteCSLL(3)
print([node.value for node in circularSLL])