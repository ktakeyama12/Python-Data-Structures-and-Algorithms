class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def listprint(self):
        current = self.root
        while current is not None:
            print(current.val)
            current = current.next

    def insertBeginning(self, val):
        node = Node(val)
        node.next = self.root
        self.root = node

    def insertEnd(self, val):
        if self.root is None:
            return
        current = self.root
        while current.next is not None:
            current = current.next
        node = Node(val)
        current.next = node


if __name__ == '__main__':
    list = LinkedList()
    list.root = Node("Mon")
    e2 = Node("Tue")
    list.root.next = e2
    list.insertBeginning("Sat")
    list.insertEnd("Sun")
    list.listprint()