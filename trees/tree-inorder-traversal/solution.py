class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    stack = [root]
    res = []

    while len(stack) > 0:
        n = stack.pop(-1)
        if n.left is None and n.right is None:
            res.append(n.info)
            continue

        if n.right is not None:
            stack.append(n.right)
        stack.append(Node(n.info))
        if n.left is not None:
            stack.append(n.left)

    print(' '.join(map(str, res)))


