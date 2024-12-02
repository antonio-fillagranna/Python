class Tree:
    def __init__(self, val=None):
        # Initialize the node with a value and left and right subtrees
        self.value = val
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
    
    def isempty(self):
        # Check if the tree is empty
        return self.value is None
    
    def insert(self, data):
        # Insert a value into the tree
        if self.isempty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
        elif self.value == data:
            return
        elif data < self.value:
            self.left.insert(data)
        elif data > self.value:
            self.right.insert(data)
    
    def isleaf(self):
        # Check if the node is a leaf node
        return self.left is None and self.right is None
    
    def inorder(self):
        # Perform inorder traversal
        if self.isempty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

# Example usage
t = Tree(10)
t.insert(8)
t.insert(6)
t.insert(12)

print("Inorder Traversal : ")
print(t.inorder())