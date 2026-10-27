#!/usr/bin/env python3
"""
make_homework_missing_md.py -- generate DSA301_homework_missing.md.

Emits every homework problem from LEC-11 to LEC-40, in sheet order, deduped.
Reuses every homework dict already defined in make_md.py / dp_problems.py and
adds fresh dicts for the ~43 that were missing (the pen-and-paper Easy trace
exercises and the LC/GfG problems not yet authored). Sample outputs are
COMPUTED by the reference solutions, never typed by hand.

    python make_homework_missing_md.py
    python make_homework_missing_md.py --missing-only

Extends problem_links.LEETCODE / GFG at runtime so the shared emit() picks up
LC / GfG links for every new problem without touching problem_links.py.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import make_md
import dp_problems
import problem_links
from collections import deque

from make_md import (
    N, build, two, levels, inorder, preorder, postorder, serialize,
    fmt, fmt_bool, ints, rows, iter_nodes,
    depth, min_depth, diameter, balanced, leaves, invert,
    bst_find, in_list, is_bst, sorted_to_bst, kth_smallest, kth_largest,
    find_lca, TREE_IN, TREE_IN2, SEQ_OUT, NUM_OUT, BOOL_OUT, CONS,
    BST_IN, BST_CONS, SER_OUT, IV_IN, ARR_IN, IV_CASES, ARR_CASES,
    TREES, BSTS, with_key,
)


# ------------------------------------------------------- link table extensions
# LC entries needed by the homework rows below that are not already in
# problem_links.LEETCODE. Merged at runtime, so problem_links.py itself does
# not need editing.
_NEW_LEETCODE_HW = {
    100 : ("same-tree",                                       "Same Tree",                                       False),
    116 : ("populating-next-right-pointers-in-each-node",     "Populating Next Right Pointers in Each Node",     False),
    118 : ("pascals-triangle",                                "Pascal's Triangle",                               False),
    121 : ("best-time-to-buy-and-sell-stock",                 "Best Time to Buy and Sell Stock",                 False),
    125 : ("valid-palindrome",                                "Valid Palindrome",                                False),
    129 : ("sum-root-to-leaf-numbers",                        "Sum Root to Leaf Numbers",                        False),
    252 : ("meeting-rooms",                                   "Meeting Rooms",                                   True),
    257 : ("binary-tree-paths",                               "Binary Tree Paths",                               False),
    392 : ("is-subsequence",                                  "Is Subsequence",                                  False),
    404 : ("sum-of-left-leaves",                              "Sum of Left Leaves",                              False),
    426 : ("convert-binary-search-tree-to-sorted-doubly-linked-list",
           "Convert Binary Search Tree to Sorted Doubly Linked List",                                            True),
    559 : ("maximum-depth-of-n-ary-tree",                     "Maximum Depth of N-ary Tree",                     False),
    561 : ("array-partition",                                 "Array Partition",                                 False),
    589 : ("n-ary-tree-preorder-traversal",                   "N-ary Tree Preorder Traversal",                   False),
    617 : ("merge-two-binary-trees",                          "Merge Two Binary Trees",                          False),
    653 : ("two-sum-iv-input-is-a-bst",                       "Two Sum IV - Input is a BST",                     False),
    669 : ("trim-a-binary-search-tree",                       "Trim a Binary Search Tree",                       False),
    897 : ("increasing-order-search-tree",                    "Increasing Order Search Tree",                    False),
    938 : ("range-sum-of-bst",                                "Range Sum of BST",                                False),
    942 : ("di-string-match",                                 "DI String Match",                                 False),
    993 : ("cousins-in-binary-tree",                          "Cousins in Binary Tree",                          False),
    1137: ("n-th-tribonacci-number",                          "N-th Tribonacci Number",                          False),
    1650: ("lowest-common-ancestor-of-a-binary-tree-iii",     "Lowest Common Ancestor of a Binary Tree III",     True),
    1710: ("maximum-units-on-a-truck",                        "Maximum Units on a Truck",                        False),
}
for _num, _val in _NEW_LEETCODE_HW.items():
    problem_links.LEETCODE.setdefault(_num, _val)

_NEW_GFG_HW = {
    "Homework: Right view of a binary tree (GfG)":
        ("right-view-of-binary-tree", "Right View of Binary Tree"),
    "Homework: Kth ancestor of a node in a tree (GfG)":
        ("kth-ancestor-in-a-tree", "Kth Ancestor in a Tree"),
    "Homework: Find the floor value of a key in a BST (GfG)":
        ("floor-in-bst", "Floor in BST"),
    "Homework: Count ways to climb stairs with steps of 1, 2 or 3 (GfG)":
        ("count-ways-to-reach-the-nth-stair", "Count Ways to Reach the Nth Stair"),
    "Homework: Count ways to reach amount N using coins of 1 and 2 (GfG)":
        ("count-ways-to-reach-the-nth-stair", "Count Ways to Reach the Nth Stair"),
}
for _t, _v in _NEW_GFG_HW.items():
    problem_links.GFG.setdefault(_t, _v)


# ------------------------------------------------------------- solving helpers
def sum_all_nodes(root):
    return sum(n.v for n in iter_nodes(root))


def max_node_value(root):
    vs = [n.v for n in iter_nodes(root)]
    return max(vs) if vs else None


def count_leaves(root):
    return len(leaves(root))


def is_same_tree(a, b):
    if not a and not b: return True
    if not a or not b: return False
    return (a.v == b.v and is_same_tree(a.l, b.l)
            and is_same_tree(a.r, b.r))


def right_view(root):
    out, q = [], deque([root] if root else [])
    while q:
        n_items = len(q)
        for i in range(n_items):
            n = q.popleft()
            if i == n_items - 1:
                out.append(n.v)
            if n.l: q.append(n.l)
            if n.r: q.append(n.r)
    return out


def cousins(root, x, y):
    """Two values are cousins if they sit at the same depth but have
    different parents."""
    info = {}
    def go(n, par, d):
        if not n: return
        info[n.v] = (par, d)
        go(n.l, n.v, d + 1)
        go(n.r, n.v, d + 1)
    go(root, None, 0)
    if x not in info or y not in info:
        return False
    px, dx = info[x]
    py, dy = info[y]
    return dx == dy and px != py


def merge_trees(a, b):
    if not a and not b: return None
    if not a: return b
    if not b: return a
    n = N(a.v + b.v)
    n.l = merge_trees(a.l, b.l)
    n.r = merge_trees(a.r, b.r)
    return n


def binary_tree_paths(root):
    """Every root-to-leaf path, one per line, values joined by '->'."""
    out, cur = [], []
    def go(n):
        if not n: return
        cur.append(str(n.v))
        if not n.l and not n.r:
            out.append("->".join(cur))
        else:
            go(n.l); go(n.r)
        cur.pop()
    go(root)
    return out


def sum_root_to_leaf(root):
    """LC129: each root-to-leaf path concatenates its digits into a number."""
    total = [0]
    def go(n, run):
        if not n: return
        run = run * 10 + n.v
        if not n.l and not n.r:
            total[0] += run
        else:
            go(n.l, run); go(n.r, run)
    go(root, 0)
    return total[0]


def level_of_value(root, v):
    """1-indexed level of the first node holding v, or -1 if absent."""
    q = deque([(root, 1)] if root else [])
    while q:
        n, d = q.popleft()
        if n.v == v: return d
        if n.l: q.append((n.l, d + 1))
        if n.r: q.append((n.r, d + 1))
    return -1


def lca_binary_tree(root, p, q):
    """Standard LCA on the tree by value; returns the LCA's value, or -1."""
    r = find_lca(root, p, q)
    return r.v if r else -1


def kth_ancestor(root, node_val, k):
    """The value k levels above the given node, or -1 if it does not exist."""
    par = {}
    def link(n, p):
        if not n: return
        par[n.v] = p
        link(n.l, n)
        link(n.r, n)
    link(root, None)
    if node_val not in par:
        return -1
    cur = par[node_val]
    steps = 1
    while cur and steps < k:
        cur = par.get(cur.v)
        steps += 1
    if cur is None or steps < k:
        return -1
    return cur.v


def build_nary(rows_):
    """Parse our N-ary format:
       Line 1: n
       Line 2: n values in preorder position (first is root)
       Line 3 (present iff n >= 2): n-1 parent values, one per non-root node.
       Returns (root_value, children_map value -> list children in insertion
       order). Duplicate values are not supported in this format.
    """
    n = int(rows_[0])
    if n == 0:
        return None, {}
    vals = ints(rows_[1])
    root = vals[0]
    children = {v: [] for v in vals}
    if n >= 2:
        parents = ints(rows_[2])
        for child, par in zip(vals[1:], parents):
            children[par].append(child)
    return root, children


def nary_preorder(root, children):
    if root is None:
        return []
    out = []
    def go(v):
        out.append(v)
        for c in children.get(v, []):
            go(c)
    go(root)
    return out


def nary_depth(root, children):
    if root is None:
        return 0
    def go(v):
        cs = children.get(v, [])
        if not cs:
            return 1
        return 1 + max(go(c) for c in cs)
    return go(root)


def bst_from_sorted(xs):
    """LC108: balanced BST from sorted array; return its serialized form."""
    return serialize(sorted_to_bst(xs))


def from_pre_post(pre, post):
    """LC889: reconstruct a full binary tree from preorder + postorder."""
    pos = {v: i for i, v in enumerate(post)}
    it = [0]
    def go(lo, hi):
        if lo > hi: return None
        v = pre[it[0]]; it[0] += 1
        n = N(v)
        if lo == hi: return n
        m = pos[pre[it[0]]]
        n.l = go(lo, m)
        n.r = go(m + 1, hi - 1)
        return n
    return go(0, len(post) - 1)


def sum_left_leaves(root):
    total = [0]
    def go(n, is_left):
        if not n: return
        if is_left and not n.l and not n.r:
            total[0] += n.v
        go(n.l, True)
        go(n.r, False)
    go(root, False)
    return total[0]


def populating_next_right(root):
    """Print each level's values space-separated, then a `#` marker, ending in
    a `#`. Reproduces what a valid `next` chain would traverse level by level."""
    if not root:
        return "#"
    out = []
    for row in levels(root):
        out.extend(str(n.v) for n in row)
        out.append("#")
    return " ".join(out)


def bst_min_max(root):
    if not root:
        return None
    lo = hi = root.v
    n = root
    while n.l:
        n = n.l
        lo = n.v
    n = root
    while n.r:
        n = n.r
        hi = n.v
    return lo, hi


def increasing_order_bst(root):
    """LC897: rearrange the BST into a right-only chain whose values are in
    inorder. Output as a space-separated sequence."""
    return fmt(in_list(root))


def bst_floor(root, key):
    """Largest value <= key, or None."""
    res, n = None, root
    while n:
        if n.v == key:
            return n.v
        if n.v < key:
            res = n.v
            n = n.r
        else:
            n = n.l
    return res


def trim_bst(n, lo, hi):
    if not n:
        return None
    if n.v < lo:
        return trim_bst(n.r, lo, hi)
    if n.v > hi:
        return trim_bst(n.l, lo, hi)
    n.l = trim_bst(n.l, lo, hi)
    n.r = trim_bst(n.r, lo, hi)
    return n


def bst_count_and_height(root):
    return sum(1 for _ in iter_nodes(root)), depth(root)


def two_sum_bst(root, target):
    seen = set()
    for v in in_list(root):
        if target - v in seen:
            return True
        seen.add(v)
    return False


def range_sum_bst(root, lo, hi):
    return sum(v for v in in_list(root) if lo <= v <= hi)


def array_partition(xs):
    """LC561: pair up numbers to maximise the sum of the minimums."""
    xs = sorted(xs)
    return sum(xs[i] for i in range(0, len(xs), 2))


def meeting_rooms(iv):
    """LC252: can one person attend every meeting? Touching endpoints do NOT
    overlap: a meeting may start exactly when another finishes."""
    iv = sorted(iv, key=lambda x: x[0])
    for i in range(1, len(iv)):
        if iv[i][0] < iv[i - 1][1]:
            return False
    return True


def max_units_truck(boxes, size):
    """LC1710: pick boxes to fit `size` total units, prefer high `units` first.
    boxes: list of (count, units_per_box)."""
    total = 0
    for c, u in sorted(boxes, key=lambda x: -x[1]):
        take = min(c, size)
        total += take * u
        size -= take
        if size == 0:
            break
    return total


def best_stock(prices):
    """LC121: max profit from one buy then one sell."""
    if not prices:
        return 0
    lo, best = prices[0], 0
    for p in prices[1:]:
        best = max(best, p - lo)
        lo = min(lo, p)
    return best


