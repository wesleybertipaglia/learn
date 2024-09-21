# Ordered: Depends on the type of tree (e.g., binary search trees are ordered, general trees may not be)
# Mutable: Yes
# Duplicates: Depends on the tree type (e.g., binary search trees typically do not allow duplicates)
# Indexing: No (but can traverse nodes)
# Different Data Types: Yes (nodes can hold data of various types)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # In-order traversal (left, root, right)
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

    # Print the tree
    def print_tree(self):
        self.in_order_traversal(self.root)
        print()

# Create a binary tree and insert elements
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Print the tree using in-order traversal
tree.print_tree()  # Output: 2 3 4 5 6 7 8
