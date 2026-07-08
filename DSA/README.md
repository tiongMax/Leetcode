# DSA Practice Notes

This folder is my personal data structures and algorithms practice hub. It contains LeetCode solutions, revision targets, and pattern notes that help me recognize problem types faster.

## Progress Snapshot

<!-- progress-start -->
- `done/` - 296 solved solution files
- `to_revise/` - 152 problems to revisit
- `to_memorize/` - 8 important patterns or solutions to remember
<!-- progress-end -->

Update this section with:

```bash
python scripts/update-dsa-readme.py
```

## Folder Guide

- `done/` - Problems I have solved and can reference later
- `to_revise/` - Problems that need another pass
- `to_memorize/` - High-value patterns, templates, or tricky solutions

## File Naming

Most files follow this format:

```text
problemNumber - problemName.extension
```

Examples:

```text
200 - numberOfIsland.py
994 - rottingOrange.py
695 - maxAreaIsland.py
```

## Study Workflow

1. Try solving the problem without looking at notes.
2. If the pattern is unclear, move it to `to_revise/`.
3. If the technique is especially reusable, move it to `to_memorize/`.
4. Revisit older problems by topic instead of only by number.
5. Add short notes when a problem teaches a reusable trick.

## Helper Scripts

Run these from the repository root.

```bash
python scripts/update-dsa-readme.py
python scripts/catalog-dsa.py
python scripts/stats-dsa.py
python scripts/find-dsa-problem.py 130
python scripts/find-dsa-problem.py surrounded --open
python scripts/move-dsa-problem.py 130 done --from to_revise
```

- `update-dsa-readme.py` refreshes the progress snapshot.
- `catalog-dsa.py` generates `DSA/CATALOG.md`.
- `stats-dsa.py` prints folder, language, and unique problem counts.
- `find-dsa-problem.py` searches by problem number or title.
- `move-dsa-problem.py` moves problem files between `done/`, `to_revise/`, and `to_memorize/`, then updates the snapshot.

## Pattern Index

Use this section as a quick map when reviewing a topic.

## Topic Catalog

