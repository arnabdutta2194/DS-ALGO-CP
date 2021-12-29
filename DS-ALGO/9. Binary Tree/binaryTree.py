import queueLinkedList as queue
# --- Initializing a Tree Node
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
newBTree.leftChild = leftChild #-- Add Left Child
newBTree.rightChild = rightChild #-- Add Right Child

# --- Pre Order Traversal(Root --> LST --> RST)
def preOrderTraversal(rootNode):
    if not rootNode: # ----> O(1)
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild) # ----> O(n/2)
    preOrderTraversal(rootNode.rightChild) # ----> O(n/2)
    
    #---- Time Complexity --- O(n)
    #---- Space Complexity --- O(n) [As we are using Stack Memory]

# --- In Order Traversal(LST --> Root Node --> RST)
def inOrderTraversal(rootNode):
    if not rootNode: return #----> O(1)
    inOrderTraversal(rootNode.leftChild) # ----> O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild) # ----> O(n/2)

    #---- Time Complexity --- O(n)
    #---- Space Complexity --- O(n) [As we are using Stack Memory]

# --- Post Order Traversal(LST --> RST --> Root Node)
def postOrderTraversal(rootNode):
    if not rootNode: return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    #---- Time Complexity --- O(n)
    #---- Space Complexity --- O(n) [As we are using Stack Memory]

# --- Level Order Traversal(Traverse Level By Level)
def levelOrderTraversal(rootNode):
    if not rootNode: return # -----> O(1)
    else:
        customQueue = queue.Queue() # -----> O(1)
        customQueue.enqueue(rootNode)  # -----> O(1)
        while not(customQueue.isEmpty()): # -----> O(n)
            root = customQueue.dequeue() 
            print(root.value.data) 
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild) # -----> O(1)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild) # -----> O(1)
    #---- Time Complexity --- O(n)
    #---- Space Complexity --- O(n) [As we are Creating Custom Queue Memory]
            
# --- Searching a Binary Tree
def searchBinaryTree(rootNode,nodeValue):
    if not rootNode: return "Binary Tree Does Not Exists" 
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Node Exists in Binary Tree"
            # print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
    return "Node Does Not Exist in Binary Tree"

# --- Inserting a Node
def insertNodeBTree(rootNode,newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode) 
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Node successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Node successfully Inserted"

# --- Get the Deepest Node
def getDeepestNode(rootNode):
    if not rootNode: return "Binary Tree Does Not Exists" 
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

# --- Delete the Deepest Node
def deleteDeepestNode(rootNode,deepestNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root is deepestNode:
                root.value = None
                return
            if (root.value.leftChild is not None):
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)

# --- Delete a Custom Node
def deleteNodeBtree(rootNode,node):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "Node Has Been Successfully Deleted"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Node is Not Found"

# --- Delete Entire Binary Tree
def deleteBinaryTree(rootNode):  #--- Time Complexity - O(1)
    rootNode.data = None        
    rootNode.leftChild = None        
    rootNode.rightChild = None
    return "Binary Tree has been deleted successfully"      

print("Preorder Traversal : ")
preOrderTraversal(newBTree)
print("Inorder Traversal : ")
inOrderTraversal(newBTree)
print("PostOrder Traversal : ")
postOrderTraversal(newBTree)
print("LevelOrder Traversal : ")
levelOrderTraversal(newBTree)
print("-----*****-----")
print(searchBinaryTree(newBTree,"Coffee"))
print(searchBinaryTree(newBTree,"Pepsi"))

pepsi = TreeNode("Pepsi")
print(insertNodeBTree(newBTree,pepsi))
print("LevelOrder Traversal : ")
levelOrderTraversal(newBTree)
print("-----*****-----")
deepestNode = getDeepestNode(newBTree)
print(deepestNode.data)
# print("-----*****-----")
# deleteDeepestNode(newBTree,deepestNode)
# levelOrderTraversal(newBTree)
print(deleteNodeBtree(newBTree,"Hot"))
levelOrderTraversal(newBTree)
print("-----*****-----")
deleteBinaryTree(newBTree)
levelOrderTraversal(newBTree)