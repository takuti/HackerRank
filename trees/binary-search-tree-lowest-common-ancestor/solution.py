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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    n = root
    if v1 > v2:
        v1, v2 = v2, v1
    while n.left is not None or n.right is not None:
        if v1 <= n.info and n.info <= v2:
            return n
        elif v1 < n.info:
            if n.left is None:
                return n
            n = n.left
        else:
            if n.right is None:
                return n
            n = n.right
    return n


tree = BinarySearchTree()
