#!/usr/bin/env python3
"""
problem_links.py -- the original-source link for each challenge.

Most of these problems are somebody else's: an `LC<n>` in the title means
LeetCode problem <n>, and a `(GfG)` suffix means a GeeksforGeeks problem. This
module maps a challenge title to that source's URL, and make_md.py appends the
link to the end of the problem statement.

Two tables, both fixed lists rather than guesses:

- LEETCODE maps a problem number to its slug and official title. Slugs cannot be
  derived from our titles -- ours are sometimes shortened ("LC105 Construct
  Binary Tree from Preorder and Inorder" is really "... and Inorder Traversal").
  Every entry here was read from LeetCode's own problem list at
  https://leetcode.com/api/problems/all/, so the slug is the real one.

- GFG maps our full title to a URL. GeeksforGeeks practice slugs carry arbitrary
  numeric suffixes -- `minimum-platforms-1587115620`, `rod-cutting0840` -- so
  these cannot be derived either. They came from their practice search API,
  https://practiceapi.geeksforgeeks.org/api/v1/problems/search/?query=<terms>.
  Three problems have no practice equivalent and point at the article instead.

Neither table is fetched at generation time. They are checked in so make_md.py
runs offline, and so a link never silently changes under you.

link_for(title) returns (label, url) or None. It RAISES on a title that looks
like it has a source but has no entry -- a new `LC999` problem is a missing
mapping, not a problem without a link, and failing loudly is how a typo in a
problem number gets caught.
"""

import re

LEETCODE_URL = "https://leetcode.com/problems/%s/"

