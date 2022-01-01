import queueLinkedList as queue

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
def insertNode(rootNode,nodeValue):
    if rootNode.data == None:  #---->O(1)
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)  #---->O(1)
        else:
            insertNode(rootNode.leftChild,nodeValue) #---->O(n/2)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue) #---->O(1)
        else:
            insertNode(rootNode.rightChild,nodeValue) #---->O(n/2)
    return "Node has been Successfully Inserted"

    #--- Time Complexity O(logn)
    #--- Space Complexity O(logn)

def preOrderTraversal(rootNode):
    if not rootNode: return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode: return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode: return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if rootNode is None: return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
    #---- Time Complexity --- O(n)
    #---- Space Complexity --- O(n) [As we are Creating Custom Queue Memory]


def searchBST(rootNode,nodeValue):
    if rootNode is None : return
    elif rootNode.data == nodeValue: print("Value is Found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("Value is Found")
        else:
            searchBST(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightChild.data == nodeValue:
            print("Value is Found")
        else:
            searchBST(rootNode.rightChild,nodeValue)
    #---- Time Complexity --- O(logn)
    #---- Space Complexity --- O(logn)       

def minValueNode(rootNode):
    currentNode = rootNode
    while (currentNode.leftChild is not None):
        currentNode = currentNode.leftChild
    return currentNode

def deleteNode(rootNode,nodeValue):
    if rootNode is None: return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        #-- If Root Node has Only One Child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        
        #-- If Root Node has Two Childs
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been deleted successfully"


newBST = BSTNode(None)
print(insertNode(newBST,55))
print(insertNode(newBST,90))
print(insertNode(newBST,35))
print(newBST.data)
print(newBST.leftChild.data)
print(newBST.rightChild.data)
insertNode(newBST,100)
insertNode(newBST,29)
insertNode(newBST,68)
insertNode(newBST,10)
insertNode(newBST,16)
insertNode(newBST,5)
print("*****")
print("Pre Order Traversal----")
preOrderTraversal(newBST)
print("In Order Traversal----")
inOrderTraversal(newBST)
print("Post Order Traversal----")
postOrderTraversal(newBST)
print("Level Order Traversal----")
levelOrderTraversal(newBST)
print("Level Order Traversal----")
searchBST(newBST,1)
