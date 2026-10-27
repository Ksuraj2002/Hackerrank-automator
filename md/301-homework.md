# DSA 301 - Homework

Generated from `DSA_101_Curriculum.xlsx`, sheet `DSA_301`, column `Homework`.
This file is the source of truth for `create_contests.py` - edit it here, not in
the spreadsheet, once you start filling in slugs.

- **Contest name:** DSA 301 - Homework
- **Contest slug:** `dsa-301-homework`
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
- `python resolve_slugs.py --course 301 --homework` uses this account's own
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
| HW-D01-1 | Sum a vector via for_each capturing an accumulator by reference | sum-of-vector-using-for-each | code |
| HW-D01-2 | Store three lambdas in vector<function<int(int)>> and apply each | store-and-apply-lambdas-using-function | code |
| HW-D01-3 | Write a lambda capturing a threshold by value to filter a vector | filter-a-vector-capturing-threshold-by-value | code |

### LEC-2 - Lambdas II — uses & tricks

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D02-1 | Print unordered_map entries sorted by count using a lambda | homework-print-unordered-map-entries-sorted-by-count-using-a-lambda | code |
| HW-D02-2 | Sort strings by length then lexicographically with one lambda | homework-sort-strings-by-length-then-lexicographically-with-one-lambda | code |
| HW-D02-3 | Write a function that returns a lambda multiplying by a captured factor | homework-write-a-function-that-returns-a-lambda-multiplying-by-a-captured-factor | code |

### LEC-3 - STL Remastered I — containers

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D03-1 | Compute a fixed-size sliding-window maximum using a deque | homework-compute-a-fixed-size-sliding-window-maximum-using-a-deque | code |
| HW-D03-2 | Maintain a sorted stream with a multiset and query the smallest | homework-maintain-a-sorted-stream-with-a-multiset-and-query-the-smallest | code |
| HW-D03-3 | Group anagrams together using map<string, vector<string>> |  | code |

### LEC-4 - STL Remastered II — algorithms

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D04-1 | Merge k sorted vectors into one using a min-heap | homework-merge-k-sorted-vectors-into-one-using-a-min-heap | code |
| HW-D04-2 | Generate all permutations of a string with next_permutation | homework-generate-all-permutations-of-a-string-with-next-permutation | code |
| HW-D04-3 | Answer range-sum queries using prefix sums (partial_sum) | homework-answer-range-sum-queries-using-prefix-sums-partial-sum | code |

