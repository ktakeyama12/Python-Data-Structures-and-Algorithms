class Heap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def printheap(self):
        print(self.heapList)

    def percUp(self, i):
        while i // 2 > 0:  # Parent of the current node can be calculated by diving by 2.
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            print(self.heapList)
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while i * 2 < self.currentSize:  # While there is a child
            mc = self.minChild(i)  # Get the minimum out of all childs
            if self.heapList[i] > self.heapList[mc]:  # Swao selected index with minimum index
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):  # Returns smallest child
        if i * 2 + 1 > self.currentSize:  # Go down if there are still 2 or more levels
            return i * 2
        else:  # Parent has to be larger than child, so we can't blindly go down
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2  # Return left child
            else:
                return i * 2 + 1  # Return right child

    def delMin(self):  # Removes root (smallest)
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]  # Overwrites root with last leaf
        self.currentSize = self.currentSize - 1
        self.heapList.pop()  # Removes last element
        self.percDown(1)  # Stores root in the correct spot
        return retval


if __name__ == '__main__':
    heap = Heap()
    heap.insert(3)
    heap.insert(5)
    heap.insert(2)
    heap.insert(4)
    heap.insert(1)
    heap.delMin()
    heap.printheap()
