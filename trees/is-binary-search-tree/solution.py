""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    queue = [(root, -1, 10**4+1)]
    while len(queue) > 0:
        node, lower, upper = queue.pop(0)

        if node.data <= lower or upper <= node.data:
            return False

        if node.left is not None:
            if node.left.data >= node.data:
                return False
            else:
                # left subtree must not be greater than current node
                queue.append((node.left, lower, node.data))
        if node.right is not None:
            if node.right.data <= node.data:
                return False
            else:
                # right subtree must not be smaller than current node
                queue.append((node.right, node.data, upper))
    return True


