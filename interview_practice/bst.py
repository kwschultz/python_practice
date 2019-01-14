# Simple binary search tree

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
             if node.left is None:
                node.left = Node(value)
             else:
                self._insert(value, node.left)
        elif value > node.value:
             if node.right is None:
                node.right = Node(value)
             else:
                self._insert(value, node.right)
        else:
             print("We already have a {}".format(value))
                             
    def find(self, value):
        if self.root:
            is_found = self._find(value, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None
                            
    def _find(self, value, node):
        if value > node.value and node.right is not None:
            return self._find(value, node.right)
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value == node.value:
            return True

    
                             

                             
                             
bst = BST()
                             
bst.insert(4)
bst.insert(5)
bst.insert(10)
bst.insert(9)
bst.insert(8)

print(bst.find(9))
print(bst.find(10))
print(bst.find(4))
print(bst.find(43))