def greedy_coins(coins, amt):
    """Take the largest denom that fits, repeat. Returns -1 if it fails to
    reach exactly amt using this rule."""
    coins = sorted(coins, reverse=True)
    used = 0
    for c in coins:
        used += amt // c
        amt %= c
    return used if amt == 0 else -1


def min_coins_dp(coins, amt):
    dp = [0] + [amt + 1] * amt
    for i in range(1, amt + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amt] if dp[amt] <= amt else -1


def di_match(s):
    """LC942: for `I` output the smallest unused; for `D` output the largest."""
    lo, hi = 0, len(s)
    out = []
    for c in s:
        if c == "I":
            out.append(lo); lo += 1
        else:
            out.append(hi); hi -= 1
    out.append(lo)  # lo == hi here
    return out


def tribonacci(n):
    """LC1137: T(0)=0, T(1)=T(2)=1, T(n)=T(n-1)+T(n-2)+T(n-3)."""
    if n == 0: return 0
    if n <= 2: return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


def stairs_123(n):
    """Ways to reach step n using strides in {1, 2, 3}."""
    if n < 0: return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for k in (1, 2, 3):
            if i - k >= 0:
                dp[i] += dp[i - k]
    return dp[n]


def coin_ways_12(n):
    """Number of ordered ways to reach amount n using coins of {1, 2}."""
    if n < 0: return 0
    a, b = 1, 1
    if n == 0: return 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def coin_change_ways(coins, amt):
    """LC518 unordered."""
    dp = [0] * (amt + 1)
    dp[0] = 1
    for c in coins:
        for i in range(c, amt + 1):
            dp[i] += dp[i - c]
    return dp[amt]


def is_subseq(s, t):
    """LC392: is s a subsequence of t?"""
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    return i == len(s)


def pascals_triangle(n):
    """LC118: first n rows of Pascal's triangle, one row per line."""
    rows_ = []
    prev = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev[j - 1] + prev[j]
        rows_.append(row)
        prev = row
    return rows_


def count_subsets_sum_k(xs, k):
    n = len(xs)
    tot = 0
    for mask in range(1 << n):
        s = sum(xs[i] for i in range(n) if mask >> i & 1)
        if s == k:
            tot += 1
    return tot


def subset_sum_table(xs, k):
    """(n+1) x (k+1) boolean DP table, 1/0 tokens."""
    n = len(xs)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            if xs[i - 1] <= j and dp[i - 1][j - xs[i - 1]]:
                dp[i][j] = 1
    return dp


def valid_palindrome(s):
    """LC125: consider only alphanumerics, ignore case."""
    filt = [c.lower() for c in s if c.isalnum()]
    return filt == filt[::-1]


