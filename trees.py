from anytree import Node
from anytree.exporter import UniqueDotExporter


def convert_to_anytree(node, parent=None):
    """
    Converts a binary tree node to an AnyTree node.

    Args:
        node (BinaryTreeNode): The binary tree node to convert.
        parent (AnyTreeNode, optional): The parent node in the AnyTree structure. Defaults to None.

    Returns:
        AnyTreeNode: The converted AnyTree node.
    """
    if not node:
        return None

    current_node = Node(str(node.key), parent=parent)
    convert_to_anytree(node.left, parent=current_node)
    convert_to_anytree(node.right, parent=current_node)

    return current_node


class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        key: The value stored in the node.
        left: The left child of the node.
        right: The right child of the node.
        height: The height of the node (for AVL trees).
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class BST:
    """
    Binary Search Tree (BST) implementation.

    Attributes:
        root (TreeNode): The root node of the BST.

    Methods:
        insert(key): Inserts a new node with the given key into the BST.
        search(key): Searches for a node with the given key in the BST.
        delete(key): Deletes a node with the given key from the BST.
        display(): Displays the BST in a tree-like structure.
        visualize_tree(output_name): Visualizes the BST as a picture using UniqueDotExporter.
        get_all_numbers(root): Returns a list of all numbers in the BST using inorder traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            root.key = self._get_min_value_node(root.right).key
            root.right = self._delete(root.right, root.key)

        return root

    def _get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def display(self):
        self._display(self.root, 0)

    def _display(self, root, level):
        if root:
            self._display(root.right, level + 1)
            print(" " * 4 * level + "->", root.key)
            self._display(root.left, level + 1)

    def visualize_tree(self, output_name):
        if not self.root:
            print("Tree is empty.")
            return

        # Convert the BST to anytree structure
        root_node = convert_to_anytree(self.root)

        # Export the tree to a picture using UniqueDotExporter
        UniqueDotExporter(root_node).to_picture(output_name)

    def get_all_numbers(self, root):
        numbers = []
        self._inorder_traversal(root, numbers)
        return numbers

    def _inorder_traversal(self, node, numbers):
        if node:
            self._inorder_traversal(node.left, numbers)
            numbers.append(node.key)
            self._inorder_traversal(node.right, numbers)


class AVL(BST):
    """
    AVL tree implementation.

    Inherits from BST (Binary Search Tree) class.

    Methods:
    - insert(key): Insert a key into the AVL tree.
    - delete(key): Delete a key from the AVL tree.
    - visualize_tree(output_name): Visualize the AVL tree and export it to a picture.
    - get_all_numbers(root): Get all numbers in the AVL tree using inorder traversal.

    Private Methods:
    - _height(node): Get the height of a node.
    - _update_height(node): Update the height of a node.
    - _balance(node): Get the balance factor of a node.
    - _rotate_right(y): Perform a right rotation on a node.
    - _rotate_left(x): Perform a left rotation on a node.
    - _insert(root, key): Recursive helper function to insert a key into the AVL tree.
    - _delete(root, key): Recursive helper function to delete a key from the AVL tree.
    - _inorder_traversal(node, numbers): Recursive helper function for inorder traversal.

    Attributes:
    - root: The root node of the AVL tree.
    """
    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            return root  # Duplicates are not allowed

        self._update_height(root)

        balance = self._balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            root.key = self._get_min_value_node(root.right).key
            root.right = self._delete(root.right, root.key)

        self._update_height(root)

        balance = self._balance(root)

        # Left Left Case
        if balance > 1 and self._balance(root.left) >= 0:
            return self._rotate_right(root)

        # Left Right Case
        if balance > 1 and self._balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Right Case
        if balance < -1 and self._balance(root.right) <= 0:
            return self._rotate_left(root)

        # Right Left Case
        if balance < -1 and self._balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def visualize_tree(self, output_name):
        if not self.root:
            print("Tree is empty.")
            return

        # Convert the AVL tree to anytree structure
        avl_root_node = convert_to_anytree(self.root)

        # Export the AVL tree to a picture using UniqueDotExporter
        UniqueDotExporter(avl_root_node).to_picture(output_name)

    def get_all_numbers(self, root):
        numbers = []
        self._inorder_traversal(root, numbers)
        return numbers

    def _inorder_traversal(self, node, numbers):
        if node:
            self._inorder_traversal(node.left, numbers)
            numbers.append(node.key)
            self._inorder_traversal(node.right, numbers)
