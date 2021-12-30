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