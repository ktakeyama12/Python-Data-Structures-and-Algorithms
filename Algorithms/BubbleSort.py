class BubbleSort:
    def sort(self, arr):
        length = len(arr)
        for i in range(length):
            for j in range(0,length-i-1):  # Last i elements are already sorted
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubblesort = BubbleSort()
    bubblesort.sort(arr)
