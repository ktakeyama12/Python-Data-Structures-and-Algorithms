class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def printarr(self):
        for i in self.arr:
            print(i)

    def initmergesort(self):
        self.mergesort(self.arr)

    def mergesort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2  # Returns int, base down
            L = arr[:mid]
            R = arr[mid:]

            self.mergesort(L)  # Recursively splits array into 2 until each array is 1 element (to compare)
            self.mergesort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):  # For each split, compare 2 elements and store into array
                if L[i] < R[j]:
                    arr[k] = L[i]  # This array is used to store the result for each call. This is not the original array.
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left. If we still have values we can just add.
            # Might need more explanation here.
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


if __name__ == '__main__':
    arr = [38,27,43,3,9,82,10]
    ans = MergeSort(arr)
    ans.initmergesort()
    ans.printarr()
