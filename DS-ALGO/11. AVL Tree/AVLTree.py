import queueLinkedList as queue
class AVLNode:
    def __init__(self,data) -> None:
        self.data = data
        self.rightChild = None
        self.leftChild = None
        self.height = 1 #---Height property is needed to determine if the tree is balanced or not


def preOrderTraversal(rootNode):
    if not rootNode : return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode : return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrdertraversal(rootNode):
    if not rootNode : return
    postOrdertraversal(rootNode.leftChild)
    postOrdertraversal(rootNode.rightChild)
    print(rootNode.data)
def levelOrderTraversal(rootNode):
    if rootNode is None : return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode,nodeValue):
    if rootNode.data ==  nodeValue:
        print("The value is found")   
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue: 
            print("The value is found")   
        else : 
            searchNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue: 
            print("The value is found")   
        else : 
            searchNode(rootNode.rightChild,nodeValue)



newAVL =AVLNode(10)