# number: (slug, official LeetCode title, premium-only)
LEETCODE = {
    1    : ("two-sum",                                                 "Two Sum",                                                 False),
    3    : ("longest-substring-without-repeating-characters",          "Longest Substring Without Repeating Characters",          False),
    5    : ("longest-palindromic-substring",                           "Longest Palindromic Substring",                           False),
    11   : ("container-with-most-water",                               "Container With Most Water",                               False),
    15   : ("3sum",                                                    "3Sum",                                                    False),
    22   : ("generate-parentheses",                                    "Generate Parentheses",                                    False),
    23   : ("merge-k-sorted-lists",                                    "Merge k Sorted Lists",                                    False),
    37   : ("sudoku-solver",                                           "Sudoku Solver",                                           False),
    39   : ("combination-sum",                                         "Combination Sum",                                         False),
    45   : ("jump-game-ii",                                            "Jump Game II",                                            False),
    46   : ("permutations",                                            "Permutations",                                            False),
    49   : ("group-anagrams",                                          "Group Anagrams",                                          False),
    51   : ("n-queens",                                                "N-Queens",                                                False),
    55   : ("jump-game",                                               "Jump Game",                                               False),
    56   : ("merge-intervals",                                         "Merge Intervals",                                         False),
    57   : ("insert-interval",                                         "Insert Interval",                                         False),
    62   : ("unique-paths",                                            "Unique Paths",                                            False),
    63   : ("unique-paths-ii",                                         "Unique Paths II",                                         False),
    64   : ("minimum-path-sum",                                        "Minimum Path Sum",                                        False),
    70   : ("climbing-stairs",                                         "Climbing Stairs",                                         False),
    72   : ("edit-distance",                                           "Edit Distance",                                           False),
    76   : ("minimum-window-substring",                                "Minimum Window Substring",                                False),
    77   : ("combinations",                                            "Combinations",                                            False),
    78   : ("subsets",                                                 "Subsets",                                                 False),
    79   : ("word-search",                                             "Word Search",                                             False),
    90   : ("subsets-ii",                                              "Subsets II",                                              False),
    91   : ("decode-ways",                                             "Decode Ways",                                             False),
    93   : ("restore-ip-addresses",                                    "Restore IP Addresses",                                    False),
    94   : ("binary-tree-inorder-traversal",                           "Binary Tree Inorder Traversal",                           False),
    97   : ("interleaving-string",                                     "Interleaving String",                                     False),
    98   : ("validate-binary-search-tree",                             "Validate Binary Search Tree",                             False),
    99   : ("recover-binary-search-tree",                              "Recover Binary Search Tree",                              False),
    102  : ("binary-tree-level-order-traversal",                       "Binary Tree Level Order Traversal",                       False),
    103  : ("binary-tree-zigzag-level-order-traversal",                "Binary Tree Zigzag Level Order Traversal",                False),
    104  : ("maximum-depth-of-binary-tree",                            "Maximum Depth of Binary Tree",                            False),
    105  : ("construct-binary-tree-from-preorder-and-inorder-traversal", "Construct Binary Tree from Preorder and Inorder Traversal", False),
    106  : ("construct-binary-tree-from-inorder-and-postorder-traversal", "Construct Binary Tree from Inorder and Postorder Traversal", False),
    107  : ("binary-tree-level-order-traversal-ii",                    "Binary Tree Level Order Traversal II",                    False),
    108  : ("convert-sorted-array-to-binary-search-tree",              "Convert Sorted Array to Binary Search Tree",              False),
    109  : ("convert-sorted-list-to-binary-search-tree",               "Convert Sorted List to Binary Search Tree",               False),
    110  : ("balanced-binary-tree",                                    "Balanced Binary Tree",                                    False),
    111  : ("minimum-depth-of-binary-tree",                            "Minimum Depth of Binary Tree",                            False),
    112  : ("path-sum",                                                "Path Sum",                                                False),
    113  : ("path-sum-ii",                                             "Path Sum II",                                             False),
    114  : ("flatten-binary-tree-to-linked-list",                      "Flatten Binary Tree to Linked List",                      False),
    115  : ("distinct-subsequences",                                   "Distinct Subsequences",                                   False),
    120  : ("triangle",                                                "Triangle",                                                False),
    128  : ("longest-consecutive-sequence",                            "Longest Consecutive Sequence",                            False),
    131  : ("palindrome-partitioning",                                 "Palindrome Partitioning",                                 False),
    132  : ("palindrome-partitioning-ii",                              "Palindrome Partitioning II",                              False),
    133  : ("clone-graph",                                             "Clone Graph",                                             False),
    134  : ("gas-station",                                             "Gas Station",                                             False),
    135  : ("candy",                                                   "Candy",                                                   False),
    136  : ("single-number",                                           "Single Number",                                           False),
    144  : ("binary-tree-preorder-traversal",                          "Binary Tree Preorder Traversal",                          False),
    146  : ("lru-cache",                                                "LRU Cache",                                               False),
    145  : ("binary-tree-postorder-traversal",                         "Binary Tree Postorder Traversal",                         False),
    161  : ("one-edit-distance",                                       "One Edit Distance",                                       True),
    198  : ("house-robber",                                            "House Robber",                                            False),
    200  : ("number-of-islands",                                       "Number of Islands",                                       False),
    207  : ("course-schedule",                                         "Course Schedule",                                         False),
    209  : ("minimum-size-subarray-sum",                               "Minimum Size Subarray Sum",                               False),
    210  : ("course-schedule-ii",                                      "Course Schedule II",                                      False),
    212  : ("word-search-ii",                                          "Word Search II",                                          False),
    213  : ("house-robber-ii",                                         "House Robber II",                                         False),
    215  : ("kth-largest-element-in-an-array",                         "Kth Largest Element in an Array",                         False),
    217  : ("contains-duplicate",                                      "Contains Duplicate",                                      False),
    219  : ("contains-duplicate-ii",                                   "Contains Duplicate II",                                   False),
    221  : ("maximal-square",                                          "Maximal Square",                                          False),
    222  : ("count-complete-tree-nodes",                               "Count Complete Tree Nodes",                               False),
    226  : ("invert-binary-tree",                                      "Invert Binary Tree",                                      False),
    230  : ("kth-smallest-element-in-a-bst",                           "Kth Smallest Element in a BST",                           False),
    235  : ("lowest-common-ancestor-of-a-binary-search-tree",          "Lowest Common Ancestor of a Binary Search Tree",          False),
    236  : ("lowest-common-ancestor-of-a-binary-tree",                 "Lowest Common Ancestor of a Binary Tree",                 False),
    242  : ("valid-anagram",                                           "Valid Anagram",                                           False),
    255  : ("verify-preorder-sequence-in-binary-search-tree",          "Verify Preorder Sequence in Binary Search Tree",          True),
    269  : ("alien-dictionary",                                        "Alien Dictionary",                                        True),
    279  : ("perfect-squares",                                         "Perfect Squares",                                         False),
    285  : ("inorder-successor-in-bst",                                "Inorder Successor in BST",                                True),
    295  : ("find-median-from-data-stream",                            "Find Median from Data Stream",                            False),
    300  : ("longest-increasing-subsequence",                          "Longest Increasing Subsequence",                          False),
    312  : ("burst-balloons",                                          "Burst Balloons",                                          False),
    322  : ("coin-change",                                             "Coin Change",                                             False),
    333  : ("largest-bst-subtree",                                     "Largest BST Subtree",                                     True),
    337  : ("house-robber-iii",                                        "House Robber III",                                        False),
    343  : ("integer-break",                                           "Integer Break",                                           False),
    347  : ("top-k-frequent-elements",                                 "Top K Frequent Elements",                                 False),
    355  : ("design-twitter",                                          "Design Twitter",                                          False),
    377  : ("combination-sum-iv",                                      "Combination Sum IV",                                      False),
    378  : ("kth-smallest-element-in-a-sorted-matrix",                 "Kth Smallest Element in a Sorted Matrix",                 False),
    387  : ("first-unique-character-in-a-string",                      "First Unique Character in a String",                      False),
    416  : ("partition-equal-subset-sum",                              "Partition Equal Subset Sum",                              False),
    424  : ("longest-repeating-character-replacement",                 "Longest Repeating Character Replacement",                 False),
    432  : ("all-oone-data-structure",                                  "All O`one Data Structure",                                False),
    435  : ("non-overlapping-intervals",                               "Non-overlapping Intervals",                               False),
    437  : ("path-sum-iii",                                            "Path Sum III",                                            False),
    450  : ("delete-node-in-a-bst",                                    "Delete Node in a BST",                                    False),
    451  : ("sort-characters-by-frequency",                            "Sort Characters By Frequency",                            False),
    452  : ("minimum-number-of-arrows-to-burst-balloons",              "Minimum Number of Arrows to Burst Balloons",              False),
    455  : ("assign-cookies",                                          "Assign Cookies",                                          False),
    494  : ("target-sum",                                              "Target Sum",                                              False),
    501  : ("find-mode-in-binary-search-tree",                         "Find Mode in Binary Search Tree",                         False),
    506  : ("relative-ranks",                                          "Relative Ranks",                                          False),
    509  : ("fibonacci-number",                                        "Fibonacci Number",                                        False),
    516  : ("longest-palindromic-subsequence",                         "Longest Palindromic Subsequence",                         False),
    518  : ("coin-change-ii",                                          "Coin Change II",                                          False),
    530  : ("minimum-absolute-difference-in-bst",                      "Minimum Absolute Difference in BST",                      False),
    538  : ("convert-bst-to-greater-tree",                             "Convert BST to Greater Tree",                             False),
    542  : ("01-matrix",                                               "01 Matrix",                                               False),
    543  : ("diameter-of-binary-tree",                                 "Diameter of Binary Tree",                                 False),
    547  : ("number-of-provinces",                                     "Number of Provinces",                                     False),
    560  : ("subarray-sum-equals-k",                                   "Subarray Sum Equals K",                                   False),
    583  : ("delete-operation-for-two-strings",                        "Delete Operation for Two Strings",                        False),
    621  : ("task-scheduler",                                          "Task Scheduler",                                          False),
    637  : ("average-of-levels-in-binary-tree",                        "Average of Levels in Binary Tree",                        False),
    646  : ("maximum-length-of-pair-chain",                            "Maximum Length of Pair Chain",                            False),
    647  : ("palindromic-substrings",                                  "Palindromic Substrings",                                  False),
    662  : ("maximum-width-of-binary-tree",                            "Maximum Width of Binary Tree",                            False),
    673  : ("number-of-longest-increasing-subsequence",                "Number of Longest Increasing Subsequence",                False),
    684  : ("redundant-connection",                                    "Redundant Connection",                                    False),
    687  : ("longest-univalue-path",                                   "Longest Univalue Path",                                   False),
    692  : ("top-k-frequent-words",                                    "Top K Frequent Words",                                    False),
    695  : ("max-area-of-island",                                      "Max Area of Island",                                      False),
    700  : ("search-in-a-binary-search-tree",                          "Search in a Binary Search Tree",                          False),
    701  : ("insert-into-a-binary-search-tree",                        "Insert into a Binary Search Tree",                        False),
    703  : ("kth-largest-element-in-a-stream",                         "Kth Largest Element in a Stream",                         False),
    712  : ("minimum-ascii-delete-sum-for-two-strings",                "Minimum ASCII Delete Sum for Two Strings",                False),
    733  : ("flood-fill",                                              "Flood Fill",                                              False),
    740  : ("delete-and-earn",                                         "Delete and Earn",                                         False),
    743  : ("network-delay-time",                                      "Network Delay Time",                                      False),
    746  : ("min-cost-climbing-stairs",                                "Min Cost Climbing Stairs",                                False),
    763  : ("partition-labels",                                        "Partition Labels",                                        False),
    767  : ("reorganize-string",                                       "Reorganize String",                                       False),
    783  : ("minimum-distance-between-bst-nodes",                      "Minimum Distance Between BST Nodes",                      False),
    785  : ("is-graph-bipartite",                                      "Is Graph Bipartite?",                                     False),
    787  : ("cheapest-flights-within-k-stops",                         "Cheapest Flights Within K Stops",                         False),
    860  : ("lemonade-change",                                         "Lemonade Change",                                         False),
    863  : ("all-nodes-distance-k-in-binary-tree",                     "All Nodes Distance K in Binary Tree",                     False),
    872  : ("leaf-similar-trees",                                      "Leaf-Similar Trees",                                      False),
    886  : ("possible-bipartition",                                    "Possible Bipartition",                                    False),
    889  : ("construct-binary-tree-from-preorder-and-postorder-traversal", "Construct Binary Tree from Preorder and Postorder Traversal", False),
    895  : ("maximum-frequency-stack",                                 "Maximum Frequency Stack",                                 False),
    931  : ("minimum-falling-path-sum",                                "Minimum Falling Path Sum",                                False),
    951  : ("flip-equivalent-binary-trees",                            "Flip Equivalent Binary Trees",                            False),
    965  : ("univalued-binary-tree",                                   "Univalued Binary Tree",                                   False),
    968  : ("binary-tree-cameras",                                     "Binary Tree Cameras",                                     False),
    973  : ("k-closest-points-to-origin",                              "K Closest Points to Origin",                              False),
    974  : ("subarray-sums-divisible-by-k",                            "Subarray Sums Divisible by K",                            False),
    986  : ("interval-list-intersections",                             "Interval List Intersections",                             False),
    987  : ("vertical-order-traversal-of-a-binary-tree",               "Vertical Order Traversal of a Binary Tree",               False),
    988  : ("smallest-string-starting-from-leaf",                      "Smallest String Starting From Leaf",                      False),
    994  : ("rotting-oranges",                                         "Rotting Oranges",                                         False),
    1008 : ("construct-binary-search-tree-from-preorder-traversal",    "Construct Binary Search Tree from Preorder Traversal",    False),
    1035 : ("uncrossed-lines",                                         "Uncrossed Lines",                                         False),
    1043 : ("partition-array-for-maximum-sum",                         "Partition Array for Maximum Sum",                         False),
    1046 : ("last-stone-weight",                                       "Last Stone Weight",                                       False),
    1049 : ("last-stone-weight-ii",                                    "Last Stone Weight II",                                    False),
    1091 : ("shortest-path-in-binary-matrix",                          "Shortest Path in Binary Matrix",                          False),
    1092 : ("shortest-common-supersequence",                           "Shortest Common Supersequence",                           False),
    1094 : ("car-pooling",                                             "Car Pooling",                                             False),
    1123 : ("lowest-common-ancestor-of-deepest-leaves",                "Lowest Common Ancestor of Deepest Leaves",                False),
    1143 : ("longest-common-subsequence",                              "Longest Common Subsequence",                              False),
    1192 : ("critical-connections-in-a-network",                       "Critical Connections in a Network",                       False),
    1207 : ("unique-number-of-occurrences",                            "Unique Number of Occurrences",                            False),
    1312 : ("minimum-insertion-steps-to-make-a-string-palindrome",     "Minimum Insertion Steps to Make a String Palindrome",     False),
    1337 : ("the-k-weakest-rows-in-a-matrix",                          "The K Weakest Rows in a Matrix",                          False),
    1353 : ("maximum-number-of-events-that-can-be-attended",           "Maximum Number of Events That Can Be Attended",           False),
    1382 : ("balance-a-binary-search-tree",                            "Balance a Binary Search Tree",                            False),
    1394 : ("find-lucky-integer-in-an-array",                          "Find Lucky Integer in an Array",                          False),
    1464 : ("maximum-product-of-two-elements-in-an-array",             "Maximum Product of Two Elements in an Array",             False),
    1462 : ("course-schedule-iv",                                      "Course Schedule IV",                                      False),
    1512 : ("number-of-good-pairs",                                    "Number of Good Pairs",                                    False),
    1547 : ("minimum-cost-to-cut-a-stick",                             "Minimum Cost to Cut a Stick",                             False),
    1584 : ("min-cost-to-connect-all-points",                          "Min Cost to Connect All Points",                          False),
    1631 : ("path-with-minimum-effort",                                "Path With Minimum Effort",                                False),
    1636 : ("sort-array-by-increasing-frequency",                      "Sort Array by Increasing Frequency",                      False),
    1971 : ("find-if-path-exists-in-graph",                            "Find if Path Exists in Graph",                            False),
    2115 : ("find-all-possible-recipes-from-given-supplies",           "Find All Possible Recipes from Given Supplies",           False),
}

