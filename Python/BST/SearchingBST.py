class Tree:
    def __init__(self, val=None):
        # Initialize a tree node with a value
        self.value = val
        if self.value:
            # If a value is provided, 
            #create left and right children as empty trees
            self.left = Tree()
            self.right = Tree()
        else:
            # If no value is provided, set left and 
            #right children to None
            self.left = None
            self.right = None
    
    def isempty(self):
        # Check if the tree node is empty
        return self.value == None
    
    def isleaf(self):
        # Check if the tree node is a leaf node (both left and right children are None)
        if self.left.left == None and self.right.right == None:
            return True
        else:
            return False
    
    def insert(self, data):
        if self.isempty():
            # If the current node is empty, 
            #insert the data as its value
            self.value = data
            # Create empty left and right children
            self.left = Tree()
            self.right = Tree()
        elif self.value == data:
            # If the data already exists in the tree, return
            return
        elif data < self.value:
            # If the data is less than the current node's value, 
            #insert it into the left subtree
            self.left.insert(data)
            return
        elif data > self.value:
            # If the data is greater than the current node's value, 
            #insert it into the right subtree
            self.right.insert(data)
            return
    
    def find(self, v):
        if self.isempty():
            # If the tree is empty, the value is not found
            print("{} is not found".format(v))
            return False
        if self.value == v:
            # If the value is found at the current node, 
            #print a message and return True
            print("{} is found".format(v))
            return True
        if v < self.value:
            # If the value is less than the current node's value, 
            #search in the left subtree
            return self.left.find(v)
        else:
            # If the value is greater than the current node's value, 
            #search in the right subtree
            return self.right.find(v)
    
    def inorder(self):
        if self.isempty():
            # If the tree is empty, return an empty list
            return []
        else:
            # Return the inorder traversal of the tree (left subtree, root, right subtree)
            return self.left.inorder() + [self.value] + self.right.inorder()

# Example usage
t = Tree(20)
t.insert(15)
t.insert(25)
t.insert(8)
t.insert(16)
t.find(8)
print(t.inorder())