class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    

    
newBTree = TreeNode("Drinks") #--Initialize Binary Tree by Creating Root Node
leftChild = TreeNode("Hot") #-- Create Left Child
rightChild = TreeNode("Cold") #-- Create Right Node
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
preOrderTraversal(newBTree)