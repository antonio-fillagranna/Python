# Python Program Invert a Binary Tree using Recursive Postorder

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# function to return the root of inverted tree
def mirror(root):
    if root is None:
        return None
    
    # Invert the left and right subtree
    left = mirror(root.left)
    right = mirror(root.right)
  
    # Swap the left and right subtree
    root.left = right
    root.right = left
  
    return root

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)

if __name__ == "__main__":
    
    # Input Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root = mirror(root)
  
    # Mirror Tree:
    #       1
    #      / \
    #     3   2
    #        / \
    #       5   4
    in_order(root)