class Quicksort:
    # Takes last element as pivot
    # Places pivot in correct position, puts smaller in left and larger in right
    # low and high are indexes
    def partition(self, arr, low, high):
        i = low-1  # index of lower element
        pivot = arr[high]  # Pivot element that is used to compare

        for j in range(low, high):  # Compare current element to pivot
            if arr[j] <= pivot:  # Basically pushes (swaps) the larget element to back
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        # Place the pivot at the correct position. Pivot is at high, and i is how far we swapped
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1  # Returns the position of the pivot

    def sort(self, arr, low, high):
        if low < high:  # Will end if low and high are the same
            pi = self.partition(arr, low, high)  # Declare how we partition, returns the position of the pivot
            self.sort(arr, low, pi-1)  # Sort the left
            self.sort(arr, pi+1, high)  # Sort the right
        return arr

if __name__ == '__main__':
    arrpass = [10, 7, 8, 9, 1, 5]
    length = len(arrpass)
    quicksort = Quicksort()
    print(quicksort.sort(arrpass, 0, length-1))