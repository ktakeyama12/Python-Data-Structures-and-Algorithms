class InsertionSort:
    def __init__(self, arr):
        for i in range(1, len(arr)):  # Start loop at second element because first is already sorted
            key = arr[i]  # The item to compare

            j = i-1 # The last item we will compare
            while j > -1 and key < arr[j]: # We will keep moving back as long as the it is similar than last item in array
                arr[j + 1] = arr[j]  # Move the last item one step ahead for room for key
                j -= 1  # Check next item (Move back~
            arr[j + 1] = key  # j is not greater so key belongs at j+1
        print(arr)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    ans = InsertionSort(arr)