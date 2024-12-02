class Tree:
    def __init__(self,val=None):
      
        # Initialize the Tree node with a value
        self.value = val
        
        # If the node has a value, 
        #create left and right children nodes
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
          
            # If the node has no value, 
            #set left and right children to None
            self.left = None
            self.right = None
    
    # Check if the node is empty (has no value)
    def isempty(self):
        return (self.value == None)
    
    # Insert a new value into the tree
    def insert(self,data):
      
        # If the node is empty, insert the data here
        if self.isempty():
            self.value = data
            
            # Create left and right children 
            #for the inserted node
            self.left = Tree()
            self.right = Tree()
            print("{} is inserted successfully".format(self.value))
            
        # If data is less than current node value, 
        #insert into left subtree
        elif data < self.value:
            self.left.insert(data)
            return
          
        # If data is greater than current node value, 
        #insert into right subtree
        elif data > self.value:
            self.right.insert(data)
            
        # If data is equal to current node value, do nothing
        elif data == self.value:
            return

# Create a tree with root value 15
t = Tree(15)
# Insert some values into the tree
t.insert(10)
t.insert(18)
t.insert(4)
t.insert(11)
t.insert(16)
t.insert(20)
t.insert(13)