GFG_URL = "https://www.geeksforgeeks.org/problems/%s/1"

# our full title: (practice slug, name) -- or (absolute article URL, name) for
# the three problems GeeksforGeeks has no practice equivalent for.
GFG = {
    "Classwork: 0/1 Knapsack (GfG)":
        ("0-1-knapsack-problem0945", "0 - 1 Knapsack Problem"),
    "Classwork: Bellman-Ford algorithm (GfG)":
        ("distance-from-the-source-bellman-ford-algorithm", "Bellman Ford"),
    "Classwork: Boundary traversal of a binary tree (GfG)":
        ("boundary-traversal-of-binary-tree", "Tree Boundary Traversal"),
    "Classwork: Detect cycle in an undirected graph (GfG)":
        ("detect-cycle-in-an-undirected-graph", "Undirected Graph Cycle"),
    "Classwork: Dijkstra's shortest path (GfG)":
        ("implementing-dijkstra-set-1-adjacency-matrix", "Dijkstra Algorithm"),
    "Classwork: Distance between two nodes via LCA (GfG)":
        ("min-distance-between-two-given-nodes-of-a-binary-tree",
         "Min Distance Between Two in Binary Tree"),
    "Classwork: Floyd-Warshall all-pairs shortest path (GfG)":
        ("implementing-floyd-warshall2042", "Floyd Warshall"),
    "Classwork: Fractional Knapsack (GfG)":
        ("fractional-knapsack-1587115620", "Fractional Knapsack"),
    "Classwork: Frequency of elements (GfG)":
        ("frequency-of-elements--111353", "Frequency of Elements"),
    "Classwork: Iterative BST search (GfG)":
        ("search-a-node-in-bst", "Search a node in BST"),
    "Classwork: Job Sequencing Problem (GfG)":
        ("job-sequencing-problem-1587115620", "Job Sequencing Problem"),
    "Classwork: Kahn's algorithm for topological sort (GfG)":
        ("topological-sort", "Topological Sort"),
    "Classwork: Kth largest element in a BST (GfG)":
        ("kth-largest-element-in-bst", "Kth Largest in BST"),
    "Classwork: Kth smallest element (GfG)":
        ("kth-smallest-element5635", "Kth Smallest"),
    "Classwork: Longest Increasing Subsequence in O(n log n) (GfG)":
        ("longest-increasing-subsequence-1587115620",
         "Longest Increasing Subsequence"),
    "Classwork: Matrix Chain Multiplication (GfG)":
        ("matrix-chain-multiplication0303", "Matrix Chain Multiplication"),
    "Classwork: Maximum number of activities selected (GfG)":
        ("activity-selection-1587115620", "Activity Selection"),
    "Classwork: Minimum number of platforms (GfG)":
        ("minimum-platforms-1587115620", "Minimum Platforms"),
    "Classwork: N meetings in one room (GfG)":
        ("maximum-meetings-in-one-room", "Maximum Meetings in One Room"),
    "Classwork: Rod Cutting (GfG)":
        ("rod-cutting0840", "Rod Cutting"),
    "Classwork: Subset Sum (GfG)":
        ("subset-sum-problem-1611555638", "Subset Sum Problem"),
    "Classwork: Top view of a binary tree (GfG)":
        ("top-view-of-binary-tree", "Top View of Binary Tree"),
    "Classwork: Topological Sort (GfG)":
        ("topological-sort", "Topological Sort"),
    "Classwork: Unbounded Knapsack (GfG)":
        ("knapsack-with-duplicate-items4201", "Knapsack with Duplicate Items"),

    "Homework: 0/1 BFS shortest path (GfG)":
        ("https://www.geeksforgeeks.org/0-1-bfs-shortest-path-binary-graph/",
         "0-1 BFS: shortest path in a binary weight graph"),
    "Homework: Boolean Parenthesization (GfG)":
        ("boolean-parenthesization5610", "Boolean Parenthesization"),
    "Homework: Bottom view of a binary tree (GfG)":
        ("bottom-view-of-binary-tree", "Bottom View of Binary Tree"),
    "Homework: Check if one tree is the mirror of another (GfG)":
        ("two-mirror-trees", "Two Mirror Trees"),
    "Homework: Convert a tree to its mirror in place (GfG)":
        ("mirror-tree", "Mirror Tree"),
    "Homework: Count BST nodes lying in a given range (GfG)":
        ("count-bst-nodes-that-lie-in-a-given-range", "Count BST Nodes in a Range"),
    "Homework: Count of subsets with a given sum (GfG)":
        ("perfect-sum-problem5633", "Count Subsets with Sum"),
    "Homework: Count subsets with a given difference (GfG)":
        ("partitions-with-given-difference", "Partitions with Given Difference"),
    "Homework: Detect cycle in a directed graph (GfG)":
        ("detect-cycle-in-a-directed-graph", "Directed Graph Cycle"),
    "Homework: Diagonal traversal of a binary tree (GfG)":
        ("diagonal-traversal-of-binary-tree", "Diagonal Tree Traversal"),
    "Homework: Huffman Encoding (GfG)":
        ("huffman-encoding3345", "Huffman Encoding"),
    "Homework: Inorder predecessor in a BST (GfG)":
        ("predecessor-and-successor", "Predecessor and Successor"),
    "Homework: Iterative BST insert (GfG)":
        ("insert-a-node-in-a-bst", "BST Insert"),
    "Homework: Largest subarray with 0 sum (GfG)":
        ("largest-subarray-with-0-sum", "Largest subarray with 0 sum"),
    "Homework: Longest common substring (GfG)":
        ("longest-common-substring1452", "Longest Common Substring"),
    "Homework: Maximize meetings attended in one room (GfG)":
        ("maximum-meetings-in-one-room", "Maximum Meetings in One Room"),
    "Homework: Maximum number of overlapping intervals (GfG)":
        ("intersecting-intervals", "Maximum number of overlapping Intervals"),
    "Homework: Maximum ribbon cut (GfG)":
        ("cutted-segments1642", "Maximize The Cut Segments"),
    "Homework: Maximum sum of non-adjacent elements (GfG)":
        ("stickler-theif-1587115621", "Stickler Thief"),
    "Homework: Maximum sum of non-adjacent nodes in a tree (GfG)":
        ("maximum-sum-of-non-adjacent-nodes", "Maximum Non-Adjacent Nodes Sum"),
    "Homework: Minimum cost of ropes (GfG)":
        ("minimum-cost-of-ropes-1587115620", "Min Cost to Connect Ropes"),
    "Homework: Minimum number of coins (GfG)":
        ("number-of-coins1824", "Coin Change (Minimum Coins)"),
    "Homework: Minimum subset-sum difference (GfG)":
        ("https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-"
         "that-the-difference-of-subset-sums-is-minimum/",
         "Minimum subset sum difference"),
    "Homework: Morris inorder traversal (O(1) space) (GfG)":
        ("inorder-traversal", "Inorder Traversal"),
    "Homework: Number of ways to make change (GfG)":
        ("coin-change2448", "Coin Change (Count Ways)"),
    "Homework: Rearrange characters so that none are adjacent (GfG)":
        ("https://www.geeksforgeeks.org/"
         "rearrange-characters-string-no-two-adjacent/",
         "Rearrange characters so that no two are adjacent"),
    "Homework: Search keys within a range in a BST (GfG)":
        ("print-bst-elements-in-given-range", "BST Keys in a Range"),
}


