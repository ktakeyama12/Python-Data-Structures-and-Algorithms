class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = node

    def printall(self):
        if self.root is None:
            return None
        else:
            current = self.root
            while current:
                print(current.val)
                current = current.next

    def reverselist(self):
        current = self.root
        prev = None
        while current:
            if current.next is None:
                self.root = current
                self.root.next = prev
                current = None
            else:
                next = current.next
                current.next = prev
                prev = current
                current = next

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.add(5)
    linkedlist.add(1)
    linkedlist.add(4)
    linkedlist.add(2)
    linkedlist.reverselist()
    linkedlist.printall()
