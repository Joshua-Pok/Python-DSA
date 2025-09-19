# A red black tree is a kind of BST that solves the balancing problem, it contains a bit of extra logic to ensure that the tree remains balanced when nodes are inserted or deleted


## AFter insertion, we check if it is balanced, if it is not we perform a rotations. Red/Black is just a boolean we attach to each node.

## Each node in a RB tree stores an extra bit, called the color. Either red or black. When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in worst case 

# List of rules

# 1) Each node is either red or black
# 2) The root has to be black
# 3) All Nil leaf nodes must be black
# 4) IF the node is red, both its children are black
# 5) All paths from a single node go thru the same number of black nodes to reach any of its descendants

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

class RBTree: 
    def __init__(self):
        self.nil = RBNode(None) #Sentinel node that represents leaf node in the tree
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil #root of tree points to this sentinel node to signify the tree is empty

    def insert(self,val):
        newNode = RBNode(val)
        newNode.parent = None
        newNode.left = self.nil
        newNode.right = self.nil
        new_node.red = True

        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if newNode.val < current.val:
                current = current.left
            else: 
                current = current.right

        
