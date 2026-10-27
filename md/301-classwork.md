# DSA 301 - Classwork

Generated from `DSA_101_Curriculum.xlsx`, sheet `DSA_301`, column `Classwork`.
This file is the source of truth for `create_contests.py` - edit it here, not in
the spreadsheet, once you start filling in slugs.

- **Contest name:** DSA 301 - Classwork
- **Contest slug:** `dsa-301-classwork`
- **Coverage:** LEC 1 to LEC 50.
- **Counts:** 150 problems total - 150 codeable, 0 theory.

## How to fill this in

Every problem needs a **Slug** before it can be added to the contest. The slug is
the last path segment of the challenge URL on HackerRank:

```
https://www.hackerrank.com/challenges/simple-array-sum/problem
                                      ^^^^^^^^^^^^^^^^ this part
```

- Put the bare slug in the Slug column. No full URL, no backticks needed.
- Leave Slug empty for anything not mapped yet. Those are reported as unmapped
  and skipped; everything else still gets added.
- Rows with Type `theory` are paper or reading exercises with no judge problem.
  They are always skipped, whatever the Slug column says.
- `python resolve_slugs.py --course 301 --classwork` uses this account's own
  challenge bank plus HackerRank's search to propose candidate slugs and writes
  them into this file. Review them before trusting them - a keyword search will
  happily return the wrong problem.
- Order matters: challenges are added to the contest in the order they appear
  below, so the first lecture lands first.

---


## Week 1

### LEC-1 - Lambdas I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D01-1 | Sort a vector<int> in descending order using a lambda comparator | descending-order-sort | code |
| CW-D01-2 | Use count_if with a lambda to count elements greater than K | count-elements-greater-than-k | code |
| CW-D01-3 | Write a generic lambda add and verify it with int and double | generic-lambda-add | code |

### LEC-2 - Lambdas II — uses & tricks

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D02-1 | Sort vector<pair<int,int>> by second value then first via a lambda | sort-pairs-by-second-then-first | code |
| CW-D02-2 | Use find_if to return the first element greater than K | classwork-use-find-if-to-return-the-first-element-greater-than-k | code |
| CW-D02-3 | Use remove_if + erase to delete all odd numbers from a vector | classwork-use-remove-if-erase-to-delete-all-odd-numbers-from-a-vector | code |

### LEC-3 - STL Remastered I — containers

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D03-1 | Remove duplicates from a vector using a set | classwork-remove-duplicates-from-a-vector-using-a-set | code |
| CW-D03-2 | Count word frequencies from input using unordered_map | classwork-count-word-frequencies-from-input-using-unordered-map | code |
| CW-D03-3 | Implement browser back/forward history using two stacks | classwork-implement-browser-backforward-history-using-two-stacks | code |

### LEC-4 - STL Remastered II — algorithms

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D04-1 | Find the k-th largest element using a priority_queue | classwork-find-the-k-th-largest-element-using-a-priority-queue | code |
| CW-D04-2 | Binary-search a target in a sorted vector with lower_bound | classwork-binary-search-a-target-in-a-sorted-vector-with-lower-bound | code |
| CW-D04-3 | Count distinct elements using sort + unique | classwork-count-distinct-elements-using-sort-unique | code |

### LEC-5 - DSA Basics Quick Revision

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D05-1 | Compute factorial and nCr recursively | classwork-compute-factorial-and-ncr-recursively | code |
| CW-D05-2 | Reverse a singly linked list iteratively | classwork-reverse-a-singly-linked-list-iteratively | code |
| CW-D05-3 | Print numbers 1..N and N..1 using recursion | classwork-print-numbers-1-n-and-n-1-using-recursion | code |


## Week 2

### LEC-6 - Hashmaps Fundamentals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D06-1 | LC1 Two Sum | classwork-lc1-two-sum | code |
| CW-D06-2 | Frequency of elements (GfG) | classwork-frequency-of-elements-gfg | code |
| CW-D06-3 | LC217 Contains Duplicate | classwork-lc217-contains-duplicate | code |

### LEC-7 - Hashmaps - Subarrays & Patterns

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D07-1 | LC560 Subarray Sum Equals K | classwork-lc560-subarray-sum-equals-k | code |
| CW-D07-2 | LC49 Group Anagrams | classwork-lc49-group-anagrams | code |
| CW-D07-3 | LC3 Longest Substring Without Repeating Characters | classwork-lc3-longest-substring-without-repeating-characters | code |