class MissingLink(Exception):
    """A title names a source we have no URL for."""


def link_for(title):
    """(label, url) for a title, or None when it names no external source.

    Raises MissingLink when the title clearly names a source -- an LC number or
    a `(GfG)` suffix -- that has no entry above. A new LC999 problem is a
    missing mapping, not a problem without a source, and failing loudly is how
    a mistyped problem number gets caught.
    """
    m = re.search(r"\bLC(\d+)\b", title)
    if m:
        n = int(m.group(1))
        if n not in LEETCODE:
            raise MissingLink("no LeetCode entry for LC%d (%s)" % (n, title))
        slug, official, paid = LEETCODE[n]
        label = "LeetCode %d - %s" % (n, official)
        if paid:
            label += " (LeetCode Premium)"
        return label, LEETCODE_URL % slug

    if "(GfG)" in title:
        if title not in GFG:
            raise MissingLink("no GeeksforGeeks entry for %s" % title)
        target, name = GFG[title]
        url = target if target.startswith("http") else GFG_URL % target
        return "GeeksforGeeks - %s" % name, url

    return None


# The statement is markdown, and this line must not begin with `**`: editor.py
# ends the Problem Statement field at the next line-initial `**`, so a bolded
# lead-in here would silently truncate the statement it is appended to.
NOTE = "You can also try this problem on: [%s](%s)."