def is_palindrome_table(s):
    """n x n table where entry (i, j) is 1 when s[i..j] is a palindrome, else
    0. Prints only the upper triangle values (i <= j); the lower half is 0."""
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
    for L in range(3, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
    return dp


def count_palindromes_1_2(s):
    """Count palindromic substrings of length 1 or 2 only."""
    n = len(s)
    return n + sum(1 for i in range(n - 1) if s[i] == s[i + 1])


# ---------------------------------------------------- constants used by cases
SIZED_ARR_IN = ("The first line contains an integer `n`. The second line "
                "contains `n` space-separated integers.")

TARGET_LINE_2 = "\n\nA second line contains the integer target value."

BST_IN_KEY = BST_IN + "\n\nA second line contains the integer key."

RANGE_LINE_2 = "\n\nA second line contains the two bounds `lo` and `hi`, "\
               "separated by a space."

NARY_IN = ("The first line contains an integer `n`, the number of nodes. "
           "The second line contains `n` space-separated integers -- the "
           "node values, with the first value being the root. If `n >= 2`, "
           "a third line contains `n - 1` integers: the parent value of "
           "each non-root node, in the same order as the values on line 2. "
           "All values are distinct.")

NARY_CASES = [
    "6\n1 3 5 6 2 4\n1 3 3 1 1",           # LC classic 1 [3,2,4] with 3 -> [5,6]
    "1\n7",
    "3\n1 2 3\n1 1",
    "0\n",
    "5\n10 20 30 40 50\n10 10 10 10",
    "7\n1 2 3 4 5 6 7\n1 1 1 2 2 3",
    "4\n5 6 7 8\n5 6 7",
    "6\n1 2 3 4 5 6\n1 2 3 4 5",
]


# ------------------------------------------------------------ new problem set
NEW_PROBLEMS_HW = [
    # ---- LEC-11 ------------------------------------------------------------
    dict(title="Homework: Find the sum of all node values in a binary tree",
         stmt="Given the root of a binary tree, print the sum of every "
              "node's value. The sum of an empty tree is 0.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(sum_all_nodes(build(s))),
         cases=TREES),

    dict(title="Homework: LC589 N-ary Tree Preorder Traversal",
         stmt="Given an N-ary tree, print its **preorder** traversal: root "
              "first, then each child's subtree in the order the children "
              "were added.",
         inp=NARY_IN, out=SEQ_OUT,
         cons="- `0 <= n <= 10^4`\n- values are distinct",
         solve=lambda s: (lambda r: fmt(nary_preorder(*build_nary(rows(s)))))(s),
         cases=NARY_CASES),

    # ---- LEC-13 ------------------------------------------------------------
    dict(title="Homework: Find the maximum node value in a binary tree",
         stmt="Given the root of a **non-empty** binary tree, print the "
              "largest value stored in any node.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(max_node_value(build(s))),
         cases=[t for t in TREES if t != "null"]),

    dict(title="Homework: LC559 Maximum Depth of N-ary Tree",
         stmt="Given an N-ary tree, print its maximum depth: the number of "
              "nodes on the longest root-to-leaf path. An empty tree has "
              "depth 0.",
         inp=NARY_IN, out=NUM_OUT,
         cons="- `0 <= n <= 10^4`\n- values are distinct",
         solve=lambda s: str(nary_depth(*build_nary(rows(s)))),
         cases=NARY_CASES),

    # ---- LEC-14 ------------------------------------------------------------
    dict(title="Homework: Count the number of leaf nodes in a binary tree",
         stmt="Given the root of a binary tree, print the number of **leaf** "
              "nodes (nodes with no children). An empty tree has 0 leaves.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(count_leaves(build(s))),
         cases=TREES),

    dict(title="Homework: LC100 Same Tree",
         stmt="Given two binary trees, decide whether they are the **same** "
              "tree: identical shape and identical values at every "
              "corresponding position.",
         inp=TREE_IN2, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(is_same_tree(*two(s))),
         cases=["1 2 3\n1 2 3",
                "1 2 3\n1 3 2",
                "1 2\n1 null 2",
                "null\nnull",
                "1\n1",
                "5 3 8 2 4 7 9\n5 3 8 2 4 7 9",
                "1 2 3 4\n1 2 3 4 5",
                "10 5 15\n10 5 15"]),

    # ---- LEC-12 ------------------------------------------------------------
    dict(title="Homework: LC993 Cousins in Binary Tree",
         stmt="Two nodes are **cousins** if they sit at the same depth but "
              "have different parents. Given a binary tree with unique "
              "values and two target values `x` and `y`, decide whether they "
              "are cousins.",
         inp=TREE_IN + "\n\nA second line contains the two values `x` and "
                       "`y`, separated by a space.",
         out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(
             cousins(build(rows(s)[0]), *ints(rows(s)[1]))),
         cases=["1 2 3 4\n4 3",
                "1 2 3 null 4 null 5\n5 4",
                "1 2 3 null 4\n2 3",
                "1 2 3 4 5 6 7\n4 6",
                "1 2 3 4 5 6 7\n4 5",
                "5 3 8 2 4 7 9\n2 7",
                "10 5 15 3 7 null 18\n3 18",
                "1 2 3\n2 3"]),

    # ---- LEC-15 ------------------------------------------------------------
    dict(title="Homework: Right view of a binary tree (GfG)",
         stmt="Print the **right view** of a binary tree: the nodes you "
              "would see looking at the tree from the right side, one per "
              "level from top to bottom.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(right_view(build(s))),
         cases=TREES),

    # ---- LEC-16 ------------------------------------------------------------
    dict(title="Homework: LC617 Merge Two Binary Trees",
         stmt="Two binary trees are overlaid. Where both have a node, the "
              "merged node's value is the sum of the two values. Where only "
              "one has a node, the merged tree uses that node as-is. Print "
              "the merged tree in level order.",
         inp=TREE_IN2, out=SER_OUT, cons=CONS,
         solve=lambda s: serialize(merge_trees(*two(s))),
         cases=["1 3 2 5\n2 1 3 null 4 null 7",
                "1\n2",
                "null\n1 2 3",
                "1 2 3\nnull",
                "null\nnull",
                "5 3 8 2 4 7 9\n1 1 1 1 1 1 1",
                "1 2 3 4 5\n6 7 8",
                "10 5 15\n1 2 3"]),

    # ---- LEC-17 ------------------------------------------------------------
    dict(title="Homework: LC257 Binary Tree Paths",
         stmt="Print every **root-to-leaf** path in a binary tree. Each path "
              "is a sequence of node values joined by `->` on its own line. "
              "Paths are listed in DFS order (left subtree first).",
         inp=TREE_IN,
         out="One line per root-to-leaf path, values joined by `->`. Print "
             "nothing for an empty tree.",
         cons=CONS,
         solve=lambda s: "\n".join(binary_tree_paths(build(s))),
         cases=TREES),

    dict(title="Homework: LC129 Sum Root to Leaf Numbers",
         stmt="Every root-to-leaf path forms a number by concatenating the "
              "digits along the path. Print the sum of all such numbers.\n\n"
              "All node values are between 0 and 9.",
         inp=TREE_IN, out=NUM_OUT,
         cons="- `1 <= N <= 1000`\n- `0 <= node value <= 9`",
         solve=lambda s: str(sum_root_to_leaf(build(s))),
         cases=["1 2 3",
                "4 9 0 5 1",
                "1",
                "1 2",
                "1 null 2 null 3",
                "1 2 3 4 5 6 7",
                "3 1 4 null 2",
                "9 8 7 6 5 4 3"]),

    # ---- LEC-18 ------------------------------------------------------------
    dict(title="Homework: Find the level of a given node in a binary tree",
         stmt="Given a binary tree and a target value, print the level of "
              "the first node holding that value, counting the root as level "
              "1. Print `-1` if the value is not in the tree.",
         inp=TREE_IN + TARGET_LINE_2,
         out="A single line: the level of the target, or `-1`.",
         cons=CONS,
         solve=lambda s: str(level_of_value(build(rows(s)[0]),
                                             int(rows(s)[1]))),
         cases=["1 2 3\n2",
                "1 2 3\n4",
                "5 3 8 2 4 7 9\n9",
                "5 3 8 2 4 7 9\n5",
                "null\n0",
                "1\n1",
                "10 5 15 3 7 null 18\n7",
                "10 5 15 3 7 null 18\n99"]),

    dict(title="Homework: LC1650 Lowest Common Ancestor III",
         stmt="Given a binary tree and two node values that are both "
              "present, print the value of their **lowest common ancestor**: "
              "the deepest node that has both of them in its subtree.\n\n"
              "In LeetCode's version, parent pointers are provided; here the "
              "tree is given in level order and both target values are "
              "guaranteed to appear exactly once.",
         inp=TREE_IN + "\n\nA second line contains the two target values, "
                       "separated by a space.",
         out=NUM_OUT, cons=CONS,
         solve=lambda s: str(lca_binary_tree(build(rows(s)[0]),
                                              *ints(rows(s)[1]))),
         cases=["3 5 1 6 2 0 8 null null 7 4\n5 1",
                "3 5 1 6 2 0 8 null null 7 4\n5 4",
                "1 2\n1 2",
                "1 2 3\n2 3",
                "5 3 8 2 4 7 9\n2 4",
                "5 3 8 2 4 7 9\n2 9",
                "1 2 null 3 null 4\n3 4",
                "10 5 15 3 7 null 18\n3 18"]),

    dict(title="Homework: Kth ancestor of a node in a tree (GfG)",
         stmt="Given a binary tree, a target node's value, and an integer "
              "`k`, print the value of the target's `k`-th ancestor (its "
              "parent is the 1st ancestor). Print `-1` if the target does "
              "not exist or if walking `k` steps up runs off the tree.\n\n"
              "All node values are distinct.",
         inp=TREE_IN + "\n\nA second line contains the target value and the "
                       "integer `k`, separated by a space.",
         out="A single line: the ancestor value, or `-1`.",
         cons=CONS,
         solve=lambda s: str(kth_ancestor(build(rows(s)[0]),
                                           *ints(rows(s)[1]))),
         cases=["1 2 3 4 5 6 7\n5 1",
                "1 2 3 4 5 6 7\n5 2",
                "1 2 3 4 5 6 7\n4 3",
                "1 2 3 4 5 6 7\n1 1",
                "1 2 3 4 5 6 7\n99 1",
                "5 3 8 2 4 7 9\n7 1",
                "10 5 15 3 7 null 18\n18 2",
                "1 2 3 4 5 6 7\n7 2"]),

    # ---- LEC-19 ------------------------------------------------------------
    dict(title="Homework: LC108 Convert Sorted Array to Binary Search Tree",
         stmt="Given a sorted integer array with distinct values, build a "
              "**height-balanced** BST by picking the middle element as the "
              "root at every step. Print the resulting BST in level order.",
         inp=SIZED_ARR_IN, out=SER_OUT,
         cons="- `1 <= n <= 10^4`\n- the array is sorted increasing",
         solve=lambda s: bst_from_sorted(ints(rows(s)[1])),
         cases=["5\n-10 -3 0 5 9",
                "1\n42",
                "2\n1 2",
                "3\n1 2 3",
                "7\n1 2 3 4 5 6 7",
                "6\n-5 -3 0 2 4 8",
                "4\n10 20 30 40",
                "8\n1 2 3 4 5 6 7 8"]),

    dict(title="Homework: LC889 Construct Binary Tree from Preorder and Postorder",
         stmt="Given the preorder and postorder traversals of a **full** "
              "binary tree (every internal node has two children) with "
              "distinct values, rebuild the tree and print it in level order. "
              "The reconstruction is unique for full binary trees.",
         inp="Two lines: line 1 is the preorder traversal (space-separated "
             "integers); line 2 is the postorder traversal (same values, "
             "space-separated).",
         out=SER_OUT,
         cons="- `1 <= n <= 30`\n- values are distinct",
         solve=lambda s: serialize(from_pre_post(ints(rows(s)[0]),
                                                  ints(rows(s)[1]))),
         cases=["1 2 4 5 3 6 7\n4 5 2 6 7 3 1",
                "1\n1",
                "1 2 3\n2 3 1",
                "1 2 4 5 3\n4 5 2 3 1",
                "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15\n"
                "8 9 4 10 11 5 2 12 13 6 14 15 7 3 1",
                "3 1 2\n2 1 3",
                "2 1 3\n1 3 2",
                "5 3 1 2 4 8 7 9\n2 1 4 3 7 9 8 5"]),

    dict(title="Homework: LC426 Convert BST to Sorted Doubly Linked List",
         stmt="Given a BST, imagine transforming it into a sorted, circular "
              "**doubly linked list** in place: `left` becomes the previous "
              "pointer and `right` becomes the next pointer, values ordered "
              "increasingly, with the smallest and largest looped back to "
              "each other.\n\nPrint the resulting sequence -- the values as "
              "they appear when walking `next` from the smallest to the "
              "largest -- as a space-separated line.",
         inp=BST_IN, out=SEQ_OUT, cons=BST_CONS,
         solve=lambda s: fmt(in_list(build(s))),
         cases=BSTS),

    # ---- LEC-20 ------------------------------------------------------------
    dict(title="Homework: LC404 Sum of Left Leaves",
         stmt="Print the sum of every **left leaf** in a binary tree. A left "
              "leaf is a leaf that is the left child of its parent.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(sum_left_leaves(build(s))),
         cases=TREES),

    dict(title="Homework: LC116 Populating Next Right Pointers in Each Node",
         stmt="Given a **perfect** binary tree, imagine wiring every node's "
              "`next` pointer to the node immediately to its right on the "
              "same level, with the rightmost `next` set to null.\n\nPrint "
              "the sequence of values you would visit by walking the "
              "wired-up tree level by level: each level's values in "
              "left-to-right order, terminated by `#`. An empty tree prints "
              "a single `#`.",
         inp=TREE_IN,
         out="A single line: the values level by level, `#` after each level.",
         cons=CONS,
         solve=lambda s: populating_next_right(build(s)),
         cases=["1 2 3 4 5 6 7",
                "1",
                "null",
                "1 2 3",
                "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15",
                "10 5 15 3 7 12 18",
                "1 2 3 4 5 6 7 8 9",
                "42"]),

    # ---- LEC-21 ------------------------------------------------------------
    dict(title="Homework: Find the minimum and maximum value in a BST",
         stmt="Given a **non-empty** BST, print two integers on one line: "
              "the smallest value and the largest value in the tree, "
              "separated by a space.",
         inp=BST_IN,
         out="A single line: the minimum and the maximum, separated by a "
             "space.",
         cons=BST_CONS,
         solve=lambda s: (lambda r: "%d %d" % r)(bst_min_max(build(s))),
         cases=[b for b in BSTS if b != "null"]),

    # ---- LEC-22 ------------------------------------------------------------
    dict(title="Homework: LC897 Increasing Order Search Tree",
         stmt="Rearrange a BST into a `right-only` chain whose values appear "
              "in increasing order (each node has no left child and its "
              "right child is the next in-order value).\n\nPrint the "
              "resulting sequence of values -- equivalently, the BST's "
              "inorder traversal -- on a single line.",
         inp=BST_IN, out=SEQ_OUT, cons=BST_CONS,
         solve=lambda s: increasing_order_bst(build(s)),
         cases=BSTS),

    # ---- LEC-23 ------------------------------------------------------------
    dict(title="Homework: Find the floor value of a key in a BST (GfG)",
         stmt="Given a BST and a key, print the **floor** of the key: the "
              "largest value in the BST that is `<= key`. Print `-1` if "
              "every value in the tree is larger than the key.",
         inp=BST_IN_KEY, out="A single line: the floor value, or `-1`.",
         cons=BST_CONS,
         solve=lambda s: (lambda r: "-1" if r is None else str(r))(
             bst_floor(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [4, 8, 2, 9, 6, 11, 5, 45, 22])),

    dict(title="Homework: LC669 Trim a Binary Search Tree",
         stmt="Given a BST and an inclusive range `[lo, hi]`, remove every "
              "node whose value falls outside the range so that the result "
              "is still a valid BST, and print it in level order.",
         inp=BST_IN + RANGE_LINE_2, out=SER_OUT, cons=BST_CONS,
         solve=lambda s: serialize(trim_bst(build(rows(s)[0]),
                                             *ints(rows(s)[1]))),
         cases=["1 0 2\n1 2",
                "3 0 4 null 2 null null 1\n1 3",
                "8\n1 10",
                "2 1 3\n2 3",
                "5 3 8 2 4 7 9\n3 8",
                "10 5 15 null null 6 20\n6 15",
                "8 3 10 1 6 null 14 null null 4 7 13\n5 13",
                "50 30 70 20 40 60 80\n35 75"]),

    # ---- LEC-24 ------------------------------------------------------------
    dict(title="Homework: Count the total nodes and height of a BST",
         stmt="Given a BST, print two lines: the total number of nodes on "
              "line 1, and the height of the tree (the number of nodes on "
              "its longest root-to-leaf path) on line 2. An empty tree has "
              "0 nodes and height 0.",
         inp=BST_IN,
         out="Two lines: the node count and the height, one per line.",
         cons=BST_CONS,
         solve=lambda s: (lambda r: "%d\n%d" % r)(
             bst_count_and_height(build(s))),
         cases=BSTS),

    dict(title="Homework: LC653 Two Sum IV - Input is a BST",
         stmt="Given a BST and a target integer, decide whether **two "
              "different** nodes have values that add up to the target.",
         inp=BST_IN + TARGET_LINE_2, out=BOOL_OUT, cons=BST_CONS,
         solve=lambda s: fmt_bool(two_sum_bst(build(rows(s)[0]),
                                               int(rows(s)[1]))),
         cases=with_key(BSTS, [9, 10, 5, 18, 12, 22, 11, 90, 40])),

    dict(title="Homework: LC938 Range Sum of BST",
         stmt="Given a BST and an inclusive range `[lo, hi]`, print the sum "
              "of every value in the BST that falls inside the range.",
         inp=BST_IN + RANGE_LINE_2, out=NUM_OUT, cons=BST_CONS,
         solve=lambda s: str(range_sum_bst(build(rows(s)[0]),
                                            *ints(rows(s)[1]))),
         cases=["8\n3 10",
                "2 1 3\n1 3",
                "8 3 10\n5 15",
                "5 3 8 2 4 7 9\n3 8",
                "10 5 15 null null 6 20\n6 15",
                "8 3 10 1 6 null 14 null null 4 7 13\n4 13",
                "50 30 70 20 40 60 80\n35 75",
                "20 10 30 5 15 25 35 1\n1 20"]),

    # ---- LEC-25 ------------------------------------------------------------
    dict(title="Homework: Convert a BST into a sorted vector",
         stmt="Given a BST, print all of its values on a single line, in "
              "increasing order (equivalently, the BST's inorder "
              "traversal). Print an empty line for an empty tree.",
         inp=BST_IN, out=SEQ_OUT, cons=BST_CONS,
         solve=lambda s: fmt(in_list(build(s))),
         cases=BSTS),

    # ---- LEC-26 ------------------------------------------------------------
    dict(title="Homework: LC561 Array Partition",
         stmt="You are given `2n` integers. Group them into `n` pairs so "
              "that the sum of the smaller number in each pair is as large "
              "as possible. Print that maximum sum.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `n` is even, `1 <= n <= 10^4`\n- `-10^4 <= value <= 10^4`",
         solve=lambda s: str(array_partition(ints(rows(s)[1]))),
         cases=["4\n1 4 3 2",
                "6\n6 2 6 5 1 2",
                "2\n1 2",
                "2\n-5 -3",
                "8\n1 2 3 4 5 6 7 8",
                "4\n-1 -2 -3 -4",
                "6\n10 20 30 40 50 60",
                "4\n0 0 0 0"]),

    # ---- LEC-27 ------------------------------------------------------------
    dict(title="Homework: LC252 Meeting Rooms",
         stmt="Given a list of meeting time intervals, decide whether one "
              "person can attend every meeting.\n\nTwo intervals `[a, b]` "
              "and `[c, d]` **overlap** when `a < d` and `c < b`; touching "
              "endpoints (one meeting ending exactly when the next starts) "
              "do NOT count as overlapping.",
         inp=IV_IN, out=BOOL_OUT,
         cons="- `1 <= n <= 10^4`\n- `0 <= start < end <= 10^9`",
         solve=lambda s: fmt_bool(meeting_rooms(
             [tuple(ints(r)) for r in rows(s)[1:1 + int(rows(s)[0])]])),
         cases=IV_CASES),

    # ---- LEC-28 ------------------------------------------------------------
    dict(title="Homework: LC1710 Maximum Units on a Truck",
         stmt="You have a truck that can carry `size` boxes. Each box type "
              "is given by two integers: how many boxes of that type are "
              "available, and how many units each box holds. Print the "
              "largest total number of units the truck can carry.",
         inp="The first line contains `n` (number of box types) and `size` "
             "(truck capacity), separated by a space. Each of the next `n` "
             "lines contains two integers describing one box type: the "
             "count of boxes and the units per box.",
         out=NUM_OUT,
         cons="- `1 <= n <= 1000`\n- `1 <= size <= 10^4`",
         solve=lambda s: str(max_units_truck(
             [tuple(ints(r)) for r in rows(s)[1:1 + ints(rows(s)[0])[0]]],
             ints(rows(s)[0])[1])),
         cases=["3 4\n1 3\n2 2\n3 1",
                "5 10\n5 10\n2 5\n4 7\n3 9\n1 8",
                "1 5\n10 100",
                "2 3\n1 5\n1 10",
                "3 10\n2 3\n5 2\n4 1",
                "4 6\n2 4\n3 3\n5 2\n1 5",
                "2 100\n5 5\n5 5",
                "3 0\n1 1\n1 1\n1 1"]),

    # ---- LEC-29 ------------------------------------------------------------
    dict(title="Homework: LC121 Best Time to Buy and Sell Stock",
         stmt="You are given the daily prices of a stock. Choose one day to "
              "buy and a later day to sell, and print the largest profit "
              "you can make. If no positive profit is possible, print `0`.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `0 <= price <= 10^4`",
         solve=lambda s: str(best_stock(ints(rows(s)[1]))),
         cases=["6\n7 1 5 3 6 4",
                "5\n7 6 4 3 1",
                "1\n5",
                "2\n1 2",
                "2\n2 1",
                "5\n2 4 1 7 3",
                "6\n1 2 3 4 5 6",
                "5\n5 5 5 5 5"]),

    dict(title="Homework: Write-up: a coin system where greedy fails (counterexample)",
         stmt="You are given a coin system and a target amount. Compute two "
              "answers:\n\n"
              "1. The number of coins the **greedy** rule (always take the "
              "largest denomination that still fits) uses to make the "
              "amount, or `-1` if that rule cannot exactly reach it.\n"
              "2. The **optimal** minimum-coins count, or `-1` if the "
              "amount cannot be made with any combination.\n\n"
              "When the two differ, this input is a counterexample proving "
              "the greedy rule is not always right.",
         inp="The first line contains an integer `n`, the number of "
             "denominations. The second line contains those `n` "
             "denominations, space separated. The third line contains the "
             "target amount.",
         out="Two lines: the greedy count on line 1 (or `-1`), and the "
             "optimal count on line 2 (or `-1`).",
         cons="- `1 <= n <= 20`\n- `1 <= amount <= 10^4`\n- denominations "
              "are positive",
         solve=lambda s: "%d\n%d" % (
             greedy_coins(ints(rows(s)[1]), int(rows(s)[2])),
             min_coins_dp(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=["3\n1 3 4\n6",       # greedy 4+1+1=3, optimal 3+3=2
                "3\n1 5 10\n20",     # both 2
                "3\n1 7 10\n14",     # greedy 10+1+1+1+1=5, optimal 7+7=2
                "3\n1 6 10\n12",     # greedy 10+1+1=3, optimal 6+6=2
                "3\n1 2 5\n11",      # both 3
                "2\n2 5\n3",         # greedy -1 (5>3, then 2+... leaves 1), optimal -1
                "3\n1 9 10\n18",     # greedy 10+1+1+1+1+1+1+1+1=9, optimal 9+9=2
                "1\n1\n7"]),         # both 7

    # ---- LEC-30 ------------------------------------------------------------
    dict(title="Homework: LC942 DI String Match",
         stmt="Given a string of `n` letters using only `I` (increase) and "
              "`D` (decrease), print any permutation `p` of `0..n` such "
              "that:\n\n"
              "- `p[i] < p[i+1]` when the `i`-th letter is `I`, and\n"
              "- `p[i] > p[i+1]` when the `i`-th letter is `D`.\n\n"
              "The construction below always uses the smallest unused "
              "number for `I` and the largest unused number for `D`, "
              "producing a deterministic answer.",
         inp="A single line: the string of `I` / `D` characters.",
         out="A single line: `n + 1` integers separated by spaces.",
         cons="- `1 <= length <= 10^5`\n- characters are `I` or `D` only",
         solve=lambda s: fmt(di_match(s.strip())),
         cases=["IDID",
                "III",
                "DDI",
                "I",
                "D",
                "IIDDI",
                "DIDIDID",
                "IIIDDD"]),

    # ---- LEC-31 ------------------------------------------------------------
    dict(title="Homework: LC1137 N-th Tribonacci Number",
         stmt="Print `T(n)` where `T(0) = 0`, `T(1) = T(2) = 1`, and each "
              "later value is the sum of the previous three: "
              "`T(k) = T(k-1) + T(k-2) + T(k-3)`.",
         inp="A single line containing the integer `n`.",
         out=NUM_OUT,
         cons="- `0 <= n <= 37`",
         solve=lambda s: str(tribonacci(int(s.strip()))),
         cases=["0", "1", "2", "3", "4", "10", "25", "37"]),

    # ---- LEC-32 ------------------------------------------------------------
    dict(title="Homework: Count ways to climb stairs with steps of 1, 2 or 3 (GfG)",
         stmt="You are climbing a staircase with `n` steps. On each move "
              "you may go up 1, 2, or 3 steps. Print the total number of "
              "distinct ways to reach the top.",
         inp="A single line containing the integer `n`.",
         out=NUM_OUT,
         cons="- `0 <= n <= 30`",
         solve=lambda s: str(stairs_123(int(s.strip()))),
         cases=["0", "1", "2", "3", "4", "5", "10", "20"]),

    # ---- LEC-33 ------------------------------------------------------------
    dict(title="Homework: LC392 Is Subsequence",
         stmt="Given two strings `s` and `t`, decide whether `s` is a "
              "**subsequence** of `t`: whether the characters of `s` appear "
              "in `t` in the same relative order (not necessarily "
              "consecutively).",
         inp="Two lines: `s` on line 1 and `t` on line 2. Either string may "
             "be empty (the corresponding line may be blank).",
         out=BOOL_OUT,
         cons="- `0 <= length of each string <= 10^4`",
         solve=lambda s: fmt_bool(is_subseq(
             rows(s)[0] if len(rows(s)) > 0 else "",
             rows(s)[1] if len(rows(s)) > 1 else "")),
         cases=["abc\nahbgdc",
                "axc\nahbgdc",
                "\nahbgdc",
                "abc\n",
                "abc\nabc",
                "b\nabc",
                "ace\nabcde",
                "aec\nabcde"]),

    # ---- LEC-34 ------------------------------------------------------------
    dict(title="Homework: LC118 Pascal's Triangle",
         stmt="Print the first `n` rows of Pascal's triangle. Each row `i` "
              "has `i + 1` numbers; the first and last are `1`, and every "
              "other number is the sum of the two above it in the previous "
              "row.",
         inp="A single line containing the integer `n`.",
         out="`n` lines: row `i` (0-indexed) has `i + 1` integers separated "
             "by spaces.",
         cons="- `1 <= n <= 30`",
         solve=lambda s: "\n".join(fmt(r) for r in
                                    pascals_triangle(int(s.strip()))),
         cases=["1", "2", "3", "5", "6", "7", "10", "4"]),

    # ---- LEC-35 ------------------------------------------------------------
    dict(title="Homework: Count subsets of a 5-element array with sum K by brute force",
         stmt="Given a small array of length `n` and a target `K`, print "
              "the number of subsets whose values sum to exactly `K` by "
              "trying every one of the `2^n` subsets.",
         inp=SIZED_ARR_IN + "\n\nA final line contains the target `K`.",
         out=NUM_OUT,
         cons="- `1 <= n <= 15`\n- `-100 <= value <= 100`\n- `-1500 <= K "
              "<= 1500`",
         solve=lambda s: str(count_subsets_sum_k(ints(rows(s)[1]),
                                                  int(rows(s)[2]))),
         cases=["5\n1 2 3 4 5\n5",
                "5\n1 2 3 4 5\n0",
                "4\n2 4 6 10\n16",
                "3\n1 1 1\n2",
                "5\n5 5 5 5 5\n15",
                "4\n1 2 3 4\n7",
                "5\n-1 1 -2 2 3\n3",
                "1\n7\n7"]),

    # ---- LEC-36 ------------------------------------------------------------
    dict(title="Homework: Print the full DP table for subset-sum on a 4-element array",
         stmt="Given an array of `n` non-negative integers and a target "
              "`K`, print the full `(n + 1) x (K + 1)` subset-sum DP table. "
              "Entry `dp[i][j]` is `1` when some subset of the first `i` "
              "values sums to `j`, else `0`.",
         inp=SIZED_ARR_IN + "\n\nA final line contains the target `K`.",
         out="`n + 1` lines, each with `K + 1` `0`/`1` tokens separated by "
             "spaces.",
         cons="- `1 <= n <= 6`\n- `0 <= K <= 30`\n- values are non-negative",
         solve=lambda s: "\n".join(fmt(r) for r in
                                    subset_sum_table(ints(rows(s)[1]),
                                                      int(rows(s)[2]))),
         cases=["4\n2 3 5 6\n8",
                "4\n1 2 3 4\n6",
                "3\n1 2 3\n5",
                "4\n2 4 6 8\n10",
                "1\n5\n5",
                "4\n1 1 1 1\n3",
                "3\n3 34 4\n7",
                "4\n2 3 7 8\n11"]),

    # ---- LEC-37 ------------------------------------------------------------
    dict(title="Homework: Count ways to reach amount N using coins of 1 and 2 (GfG)",
         stmt="Print the number of **ordered** ways to reach the amount `N` "
              "using only coins of denomination `1` and `2`. The order of "
              "the coins matters: paying `1 + 2` is counted separately "
              "from `2 + 1`.",
         inp="A single line containing the non-negative integer `N`.",
         out=NUM_OUT,
         cons="- `0 <= N <= 40`",
         solve=lambda s: str(coin_ways_12(int(s.strip()))),
         cases=["0", "1", "2", "3", "4", "5", "10", "20"]),

    dict(title="Homework: LC518 Coin Change II",
         stmt="Given a set of coin denominations (each can be used any "
              "number of times) and a target amount, print the number of "
              "**distinct combinations** of coins that add up to the "
              "amount. Two combinations that use the same multiset of coins "
              "are counted once.",
         inp="The first line contains the amount `A` and the number of "
             "denominations `k`, separated by a space. The second line "
             "contains the `k` denominations, separated by spaces.",
         out=NUM_OUT,
         cons="- `0 <= A <= 5000`\n- `1 <= k <= 300`\n- denominations are "
              "positive and distinct",
         solve=lambda s: str(coin_change_ways(ints(rows(s)[1]),
                                                ints(rows(s)[0])[0])),
         cases=["5 3\n1 2 5",
                "3 1\n2",
                "10 1\n10",
                "0 1\n7",
                "11 3\n1 2 5",
                "500 3\n1 2 5",
                "7 3\n2 3 6",
                "10 3\n2 5 10"]),

    # ---- LEC-38 ------------------------------------------------------------
    dict(title="Homework: LC125 Valid Palindrome",
         stmt="Given a string, consider only its alphanumeric characters "
              "and treat uppercase and lowercase as the same. Decide "
              "whether the resulting sequence reads the same forwards and "
              "backwards.",
         inp="A single line containing the string. It may include spaces "
             "and punctuation.",
         out=BOOL_OUT,
         cons="- `0 <= length <= 10^5`",
         solve=lambda s: fmt_bool(valid_palindrome(s.rstrip("\n"))),
         cases=["A man, a plan, a canal: Panama",
                "race a car",
                " ",
                "0P",
                "Was it a car or a cat I saw?",
                "No lemon, no melon",
                "hello",
                "a"]),

    # ---- LEC-39 ------------------------------------------------------------
    dict(title="Homework: Count palindromic substrings of length 1 and 2 by brute force",
         stmt="Given a string of length `n`, count the palindromic "
              "substrings of length 1 or 2 only.\n\n"
              "Every length-1 substring is a palindrome (there are `n` of "
              "them), and a length-2 substring `s[i..i+1]` is a palindrome "
              "exactly when its two characters are equal.",
         inp="A single line containing the string.",
         out=NUM_OUT,
         cons="- `1 <= length <= 10^5`",
         solve=lambda s: str(count_palindromes_1_2(s.rstrip("\n"))),
         cases=["aaa",
                "abc",
                "aabb",
                "a",
                "abba",
                "abcba",
                "zzzz",
                "abab"]),

    # ---- LEC-40 ------------------------------------------------------------
    dict(title="Homework: Precompute an isPalindrome[i][j] table for a string",
         stmt="Given a string of length `n`, print the `n x n` table where "
              "entry `(i, j)` is `1` when the substring `s[i..j]` is a "
              "palindrome and `0` otherwise. Only the entries with `i <= j` "
              "are ever set to `1`; the lower triangle stays `0`.",
         inp="A single line containing the string.",
         out="`n` lines, each with `n` `0`/`1` tokens separated by spaces.",
         cons="- `1 <= length <= 30`",
         solve=lambda s: "\n".join(fmt(r) for r in
                                    is_palindrome_table(s.rstrip("\n"))),
         cases=["aba",
                "abba",
                "abc",
                "a",
                "aaa",
                "abcba",
                "racecar",
                "ab"]),
]


# ------------------------------------------------------ homework title order
# The exact list of homework problems in the sheet for LEC-11 to LEC-40,
# in the order they appear. Duplicates are kept for reference; dedupe below.
SHEET_TITLES_HW = [
    # ---- LEC-11 -------------------------------------------------------------
    "Homework: Find the sum of all node values in a binary tree",
    "Homework: LC589 N-ary Tree Preorder Traversal",
    "Homework: Count the total number of nodes recursively",
    "Homework: Print all leaf nodes from left to right",
    # ---- LEC-12 -------------------------------------------------------------
    "Homework: LC993 Cousins in Binary Tree",
    "Homework: LC637 Average of Levels in Binary Tree",
    "Homework: LC103 Binary Tree Zigzag Level Order Traversal",
    "Homework: LC107 Binary Tree Level Order Traversal II",
    # ---- LEC-13 -------------------------------------------------------------
    "Homework: Find the maximum node value in a binary tree",
    "Homework: LC559 Maximum Depth of N-ary Tree",
    "Homework: Check whether two trees have equal height",
    "Homework: Count the number of nodes at maximum depth",
    # ---- LEC-14 -------------------------------------------------------------
    "Homework: Count the number of leaf nodes in a binary tree",
    "Homework: LC100 Same Tree",
    "Homework: LC965 Univalued Binary Tree",
    "Homework: LC872 Leaf-Similar Trees",
    # ---- LEC-15 -------------------------------------------------------------
    "Homework: Right view of a binary tree (GfG)",
    "Homework: Bottom view of a binary tree (GfG)",
    "Homework: Diagonal traversal of a binary tree (GfG)",
    "Homework: Morris inorder traversal (O(1) space) (GfG)",
    # ---- LEC-16 -------------------------------------------------------------
    "Homework: LC617 Merge Two Binary Trees",
    "Homework: Check if one tree is the mirror of another (GfG)",
    "Homework: Convert a tree to its mirror in place (GfG)",
    "Homework: LC951 Flip Equivalent Binary Trees",
    # ---- LEC-17 -------------------------------------------------------------
    "Homework: LC257 Binary Tree Paths",
    "Homework: LC437 Path Sum III",
    "Homework: LC129 Sum Root to Leaf Numbers",
    "Homework: LC988 Smallest String Starting From Leaf",
    # ---- LEC-18 -------------------------------------------------------------
    "Homework: Find the level of a given node in a binary tree",
    "Homework: LC1650 Lowest Common Ancestor III",
    "Homework: LC1123 Lowest Common Ancestor of Deepest Leaves",
    "Homework: Kth ancestor of a node in a tree (GfG)",
    # ---- LEC-19 -------------------------------------------------------------
    "Homework: LC108 Convert Sorted Array to Binary Search Tree",
    "Homework: LC889 Construct Binary Tree from Preorder and Postorder",
    "Homework: LC1008 Construct BST from Preorder Traversal",
    "Homework: LC426 Convert BST to Sorted Doubly Linked List",
    # ---- LEC-20 -------------------------------------------------------------
    "Homework: LC404 Sum of Left Leaves",
    "Homework: LC129 Sum Root to Leaf Numbers",
    "Homework: LC662 Maximum Width of Binary Tree",
    "Homework: LC116 Populating Next Right Pointers in Each Node",
    # ---- LEC-21 -------------------------------------------------------------
    "Homework: Find the minimum and maximum value in a BST",
    "Homework: Count BST nodes lying in a given range (GfG)",
    "Homework: Iterative BST insert (GfG)",
    "Homework: Search keys within a range in a BST (GfG)",
    # ---- LEC-22 -------------------------------------------------------------
    "Homework: LC897 Increasing Order Search Tree",
    "Homework: LC783 Minimum Distance Between BST Nodes",
    "Homework: LC99 Recover Binary Search Tree",
    "Homework: LC255 Verify Preorder Sequence in BST",
    # ---- LEC-23 -------------------------------------------------------------
    "Homework: Find the floor value of a key in a BST (GfG)",
    "Homework: LC669 Trim a Binary Search Tree",
    "Homework: LC285 Inorder Successor in BST",
    "Homework: Inorder predecessor in a BST (GfG)",
    # ---- LEC-24 -------------------------------------------------------------
    "Homework: Count the total nodes and height of a BST",
    "Homework: LC653 Two Sum IV - Input is a BST",
    "Homework: LC938 Range Sum of BST",
    "Homework: LC109 Convert Sorted List to Binary Search Tree",
    # ---- LEC-25 -------------------------------------------------------------
    "Homework: Convert a BST into a sorted vector",
    "Homework: LC538 Convert BST to Greater Tree",
    "Homework: LC1382 Balance a Binary Search Tree",
    "Homework: LC333 Largest BST Subtree",
    # ---- LEC-26 -------------------------------------------------------------
    "Homework: LC561 Array Partition",
    "Homework: LC452 Minimum Number of Arrows to Burst Balloons",
    "Homework: LC646 Maximum Length of Pair Chain",
    "Homework: Maximize meetings attended in one room (GfG)",
    # ---- LEC-27 -------------------------------------------------------------
    "Homework: LC252 Meeting Rooms",
    "Homework: LC986 Interval List Intersections",
    "Homework: LC1094 Car Pooling",
    "Homework: Maximum number of overlapping intervals (GfG)",
    # ---- LEC-28 -------------------------------------------------------------
    "Homework: LC1710 Maximum Units on a Truck",
    "Homework: LC455 Assign Cookies",
    "Homework: Minimum number of coins (GfG)",
    "Homework: Huffman Encoding (GfG)",
    # ---- LEC-29 -------------------------------------------------------------
    "Homework: LC121 Best Time to Buy and Sell Stock",
    "Homework: LC45 Jump Game II",
    "Homework: LC763 Partition Labels",
    "Homework: Write-up: a coin system where greedy fails (counterexample)",
    # ---- LEC-30 -------------------------------------------------------------
    "Homework: LC942 DI String Match",
    "Homework: LC860 Lemonade Change",
    "Homework: Rearrange characters so that none are adjacent (GfG)",
    "Homework: LC1353 Maximum Number of Events That Can Be Attended",
    # ---- LEC-31 -------------------------------------------------------------
    "Homework: LC1137 N-th Tribonacci Number",
    "Homework: LC746 Min Cost Climbing Stairs",
    "Homework: LC213 House Robber II",
    "Homework: LC91 Decode Ways",
    # ---- LEC-32 -------------------------------------------------------------
    "Homework: Count ways to climb stairs with steps of 1, 2 or 3 (GfG)",
    "Homework: LC377 Combination Sum IV",
    "Homework: LC279 Perfect Squares",
    "Homework: Number of ways to make change (GfG)",
    # ---- LEC-33 -------------------------------------------------------------
    "Homework: LC392 Is Subsequence",
    "Homework: LC673 Number of Longest Increasing Subsequence",
    "Homework: LC1035 Uncrossed Lines",
    "Homework: Longest common substring (GfG)",
    # ---- LEC-34 -------------------------------------------------------------
    "Homework: LC118 Pascal's Triangle",
    "Homework: LC120 Triangle",
    "Homework: LC931 Minimum Falling Path Sum",
    "Homework: LC221 Maximal Square",
    # ---- LEC-35 -------------------------------------------------------------
    "Homework: Count subsets of a 5-element array with sum K by brute force",
    "Homework: Count of subsets with a given sum (GfG)",
    "Homework: Maximum sum of non-adjacent elements (GfG)",
    "Homework: LC740 Delete and Earn",
    # ---- LEC-36 -------------------------------------------------------------
    "Homework: Print the full DP table for subset-sum on a 4-element array",
    "Homework: Count subsets with a given difference (GfG)",
    "Homework: LC1049 Last Stone Weight II",
    "Homework: Minimum subset-sum difference (GfG)",
    # ---- LEC-37 -------------------------------------------------------------
    "Homework: Count ways to reach amount N using coins of 1 and 2 (GfG)",
    "Homework: LC518 Coin Change II",
    "Homework: Maximum ribbon cut (GfG)",
    "Homework: LC343 Integer Break",
    # ---- LEC-38 -------------------------------------------------------------
    "Homework: LC125 Valid Palindrome",
    "Homework: LC161 One Edit Distance",
    "Homework: LC97 Interleaving String",
    "Homework: LC115 Distinct Subsequences",
    # ---- LEC-39 -------------------------------------------------------------
    "Homework: Count palindromic substrings of length 1 and 2 by brute force",
    "Homework: LC5 Longest Palindromic Substring",
    "Homework: LC647 Palindromic Substrings",
    "Homework: LC1312 Minimum Insertion Steps to Make a String Palindrome",
    # ---- LEC-40 -------------------------------------------------------------
    "Homework: Precompute an isPalindrome[i][j] table for a string",
    "Homework: LC1043 Partition Array for Maximum Sum",
    "Homework: Boolean Parenthesization (GfG)",
    "Homework: LC1547 Minimum Cost to Cut a Stick",
]


# ---------------------------------------------------------- build & emit ----
def homework_only(problems):
    return [p for p in problems if p["title"].startswith("Homework:")]


def build_index():
    """title -> dict, first-occurrence wins."""
    index = {}
    for p in (homework_only(make_md.PROBLEMS)
              + homework_only(make_md.PROBLEMS_21_30)
              + homework_only(make_md.PROBLEMS_GREEDY)
              + homework_only(make_md.PROBLEMS_01_10)
              + homework_only(dp_problems.PROBLEMS)
              + NEW_PROBLEMS_HW):
        index.setdefault(p["title"], p)
    return index


# -------------------------------------------------- HackerRank id overrides
# Titles that would otherwise match multiple live HackerRank challenges, and
# the one we want editor.py to actually update. Filled in after the first
# dry-run against HackerRank shows which titles are ambiguous.
HR_ID_OVERRIDE_HW = {
    # Titles that would otherwise match multiple live HackerRank challenges.
    # Each id was verified by name: the canonical (non-" 1"/" 2" suffix,
    # Homework-not-Classwork) copy is the one pinned here.
    "Homework: LC100 Same Tree":                       591618,
    "Homework: LC129 Sum Root to Leaf Numbers":        591641,
    "Homework: Minimum number of coins (GfG)":         591974,
    "Homework: Rearrange characters so that none are adjacent (GfG)": 591986,
}


# -------------------------------------------------------- explanations ----
# One entry per homework problem title. A value can be a plain string (used
# ONLY for Sample 1), a list of strings (index i is the explanation for
# Sample i+1; None skips), or a callable f(case, output) -> str (used for
# every sample it's asked for). Explanations describe what the output MEANS
# for the given input in plain English -- no algorithm names, no code hints.
EXPLANATIONS_HW = {
    # ------------------------------------------------------------ LEC-11 ----
    "Homework: Find the sum of all node values in a binary tree":
        lambda c, o: "Adding up every node's value gives `%s`." % o,

    "Homework: LC589 N-ary Tree Preorder Traversal":
        lambda c, o: (
            "Visiting each node before its children (children in the order "
            "they were added) produces `%s`." % (o if o else
                                                 "(nothing, the tree is empty)")),

    "Homework: Count the total number of nodes recursively":
        lambda c, o: "The tree has `%s` nodes in all." % o,

    "Homework: Print all leaf nodes from left to right":
        lambda c, o: (
            "Reading the leaves (nodes with no children) from left to right "
            "gives `%s`." % (o if o else "(nothing, there are no leaves)")),

    # ------------------------------------------------------------ LEC-12 ----
    "Homework: LC993 Cousins in Binary Tree":
        lambda c, o: (
            "The two values are cousins when they sit at the same depth but "
            "have different parents. Here the answer is `%s`." % o),

    "Homework: LC637 Average of Levels in Binary Tree":
        lambda c, o: (
            "Each printed line is the mean of the values on one level, from "
            "the root downwards."),

    "Homework: LC103 Binary Tree Zigzag Level Order Traversal":
        lambda c, o: (
            "One line per level, alternating direction: left-to-right on "
            "level 0, right-to-left on level 1, and so on."),

    "Homework: LC107 Binary Tree Level Order Traversal II":
        lambda c, o: (
            "One line per level, printed deepest first. Each line lists the "
            "values on that level from left to right."),

    # ------------------------------------------------------------ LEC-13 ----
    "Homework: Find the maximum node value in a binary tree":
        lambda c, o: "The largest value stored anywhere in the tree is `%s`." % o,

    "Homework: LC559 Maximum Depth of N-ary Tree":
        lambda c, o: (
            "The longest root-to-leaf path passes through `%s` nodes." % o),

    "Homework: Check whether two trees have equal height":
        lambda c, o: (
            "The two trees %s the same height, so the answer is `%s`."
            % ("have" if o == "true" else "do not have", o)),

    "Homework: Count the number of nodes at maximum depth":
        lambda c, o: (
            "At the deepest level of the tree there are `%s` nodes." % o),

    # ------------------------------------------------------------ LEC-14 ----
    "Homework: Count the number of leaf nodes in a binary tree":
        lambda c, o: "The tree has `%s` leaf node(s) in all." % o,

    "Homework: LC100 Same Tree":
        lambda c, o: (
            "Two trees are the `same` when they share the exact same shape "
            "and the same value at every position. Here the answer is `%s`."
            % o),

    "Homework: LC965 Univalued Binary Tree":
        lambda c, o: (
            "The tree is univalued when every node holds the same value. "
            "Here the answer is `%s`." % o),

    "Homework: LC872 Leaf-Similar Trees":
        lambda c, o: (
            "Two trees are `leaf-similar` when their leaves, read left to "
            "right, form the same sequence. Here the answer is `%s`." % o),

    # ------------------------------------------------------------ LEC-15 ----
    "Homework: Right view of a binary tree (GfG)":
        lambda c, o: (
            "Standing on the right, at each level you only see the "
            "rightmost value. Reading top to bottom gives `%s`." % o),

    "Homework: Bottom view of a binary tree (GfG)":
        lambda c, o: (
            "Looking straight up from below, each vertical column shows the "
            "bottommost value. Reading columns left to right gives `%s`." % o),

    "Homework: Diagonal traversal of a binary tree (GfG)":
        lambda c, o: (
            "One line per diagonal (right children stay on the same "
            "diagonal, left children move to the next one)."),

    "Homework: Morris inorder traversal (O(1) space) (GfG)":
        lambda c, o: (
            "Same left-root-right order as a normal inorder walk, produced "
            "using no extra stack. The values are `%s`." % o),

    # ------------------------------------------------------------ LEC-16 ----
    "Homework: LC617 Merge Two Binary Trees":
        lambda c, o: (
            "Where both trees have a node, the merged value is the sum. "
            "Where only one has a node, it stays as is. Result in level "
            "order: `%s`." % o),

    "Homework: Check if one tree is the mirror of another (GfG)":
        lambda c, o: (
            "One tree is the mirror of the other when their shapes are "
            "reflections and matching values line up. Here the answer is "
            "`%s`." % o),

    "Homework: Convert a tree to its mirror in place (GfG)":
        lambda c, o: (
            "Every node's children have been swapped, flipping the tree "
            "horizontally. Result in level order: `%s`." % o),

    "Homework: LC951 Flip Equivalent Binary Trees":
        lambda c, o: (
            "Two trees are flip-equivalent when one can be turned into the "
            "other by swapping some nodes' two children. Here the answer is "
            "`%s`." % o),

    # ------------------------------------------------------------ LEC-17 ----
    "Homework: LC257 Binary Tree Paths":
        lambda c, o: (
            "Each printed line traces one root-to-leaf path, with the "
            "values joined by `->`."),

    "Homework: LC437 Path Sum III":
        lambda c, o: (
            "Counting every downward path (start and end anywhere on a "
            "root-to-leaf line) whose values sum to the target gives `%s`."
            % o),

    "Homework: LC129 Sum Root to Leaf Numbers":
        lambda c, o: (
            "Each root-to-leaf path forms a number by concatenating its "
            "digits. Adding those numbers gives `%s`." % o),

    "Homework: LC988 Smallest String Starting From Leaf":
        lambda c, o: (
            "Turning each root-to-leaf path into a string (leaf first, "
            "using `a`..`z` for `0`..`25`), the lexicographically smallest "
            "is `%s`." % o),

    # ------------------------------------------------------------ LEC-18 ----
    "Homework: Find the level of a given node in a binary tree":
        lambda c, o: (
            "Counting the root as level 1, the target sits at level `%s` "
            "(or `-1` if it is not in the tree)." % o),

    "Homework: LC1650 Lowest Common Ancestor III":
        lambda c, o: (
            "The deepest node that has both target nodes in its subtree is "
            "`%s`." % o),

    "Homework: LC1123 Lowest Common Ancestor of Deepest Leaves":
        lambda c, o: (
            "Find the deepest level; the LCA of all leaves at that level is "
            "the answer."),

    "Homework: Kth ancestor of a node in a tree (GfG)":
        lambda c, o: (
            "Starting from the target and walking `k` steps up the tree "
            "reaches `%s` (or `-1` if that walk falls off the top)." % o),

    # ------------------------------------------------------------ LEC-19 ----
    "Homework: LC108 Convert Sorted Array to Binary Search Tree":
        lambda c, o: (
            "Choosing the middle value as the root at every step keeps the "
            "tree balanced. Result in level order: `%s`." % o),

    "Homework: LC889 Construct Binary Tree from Preorder and Postorder":
        lambda c, o: (
            "The first value in preorder is the root; the value just after "
            "it identifies the left subtree's postorder segment. The rebuilt "
            "tree in level order is `%s`." % o),

    "Homework: LC1008 Construct BST from Preorder Traversal":
        lambda c, o: (
            "Values arrive in preorder; each value slots into the BST at "
            "the first empty spot that keeps the tree valid. Result: `%s`."
            % o),

    "Homework: LC426 Convert BST to Sorted Doubly Linked List":
        lambda c, o: (
            "Walking the wired-up list from smallest to largest visits the "
            "BST's values in increasing order: `%s`."
            % (o if o else "(nothing, the tree is empty)")),

    # ------------------------------------------------------------ LEC-20 ----
    "Homework: LC404 Sum of Left Leaves":
        lambda c, o: (
            "Adding the values of leaves that are the left child of their "
            "parent gives `%s`." % o),

    "Homework: LC662 Maximum Width of Binary Tree":
        lambda c, o: (
            "The widest level of the tree spans `%s` positions from its "
            "leftmost to its rightmost node." % o),

    "Homework: LC116 Populating Next Right Pointers in Each Node":
        lambda c, o: (
            "Reading the wired-up tree level by level, each level's values "
            "are printed left to right and terminated by `#`."),

    # ------------------------------------------------------------ LEC-21 ----
    "Homework: Find the minimum and maximum value in a BST":
        lambda c, o: (
            "The leftmost node holds the smallest value and the rightmost "
            "holds the largest: `%s`." % o),

    "Homework: Count BST nodes lying in a given range (GfG)":
        lambda c, o: (
            "Counting the BST values that lie inside the given range gives "
            "`%s`." % o),

    "Homework: Iterative BST insert (GfG)":
        lambda c, o: (
            "The key slots into the first empty spot that keeps the tree a "
            "valid BST. The updated tree in level order is `%s`." % o),

    "Homework: Search keys within a range in a BST (GfG)":
        lambda c, o: (
            "Every BST value that falls inside the range is listed in "
            "increasing order: `%s`." % o),

    # ------------------------------------------------------------ LEC-22 ----
    "Homework: LC897 Increasing Order Search Tree":
        lambda c, o: (
            "Rearranged as a right-only chain, the BST's values appear in "
            "increasing order: `%s`."
            % (o if o else "(nothing, the tree is empty)")),

    "Homework: LC783 Minimum Distance Between BST Nodes":
        lambda c, o: (
            "Looking at every pair of BST values, the smallest absolute "
            "difference is `%s`." % o),

    "Homework: LC99 Recover Binary Search Tree":
        lambda c, o: (
            "Exactly two nodes were swapped; putting them back yields the "
            "valid BST printed."),

    "Homework: LC255 Verify Preorder Sequence in BST":
        lambda c, o: (
            "A sequence is a valid BST preorder when it can be split into a "
            "root, a smaller left-subtree run and a larger right-subtree "
            "run. Here the answer is `%s`." % o),

    # ------------------------------------------------------------ LEC-23 ----
    "Homework: Find the floor value of a key in a BST (GfG)":
        lambda c, o: (
            "The largest BST value less than or equal to the key is `%s` "
            "(or `-1` if every value in the tree is bigger)." % o),

    "Homework: LC669 Trim a Binary Search Tree":
        lambda c, o: (
            "Nodes whose values fall outside `[lo, hi]` are dropped; the "
            "remaining nodes still form a valid BST. Result in level order: "
            "`%s`." % o),

    "Homework: LC285 Inorder Successor in BST":
        lambda c, o: (
            "The smallest BST value strictly greater than the key is `%s` "
            "(or `null` if there is none)." % o),

    "Homework: Inorder predecessor in a BST (GfG)":
        lambda c, o: (
            "The largest BST value strictly smaller than the key is `%s` "
            "(or `null` if there is none)." % o),

    # ------------------------------------------------------------ LEC-24 ----
    "Homework: Count the total nodes and height of a BST":
        lambda c, o: (
            "Line 1 is the total node count. Line 2 is the height (number "
            "of nodes on the longest root-to-leaf path)."),

    "Homework: LC653 Two Sum IV - Input is a BST":
        lambda c, o: (
            "%s two different BST values that add up to the target, so the "
            "answer is `%s`."
            % ("There exist" if o == "true" else "There are no", o)),

    "Homework: LC938 Range Sum of BST":
        lambda c, o: (
            "Adding up every BST value that falls inside `[lo, hi]` gives "
            "`%s`." % o),

    "Homework: LC109 Convert Sorted List to Binary Search Tree":
        lambda c, o: (
            "Picking the middle value as the root at every step keeps the "
            "tree balanced. Result in level order: `%s`." % o),

    # ------------------------------------------------------------ LEC-25 ----
    "Homework: Convert a BST into a sorted vector":
        lambda c, o: (
            "Reading the BST left-root-right lists the values in increasing "
            "order: `%s`."
            % (o if o else "(nothing, the tree is empty)")),

    "Homework: LC538 Convert BST to Greater Tree":
        lambda c, o: (
            "Every node's value is replaced by the sum of itself and every "
            "value larger than it in the original tree."),

    "Homework: LC1382 Balance a Binary Search Tree":
        lambda c, o: (
            "Rebuilding the BST from its sorted values so that its height "
            "is as small as possible gives the level-order tree `%s`." % o),

    "Homework: LC333 Largest BST Subtree":
        lambda c, o: (
            "The largest subtree that is itself a valid BST contains `%s` "
            "nodes." % o),

    # ------------------------------------------------------------ LEC-26 ----
    "Homework: LC561 Array Partition":
        lambda c, o: (
            "Pairing the sorted values (1st with 2nd, 3rd with 4th, ...) "
            "and summing the smaller of each pair gives `%s`." % o),

    "Homework: LC452 Minimum Number of Arrows to Burst Balloons":
        lambda c, o: (
            "Grouping overlapping balloons together, `%s` arrows are needed "
            "to burst every balloon." % o),

    "Homework: LC646 Maximum Length of Pair Chain":
        lambda c, o: (
            "Chaining pairs `(a, b) -> (c, d)` where `c > b`, the longest "
            "such chain has length `%s`." % o),

    "Homework: Maximize meetings attended in one room (GfG)":
        lambda c, o: (
            "Attending as many non-overlapping meetings as possible fits "
            "`%s` of them." % o),

    # ------------------------------------------------------------ LEC-27 ----
    "Homework: LC252 Meeting Rooms":
        lambda c, o: (
            "One person can attend every meeting only when no two intervals "
            "overlap. Here the answer is `%s`." % o),

    "Homework: LC986 Interval List Intersections":
        lambda c, o: (
            "Each printed interval is the overlap of one interval from list "
            "A with one from list B."),

    "Homework: LC1094 Car Pooling":
        lambda c, o: (
            "Watching the passenger count over time, the car %s over "
            "capacity, so the answer is `%s`."
            % ("never goes" if o == "true" else "goes", o)),

    "Homework: Maximum number of overlapping intervals (GfG)":
        lambda c, o: (
            "At the busiest moment `%s` intervals are active at the same "
            "time." % o),

    # ------------------------------------------------------------ LEC-28 ----
    "Homework: LC1710 Maximum Units on a Truck":
        lambda c, o: (
            "Loading the box types with the most units per box first, the "
            "largest total units the truck can carry is `%s`." % o),

    "Homework: LC455 Assign Cookies":
        lambda c, o: (
            "Handing the smallest sufficient cookie to each child, `%s` "
            "children end up satisfied." % o),

    "Homework: Minimum number of coins (GfG)":
        lambda c, o: (
            "Using each denomination any number of times, the smallest "
            "count of coins that sums to the amount is `%s` (or `-1` if "
            "the amount cannot be made)." % o),

    "Homework: Huffman Encoding (GfG)":
        lambda c, o: (
            "Each printed line is the code word assigned to one character "
            "by the Huffman construction."),

    # ------------------------------------------------------------ LEC-29 ----
    "Homework: LC121 Best Time to Buy and Sell Stock":
        lambda c, o: (
            "Buying on the day with the lowest price seen so far and "
            "selling later, the largest profit is `%s`." % o),

    "Homework: LC45 Jump Game II":
        lambda c, o: (
            "The fewest jumps needed to reach the last index from index 0 "
            "is `%s`." % o),

    "Homework: LC763 Partition Labels":
        lambda c, o: (
            "The string is split into as many pieces as possible such that "
            "no letter appears in two pieces; the printed numbers are those "
            "piece lengths."),

    "Homework: Write-up: a coin system where greedy fails (counterexample)":
        lambda c, o: (
            "Line 1 is the greedy answer (always take the largest coin "
            "that fits). Line 2 is the true optimum. When they differ, "
            "this input proves the greedy rule is not always right."),

    # ------------------------------------------------------------ LEC-30 ----
    "Homework: LC942 DI String Match":
        lambda c, o: (
            "The printed permutation of `0..n` matches the `I`/`D` pattern: "
            "goes up at each `I` and down at each `D`."),

    "Homework: LC860 Lemonade Change":
        lambda c, o: (
            "Handing change from the largest bills first, the vendor %s "
            "give correct change to every customer, so the answer is `%s`."
            % ("can" if o == "true" else "cannot", o)),

    "Homework: Rearrange characters so that none are adjacent (GfG)":
        lambda c, o: (
            "A valid rearrangement has no two neighbouring characters "
            "equal. If none is possible the output is empty."),

    "Homework: LC1353 Maximum Number of Events That Can Be Attended":
        lambda c, o: (
            "Attending one event per day, `%s` events can be attended in "
            "total." % o),

    # ------------------------------------------------------------ LEC-31 ----
    "Homework: LC1137 N-th Tribonacci Number":
        lambda c, o: (
            "`T(0) = 0`, `T(1) = T(2) = 1`, and each later value is the "
            "sum of the previous three. `T(%s) = %s`." % (c.strip(), o)),

    "Homework: LC746 Min Cost Climbing Stairs":
        lambda c, o: (
            "The smallest total cost to reach the top of the staircase is "
            "`%s`." % o),

    "Homework: LC213 House Robber II":
        lambda c, o: (
            "Houses are arranged in a circle; robbing two adjacent ones is "
            "not allowed. The largest safe total is `%s`." % o),

    "Homework: LC91 Decode Ways":
        lambda c, o: (
            "Using the mapping `1 -> A, 2 -> B, ..., 26 -> Z`, the digit "
            "string can be decoded in `%s` distinct ways." % o),

    # ------------------------------------------------------------ LEC-32 ----
    "Homework: Count ways to climb stairs with steps of 1, 2 or 3 (GfG)":
        lambda c, o: (
            "Taking strides of 1, 2, or 3 steps at a time, the staircase of "
            "height `%s` can be climbed in `%s` distinct ways."
            % (c.strip(), o)),

    "Homework: LC377 Combination Sum IV":
        lambda c, o: (
            "The number of **ordered** ways to reach the target using the "
            "given numbers (any number may be picked more than once) is "
            "`%s`." % o),

    "Homework: LC279 Perfect Squares":
        lambda c, o: (
            "The smallest number of perfect squares that add up to the "
            "given integer is `%s`." % o),

    "Homework: Number of ways to make change (GfG)":
        lambda c, o: (
            "Using each denomination any number of times, the number of "
            "distinct combinations that make the amount is `%s`." % o),

    # ------------------------------------------------------------ LEC-33 ----
    "Homework: LC392 Is Subsequence":
        lambda c, o: (
            "`s` is a subsequence of `t` when its characters appear in `t` "
            "in the same order (not necessarily consecutively). Here the "
            "answer is `%s`." % o),

    "Homework: LC673 Number of Longest Increasing Subsequence":
        lambda c, o: (
            "Counting every longest strictly increasing subsequence gives "
            "`%s`." % o),

    "Homework: LC1035 Uncrossed Lines":
        lambda c, o: (
            "Matching equal values without crossing lines, the largest "
            "number of lines is `%s`." % o),

    "Homework: Longest common substring (GfG)":
        lambda c, o: (
            "The longest run of characters that appears **contiguously** in "
            "both strings has length `%s`." % o),

    # ------------------------------------------------------------ LEC-34 ----
    "Homework: LC118 Pascal's Triangle":
        lambda c, o: (
            "Row `i` has `i + 1` entries; the first and last are `1` and "
            "each other entry is the sum of the two above it."),

    "Homework: LC120 Triangle":
        lambda c, o: (
            "Moving from top to bottom taking one of the two adjacent "
            "numbers each step, the smallest possible total is `%s`." % o),

    "Homework: LC931 Minimum Falling Path Sum":
        lambda c, o: (
            "Falling one row at a time (each step goes straight down or "
            "diagonally), the smallest total is `%s`." % o),

    "Homework: LC221 Maximal Square":
        lambda c, o: (
            "The largest all-`1`s square that fits inside the grid has "
            "area `%s`." % o),

    # ------------------------------------------------------------ LEC-35 ----
    "Homework: Count subsets of a 5-element array with sum K by brute force":
        lambda c, o: (
            "Trying every subset of the input array, `%s` of them sum "
            "exactly to the target." % o),

    "Homework: Count of subsets with a given sum (GfG)":
        lambda c, o: (
            "Counting subsets that sum to the target gives `%s`." % o),

    "Homework: Maximum sum of non-adjacent elements (GfG)":
        lambda c, o: (
            "Picking values without taking two neighbours, the largest sum "
            "you can get is `%s`." % o),

    "Homework: LC740 Delete and Earn":
        lambda c, o: (
            "Deleting a value costs you all copies of the neighbours "
            "(value-1 and value+1); the largest total you can still earn "
            "is `%s`." % o),

    # ------------------------------------------------------------ LEC-36 ----
    "Homework: Print the full DP table for subset-sum on a 4-element array":
        lambda c, o: (
            "Row `i`, column `j`: `1` if some subset of the first `i` "
            "values of the array sums to `j`, else `0`. Row 0 is the empty "
            "subset -- only column 0 is `1`."),

    "Homework: Count subsets with a given difference (GfG)":
        lambda c, o: (
            "Splitting the array into two subsets whose sums differ by the "
            "target, the number of valid splits is `%s`." % o),

    "Homework: LC1049 Last Stone Weight II":
        lambda c, o: (
            "Splitting the stones into two groups and taking the "
            "difference of their weights, the smallest possible remainder "
            "is `%s`." % o),

    "Homework: Minimum subset-sum difference (GfG)":
        lambda c, o: (
            "Splitting the array into two subsets, the smallest possible "
            "difference of their sums is `%s`." % o),

    # ------------------------------------------------------------ LEC-37 ----
    "Homework: Count ways to reach amount N using coins of 1 and 2 (GfG)":
        lambda c, o: (
            "Using coins of denomination 1 and 2, and counting the order "
            "of use as different, there are `%s` ways to make `%s`."
            % (o, c.strip())),

    "Homework: LC518 Coin Change II":
        lambda c, o: (
            "Counting distinct combinations of coins (order does not "
            "matter) that add up to the target amount gives `%s`." % o),

    "Homework: Maximum ribbon cut (GfG)":
        lambda c, o: (
            "Cutting a ribbon of the given length into pieces of the "
            "allowed sizes, the largest number of pieces possible is `%s`."
            % o),

    "Homework: LC343 Integer Break":
        lambda c, o: (
            "Splitting the integer into at least two positive parts, the "
            "largest possible product of those parts is `%s`." % o),

    # ------------------------------------------------------------ LEC-38 ----
    "Homework: LC125 Valid Palindrome":
        lambda c, o: (
            "Ignoring case and non-alphanumeric characters, the string %s "
            "read the same forwards and backwards, so the answer is `%s`."
            % ("does" if o == "true" else "does not", o)),

    "Homework: LC161 One Edit Distance":
        lambda c, o: (
            "The two strings differ by exactly one insertion, deletion, or "
            "substitution: `%s`." % o),

    "Homework: LC97 Interleaving String":
        lambda c, o: (
            "The third string %s be formed by interleaving the first two "
            "in order, so the answer is `%s`."
            % ("can" if o == "true" else "cannot", o)),

    "Homework: LC115 Distinct Subsequences":
        lambda c, o: (
            "Counting how many ways the second string appears as a "
            "subsequence of the first gives `%s`." % o),

    # ------------------------------------------------------------ LEC-39 ----
    "Homework: Count palindromic substrings of length 1 and 2 by brute force":
        lambda c, o: (
            "Every length-1 substring is a palindrome, and a length-2 one "
            "is a palindrome exactly when both characters match. The total "
            "is `%s`." % o),

    "Homework: LC5 Longest Palindromic Substring":
        lambda c, o: (
            "The longest **contiguous** run of characters in the string "
            "that reads the same forwards and backwards is `%s`." % o),

    "Homework: LC647 Palindromic Substrings":
        lambda c, o: (
            "Counting every contiguous substring that is a palindrome "
            "gives `%s`." % o),

    "Homework: LC1312 Minimum Insertion Steps to Make a String Palindrome":
        lambda c, o: (
            "Inserting `%s` character(s) somewhere in the string turns it "
            "into a palindrome." % o),

    # ------------------------------------------------------------ LEC-40 ----
    "Homework: Precompute an isPalindrome[i][j] table for a string":
        lambda c, o: (
            "Row `i`, column `j`: `1` when the substring from index `i` "
            "through `j` reads the same forwards and backwards, else `0`."),

    "Homework: LC1043 Partition Array for Maximum Sum":
        lambda c, o: (
            "Splitting the array into contiguous pieces of length at most "
            "`k` and replacing each piece by its maximum times its length, "
            "the largest total is `%s`." % o),

    "Homework: Boolean Parenthesization (GfG)":
        lambda c, o: (
            "Counting how many ways the boolean expression can be "
            "parenthesised so that it evaluates to `true` gives `%s`." % o),

    "Homework: LC1547 Minimum Cost to Cut a Stick":
        lambda c, o: (
            "Choosing the cut order carefully, the smallest total cost of "
            "making every cut is `%s`." % o),
}


# ---------------------------------------------------------- local emit -----
# Local copy of make_md.emit that also drops a plain-language
# `**Sample Explanation N**` after the first `N_EXPLAIN_CASES` sample outputs
# whenever EXPLANATIONS_HW knows about the title.
N_EXPLAIN_CASES = 2


def _explain_for(title, idx, case, output):
    entry = EXPLANATIONS_HW.get(title)
    if entry is None:
        return ""
    if callable(entry):
        return entry(case, output)
    if isinstance(entry, str):
        return entry if idx == 1 else ""
    if isinstance(entry, (list, tuple)):
        if idx - 1 < len(entry):
            v = entry[idx - 1]
            if callable(v):
                return v(case, output)
            return v or ""
    return ""


def emit_with_explanations(path, problems, links=True):
    lines = ["# DSA-301 homework challenges", "",
             "Generated by make_homework_missing_md.py. Sample outputs are "
             "computed from the reference solutions, not written by hand.",
             "", "---", ""]
    for p in problems:
        lines.append("## %s" % p["title"])
        hr_id = HR_ID_OVERRIDE_HW.get(p["title"]) or p.get("hr_id")
        if hr_id:
            lines.append("<!-- hackerrank_id: %s -->" % hr_id)
        lines.append("")
        diff = DIFFICULTY_HW.get(p["title"])
        if diff:
            lines.append("**Difficulty**: %s" % diff)
            lines.append("")
        lines.append("**Problem Statement**")
        lines.append(p["stmt"])

        note = problem_links.note_for(p["title"]) if links else ""
        if note:
            lines.append("")
            lines.append(note)
        lines.append("")

        lines.append("**Input Format**")
        lines.append(p["inp"])
        lines.append("")
        lines.append("**Output Format**")
        lines.append(p["out"])
        lines.append("")
        lines.append("**Constraints**")
        lines.append(p["cons"])
        lines.append("")

        for i, c in enumerate(p["cases"], 1):
            out = p["solve"](c)
            lines.append("**Sample Input %d**" % i)
            lines.append("```")
            lines.append(c)
            lines.append("```")
            lines.append("**Sample Output %d**" % i)
            lines.append("```")
            lines.append(out)
            lines.append("```")
            if i <= N_EXPLAIN_CASES:
                expl = _explain_for(p["title"], i, c, out)
                if expl:
                    lines.append("**Sample Explanation %d**" % i)
                    lines.append(expl)
            lines.append("")
        lines.append("---")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


# Titles that don't yet have a HackerRank challenge shell. Pass
# --missing-only to emit just these into DSA301_homework_shells_todo.md.
# Populated from the first HackerRank dry-run.
SHELLS_TO_CREATE_HW = {
    # Titles with no existing HackerRank challenge. Pass --missing-only to
    # emit a DSA301_homework_shells_todo.md containing just these, ready
    # for you to create shells (title + difficulty only) on HackerRank.
    # After the shells exist, editor.py --apply --tests fills them in.
    "Homework: Find the sum of all node values in a binary tree",
    "Homework: LC993 Cousins in Binary Tree",
    "Homework: Find the maximum node value in a binary tree",
    "Homework: Count the number of leaf nodes in a binary tree",
    "Homework: Right view of a binary tree (GfG)",
    "Homework: LC617 Merge Two Binary Trees",
    "Homework: LC257 Binary Tree Paths",
    "Homework: Find the level of a given node in a binary tree",
    "Homework: LC404 Sum of Left Leaves",
    "Homework: Find the minimum and maximum value in a BST",
    "Homework: LC897 Increasing Order Search Tree",
    "Homework: Find the floor value of a key in a BST (GfG)",
    "Homework: Count the total nodes and height of a BST",
    "Homework: Convert a BST into a sorted vector",
    "Homework: LC561 Array Partition",
    "Homework: LC252 Meeting Rooms",
    "Homework: LC1710 Maximum Units on a Truck",
    "Homework: LC121 Best Time to Buy and Sell Stock",
    "Homework: LC942 DI String Match",
    "Homework: LC1137 N-th Tribonacci Number",
    "Homework: Count ways to climb stairs with steps of 1, 2 or 3 (GfG)",
    "Homework: LC392 Is Subsequence",
    "Homework: LC118 Pascal's Triangle",
    "Homework: Count subsets of a 5-element array with sum K by brute force",
    "Homework: Print the full DP table for subset-sum on a 4-element array",
    "Homework: Count ways to reach amount N using coins of 1 and 2 (GfG)",
    "Homework: LC125 Valid Palindrome",
    "Homework: Count palindromic substrings of length 1 and 2 by brute force",
    "Homework: Precompute an isPalindrome[i][j] table for a string",
}


# The difficulty label per the curriculum sheet, for every homework row.
# Deduped by title -- if the sheet lists the same problem in two lectures
# with the same difficulty, one entry covers both. Any title not in this
# dict has no `**Difficulty**:` line rendered.
DIFFICULTY_HW = {
    # ---- LEC-11 (Easy, Easy, Easy, Easy) -----------------------------------
    "Homework: Find the sum of all node values in a binary tree": "Easy",
    "Homework: LC589 N-ary Tree Preorder Traversal": "Easy",
    "Homework: Count the total number of nodes recursively": "Easy",
    "Homework: Print all leaf nodes from left to right": "Easy",
    # ---- LEC-12 (Easy, Easy, Medium, Medium) -------------------------------
    "Homework: LC993 Cousins in Binary Tree": "Easy",
    "Homework: LC637 Average of Levels in Binary Tree": "Easy",
    "Homework: LC103 Binary Tree Zigzag Level Order Traversal": "Medium",
    "Homework: LC107 Binary Tree Level Order Traversal II": "Medium",
    # ---- LEC-13 (Easy, Easy, Easy, Medium) ---------------------------------
    "Homework: Find the maximum node value in a binary tree": "Easy",
    "Homework: LC559 Maximum Depth of N-ary Tree": "Easy",
    "Homework: Check whether two trees have equal height": "Easy",
    "Homework: Count the number of nodes at maximum depth": "Medium",
    # ---- LEC-14 (Easy, Easy, Easy, Easy) -----------------------------------
    "Homework: Count the number of leaf nodes in a binary tree": "Easy",
    "Homework: LC100 Same Tree": "Easy",
    "Homework: LC965 Univalued Binary Tree": "Easy",
    "Homework: LC872 Leaf-Similar Trees": "Easy",
    # ---- LEC-15 (Easy, Medium, Medium, Hard) -------------------------------
    "Homework: Right view of a binary tree (GfG)": "Easy",
    "Homework: Bottom view of a binary tree (GfG)": "Medium",
    "Homework: Diagonal traversal of a binary tree (GfG)": "Medium",
    "Homework: Morris inorder traversal (O(1) space) (GfG)": "Hard",
    # ---- LEC-16 (Easy, Easy, Easy, Medium) ---------------------------------
    "Homework: LC617 Merge Two Binary Trees": "Easy",
    "Homework: Check if one tree is the mirror of another (GfG)": "Easy",
    "Homework: Convert a tree to its mirror in place (GfG)": "Easy",
    "Homework: LC951 Flip Equivalent Binary Trees": "Medium",
    # ---- LEC-17 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC257 Binary Tree Paths": "Easy",
    "Homework: LC437 Path Sum III": "Medium",
    "Homework: LC129 Sum Root to Leaf Numbers": "Medium",
    "Homework: LC988 Smallest String Starting From Leaf": "Medium",
    # ---- LEC-18 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: Find the level of a given node in a binary tree": "Easy",
    "Homework: LC1650 Lowest Common Ancestor III": "Medium",
    "Homework: LC1123 Lowest Common Ancestor of Deepest Leaves": "Medium",
    "Homework: Kth ancestor of a node in a tree (GfG)": "Medium",
    # ---- LEC-19 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC108 Convert Sorted Array to Binary Search Tree": "Easy",
    "Homework: LC889 Construct Binary Tree from Preorder and Postorder": "Medium",
    "Homework: LC1008 Construct BST from Preorder Traversal": "Medium",
    "Homework: LC426 Convert BST to Sorted Doubly Linked List": "Medium",
    # ---- LEC-20 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC404 Sum of Left Leaves": "Easy",
    # LC129 dup -- already Medium above.
    "Homework: LC662 Maximum Width of Binary Tree": "Medium",
    "Homework: LC116 Populating Next Right Pointers in Each Node": "Medium",
    # ---- LEC-21 (Easy, Easy, Medium, Medium) -------------------------------
    "Homework: Find the minimum and maximum value in a BST": "Easy",
    "Homework: Count BST nodes lying in a given range (GfG)": "Easy",
    "Homework: Iterative BST insert (GfG)": "Medium",
    "Homework: Search keys within a range in a BST (GfG)": "Medium",
    # ---- LEC-22 (Easy, Easy, Medium, Medium) -------------------------------
    "Homework: LC897 Increasing Order Search Tree": "Easy",
    "Homework: LC783 Minimum Distance Between BST Nodes": "Easy",
    "Homework: LC99 Recover Binary Search Tree": "Medium",
    "Homework: LC255 Verify Preorder Sequence in BST": "Medium",
    # ---- LEC-23 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: Find the floor value of a key in a BST (GfG)": "Easy",
    "Homework: LC669 Trim a Binary Search Tree": "Medium",
    "Homework: LC285 Inorder Successor in BST": "Medium",
    "Homework: Inorder predecessor in a BST (GfG)": "Medium",
    # ---- LEC-24 (Easy, Easy, Easy, Medium) ---------------------------------
    "Homework: Count the total nodes and height of a BST": "Easy",
    "Homework: LC653 Two Sum IV - Input is a BST": "Easy",
    "Homework: LC938 Range Sum of BST": "Easy",
    "Homework: LC109 Convert Sorted List to Binary Search Tree": "Medium",
    # ---- LEC-25 (Easy, Medium, Medium, Hard) -------------------------------
    "Homework: Convert a BST into a sorted vector": "Easy",
    "Homework: LC538 Convert BST to Greater Tree": "Medium",
    "Homework: LC1382 Balance a Binary Search Tree": "Medium",
    "Homework: LC333 Largest BST Subtree": "Hard",
    # ---- LEC-26 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC561 Array Partition": "Easy",
    "Homework: LC452 Minimum Number of Arrows to Burst Balloons": "Medium",
    "Homework: LC646 Maximum Length of Pair Chain": "Medium",
    "Homework: Maximize meetings attended in one room (GfG)": "Medium",
    # ---- LEC-27 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC252 Meeting Rooms": "Easy",
    "Homework: LC986 Interval List Intersections": "Medium",
    "Homework: LC1094 Car Pooling": "Medium",
    "Homework: Maximum number of overlapping intervals (GfG)": "Medium",
    # ---- LEC-28 (Easy, Easy, Easy, Hard) -----------------------------------
    "Homework: LC1710 Maximum Units on a Truck": "Easy",
    "Homework: LC455 Assign Cookies": "Easy",
    "Homework: Minimum number of coins (GfG)": "Easy",
    "Homework: Huffman Encoding (GfG)": "Hard",
    # ---- LEC-29 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC121 Best Time to Buy and Sell Stock": "Easy",
    "Homework: LC45 Jump Game II": "Medium",
    "Homework: LC763 Partition Labels": "Medium",
    "Homework: Write-up: a coin system where greedy fails (counterexample)": "Medium",
    # ---- LEC-30 (Easy, Easy, Medium, Medium) -------------------------------
    "Homework: LC942 DI String Match": "Easy",
    "Homework: LC860 Lemonade Change": "Easy",
    "Homework: Rearrange characters so that none are adjacent (GfG)": "Medium",
    "Homework: LC1353 Maximum Number of Events That Can Be Attended": "Medium",
    # ---- LEC-31 (Easy, Easy, Medium, Medium) -------------------------------
    "Homework: LC1137 N-th Tribonacci Number": "Easy",
    "Homework: LC746 Min Cost Climbing Stairs": "Easy",
    "Homework: LC213 House Robber II": "Medium",
    "Homework: LC91 Decode Ways": "Medium",
    # ---- LEC-32 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: Count ways to climb stairs with steps of 1, 2 or 3 (GfG)": "Easy",
    "Homework: LC377 Combination Sum IV": "Medium",
    "Homework: LC279 Perfect Squares": "Medium",
    "Homework: Number of ways to make change (GfG)": "Medium",
    # ---- LEC-33 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC392 Is Subsequence": "Easy",
    "Homework: LC673 Number of Longest Increasing Subsequence": "Medium",
    "Homework: LC1035 Uncrossed Lines": "Medium",
    "Homework: Longest common substring (GfG)": "Medium",
    # ---- LEC-34 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: LC118 Pascal's Triangle": "Easy",
    "Homework: LC120 Triangle": "Medium",
    "Homework: LC931 Minimum Falling Path Sum": "Medium",
    "Homework: LC221 Maximal Square": "Medium",
    # ---- LEC-35 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: Count subsets of a 5-element array with sum K by brute force": "Easy",
    "Homework: Count of subsets with a given sum (GfG)": "Medium",
    "Homework: Maximum sum of non-adjacent elements (GfG)": "Medium",
    "Homework: LC740 Delete and Earn": "Medium",
    # ---- LEC-36 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: Print the full DP table for subset-sum on a 4-element array": "Easy",
    "Homework: Count subsets with a given difference (GfG)": "Medium",
    "Homework: LC1049 Last Stone Weight II": "Medium",
    "Homework: Minimum subset-sum difference (GfG)": "Medium",
    # ---- LEC-37 (Easy, Medium, Medium, Medium) -----------------------------
    "Homework: Count ways to reach amount N using coins of 1 and 2 (GfG)": "Easy",
    "Homework: LC518 Coin Change II": "Medium",
    "Homework: Maximum ribbon cut (GfG)": "Medium",
    "Homework: LC343 Integer Break": "Medium",
    # ---- LEC-38 (Easy, Medium, Medium, Hard) -------------------------------
    "Homework: LC125 Valid Palindrome": "Easy",
    "Homework: LC161 One Edit Distance": "Medium",
    "Homework: LC97 Interleaving String": "Medium",
    "Homework: LC115 Distinct Subsequences": "Hard",
    # ---- LEC-39 (Easy, Medium, Medium, Hard) -------------------------------
    "Homework: Count palindromic substrings of length 1 and 2 by brute force": "Easy",
    "Homework: LC5 Longest Palindromic Substring": "Medium",
    "Homework: LC647 Palindromic Substrings": "Medium",
    "Homework: LC1312 Minimum Insertion Steps to Make a String Palindrome": "Hard",
    # ---- LEC-40 (Easy, Medium, Hard, Hard) ---------------------------------
    "Homework: Precompute an isPalindrome[i][j] table for a string": "Easy",
    "Homework: LC1043 Partition Array for Maximum Sum": "Medium",
    "Homework: Boolean Parenthesization (GfG)": "Hard",
    "Homework: LC1547 Minimum Cost to Cut a Stick": "Hard",
}


def main():
    missing_only = "--missing-only" in sys.argv[1:]

    index = build_index()

    # Sheet-order, deduped: keeping the first sighting of each title.
    seen = set()
    ordered_titles = []
    missing = []
    for t in SHEET_TITLES_HW:
        if t in seen:
            continue
        seen.add(t)
        if t in index:
            ordered_titles.append(t)
        else:
            missing.append(t)

    if missing:
        print("MISSING problem dicts (%d):" % len(missing))
        for t in missing:
            print("  %s" % t)
        sys.exit(1)

    if missing_only:
        problems = [index[t] for t in ordered_titles
                    if t in SHELLS_TO_CREATE_HW]
        out_name = "DSA301_homework_shells_todo.md"
    else:
        problems = [index[t] for t in ordered_titles]
        out_name = "DSA301_homework_missing.md"

    # Runtime sanity: run each solve on every case so a broken lambda blows
    # up here rather than silently producing empty output in the MD.
    for p in problems:
        for c in p["cases"]:
            p["solve"](c)

    # Warn (but do not fail) if a problem has no explanation registered.
    unexplained = [p["title"] for p in problems
                   if p["title"] not in EXPLANATIONS_HW]
    if unexplained:
        print("no explanation registered for %d problem(s):"
              % len(unexplained))
        for t in unexplained:
            print("  %s" % t)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        out_name)
    emit_with_explanations(path, problems, links=True)

    print("wrote %s" % os.path.basename(path))
    print("  %d homework problems (deduped from %d sheet rows)"
          % (len(problems), len(SHEET_TITLES_HW)))
    print("  %d total test cases" % sum(len(p["cases"]) for p in problems))
    print("  %d problems with an explanation"
          % (len(problems) - len(unexplained)))


if __name__ == "__main__":
    main()