### LEC-8 - Heaps / Priority Queue Fundamentals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D08-1 | LC215 Kth Largest Element in an Array | classwork-lc215-kth-largest-element-in-an-array | code |
| CW-D08-2 | Kth smallest element (GfG) | classwork-kth-smallest-element-gfg | code |
| CW-D08-3 | LC1046 Last Stone Weight | classwork-lc1046-last-stone-weight | code |

### LEC-9 - Advanced Heaps

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D09-1 | LC347 Top K Frequent Elements | classwork-lc347-top-k-frequent-elements | code |
| CW-D09-2 | LC23 Merge k Sorted Lists | classwork-lc23-merge-k-sorted-lists | code |
| CW-D09-3 | LC295 Find Median from Data Stream | classwork-lc295-find-median-from-data-stream | code |

### LEC-10 - Hashmaps & Heaps Combined

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D10-1 | LC767 Reorganize String | classwork-lc767-reorganize-string-3 | code |
| CW-D10-2 | LC355 Design Twitter | classwork-lc355-design-twitter | code |
| CW-D10-3 | LC895 Maximum Frequency Stack | classwork-lc895-maximum-frequency-stack | code |


## Week 3

### LEC-11 - Trees & DFS traversals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D11-1 | LC94 Binary Tree Inorder Traversal | classwork-lc94-binary-tree-inorder-traversal | code |
| CW-D11-2 | LC144 Binary Tree Preorder Traversal | classwork-lc144-binary-tree-preorder-traversal | code |
| CW-D11-3 | LC145 Binary Tree Postorder Traversal | classwork-lc145-binary-tree-postorder-traversal | code |

### LEC-12 - Iterative traversal & BFS

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D12-1 | LC102 Binary Tree Level Order Traversal | classwork-lc102-binary-tree-level-order-traversal | code |
| CW-D12-2 | LC199 Binary Tree Right Side View | classwork-lc199-binary-tree-right-side-view | code |
| CW-D12-3 | LC94 Inorder Traversal (iterative) | classwork-lc94-inorder-traversal-iterative | code |

### LEC-13 - Height, Depth & Diameter

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D13-1 | LC104 Maximum Depth of Binary Tree | classwork-lc104-maximum-depth-of-binary-tree | code |
| CW-D13-2 | LC543 Diameter of Binary Tree | classwork-lc543-diameter-of-binary-tree | code |
| CW-D13-3 | LC111 Minimum Depth of Binary Tree | classwork-lc111-minimum-depth-of-binary-tree | code |

### LEC-14 - Balanced check & views

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D14-1 | LC110 Balanced Binary Tree | classwork-lc110-balanced-binary-tree | code |
| CW-D14-2 | LC101 Symmetric Tree | classwork-lc101-symmetric-tree | code |
| CW-D14-3 | LC199 Binary Tree Right Side View | classwork-lc199-binary-tree-right-side-view | code |

### LEC-15 - Advanced Traversals & Views

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D15-1 | LC987 Vertical Order Traversal of a Binary Tree | classwork-lc987-vertical-order-traversal-of-a-binary-tree | code |
| CW-D15-2 | Top view of a binary tree (GfG) | classwork-top-view-of-a-binary-tree-gfg | code |
| CW-D15-3 | Boundary traversal of a binary tree (GfG) | classwork-boundary-traversal-of-a-binary-tree-gfg | code |


## Week 4

### LEC-16 - Invert & Symmetric

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D16-1 | LC226 Invert Binary Tree | classwork-lc226-invert-binary-tree | code |
| CW-D16-2 | LC101 Symmetric Tree | classwork-lc101-symmetric-tree | code |
| CW-D16-3 | LC100 Same Tree | classwork-lc100-same-tree | code |

### LEC-17 - Path Sum family

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D17-1 | LC112 Path Sum | classwork-lc112-path-sum | code |
| CW-D17-2 | LC113 Path Sum II | classwork-lc113-path-sum-ii | code |
| CW-D17-3 | LC124 Binary Tree Maximum Path Sum | classwork-lc124-binary-tree-maximum-path-sum | code |