def note_for(title):
    """The markdown line to append to a statement, or "" if there is no source."""
    got = link_for(title)
    return NOTE % got if got else ""


# make_md.py --link-only uses this instead, as the WHOLE statement. The
# challenge becomes a pointer: the problem lives at the far end of the link.
LINK_ONLY = "Solve this problem here: [%s](%s)"

# ...and these three go in the other statement boxes.
#
# THEY CANNOT BE EMPTY. Leaving them "" was the first attempt and HackerRank
# refused it: the edit form validates and saves as a unit, so three blank boxes
# rejected the whole submission -- the read-back showed even `problem_statement`
# unchanged, though it had text. Measured on challenge 592083 (LC200), which
# reported `FAILED verification` on all four fields and wrote nothing.
#
# So these are as close to empty as the form allows. They also do real work:
# with no input-format prose, the samples ARE the I/O contract, and these say so.
# Set any of them to "" to retry the empty-field experiment.
LINK_ONLY_INP = "Standard input, in the form shown by the sample cases below."
LINK_ONLY_OUT = "Standard output, in the form shown by the sample cases below."
LINK_ONLY_CONS = "As stated in the linked problem."


def link_only_for(title):
    """The whole statement for a link-only challenge, or "" if it has no source.

    An empty return means "this problem is ours, there is nowhere to send the
    student" -- make_md.py keeps the full write-up for those 16.
    """
    got = link_for(title)
    return LINK_ONLY % got if got else ""


