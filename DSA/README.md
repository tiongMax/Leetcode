# Leetcode tips and question compilation

## Array
### Normal
- 3010

### Rotated:
- 1752 - We can loop through the array twice instead of explicitly creating a new array of size 2n.

## Two pointers
- 11
- 15
- 42
- 125
- 167

## Binary search
### Normal
- 34
- 74
- 162
- 240
- 540 - Take note on the index of the 2 same value elements before and after the single element
- 704
- 1901

### Search Range
- 4 - BS on smaller length arr to check on how many elems to be taken from smaller length array to form left partition.
- 410 - min max
- 774
- 875 
- 1011
- 1283
- 1482
- 1539

### Modified Array
- 33 - rotated array
- 81 - Since we have a way to solve the question that contains no duplicates, we should find and solve the issue that is stopping us to apply the solution.
- 153 - rotated array

### Lower / upper bound
- 35
- 981
- 3508 - We can use hashmap to record the packet that is still in the queue instead of looping through the queue to find them out.

## Prefix sum:
- 1352 - Prefix product
- 1422 - We can use the total numbers of 0 instead of finding the prefix sum.
- 2017
- 2270 - We can use sum(nums) instead of find the postfix sum.
- 2559
- 2657 - We can use a variable hold the sum of previous index. 

### All possible subarrays:
- 1524 - We can use odd and even to record how many prefix sum (subarray sum until that point) of odd and even value we have. Then, we can deduct them from current sum to count for how many odd subarray sum we have without odd or even.
- 1749 - We can store previous max and min prefix sum instead of loop through the prefix sum array at every new index.

## Difference array
- 3355

## Sliding window
### Fixed
- 239
- 1423

### Variable
- 3
- 76 - Instead of comparing 2 hashtables, we can use a variable to compare if the window matches the target substring
- 340
- 567
- 1004
- 1800
- 3105 

### Count all subarray
- 992 
- 930
- 1248
- 1358

## String
### Palindrome
- 1400

## Stack
### Normal stack
- 20
- 150
- 155
- 1910
- 2116
- 3174

### Monotonic stack
- 84
- 739
- 853

## Queue
### Normal queue
- 2948 - We can use a list of queue instead of a list of priority queue to maintain the order of each group and get the smallest element from the queue in O(1).

### Monotonic queue

### String comparison
- 916 - If the order is not important (unlike substring / subsequence), we can find and compare the 
occurance of each character instead.

## Linked list
- 2
- 19
- 148
- 160
- 206
- 237
- 328
- 2095

### Cycle
- 141
- 142
- 876

## Tree
### Iterative
- 1028 

### Pre, in, post order
- 889

### DFS
- 100
- 104
- 110 - Return a tuple that contains the height of the subtree and if the subtree is balanced
- 226
- 386 
- 543
- 572
- 3372

### BFS
- 102
- 199

### BST
- 235
 
### Trie
- 208
- 211
- 2185
- 3042
- 3045

## Heap
### Median

### Normal
- 1792
- 2342 - We can pop out whenever the heap's length is > 2 so that the overall time complexity is nlog m instead of n^2log m
- 2353 - We can delete lazily by comparing the popped value with the updated hash map instead of deleting from heap whenever it is updated.
- 3066 
- 3408

## Greedy
### Heap
- 1792

### Sort

## Backtrack    
### Binary 
- 78

### Unique binary
- 90

### N-nary
- 37
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
- 1857 - We can use memoization to store the largest color value of the current node.
- 2050
- 2115

### Dfs:
- 2360 - We need 2 hash tables, 1 for visited and the other to keep track the starting node of the cycle.

### Bfs:
- 1091 - The length is only updated after the nodes in the same level are processed, so the a for loop is needed to loop through the nodes in that level.
- 2493 - Bfs + bipartite

### Bfs / Dfs:
- 2359

### 0/1 bfs:
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
- 3341
- 3342 - Notice that if the sum of x and y coordinates is even then the cost will be 2, else it will be 1 

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
- 873 

### Unbounded Knapsack
- 377 (backtrack) 

### Grid

### Subsequence
- 1092 - We can use the dp table to construct the supersequence.
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

### Diagonals
- 498 - sum of i + j of a cell is the same for the same diagonal line
- 3446

## Fast exponentiation
- 50 
- 1922

## OrderedSet
- 2349 