### LEC-18 - Lowest Common Ancestor

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D18-1 | LC236 Lowest Common Ancestor of a Binary Tree | classwork-lc236-lowest-common-ancestor-of-a-binary-tree | code |
| CW-D18-2 | LCA using root-to-node paths (GfG) | classwork-lca-using-root-to-node-paths-gfg | code |
| CW-D18-3 | Distance between two nodes via LCA (GfG) | classwork-distance-between-two-nodes-via-lca-gfg | code |

### LEC-19 - Construct & Flatten

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D19-1 | LC105 Construct Binary Tree from Preorder and Inorder | classwork-lc105-construct-binary-tree-from-preorder-and-inorder | code |
| CW-D19-2 | LC106 Construct Binary Tree from Inorder and Postorder | classwork-lc106-construct-binary-tree-from-inorder-and-postorder | code |
| CW-D19-3 | LC114 Flatten Binary Tree to Linked List | classwork-lc114-flatten-binary-tree-to-linked-list | code |

### LEC-20 - Serialize & Tree Utilities

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D20-1 | LC297 Serialize and Deserialize Binary Tree | classwork-lc297-serialize-and-deserialize-binary-tree | code |
| CW-D20-2 | LC222 Count Complete Tree Nodes | classwork-lc222-count-complete-tree-nodes | code |
| CW-D20-3 | LC863 All Nodes Distance K in Binary Tree | classwork-lc863-all-nodes-distance-k-in-binary-tree | code |


## Week 5

### LEC-21 - Search & Insert

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D21-1 | LC700 Search in a Binary Search Tree | classwork-search-in-a-binary-search-tree | code |
| CW-D21-2 | LC701 Insert into a Binary Search Tree | classwork-insert-into-a-binary-search-tree | code |
| CW-D21-3 | Iterative BST search (GfG) | classwork-iterative-bst-search | code |

### LEC-22 - Validate & Min Diff

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D22-1 | LC98 Validate Binary Search Tree | classwork-validate-binary-search-tree | code |
| CW-D22-2 | LC530 Minimum Absolute Difference in BST | classwork-minimum-absolute-difference-in-bst | code |
| CW-D22-3 | LC501 Find Mode in Binary Search Tree | classwork-find-mode-in-binary-search-tree | code |

### LEC-23 - Delete & Kth smallest

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D23-1 | LC450 Delete Node in a BST | classwork-delete-node-in-a-bst | code |
| CW-D23-2 | LC230 Kth Smallest Element in a BST | classwork-kth-smallest-element-in-a-bst | code |
| CW-D23-3 | Kth largest element in a BST (GfG) | classwork-kth-largest-element-in-a-bst | code |

### LEC-24 - LCA, Build & Iterator

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D24-1 | LC235 Lowest Common Ancestor of a BST | classwork-lowest-common-ancestor-of-a-bst | code |
| CW-D24-2 | LC108 Convert Sorted Array to Binary Search Tree | classwork-convert-sorted-array-to-binary-search-tree | code |
| CW-D24-3 | LC173 Binary Search Tree Iterator | classwork-binary-search-tree-iterator | code |

### LEC-25 - BST Advanced

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D25-1 | LC653 Two Sum IV - Input is a BST | classwork-two-sum-iv-input-is-a-bst | code |
| CW-D25-2 | LC938 Range Sum of BST | classwork-range-sum-of-bst | code |
| CW-D25-3 | LC669 Trim a Binary Search Tree | classwork-trim-a-binary-search-tree | code |


## Week 6

### LEC-26 - Greedy choice & intervals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D26-1 | N meetings in one room (GfG) | classwork-n-meetings-in-one-room | code |
| CW-D26-2 | LC435 Non-overlapping Intervals | classwork-non-overlapping-intervals | code |
| CW-D26-3 | Maximum number of activities selected (GfG) | classwork-maximum-number-of-activities-selected | code |

### LEC-27 - Merge intervals & platforms

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D27-1 | LC56 Merge Intervals | classwork-merge-intervals | code |
| CW-D27-2 | LC57 Insert Interval | classwork-insert-interval | code |
| CW-D27-3 | Minimum number of platforms (GfG) | classwork-minimum-number-of-platforms | code |