def summarise(problems):
    """(leetcode, gfg, none) counts over a list of problem dicts."""
    lc = gfg = none = 0
    for p in problems:
        got = link_for(p["title"])
        if not got:
            none += 1
        elif "leetcode.com" in got[1]:
            lc += 1
        else:
            gfg += 1
    return lc, gfg, none


# --------------------------------------------------------------- verifying ---
# `python problem_links.py --verify` re-checks both tables against the live
# sites. Nothing else in this repo touches the network; this is the one place,
# and it is deliberately a separate mode you run on purpose.
#
# The two sites need different checks:
#
# - LeetCode publishes its whole problem list as JSON, so one request confirms
#   every number, slug and title at once.
# - GeeksforGeeks practice pages are a single-page app that answers HTTP 200 for
#   any slug, real or not, so a status code proves nothing. The `<title>` tag is
#   server-rendered though -- a real problem gives "Kth Smallest | Practice |
#   GeeksforGeeks", a dead slug gives the bare "Practice | GeeksforGeeks | ...".
#   That is what gets checked. Their articles do return a real 404, so for the
#   three article links the status code is enough.

LC_API = "https://leetcode.com/api/problems/all/"
UA = {"User-Agent": "Mozilla/5.0"}


def _get(url, timeout=45):
    import urllib.request
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as f:
        return f.status, f.read().decode("utf-8", "replace")


