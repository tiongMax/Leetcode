# Leetcode tips and question compilation

## Array:
### Prefix sum:
- 1422 - We can use the total numbers of 0 instead of finding the prefix sum.
- 2270 - We can use sum(nums) instead of find the postfix sum.
- 2559
- 2657 - We can use a variable hold the sum of previous index. 

## String
### Palindrome
- 1400

## Stack
- 2116

### String comparison
- 916 - If the order is not important (unlike substring / subsequence), we can find and compare the 
occurance of each character instead.

## Tree
### Trie
- 208
- 211
- 2185
- 3042
- 3045

## Graph:
### matrix:
- 130, 417 and 1020 (expand from the border): 
  - Instead of expanding from inside of the board, we can start and expand from outside of the board
- 994 (multiple entry point bfs): 
  - There can be multiple entry point for the traverse (search), we just insert all of them into a queue and do bfs.

### Kahn's / Dfs (Topological sort):
- 207
- 210
- 802
- 1462
- 2050
- 2115

### Dfs:
- 2360

### Bfs:
- 1091 - The length is only updated after the nodes in the same level are processed, so the a for loop is needed to loop through the nodes in that level.

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
- 2425
- 2429