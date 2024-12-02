class Tree:
    def __init__(self, val=None):
        # Initialize the Tree node with a value
        self.value = val
        # Create left and right child nodes 
        #if the value is not None
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isempty(self):
        # Check if the node is empty (value is None)
        return (self.value == None)

    def insert(self, data):
        # Insert a new value into the Tree
        if self.isempty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
        elif self.value == data:
            return
        elif data < self.value:
            self.left.insert(data)
            return
        elif data > self.value:
            self.right.insert(data)
            return

    def isleaf(self):
        # Check if the node is a leaf node (no children)
        if self.left == None and self.right == None:
            return True
        else:
            return False

    def maxval(self):
        # Find the maximum value in the Tree
        if self.right.right == None:
            return (self.value)
        else:
            return (self.right.maxval())

    def delete(self, v):
        # Delete a value from the Tree
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return
            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return

    def inorder(self):
        # Traverse the Tree in inorder (left-root-right) 
        #and return the values
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder() + [self.value] + self.right.inorder())

# Test the Tree class
t = Tree(15)
t.insert(10)
t.insert(18)
t.insert(4)
t.insert(11)
t.insert(16)
t.insert(20)
print("Before deleting 4: ")
print(t.inorder())
t.delete(4)
print("After deleting 4: ")
print(t.inorder())