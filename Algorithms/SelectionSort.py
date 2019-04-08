class SelectionSort:
    def __init__(self, arr):
        for i in range(len(arr)):  # Traverse through all elements
            min_index = i  # index of the minimum element in the remaining array
            for j in range(i+1, len(arr)):  # Traverse through remaining array
                if arr[min_index] > arr[j]:  # Update index if a smaller number is found
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    selectionsort = SelectionSort(arr)
