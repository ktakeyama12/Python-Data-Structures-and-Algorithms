# Algorithms Cheat Sheet

## Table of Contents

AA

## Time complexities to remember

| Name           | Best    | Worst   | Space  | Key Features              |
| -------------- | ------- | ------- | ------ | ------------------------- |
| Quicksort      | nlog(n) | n^2     | log(n) | Pivot                     |
| Mergesort      | nlog(n) | nlog(n) | n      | Split, divide-and-conquer |
| Bubble Sort    | n       | n^2     | 1      | Bubble up                 |
| Insertion Sort | n       | n^2     | 1      | Pick 1 element and move   |
|                |         |         |        |                           |

## Details of each sort

### Quicksort

##### The Good

- Average is fast
- Can run parallel because the input is divided

##### The Bad

- Worst case is slow

##### Complexity Analysis

- Best nlog(n). Pick the mid pivot.
- Worst n^2. Pick smallest or largest element. All elements are moved per call.
- Space log(n). Recursive call calls twice, creating call stack.

##### How it works

1. Pick a pivot
2. Compare and dive into 2 sub arrays
3. Recursively solve subarrays, starting from 1.

##### Pseudocode

```
def partition(list, start_index, end_index):
    pivot = end_index
    left_index = start_index
    right_index = end_index -1
    # Walk through the list and swap left and right
    while left_index <= right_index:
    	if list[left_index] > list[right_index]:
    		swap
    		right_index -= 1
        left_index += 1

```

### Mergesort

##### The Good

- Always nlog(n)
- Can run parallel because the input is divided into chunks

##### The Bad

- Takes O(n) space and O(logn) call stack
- Hard to implement

##### Complexity Analysis

- Always nlog(n). Entire chunks has to be iterated through, and there are log(n) calls because we split
- Worst n^2. Pick smallest or largest element. All elements are moved per call.
- Space log(n). Recursive call calls twice, creating call stack.

##### How it works

1. Split in half until each chunk length is 2 or 1 O(logn) calls
2. Sort each chunk
3. Iterate through 2 chunks from beginning and merge into new chunk O(logn)

```
def mergesort(list):
	if len(list) > 1:
		L = mergesort(list[:mid])
		R = mergesort(list[mid:])
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
			   list[k] = L[i]
             else:
         		...
             k += 1
         # Remaining elements
         while i < len(L):
         	arr[k] = L[i]
         	i += 1
         	k += 1
         while j < len(R):
         	...
         
```



### Bubblesort

##### The Good

- Sorted case is O(n)
- Simple and easy to implement
- Minimal space

##### The Bad

- Takes O(n^2)

##### Complexity Analysis

- Loops twice, hence O(n^2)

##### How it works

1. Loop through all n elements
2. While loop, loop again. Last elements are sorted so upto n-i-1
3. Swap neighbor elements

```
for i in range(n):
	for k in range(0,n-i-1):
		if, swap(k, k + 1)
```

### Insertion Sort

##### The Good

- Sorted case is O(n)
- Intuitive. Just like sorting cards.
- Minimal space

##### The Bad

- Usually takes O(n^2)
- No particular benefits. Not super fast, implementation is not super easy.

##### Complexity Analysis

- Best O(n), just compare each element and no swapping
- Worst O(n^2) First picked element is the largest element

##### How it works

1. Loop through each item
2. For each item, shift left until the spot is correct

```
for i in range(len(list)):
	while i > 0  and list[i-1] >= list[i]:
		list[i-1], list[i]
    i -= 1
```

