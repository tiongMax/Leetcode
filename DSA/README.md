# Leetcode tips and question compilation

## Array:
### Prefix sum:
- 1422 
  - We can use the total numbers of 0 instead of finding the prefix sum.
- 2270
  - We can use sum(nums) instead of find the postfix sum.
- 2559

## Graph:
### matrix:
- 130, 417 and 1020 (expand from the border): 
  - Instead of expanding from inside of the board, we can start and expand from outside of the board
- 994 (multiple entry point bfs): 
  - There can be multiple entry point for the traverse (search), we just insert all of them into a queue and do bfs.
- 1631 and 778 (dijkstra on matrix)
  - We should update the visited after the node is popped out from the heap instead of before pushing it into the heap. For bfs, we only visit (push and pop) each node once. As for dijkstra, we might visit it more than once to find the shortest path.

### Topological sort:
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

### Dijkstra's / Bellman Ford:
- 1631

### UnionFind: