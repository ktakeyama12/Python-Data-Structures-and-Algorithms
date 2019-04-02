# Reference https://www.laurentluce.com/posts/binary-search-tree-library-in-python/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        self.addhelper(self.root, key)

    def addhelper(self, node, key):
        if not node:  # Insert node
            return Node(key)
        else:
            if key < node.val:
                node.left = self.addhelper(node.left, key)
            else:
                node.right = self.addhelper(node.right, key)
            return node  # IMPORTANT Return unchange node pointer

    def printInorder(self):
        self.arr = []
        self.printInorderHelper(self.root)
        print(self.arr)

    def printInorderHelper(self, node):  # Simple helper to print tree inorder traversal
        if node is not None:
            self.printInorderHelper(node.left)
            self.arr.append(node.val)
            self.printInorderHelper(node.right)

    def delete(self, val):
        self.deleteHelper(self.root, val)

    def deleteHelper(self, node, val):
    #     if self.root and self.root.val == val:
            # self.root
        if node is None:  # Base Case
            return node
        if val < node.val:
            node.left = self.deleteHelper(node.left, val)
        elif val > node.val:
            node.right = self.deleteHelper(node.right, val)
        else:
            if node.right is None:
                return node.right
            if node.left is None:
                temp = node.right
                node = None
                return node
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.getMinValue(node.right)
            node.val = temp.val
            node.right = self.deleteHelper(node.right, temp.val)
        return node

    def getMinValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current



if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(30)
    tree.add(20)
    tree.add(40)
    tree.add(70)
    tree.add(60)
    tree.add(80)

    tree.delete(40)
    tree.printInorder()

