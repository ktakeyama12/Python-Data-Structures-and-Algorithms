import os
import sys
sys.path.append(os.pardir)

from Implementations.BinarySearchTree import BinarySearchTree

class TreeTraverals:
    def __init__(self):
        self.preorderarr = []
        self.inorderarr = []
        self.postorderarr = []
        self.bfsarr = []
        tree = BinarySearchTree()
        tree.add(50)
        tree.add(30)
        tree.add(20)
        tree.add(40)
        tree.add(70)
        tree.add(60)
        tree.add(80)
        root = tree.getRoot()
        self.preorder(root)
        self.inorder(root)
        self.postorder(root)
        self.bfs(root)

    def preorder(self, root):
        self.preorderhelper(root)
        print("Pre Order Traversal")
        print(self.preorderarr)

    def preorderhelper(self, node):
        if node is not None:
            self.preorderarr.append(node.val)
            self.preorderhelper(node.left)
            self.preorderhelper(node.right)

    def inorder(self, root):
        self.inorderhelper(root)
        print("In Order Traversal")
        print(self.inorderarr)

    def inorderhelper(self, node):
        if node is not None:
            self.inorderhelper(node.left)
            self.inorderarr.append(node.val)
            self.inorderhelper(node.right)

    def postorder(self, root):
        self.postorderhelper(root)
        print("Post Order Traversal")
        print(self.postorderarr)

    def postorderhelper(self, node):
        if node is not None:
            self.postorderhelper(node.left)
            self.postorderhelper(node.right)
            self.postorderarr.append(node.val)

    def bfs(self, root):
        # self.bfsqueue = []
        self.bfshelper(root)
        print("Breadth First Traversal")
        print(self.bfsarr)

    def bfshelper(self, node):
        bfsqueue = [node]
        while bfsqueue:
            temp = bfsqueue.pop(0)
            self.bfsarr.append(temp.val)
            if temp.left:
                bfsqueue.append(temp.left)
            if temp.right:
                bfsqueue.append(temp.right)


if __name__ == '__main__':
    treetraversal = TreeTraverals()