def verify():
    import json
    import time

    bad = 0

    print("checking %d LeetCode entries against %s" % (len(LEETCODE), LC_API))
    try:
        _, body = _get(LC_API)
        live = {}
        for p in json.loads(body)["stat_status_pairs"]:
            s = p["stat"]
            live[int(s["frontend_question_id"])] = (
                s["question__title_slug"], s["question__title"].strip(),
                bool(p.get("paid_only")))
    except Exception as ex:
        print("  could not read the problem list: %s" % ex)
        return 1

    for n in sorted(LEETCODE):
        ours, theirs = LEETCODE[n], live.get(n)
        if theirs is None:
            print("  LC%-5d gone from LeetCode's list" % n)
            bad += 1
        elif ours[0] != theirs[0]:
            print("  LC%-5d slug moved: %s -> %s" % (n, ours[0], theirs[0]))
            bad += 1
        elif ours[1] != theirs[1]:
            print("  LC%-5d renamed: %r -> %r" % (n, ours[1], theirs[1]))
            bad += 1
        elif ours[2] != theirs[2]:
            print("  LC%-5d premium flag is now %s" % (n, theirs[2]))
            bad += 1
    print("  %d checked, %d wrong" % (len(LEETCODE), bad))

    print()
    print("checking %d GeeksforGeeks entries, one request each" % len(GFG))
    dead_title = "Practice | GeeksforGeeks | A computer science portal for geeks"
    gbad = 0
    for title in sorted(GFG):
        target, name = GFG[title]
        _, url = link_for(title)
        try:
            status, body = _get(url)
        except Exception as ex:
            print("  %-58s unreachable: %s" % (name, ex))
            gbad += 1
            time.sleep(0.3)
            continue
        if target.startswith("http"):
            # an article: a real 404 means a real answer
            if status != 200:
                print("  %-58s HTTP %s" % (name, status))
                gbad += 1
        else:
            m = re.search(r"<title>(.*?)</title>", body, re.S)
            got = (m.group(1).strip() if m else "")
            if got == dead_title or not got:
                print("  %-58s no such problem (slug %s)" % (name, target))
                gbad += 1
            elif not got.lower().startswith(name.lower()):
                print("  %-58s page says %r" % (name, got))
                gbad += 1
        time.sleep(0.3)
    print("  %d checked, %d wrong" % (len(GFG), gbad))

    bad += gbad
    print()
    print("%d problem(s)." % bad if bad else "every link resolves.")
    return 1 if bad else 0


if __name__ == "__main__":
    import sys

    if "--verify" in sys.argv[1:]:
        sys.exit(verify())

    print("%d LeetCode problems (%d premium-only)"
          % (len(LEETCODE), sum(1 for v in LEETCODE.values() if v[2])))
    print("%d GeeksforGeeks problems (%d pointing at an article, no practice "
          "equivalent)"
          % (len(GFG), sum(1 for v in GFG.values() if v[0].startswith("http"))))
    print()
    print("  --verify re-checks every link against the live sites.")
    print()
    for t in sorted(GFG):
        print("  %-58s %s" % (t.split(": ", 1)[1], link_for(t)[1]))
