class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

def preOrder(root):
    if root == None:
        return
    print root.info,
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root

        n = self.root
        while n is not None:
            if val <= n.info:
                if n.left is not None:
                    n = n.left
                else:
                    n.left = Node(val)
                    return self.root
            else:
                if n.right is not None:
                    n = n.right
                else:
                    n.right = Node(val)
                    return self.root


tree = BinarySearchTree()
