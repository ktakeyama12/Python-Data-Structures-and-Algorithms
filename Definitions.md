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

### Definition

- Dictionary maps keys to values
- Hash table is a specific way to implement a dictionary, and takes O(1) ~ O(N)
- Red-black tree is another way to implement a dictionary, and takes O(LogN)

## Breadth First Search vs Depth First Search

--1--

-2-3-

4---5

### Breadth First Search (BFS)

- aka Level order traversal
- BFS gives you the shortest path to every other node on the graph
- [1,2,3,4,5]

### Depth First Search (DFS)

- DFS gives you more information about the graph, such as cycles, sinks, and topological sort
- Preorder Traversal [1,2,4,5,3]
- Inorder Traversal [4,2,5,1,3]
- Postorder Traversal [4,5,2,3,1]