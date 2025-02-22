# Leetcode tips and question compilation

## Array
### Rotated:
- 1752 - We can loop through the array twice instead of explicitly creating a new array of size 2n.

## Prefix sum:
- 1352 - Prefix product
- 1422 - We can use the total numbers of 0 instead of finding the prefix sum.
- 2017
- 2270 - We can use sum(nums) instead of find the postfix sum.
- 2559
- 2657 - We can use a variable hold the sum of previous index. 

## Sliding window
### Fixed

### Variable
- 76 - Instead of comparing 2 hashtables, we can use a variable to compare if the window matches the target substring
- 1800
- 3105 

## String
### Palindrome
- 1400

## Stack
### Normal stack
- 1910
- 2116
- 3174

### Monotonic stack

## Queue
### Normal queue
- 2948 - We can use a list of queue instead of a list of priority queue to maintain the order of each group and get the smallest element from the queue in O(1).

### Monotonic queue

### String comparison
- 916 - If the order is not important (unlike substring / subsequence), we can find and compare the 
occurance of each character instead.

## Tree
### Iterative
- 1028 

### Trie
- 208
- 211
- 2185
- 3042
- 3045

## Heap
### Median
### Normal
- 2342 - We can pop out whenever the heap's length is > 2 so that the overall time complexity is nlog m instead of n^2log m
- 3066 

## Backtrack    
### Binary 
- 78

### Unique binary
- 90

### N-nary
- 2698 - Similar idea as MCM

### Permutation
- 46

### Unique permutation
- 47
- 1079

## Graph:
### Matrix bfs:
- 130 - (expand from the border)
- 417 - (expand from the border)
- 542 - (multiple entry point bfs)
- 994 - There can be multiple entry point for the traverse (search), we just insert all of them into a queue and do bfs (multiple entry point bfs).
- 1020 - Instead of expanding from inside of the board, we can start and expand from outside of the board.
- 1293 - A node can store more information instead of just r, c and cost to reach; We can check the cost before pushing a node to the queue so that there is only 1 node with the same r, c in the queue.
- 1765 - (multiple entry point bfs)

### Matrix dfs:
- 827 - We can precompute the area of the island instead of traversing the island for its area for many times. Instead of flipping the adjacent 0s of an island after traversing the island, we can flip the 0 and check for its adjacent cells.
- 2658

### Kahn's / Dfs (Topological sort):
- 207
- 210
- 802
- 1462
- 2050
- 2115

### Dfs:
- 2360 - We need 2 hash tables, 1 for visited and the other to keep track the starting node of the cycle.

### Bfs:
- 1091 - The length is only updated after the nodes in the same level are processed, so the a for loop is needed to loop through the nodes in that level.
- 2493 - Bfs + bipartite

### 0/1 bfs
- 1293
- 1368 - Since the cost to reach a node is not monotonic (can decrease instead of just remain and increase), we cannot mark it as visited until the target node is reached or the deque is empty.
- 2290 - Since the cost to reach a node is monotonic, we can mark it as visited after pushing it to the deque as the cost for any other path to reach this node is either the same or larger. 

### In/out degree:
- 1557

### Dijkstra's / Bellman Ford (SSSP):
- 743
- 787
- 787 
- 1514
- 1631

### UnionFind:
- 323
- 684
- 721

### Prim's / Kruskal (MST):
- 1584

## Dp
### 1D
- 91
- 198
- 213
- 746
-

### Palindromic substring

### 2D
- 309
- 494
- 518 - Can be space optimized as the previous case required are settled beforehand.

### Grid

### Subsequence
- 1143

### MCM 

## Bitwise
### XOR   
- 2425
- 2429
- 2683

## Math
### Count
- 1726
- 2364

## OrderedSet
- 2349 