### LEC-5 - DSA Basics Quick Revision

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D05-1 | Fibonacci with memoization | homework-fibonacci-with-memoization | code |
| HW-D05-2 | Detect a cycle in a linked list (Floyd's algorithm) | homework-detect-a-cycle-in-a-linked-list-floyds-algorithm | code |
| HW-D05-3 | Find the middle node of a linked list in one pass | homework-find-the-middle-node-of-a-linked-list-in-one-pass | code |


## Week 2

### LEC-6 - Hashmaps Fundamentals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D06-1 | LC387 First Unique Character in a String | homework-lc387-first-unique-character-in-a-string | code |
| HW-D06-2 | LC242 Valid Anagram | homework-lc242-valid-anagram | code |
| HW-D06-3 | LC219 Contains Duplicate II | homework-lc219-contains-duplicate-ii | code |

### LEC-7 - Hashmaps - Subarrays & Patterns

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D07-1 | LC974 Subarray Sums Divisible by K | homework-lc974-subarray-sums-divisible-by-k | code |
| HW-D07-2 | LC128 Longest Consecutive Sequence | homework-lc128-longest-consecutive-sequence | code |
| HW-D07-3 | Largest subarray with 0 sum (GfG) | homework-largest-subarray-with-0-sum-gfg | code |

### LEC-8 - Heaps / Priority Queue Fundamentals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D08-1 | LC703 Kth Largest Element in a Stream | homework-lc703-kth-largest-element-in-a-stream | code |
| HW-D08-2 | LC973 K Closest Points to Origin | homework-lc973-k-closest-points-to-origin | code |
| HW-D08-3 | Minimum cost of ropes (GfG) | homework-minimum-cost-of-ropes-gfg | code |

### LEC-9 - Advanced Heaps

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D09-1 | LC378 Kth Smallest Element in a Sorted Matrix | homework-lc378-kth-smallest-element-in-a-sorted-matrix | code |
| HW-D09-2 | LC692 Top K Frequent Words | homework-lc692-top-k-frequent-words | code |
| HW-D09-3 | LC451 Sort Characters By Frequency | homework-lc451-sort-characters-by-frequency | code |

### LEC-10 - Hashmaps & Heaps Combined

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D10-1 | LC621 Task Scheduler | homework-lc621-task-scheduler | code |
| HW-D10-2 | LC146 LRU Cache | homework-lc146-lru-cache | code |
| HW-D10-3 | LC432 All O one Data Structure | homework-lc432-all-o-one-data-structure | code |


## Week 3

### LEC-11 - Trees & DFS traversals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D11-1 | LC589 N-ary Tree Preorder Traversal | homework-lc589-n-ary-tree-preorder-traversal | code |
| HW-D11-2 | Count the total number of nodes recursively | homework-count-the-total-number-of-nodes-recursively | code |
| HW-D11-3 | Print all leaf nodes from left to right | homework-print-all-leaf-nodes-from-left-to-right | code |

### LEC-12 - Iterative traversal & BFS

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D12-1 | LC103 Binary Tree Zigzag Level Order Traversal | homework-lc103-binary-tree-zigzag-level-order-traversal | code |
| HW-D12-2 | LC107 Binary Tree Level Order Traversal II | homework-lc107-binary-tree-level-order-traversal-ii | code |
| HW-D12-3 | LC637 Average of Levels in Binary Tree | homework-lc637-average-of-levels-in-binary-tree | code |

### LEC-13 - Height, Depth & Diameter

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D13-1 | LC559 Maximum Depth of N-ary Tree | homework-lc559-maximum-depth-of-n-ary-tree | code |
| HW-D13-2 | Count the number of nodes at maximum depth | homework-count-the-number-of-nodes-at-maximum-depth | code |
| HW-D13-3 | Check whether two trees have equal height | homework-check-whether-two-trees-have-equal-height | code |

### LEC-14 - Balanced check & views

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D14-1 | LC100 Same Tree | homework-lc100-same-tree | code |
| HW-D14-2 | LC965 Univalued Binary Tree | homework-lc965-univalued-binary-tree | code |
| HW-D14-3 | LC872 Leaf-Similar Trees | homework-lc872-leaf-similar-trees | code |

### LEC-15 - Advanced Traversals & Views

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D15-1 | Morris inorder traversal (O(1) space) (GfG) | homework-morris-inorder-traversal-o1-space-gfg | code |
| HW-D15-2 | Bottom view of a binary tree (GfG) | homework-bottom-view-of-a-binary-tree-gfg | code |
| HW-D15-3 | Diagonal traversal of a binary tree (GfG) | homework-diagonal-traversal-of-a-binary-tree-gfg | code |


## Week 4

### LEC-16 - Invert & Symmetric

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D16-1 | LC951 Flip Equivalent Binary Trees | homework-lc951-flip-equivalent-binary-trees | code |
| HW-D16-2 | Check if one tree is the mirror of another (GfG) | homework-check-if-one-tree-is-the-mirror-of-another-gfg | code |
| HW-D16-3 | Convert a tree to its mirror in place (GfG) | homework-convert-a-tree-to-its-mirror-in-place-gfg | code |

### LEC-17 - Path Sum family

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D17-1 | LC437 Path Sum III | homework-lc437-path-sum-iii | code |
| HW-D17-2 | LC129 Sum Root to Leaf Numbers | homework-lc129-sum-root-to-leaf-numbers | code |
| HW-D17-3 | LC988 Smallest String Starting From Leaf | homework-lc988-smallest-string-starting-from-leaf | code |

### LEC-18 - Lowest Common Ancestor

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D18-1 | LC1650 Lowest Common Ancestor III | homework-lc1650-lowest-common-ancestor-iii | code |
| HW-D18-2 | LC1123 Lowest Common Ancestor of Deepest Leaves | homework-lc1123-lowest-common-ancestor-of-deepest-leaves | code |
| HW-D18-3 | Kth ancestor of a node in a tree (GfG) | homework-kth-ancestor-of-a-node-in-a-tree-gfg | code |

### LEC-19 - Construct & Flatten

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D19-1 | LC889 Construct Binary Tree from Preorder and Postorder | homework-lc889-construct-binary-tree-from-preorder-and-postorder | code |
| HW-D19-2 | LC1008 Construct BST from Preorder Traversal | homework-lc1008-construct-bst-from-preorder-traversal | code |
| HW-D19-3 | LC426 Convert BST to Sorted Doubly Linked List | homework-lc426-convert-bst-to-sorted-doubly-linked-list | code |

### LEC-20 - Serialize & Tree Utilities

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D20-1 | LC129 Sum Root to Leaf Numbers | homework-lc129-sum-root-to-leaf-numbers | code |
| HW-D20-2 | LC662 Maximum Width of Binary Tree | homework-lc662-maximum-width-of-binary-tree | code |
| HW-D20-3 | LC116 Populating Next Right Pointers in Each Node | homework-lc116-populating-next-right-pointers-in-each-node | code |


## Week 5

### LEC-21 - Search & Insert

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D21-1 | Iterative BST insert (GfG) | homework-iterative-bst-insert | code |
| HW-D21-2 | Search keys within a range in a BST (GfG) | homework-search-keys-within-a-range-in-a-bst | code |
| HW-D21-3 | Count BST nodes lying in a given range (GfG) | homework-count-bst-nodes-lying-in-a-given-range | code |

### LEC-22 - Validate & Min Diff

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D22-1 | LC99 Recover Binary Search Tree | homework-recover-binary-search-tree | code |
| HW-D22-2 | LC783 Minimum Distance Between BST Nodes | homework-minimum-distance-between-bst-nodes | code |
| HW-D22-3 | LC255 Verify Preorder Sequence in BST | homework-verify-preorder-sequence-in-bst | code |

### LEC-23 - Delete & Kth smallest

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D23-1 | LC669 Trim a Binary Search Tree | homework-trim-a-binary-search-tree | code |
| HW-D23-2 | LC285 Inorder Successor in BST | homework-inorder-successor-in-bst | code |
| HW-D23-3 | Inorder predecessor in a BST (GfG) | homework-inorder-predecessor-in-a-bst | code |

### LEC-24 - LCA, Build & Iterator

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D24-1 | LC109 Convert Sorted List to Binary Search Tree | homework-convert-sorted-list-to-binary-search-tree | code |
| HW-D24-2 | LC653 Two Sum IV - Input is a BST | classwork-two-sum-iv-input-is-a-bst | code |
| HW-D24-3 | LC938 Range Sum of BST | homework-range-sum-of-bst | code |

### LEC-25 - BST Advanced

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D25-1 | LC538 Convert BST to Greater Tree | homework-convert-bst-to-greater-tree | code |
| HW-D25-2 | LC1382 Balance a Binary Search Tree | homework-balance-a-binary-search-tree | code |
| HW-D25-3 | LC333 Largest BST Subtree | homework-largest-bst-subtree | code |


## Week 6

### LEC-26 - Greedy choice & intervals

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D26-1 | LC452 Minimum Number of Arrows to Burst Balloons | homework-minimum-number-of-arrows-to-burst-balloons | code |
| HW-D26-2 | LC646 Maximum Length of Pair Chain | homework-maximum-length-of-pair-chain | code |
| HW-D26-3 | Maximize meetings attended in one room (GfG) | homework-maximize-meetings-attended-in-one-room | code |

### LEC-27 - Merge intervals & platforms

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D27-1 | LC986 Interval List Intersections | homework-interval-list-intersections | code |
| HW-D27-2 | LC1094 Car Pooling | homework-car-pooling | code |
| HW-D27-3 | Maximum number of overlapping intervals (GfG) | homework-maximum-number-of-overlapping-intervals | code |

### LEC-28 - Knapsack & job sequencing

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D28-1 | LC455 Assign Cookies | homework-assign-cookies | code |
| HW-D28-2 | Huffman Encoding (GfG) | homework-huffman-encoding | code |
| HW-D28-3 | Minimum number of coins (GfG) | homework-minimum-number-of-coins | code |

### LEC-29 - Jump family & failure cases

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D29-1 | LC45 Jump Game II | homework-jump-game-ii | code |
| HW-D29-2 | LC763 Partition Labels | homework-partition-labels | code |
| HW-D29-3 | Write-up: a coin system where greedy fails (counterexample) | homework-write-up-a-coin-system-where-greedy-fails-counterexample | code |

### LEC-30 - Greedy — More Patterns

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D30-1 | Rearrange characters so that none are adjacent (GfG) | homework-rearrange-characters-so-that-none-are-adjacent | code |
| HW-D30-2 | LC1353 Maximum Number of Events That Can Be Attended | homework-lc1353-maximum-number-of-events-that-can-be-attended-1 | code |
| HW-D30-3 | LC860 Lemonade Change | homework-lc860-lemonade-change-1 | code |


## Week 7

### LEC-31 - DP intro & 1D

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D31-1 | LC746 Min Cost Climbing Stairs | homework-lc746-min-cost-climbing-stairs | code |
| HW-D31-2 | LC213 House Robber II | homework-lc213-house-robber-ii-1 | code |
| HW-D31-3 | LC91 Decode Ways | classwork-lc91-decode-ways | code |

### LEC-32 - Coin change family

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D32-1 | LC377 Combination Sum IV |  | code |
| HW-D32-2 | LC279 Perfect Squares |  | code |
| HW-D32-3 | Number of ways to make change (GfG) | homework-number-of-ways-to-make-change-gfg | code |

### LEC-33 - LIS / LCS lite

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D33-1 | LC673 Number of Longest Increasing Subsequence | homework-lc673-number-of-longest-increasing-subsequence | code |
| HW-D33-2 | LC1035 Uncrossed Lines | homework-lc1035-uncrossed-lines | code |
| HW-D33-3 | Longest common substring (GfG) | homework-longest-common-substring-gfg | code |

### LEC-34 - Grid DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D34-1 | LC120 Triangle |  | code |
| HW-D34-2 | LC931 Minimum Falling Path Sum | homework-lc931-minimum-falling-path-sum | code |
| HW-D34-3 | LC221 Maximal Square | homework-lc221-maximal-square | code |

### LEC-35 - Subsequence DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D35-1 | Count of subsets with a given sum (GfG) | homework-count-of-subsets-with-a-given-sum-gfg | code |
| HW-D35-2 | Maximum sum of non-adjacent elements (GfG) | homework-maximum-sum-of-non-adjacent-elements-gfg | code |
| HW-D35-3 | LC740 Delete and Earn | homework-lc740-delete-and-earn | code |


## Week 8

### LEC-36 - 0/1 Knapsack

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D36-1 | Count subsets with a given difference (GfG) | homework-count-subsets-with-a-given-difference-gfg | code |
| HW-D36-2 | LC1049 Last Stone Weight II | homework-lc1049-last-stone-weight-ii | code |
| HW-D36-3 | Minimum subset-sum difference (GfG) | homework-minimum-subset-sum-difference-gfg | code |

### LEC-37 - Unbounded knapsack

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D37-1 | LC518 Coin Change II | homework-lc518-coin-change-ii | code |
| HW-D37-2 | Maximum ribbon cut (GfG) | homework-maximum-ribbon-cut-gfg | code |
| HW-D37-3 | LC343 Integer Break | homework-lc343-integer-break | code |

### LEC-38 - Edit distance

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D38-1 | LC97 Interleaving String | homework-lc97-interleaving-string | code |
| HW-D38-2 | LC115 Distinct Subsequences | homework-lc115-distinct-subsequences | code |
| HW-D38-3 | LC161 One Edit Distance | homework-lc161-one-edit-distance | code |

### LEC-39 - LCS variants / Partition DP intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D39-1 | LC5 Longest Palindromic Substring | homework-lc5-longest-palindromic-substring | code |
| HW-D39-2 | LC647 Palindromic Substrings | homework-lc647-palindromic-substrings | code |
| HW-D39-3 | LC1312 Minimum Insertion Steps to Make a String Palindrome | homework-lc1312-minimum-insertion-steps-to-make-a-string-palindrome | code |

### LEC-40 - Partition / Interval DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D40-1 | Boolean Parenthesization (GfG) | homework-boolean-parenthesization-gfg | code |
| HW-D40-2 | LC1547 Minimum Cost to Cut a Stick | homework-lc1547-minimum-cost-to-cut-a-stick | code |
| HW-D40-3 | LC1043 Partition Array for Maximum Sum | homework-lc1043-partition-array-for-maximum-sum | code |


## Week 9

### LEC-41 - Representation & traversal

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D41-1 | LC733 Flood Fill | homework-lc733-flood-fill | code |
| HW-D41-2 | LC695 Max Area of Island | homework-lc695-max-area-of-island | code |
| HW-D41-3 | LC1971 Find if Path Exists in Graph | homework-lc1971-find-if-path-exists-in-graph | code |

### LEC-42 - Cycle & Bipartite

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D42-1 | Detect cycle in a directed graph (GfG) | homework-detect-cycle-in-a-directed-graph-gfg | code |
| HW-D42-2 | LC886 Possible Bipartition | homework-lc886-possible-bipartition | code |
| HW-D42-3 | LC684 Redundant Connection | homework-lc684-redundant-connection | code |

### LEC-43 - Topological sort

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D43-1 | LC269 Alien Dictionary | homework-lc269-alien-dictionary | code |
| HW-D43-2 | LC2115 Find All Possible Recipes from Given Supplies | homework-lc2115-find-all-possible-recipes-from-given-supplies | code |
| HW-D43-3 | LC1462 Course Schedule IV | homework-lc1462-course-schedule-iv | code |

### LEC-44 - Weighted paths & MST

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D44-1 | LC787 Cheapest Flights Within K Stops | homework-lc787-cheapest-flights-within-k-stops | code |
| HW-D44-2 | LC1584 Min Cost to Connect All Points (MST) | homework-lc1584-min-cost-to-connect-all-points-mst | code |
| HW-D44-3 | 0/1 BFS shortest path (GfG) | homework-01-bfs-shortest-path-gfg | code |

### LEC-45 - Graphs — Extra

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D45-1 | LC542 01 Matrix (multi-source BFS) | homework-lc542-01-matrix | code |
| HW-D45-2 | LC1091 Shortest Path in Binary Matrix | homework-lc1091-shortest-path-in-binary-matrix | code |
| HW-D45-3 | LC1192 Critical Connections in a Network (bridges, preview) | homework-lc1192-critical-connections-in-a-network | code |


## Week 10

### LEC-46 - Tree DP

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D46-1 | LC968 Binary Tree Cameras | homework-lc968-binary-tree-cameras | code |
| HW-D46-2 | LC687 Longest Univalue Path | homework-lc687-longest-univalue-path | code |
| HW-D46-3 | Maximum sum of non-adjacent nodes in a tree (GfG) | homework-maximum-sum-of-non-adjacent-nodes-in-a-tree-gfg | code |

### LEC-47 - Backtracking foundations

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D47-1 | LC90 Subsets II | homework-lc90-subsets-ii | code |
| HW-D47-2 | LC39 Combination Sum | homework-lc39-combination-sum | code |
| HW-D47-3 | LC131 Palindrome Partitioning | homework-lc131-palindrome-partitioning | code |

### LEC-48 - Backtracking on grids & constraints

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D48-1 | LC37 Sudoku Solver | homework-lc37-sudoku-solver | code |
| HW-D48-2 | LC212 Word Search II | homework-lc212-word-search-ii | code |
| HW-D48-3 | LC93 Restore IP Addresses | homework-lc93-restore-ip-addresses | code |

### LEC-49 - Two pointers & sliding window

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D49-1 | LC76 Minimum Window Substring | homework-lc76-minimum-window-substring | code |
| HW-D49-2 | LC424 Longest Repeating Character Replacement | homework-lc424-longest-repeating-character-replacement | code |
| HW-D49-3 | LC11 Container With Most Water | homework-lc11-container-with-most-water | code |

### LEC-50 - Mixed patterns capstone

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D50-1 | LC207 Course Schedule (graph) end to end | homework-lc207-course-schedule-graph-end-to-end | code |
| HW-D50-2 | LC236 Lowest Common Ancestor (tree) end to end | homework-lc236-lowest-common-ancestor-of-a-binary-tree-tree-end-to-end | code |
| HW-D50-3 | LC322 Coin Change (DP) end to end | homework-lc322-coin-change-dp-end-to-end | code |

