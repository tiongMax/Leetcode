# Leetcode tips and question compilation

## Array:
### Prefix sum:
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
- 2115

### Dfs:
- 2360
    