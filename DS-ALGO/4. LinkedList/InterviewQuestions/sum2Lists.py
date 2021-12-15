from LinkedList import LinkedList

def sum2LL(llA,llB):
    node1 = llA.head
    node2 = llB.head
    carry = 0
    ll = LinkedList()
    while node1 or node2:
        result = carry
        if node1:
            result += node1.value
            node1 = node1.next
        if node2:
            result += node2.value
            node2 = node2.next
        
        ll.add(int(result%10))
        carry = result/10
    return ll


llA = LinkedList()
llB = LinkedList()
llA.generate(3,1,9)
llB.generate(3,1,9)
print(llA)
print(llB)
print(sum2LL(llA,llB))


