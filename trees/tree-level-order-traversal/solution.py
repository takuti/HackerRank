
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
def levelOrder(root):
    root.level = 0
    nodes = [root]
    traverse = []
    while len(nodes) > 0:
        node = nodes.pop(0)
        traverse.append(node.info)
        next_level = node.level + 1
        if node.left is not None:
            node.left.level = next_level
            nodes.append(node.left)
        if node.right is not None:
            node.right.level = next_level
            nodes.append(node.right)
    print(' '.join(map(str, traverse)))



tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.create(arr[i])

levelOrder(tree.root)
