# Exact definitions between similar data structures

## Array vs Lists

### Similarities

- Both are used for storing data
- Both are mutable
- Both can be indexed and iterated through
- Both can be sliced

### Differences

- Arrays optimized for arithmetic computations
- Lists can contain different data types, but arrays can not.
- Python has built in array type, but `numpy` array is used as well.

## Dictionary (Associative Array) vs Hash Tables

## Definition

- Dictionary maps keys to values
- Hash table is a specific way to implement a dictionary, and takes O(1) ~ O(N)
- Red-black tree is another way to implement a dictionary, and takes O(LogN)