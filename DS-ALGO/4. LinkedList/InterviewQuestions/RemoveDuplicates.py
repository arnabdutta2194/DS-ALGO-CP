from LinkedList import LinkedList

def removeDuplicates(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        visited = set([currNode.value])
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next = currNode.next.next
            else:
                visited.add(currNode.next.value)
                currNode = currNode.next
        return ll

#- In above method we are creating temporary buffer
#- Optimized approach wihout buffer is given below :

def removeDuplicateOptimized(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head

customLL = LinkedList()
# customLL.generate(10,0,90)
customLL.add(39)
customLL.add(0)
customLL.add(39)
customLL.add(77)
customLL.add(39)
customLL.add(20)
customLL.add(10)

# customLL.add(26)
print(customLL)
# removeDuplicates(customLL)
removeDuplicateOptimized(customLL)
print(customLL)