- [Arrays](#arrays)
  - [Hashing](#hashing)
  - [Basic Array](#basic-array)
  - [Rotated Array](#rotated-array)
- [Two Pointers](#two-pointers)
- [Binary Search](#binary-search)
  - [Standard Binary Search](#standard-binary-search)
  - [Search on Answer](#search-on-answer)
  - [Modified Sorted Array](#modified-sorted-array)
  - [Lower / Upper Bound](#lower--upper-bound)
- [Prefix Sum](#prefix-sum)
  - [Counting Subarrays](#counting-subarrays)
- [Difference Array](#difference-array)
- [Sliding Window](#sliding-window)
  - [Fixed Size](#fixed-size)
  - [Variable Size](#variable-size)
  - [Count All Valid Subarrays](#count-all-valid-subarrays)
- [Strings](#strings)
  - [Palindrome](#palindrome)
  - [Character Frequency](#character-frequency)
- [Stack](#stack)
  - [Standard Stack](#standard-stack)
  - [Monotonic Stack](#monotonic-stack)
- [Queue](#queue)
  - [Standard Queue](#standard-queue)
  - [Monotonic Queue](#monotonic-queue)
- [Linked List](#linked-list)
  - [Cycle Detection](#cycle-detection)
- [Trees](#trees)
  - [Traversal](#traversal)
  - [DFS](#dfs)
  - [BFS](#bfs)
  - [Binary Search Tree](#binary-search-tree)
  - [Trie](#trie)
- [Heap / Priority Queue](#heap--priority-queue)
  - [Top k](#top-k)
  - [Median](#median)
- [Greedy](#greedy)
  - [Heap-Based Greedy](#heap-based-greedy)
  - [Sorting-Based Greedy](#sorting-based-greedy)
- [Backtracking](#backtracking)
  - [Subsets](#subsets)
  - [N-ary Choices](#n-ary-choices)
  - [Permutations](#permutations)
- [Graphs](#graphs)
  - [Grid BFS / DFS](#grid-bfs--dfs)
  - [Topological Sort](#topological-sort)
  - [DFS](#dfs-1)
  - [BFS](#bfs-1)
  - [BFS / DFS](#bfs--dfs)
  - [0-1 BFS](#0-1-bfs)
  - [Degree-Based Graph Problems](#degree-based-graph-problems)
  - [Shortest Path](#shortest-path)
  - [Union Find](#union-find)
  - [Minimum Spanning Tree](#minimum-spanning-tree)
- [Dynamic Programming](#dynamic-programming)
  - [1D DP](#1d-dp)
  - [2D DP](#2d-dp)
  - [Unbounded Knapsack](#unbounded-knapsack)
  - [Subsequence DP](#subsequence-dp)
  - [Palindrome DP](#palindrome-dp)
  - [Grid DP](#grid-dp)
  - [Matrix Chain Multiplication](#matrix-chain-multiplication)
- [Bit Manipulation](#bit-manipulation)
  - [XOR](#xor)
- [Math](#math)
  - [Counting](#counting)
  - [Diagonals](#diagonals)
  - [Fast Exponentiation](#fast-exponentiation)
- [Ordered Set / Ordered Map](#ordered-set--ordered-map)

## Arrays

### Hashing

- 1
- 36
- 49
- 217
- 242

### Basic Array

- 3010
- 3637

### Rotated Array

- 1752 - Loop through the array twice conceptually instead of explicitly creating a new array of size `2n`.

## Two Pointers

- 11
- 15
- 42
- 125
- 167

## Binary Search

### Standard Binary Search

- 34
- 74
- 162
- 240
- 540 - Pay attention to the index parity around the duplicated pairs before and after the single element.
- 704
- 1901

### Search on Answer

- 4 - Binary search on the smaller array to decide how many elements should be taken for the left partition.
- 410 - Minimize the maximum value.
- 774
- 875
- 1011
- 1283
- 1482
- 1539
- 2815 - Use multi source bfs to setup the graph 
- 3620 - dijkstra or dp both works for check

### Modified Sorted Array

- 33 - Search in a rotated sorted array.
- 81 - Handle duplicates first, then reuse the no-duplicate rotated-array idea.
- 153 - Find the minimum in a rotated sorted array.

### Lower / Upper Bound

- 35
- 981
- 3508 - Use a hashmap to track packets still in the queue instead of scanning the queue repeatedly.

## Prefix Sum

- 238 - Prefix and postfix product.
- 1352 - Prefix product.
- 1422 - Use the total number of zeroes instead of building a full prefix array.
- 2017
- 2270 - Use `sum(nums)` instead of building a postfix sum.
- 2559
- 2657 - Keep a running value for the previous prefix state.
- 3756 - Use multiple array to store different prefix state.

### Counting Subarrays

- 1524 - Track how many prefix sums are odd and even, then use the current prefix parity to count valid subarrays.
- 1749 - Store previous max and min prefix sums instead of scanning the prefix array at every index.

## Difference Array

- 3355

## Sliding Window

### Fixed Size

- 239
- 1423

### Variable Size

- 3
- 76 - Use a matched-count variable instead of comparing two hash tables every time.
- 340
- 567
- 1004
- 1800
- 3105

### Count All Valid Subarrays

- 930
- 992
- 1248
- 1358

## Strings

### Palindrome

- 1400

### Character Frequency

- 916 - When order does not matter, compare character counts instead of substring or subsequence structure.

## Stack

### Standard Stack

- 20
- 150
- 155
- 1910
- 2116
- 3174

### Monotonic Stack

- 84
- 739
- 853

## Queue

### Standard Queue

- 2948 - Use a list of queues instead of priority queues to preserve group order and get the smallest available element in `O(1)`.

### Monotonic Queue

- 239
- 1438

## Linked List

- 2
- 19
- 148
- 160
- 206
- 237
- 328
- 2095

### Cycle Detection

- 141
- 142
- 876

## Trees

### Traversal

- 1028
- 889

### DFS

- 100
- 104
- 110 - Return both subtree height and whether the subtree is balanced.
- 226
- 386
- 543
- 572
- 3372

### BFS

- 102
- 199

### Binary Search Tree

- 235

### Trie

- 208
- 211
- 2185
- 3042
- 3045

## Heap / Priority Queue

### Top k
- 215
- 355 - Push the last id of each different followers instead of all of the ids.
- 621 - use q to handle the order of task to be processed instead of a heap to handle everything
- 703
- 973
- 1046
- 1792
- 2342 - Pop whenever heap length is greater than `2` so the complexity depends on a small heap instead of storing everything.
- 2353 - Use lazy deletion by comparing popped values with the latest hashmap value.
- 3066
- 3408

### Median
- 295

## Greedy

### Heap-Based Greedy

- 1792

### Sorting-Based Greedy

- Add problems here when reviewing sort-first greedy patterns.

## Backtracking

### Subsets

- 78
- 90

### N-ary Choices

- 37
- 2698 - Similar idea to matrix chain multiplication style partitioning.

### Permutations

- 46
- 47
- 1079

## Graph

### Grid BFS / DFS

- 130 - Expand from the border.
- 417 - Expand from the border.
- 542 - Multiple-source BFS.
- 827 - Precompute island areas so each flip can be evaluated quickly.
- 994 - Insert all starting rotten oranges into the queue, then run multi-source BFS.
- 1020 - Start from outside or the border instead of expanding from inside the board.
- 1293 - Store extra state in each node, not just row, column, and cost.
- 1765 - Multiple-source BFS.
- 2658

### Topological Sort

- 207
- 210
- 802
- 1462
- 1857 - Use memoization to store the largest color value from each node.
- 2050
- 2115

### DFS

- 2360 - Use one structure for visited nodes and another to track the current cycle path.

### BFS

- 1091 - Process level by level so the path length updates after each BFS layer.
- 2493 - BFS with bipartite checking.

### BFS / DFS

- 2359
- 2492

### 0-1 BFS

- 1293
- 1368 - Because the cost can improve, delay finalizing visited state until the best path is known.
- 2290 - Since cost is monotonic, a node can be marked visited when pushed.
- 3286

### Degree-Based Graph Problems

- 1557

### Shortest Path

- 743
- 787
- 1514
- 1631
- 3341
- 3342 - If `row + col` is even, the cost is `2`; otherwise, it is `1`.

### Union Find

- 323
- 684
- 721

### Minimum Spanning Tree

- 1584

## Dynamic Programming

### 1D DP

- 91
- 198
- 213
- 746

### 2D DP

- 309
- 494
- 518 - Can be space optimized because previous states are already settled.
- 873

### Unbounded Knapsack

- 377

### Subsequence DP

- 1092 - Use the DP table to reconstruct the shortest common supersequence.
- 1143

### Palindrome DP

- Add problems here when reviewing palindromic substring or subsequence patterns.

### Grid DP

- Add grid DP problems here as they are reviewed.

### Matrix Chain Multiplication

- Add interval DP or partition DP problems here.

## Bit Manipulation

### XOR

- 2425
- 2429
- 2683

## Math

### Counting

- 1726
- 2364

### Diagonals

- 498 - Cells on the same diagonal share the same `row + col`.
- 3446

### Fast Exponentiation

- 50
- 1922

## Ordered Set / Ordered Map

- 2349

## Review Tips

- Re-solve `to_revise/` problems without looking at the old solution first.
- When stuck, write down the pattern before checking the implementation.
- After solving, summarize the reusable idea in one sentence.
- Promote a problem to `to_memorize/` only if the pattern is common or easy to forget.