### LEC-28 - Knapsack & job sequencing

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D28-1 | Fractional Knapsack (GfG) | classwork-fractional-knapsack | code |
| CW-D28-2 | Job Sequencing Problem (GfG) | classwork-job-sequencing-problem | code |
| CW-D28-3 | Minimum cost to connect ropes (GfG) | classwork-minimum-cost-to-connect-ropes | code |

### LEC-29 - Jump family & failure cases

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D29-1 | LC55 Jump Game | classwork-jump-game | code |
| CW-D29-2 | LC134 Gas Station | classwork-gas-station | code |
| CW-D29-3 | LC135 Candy | classwork-candy | code |

### LEC-30 - Greedy — More Patterns

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D30-1 | LC767 Reorganize String | classwork-lc767-reorganize-string-3 | code |
| CW-D30-2 | LC621 Task Scheduler | classwork-lc621-task-scheduler-2 | code |
| CW-D30-3 | Minimum cost to connect ropes (GfG) | classwork-minimum-cost-to-connect-ropes | code |


## Week 7

### LEC-31 - DP intro & 1D

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D31-1 | LC70 Climbing Stairs | classwork-lc70-climbing-stairs | code |
| CW-D31-2 | LC198 House Robber | classwork-lc198-house-robber | code |
| CW-D31-3 | LC509 Fibonacci Number |  | code |

### LEC-32 - Coin change family

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D32-1 | LC322 Coin Change | classwork-lc322-coin-change-1 | code |
| CW-D32-2 | LC518 Coin Change II | homework-lc518-coin-change-ii | code |
| CW-D32-3 | Minimum number of coins (GfG) | classwork-minimum-number-of-coins-gfg | code |

### LEC-33 - LIS / LCS lite

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D33-1 | LC300 Longest Increasing Subsequence | classwork-lc300-longest-increasing-subsequence | code |
| CW-D33-2 | LC1143 Longest Common Subsequence | classwork-lc1143-longest-common-subsequence | code |
| CW-D33-3 | Longest Increasing Subsequence in O(n log n) (GfG) | classwork-lc300-longest-increasing-subsequence | code |

### LEC-34 - Grid DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D34-1 | LC62 Unique Paths | classwork-lc62-unique-paths | code |
| CW-D34-2 | LC64 Minimum Path Sum | classwork-lc64-minimum-path-sum | code |
| CW-D34-3 | LC63 Unique Paths II | classwork-lc63-unique-paths-ii | code |

### LEC-35 - Subsequence DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D35-1 | Subset Sum (GfG) | classwork-subset-sum-gfg | code |
| CW-D35-2 | LC416 Partition Equal Subset Sum | classwork-lc416-partition-equal-subset-sum | code |
| CW-D35-3 | LC91 Decode Ways | classwork-lc91-decode-ways | code |


## Week 8

### LEC-36 - 0/1 Knapsack

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D36-1 | 0/1 Knapsack (GfG) | classwork-01-knapsack-gfg | code |
| CW-D36-2 | LC416 Partition Equal Subset Sum | classwork-lc416-partition-equal-subset-sum | code |
| CW-D36-3 | LC494 Target Sum | classwork-lc494-target-sum | code |

### LEC-37 - Unbounded knapsack

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D37-1 | Unbounded Knapsack (GfG) | classwork-unbounded-knapsack-gfg | code |
| CW-D37-2 | Rod Cutting (GfG) | classwork-rod-cutting-gfg | code |
| CW-D37-3 | LC322 Coin Change | classwork-lc322-coin-change-1 | code |

### LEC-38 - Edit distance

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D38-1 | LC72 Edit Distance | classwork-lc72-edit-distance | code |
| CW-D38-2 | LC583 Delete Operation for Two Strings | classwork-lc583-delete-operation-for-two-strings | code |
| CW-D38-3 | LC712 Minimum ASCII Delete Sum for Two Strings | classwork-lc712-minimum-ascii-delete-sum-for-two-strings | code |

### LEC-39 - LCS variants / Partition DP intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D39-1 | LC1092 Shortest Common Supersequence | classwork-lc1092-shortest-common-supersequence | code |
| CW-D39-2 | LC516 Longest Palindromic Subsequence | classwork-lc516-longest-palindromic-subsequence | code |
| CW-D39-3 | Matrix Chain Multiplication (GfG) | classwork-matrix-chain-multiplication-gfg | code |

