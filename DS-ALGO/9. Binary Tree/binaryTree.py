import queueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    

newBTree = TreeNode("Drinks") #--Initialize Binary Tree by Creating Root Node
leftChild = TreeNode("Hot") #-- Create Left Child
rightChild = TreeNode("Cold") #-- Create Right Node
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
cola = TreeNode("Cola")
fanta = TreeNode("Fanta")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild.leftChild = cola
rightChild.rightChild = fanta
newBTree.leftChild = leftChild #-- Add Right Child
newBTree.rightChild = rightChild #-- Add Left Child


def preOrderTraversal(rootNode):
    if not rootNode: # ----> O(1)
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild) # ----> O(n/2)
    preOrderTraversal(rootNode.rightChild) # ----> O(n/2)
    
    #---- Time Complexity --- O(n)
    #---- Space Complexity --- O(n) [As we are using Stack Memory]

def inOrderTraversal(rootNode):
    if not rootNode: return #----> O(1)
    inOrderTraversal(rootNode.leftChild) # ----> O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild) # ----> O(n/2)

    #---- Time Complexity --- O(n)
    #---- Space Complexity --- O(n) [As we are using Stack Memory]

def postOrderTraversal(rootNode):
    if not rootNode: return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode: return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)



print("Preorder Traversal : ")
preOrderTraversal(newBTree)
print("Inorder Traversal : ")
inOrderTraversal(newBTree)
print("PostOrder Traversal : ")
postOrderTraversal(newBTree)
