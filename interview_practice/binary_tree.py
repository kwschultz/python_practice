class Queue(object):
    def __init__(self):
        self.queue = list()
    def enqueue(self, value):
        self.queue.append(value)
        return
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return
    def peek(self):
        if not self.is_empty():
            # We assume we are storing Node instances
            return self.queue[0].value
        return
    def is_empty(self):
        return len(self.queue) == 0
    def __len__(self):
        return len(self.queue)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


def preorder_traversal_print(node, traversal):

    if node:
        traversal += '{} '.format(node.value)
        traversal = preorder_traversal_print(node.left, traversal)
        traversal = preorder_traversal_print(node.right, traversal)

    return traversal

def inorder_traversal_print(node, traversal):
    
    if node:
        traversal = inorder_traversal_print(node.left, traversal)
        traversal += '{} '.format(node.value)
        traversal = inorder_traversal_print(node.right, traversal)

    return traversal

def postorder_traversal_print(node, traversal):
    
    if node:
        traversal = postorder_traversal_print(node.left, traversal)
        traversal = postorder_traversal_print(node.right, traversal)
        traversal += '{} '.format(node.value)
    
    return traversal

def levelorder_traversal_print(node):

    if not node:
        return

    level_queue = Queue()
    level_queue.enqueue(node)
    traversal = ''

    while not level_queue.is_empty():
        next_item = level_queue.dequeue()
        traversal += '{} '.format(next_item.value)
        left = next_item.left
        right = next_item.right
        if left:
            level_queue.enqueue(left)
        if right:
            level_queue.enqueue(right)

    return traversal


def height_of_tree(node):

    if not node:
        return -1

    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)

    return 1 + max(left_height, right_height)




if __name__ == '__main__':
    
    #        1
    #      /  \
    #     2    3
    #    / \  / \
    #   4  5 6   7
    #             \
    #              8
    
    btree = BinaryTree(1)
    btree.root.left = Node(2)
    btree.root.right = Node(3)
    btree.root.left.left = Node(4)
    btree.root.left.right = Node(5)
    btree.root.right.left = Node(6)
    btree.root.right.right = Node(7)
    btree.root.right.right.right = Node(8)

    # Expected pre-order traversal:
    # 1 2 4 5 3 6 7 8
    traversal = ''
    print(preorder_traversal_print(btree.root, traversal))
    print('')
    
    # Expected pre-order traversal:
    # 4 2 5 1 6 3 7 8
    traversal = ''
    print(inorder_traversal_print(btree.root, traversal))
    print('')
    
    # Expected post-order traversal:
    # 4 5 2 6 8 7 3 1
    traversal = ''
    print(postorder_traversal_print(btree.root, traversal))
    print('')

    # Expected level-order traversal:
    # 1 2 3 4 5 6 7 8
    print(levelorder_traversal_print(btree.root))
    print('')

    # Expected height = 3
    print('Tree is this high: {}'.format(height_of_tree(btree.root)))
    print('')