### LEC-40 - Partition / Interval DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D40-1 | Matrix Chain Multiplication (GfG) | classwork-matrix-chain-multiplication-gfg | code |
| CW-D40-2 | LC132 Palindrome Partitioning II | classwork-lc132-palindrome-partitioning-ii | code |
| CW-D40-3 | LC312 Burst Balloons | classwork-lc312-burst-balloons | code |


## Week 9

### LEC-41 - Representation & traversal

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D41-1 | LC200 Number of Islands | classwork-lc200-number-of-islands | code |
| CW-D41-2 | LC547 Number of Provinces | classwork-lc547-number-of-provinces | code |
| CW-D41-3 | LC133 Clone Graph | classwork-lc133-clone-graph | code |

### LEC-42 - Cycle & Bipartite

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D42-1 | LC207 Course Schedule | classwork-lc207-course-schedule | code |
| CW-D42-2 | LC785 Is Graph Bipartite? | classwork-lc785-is-graph-bipartite | code |
| CW-D42-3 | Detect cycle in an undirected graph (GfG) | classwork-detect-cycle-in-an-undirected-graph-gfg | code |

### LEC-43 - Topological sort

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D43-1 | LC210 Course Schedule II | classwork-lc210-course-schedule-ii | code |
| CW-D43-2 | Topological Sort (GfG) | classwork-topological-sort-gfg | code |
| CW-D43-3 | Kahn's algorithm for topological sort (GfG) | classwork-kahns-algorithm-for-topological-sort-gfg | code |

### LEC-44 - Weighted paths & MST

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D44-1 | LC743 Network Delay Time | classwork-lc743-network-delay-time | code |
| CW-D44-2 | LC1631 Path With Minimum Effort | classwork-lc1631-path-with-minimum-effort | code |
| CW-D44-3 | Dijkstra's shortest path (GfG) | classwork-dijkstras-shortest-path-gfg | code |

### LEC-45 - Graphs — Extra

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D45-1 | Bellman-Ford algorithm (GfG) | classwork-bellman-ford-algorithm-gfg | code |
| CW-D45-2 | Floyd-Warshall all-pairs shortest path (GfG) | classwork-floyd-warshall-all-pairs-shortest-path-gfg | code |
| CW-D45-3 | LC994 Rotting Oranges | classwork-lc994-rotting-oranges | code |


## Week 10

### LEC-46 - Tree DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D46-1 | LC543 Diameter of Binary Tree (via DP) | classwork-lc543-diameter-of-binary-tree | code |
| CW-D46-2 | LC337 House Robber III | classwork-lc337-house-robber-iii | code |
| CW-D46-3 | LC124 Binary Tree Maximum Path Sum | classwork-lc124-binary-tree-maximum-path-sum | code |

### LEC-47 - Backtracking foundations

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D47-1 | LC78 Subsets | classwork-lc78-subsets | code |
| CW-D47-2 | LC46 Permutations | classwork-lc46-permutations | code |
| CW-D47-3 | LC77 Combinations | classwork-lc77-combinations | code |

### LEC-48 - Backtracking on grids & constraints

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D48-1 | LC79 Word Search | classwork-lc79-word-search | code |
| CW-D48-2 | LC51 N-Queens | classwork-lc51-n-queens | code |
| CW-D48-3 | LC22 Generate Parentheses | classwork-lc22-generate-parentheses | code |

### LEC-49 - Two pointers & sliding window

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D49-1 | LC3 Longest Substring Without Repeating Characters | classwork-lc3-longest-substring-without-repeating-characters | code |
| CW-D49-2 | LC209 Minimum Size Subarray Sum | classwork-lc209-minimum-size-subarray-sum | code |
| CW-D49-3 | LC15 3Sum | classwork-lc15-3sum | code |

### LEC-50 - Mixed patterns capstone

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D50-1 | Classify five mixed problems by technique | classwork-classify-five-mixed-problems-by-technique | code |
| CW-D50-2 | LC994 Rotting Oranges (BFS) walkthrough | classwork-lc994-rotting-oranges-bfs-walkthrough | code |
| CW-D50-3 | LC300 Longest Increasing Subsequence (DP) walkthrough | classwork-lc300-longest-increasing-subsequence-dp-walkthrough | code |

