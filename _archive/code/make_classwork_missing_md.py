#!/usr/bin/env python3
"""
make_classwork_missing_md.py -- generate DSA301_classwork_missing.md.

Emits every classwork problem from LEC-11 to LEC-40, in sheet order, deduped.
Reuses every classwork dict already defined in make_md.py / dp_problems.py and
adds fresh dicts for the ~30 that were missing (the pen-and-paper Easy trace
exercises and the LC/GfG problems not yet authored). Sample outputs are
COMPUTED by the reference solutions, never typed by hand.

    python make_classwork_missing_md.py

Extends problem_links.LEETCODE / GFG at runtime so the shared emit() picks up
LC / GfG links for every new problem without touching problem_links.py.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import make_md
import dp_problems
import problem_links
from collections import Counter, deque

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
# The LC entries and the GfG entries that the ~30 new problems below reference.
# Merging them at runtime lets make_md.emit() append the standard "You can also
# try this problem on: [...]" line without touching problem_links.py.
_NEW_LEETCODE = {
    100 : ("same-tree",                                       "Same Tree",                                       False),
    101 : ("symmetric-tree",                                  "Symmetric Tree",                                  False),
    124 : ("binary-tree-maximum-path-sum",                    "Binary Tree Maximum Path Sum",                    False),
    173 : ("binary-search-tree-iterator",                     "Binary Search Tree Iterator",                     False),
    199 : ("binary-tree-right-side-view",                     "Binary Tree Right Side View",                     False),
    297 : ("serialize-and-deserialize-binary-tree",           "Serialize and Deserialize Binary Tree",           False),
    605 : ("can-place-flowers",                               "Can Place Flowers",                               False),
    653 : ("two-sum-iv-input-is-a-bst",                       "Two Sum IV - Input is a BST",                     False),
    669 : ("trim-a-binary-search-tree",                       "Trim a Binary Search Tree",                       False),
    674 : ("longest-continuous-increasing-subsequence",       "Longest Continuous Increasing Subsequence",       False),
    938 : ("range-sum-of-bst",                                "Range Sum of BST",                                False),
    1005: ("maximize-sum-of-array-after-k-negations",         "Maximize Sum Of Array After K Negations",         False),
    1480: ("running-sum-of-1d-array",                         "Running Sum of 1d Array",                         False),
}
problem_links.LEETCODE.update(_NEW_LEETCODE)

_NEW_GFG = {
    "Classwork: Left view of a binary tree (GfG)":
        ("left-view-of-binary-tree", "Left View of Binary Tree"),
    "Classwork: LCA using root-to-node paths (GfG)":
        ("lowest-common-ancestor-in-a-binary-tree",
         "Lowest Common Ancestor in a Binary Tree"),
    "Classwork: Find the ceiling of a key in a BST (GfG)":
        ("implementing-ceil-in-bst", "Implementing Ceil in BST"),
    "Classwork: Minimum cost to connect ropes (GfG)":
        ("minimum-cost-of-ropes-1587115620", "Min Cost to Connect Ropes"),
    "Classwork: Minimum number of coins (GfG)":
        ("number-of-coins1824", "Coin Change (Minimum Coins)"),
}
problem_links.GFG.update(_NEW_GFG)


# ------------------------------------------------------------- solving helpers
def right_view(root):
    """Rightmost node value at each level, top-down."""
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


def left_view(root):
    """Leftmost node value at each level, top-down."""
    out, q = [], deque([root] if root else [])
    while q:
        n_items = len(q)
        for i in range(n_items):
            n = q.popleft()
            if i == 0:
                out.append(n.v)
            if n.l: q.append(n.l)
            if n.r: q.append(n.r)
    return out


def bfs_flat(root):
    """Every node value in BFS order as one flat list."""
    out, q = [], deque([root] if root else [])
    while q:
        n = q.popleft()
        out.append(n.v)
        if n.l: q.append(n.l)
        if n.r: q.append(n.r)
    return out


def is_full(root):
    """A full binary tree has every internal node with EXACTLY two children."""
    if not root:
        return True
    for n in iter_nodes(root):
        if (n.l is None) != (n.r is None):
            return False
    return True


def is_symmetric(root):
    def sym(a, b):
        if not a and not b: return True
        if not a or not b: return False
        return a.v == b.v and sym(a.l, b.r) and sym(a.r, b.l)
    return sym(root, root)


def is_same(a, b):
    if not a and not b: return True
    if not a or not b: return False
    return a.v == b.v and is_same(a.l, b.l) and is_same(a.r, b.r)


def swap_root_children(root):
    if root:
        root.l, root.r = root.r, root.l
    return root


def sum_leaves(root):
    return sum(leaves(root))


def contains_value(root, v):
    for n in iter_nodes(root):
        if n.v == v:
            return True
    return False


def max_path_sum(root):
    """LC124: any path down through any pivot node."""
    if not root:
        return 0
    best = [float("-inf")]
    def go(n):
        if not n: return 0
        l = max(0, go(n.l))
        r = max(0, go(n.r))
        best[0] = max(best[0], n.v + l + r)
        return n.v + max(l, r)
    go(root)
    return best[0]


def bst_ceiling(root, key):
    """Smallest value >= key, or None."""
    res = None
    n = root
    while n:
        if n.v == key:
            return n.v
        if n.v < key:
            n = n.r
        else:
            res = n.v
            n = n.l
    return res


def range_sum_bst(root, lo, hi):
    tot = 0
    for n in iter_nodes(root):
        if lo <= n.v <= hi:
            tot += n.v
    return tot


def two_sum_bst(root, target):
    seen = set()
    for v in in_list(root):
        if target - v in seen:
            return True
        seen.add(v)
    return False


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


def bst_iterator_run(lines):
    """Input: BST on line 1, then a line with the query count `q`, then `q`
    lines each `next` or `hasNext`. Emit one line per query: the returned
    value for `next` (or `null` if the iterator is exhausted) and `true` /
    `false` for `hasNext`."""
    root = build(lines[0])
    q = int(lines[1])
    order = in_list(root)
    i = 0
    out = []
    for op in lines[2:2 + q]:
        cmd = op.strip()
        if cmd == "next":
            out.append(str(order[i]) if i < len(order) else "null")
            if i < len(order):
                i += 1
        elif cmd == "hasNext":
            out.append(fmt_bool(i < len(order)))
    return "\n".join(out)


def can_place_flowers(bed, k):
    """LC605: no two adjacent flowers; return whether k more can be planted."""
    a = bed[:]
    n = len(a)
    placed = 0
    for i in range(n):
        if a[i] == 0:
            left = (i == 0) or (a[i - 1] == 0)
            right = (i == n - 1) or (a[i + 1] == 0)
            if left and right:
                a[i] = 1
                placed += 1
    return placed >= k


def maximize_after_k_neg(a, k):
    """LC1005: negate any element up to k times to maximise the sum. Repeats
    on one element are allowed."""
    a = sorted(a)
    for i in range(len(a)):
        if k > 0 and a[i] < 0:
            a[i] = -a[i]
            k -= 1
        else:
            break
    a.sort()
    if k % 2 == 1:
        a[0] = -a[0]
    return sum(a)


def reorganize_string(s):
    """LC767: rearrange so no two adjacent are equal, or return '' impossible."""
    import heapq as _hq
    cnt = Counter(s)
    if max(cnt.values()) > (len(s) + 1) // 2:
        return ""
    h = [(-v, ch) for ch, v in cnt.items()]
    _hq.heapify(h)
    out = []
    prev_v, prev_ch = 0, ""
    while h:
        v, ch = _hq.heappop(h)
        out.append(ch)
        if prev_v < 0:
            _hq.heappush(h, (prev_v, prev_ch))
        prev_v, prev_ch = v + 1, ch
    return "".join(out) if len(out) == len(s) else ""


def task_scheduler(tasks, n):
    """LC621: minimum intervals to run every task with cooldown n between
    equal tasks."""
    c = Counter(tasks)
    mx = max(c.values())
    ties = sum(1 for v in c.values() if v == mx)
    return max(len(tasks), (mx - 1) * (n + 1) + ties)


def longest_cont_inc(a):
    """LC674: length of the longest strictly increasing run."""
    if not a:
        return 0
    best = cur = 1
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best


def running_sum(a):
    out = []
    s = 0
    for x in a:
        s += x
        out.append(s)
    return out


def decode_ways(s):
    """LC91."""
    if not s or s[0] == "0":
        return 0
    n = len(s)
    a, b = 1, 1
    for i in range(1, n):
        cur = 0
        if s[i] != "0":
            cur += b
        two_ = int(s[i - 1: i + 1])
        if 10 <= two_ <= 26:
            cur += a
        a, b = b, cur
    return b


def lca_via_paths(root, p, q):
    """LEC-18 GfG variant: find root-to-target paths for p and q, then walk
    until they diverge."""
    def path(n, t, cur):
        if not n:
            return False
        cur.append(n.v)
        if n.v == t or path(n.l, t, cur) or path(n.r, t, cur):
            return True
        cur.pop()
        return False
    ap, bp = [], []
    path(root, p, ap)
    path(root, q, bp)
    last = None
    for x, y in zip(ap, bp):
        if x == y:
            last = x
        else:
            break
    return last


def min_cost_ropes(a):
    """Repeatedly join the two shortest ropes; total cost = sum of joins."""
    import heapq as _hq
    h = list(a)
    _hq.heapify(h)
    total = 0
    while len(h) > 1:
        x = _hq.heappop(h)
        y = _hq.heappop(h)
        total += x + y
        _hq.heappush(h, x + y)
    return total


def min_coins_dp(coins, amt):
    """DP min-coins for `amt`, or -1 when impossible."""
    dp = [0] + [amt + 1] * amt
    for i in range(1, amt + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amt] if dp[amt] <= amt else -1


def coin_change_dp_row(coins, amt):
    """Line of dp[0..amt] where dp[i] is the min pieces for amount i;
    'x' when unreachable."""
    dp = [0] + [amt + 1] * amt
    for i in range(1, amt + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return " ".join((str(v) if v <= amt else "x") for v in dp)


def knap_dp_table(items, cap):
    """Full (n+1) x (cap+1) 0/1 knapsack DP table, printed one row per line."""
    n = len(items)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = items[i - 1]
        for c in range(cap + 1):
            dp[i][c] = dp[i - 1][c]
            if w <= c:
                dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)
    return "\n".join(" ".join(str(x) for x in row) for row in dp)


def parse_kn(s):
    """First line 'n W', next n lines 'w v'."""
    r = rows(s)
    n, cap = ints(r[0])
    items = [tuple(ints(x)) for x in r[1:1 + n]]
    return items, cap


def value_weight_order(items):
    """LEC-28 warm-up: sort by value/weight descending, ties by higher value
    first, then by lower weight."""
    return sorted(items, key=lambda x: (-(x[0] / float(x[1])), -x[0], x[1]))


def fib_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def match_at_index(a, b):
    return sum(1 for i in range(min(len(a), len(b))) if a[i] == b[i])


def is_palindrome_two_ptr(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def split_sums(a):
    n = len(a)
    total = sum(a)
    left = 0
    out = []
    for i in range(1, n):
        left += a[i - 1]
        out.append("%d %d" % (left, total - left))
    return "\n".join(out)


def subset_sums(arr):
    n = len(arr)
    out = []
    for mask in range(1 << n):
        out.append(sum(arr[i] for i in range(n) if mask >> i & 1))
    return out


def is_sorted(xs):
    for i in range(1, len(xs)):
        if xs[i] <= xs[i - 1]:
            return False
    return True


def bst_reverse_inorder(root):
    return list(reversed(in_list(root)))


def sort_activities(iv):
    return sorted(iv, key=lambda x: (x[1], x[0]))


def any_overlap_sorted(iv):
    """Input intervals are given sorted; if a later start is < earlier end,
    they overlap."""
    for i in range(1, len(iv)):
        if iv[i][0] < iv[i - 1][1]:
            return True
    return False


def inorder_successor_array(xs, key):
    for x in xs:
        if x > key:
            return x
    return None


# ---------------------------------------------------- constants used by cases
SIZED_ARR_IN = ("The first line contains an integer `n`. The second line "
                "contains `n` space-separated integers.")

TARGET_LINE_2 = "\n\nA second line contains the integer target value."

BST_IN_KEY = BST_IN + "\n\nA second line contains the integer key."

RANGE_LINE_2 = "\n\nA second line contains the two bounds `lo` and `hi`, "\
               "separated by a space."


# ------------------------------------------------------------ new problem set
NEW_PROBLEMS = [
    # ---- LEC-11 ------------------------------------------------------------
    dict(title="Classwork: Build a 3-node binary tree manually and print root, left, right",
         stmt="You are given three integers that form a binary tree with a "
              "root, a left child and a right child in that order. Print them "
              "on three separate lines: the root first, then the left child, "
              "then the right child.",
         inp="A single line with three integers separated by spaces: the root "
             "value, the left child's value and the right child's value.",
         out="Three lines: the root value on line 1, the left child's value on "
             "line 2, the right child's value on line 3.",
         cons="- `-10^4 <= each value <= 10^4`",
         solve=lambda s: "\n".join(s.split()),
         cases=["1 2 3", "10 5 15", "-1 -2 -3", "0 0 0",
                "7 -3 12", "100 50 150", "42 41 43", "-5 -10 5"]),

    # ---- LEC-12 ------------------------------------------------------------
    dict(title="Classwork: Print all nodes level by level into one list using BFS",
         stmt="Print every value in a binary tree in **breadth-first (level "
              "order)** as a single flat list.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(bfs_flat(build(s))), cases=TREES),

    dict(title="Classwork: LC199 Binary Tree Right Side View",
         stmt="Standing on the right of a binary tree, print the value seen "
              "at each level, from the top down.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(right_view(build(s))), cases=TREES),

    dict(title="Classwork: LC94 Inorder Traversal (iterative)",
         stmt="Given the root of a binary tree, return its inorder traversal. "
              "Use an **iterative** approach that maintains its own stack "
              "rather than the call stack.",
         inp=TREE_IN, out=SEQ_OUT,
         cons=CONS + "\n- Must be iterative",
         solve=lambda s: inorder(s), cases=TREES),

    # ---- LEC-13 ------------------------------------------------------------
    dict(title="Classwork: Count the number of levels in a binary tree",
         stmt="Print how many distinct levels a binary tree has. An empty "
              "tree has 0 levels; a single node has 1.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(depth(build(s))), cases=TREES),

    # ---- LEC-14 ------------------------------------------------------------
    dict(title="Classwork: Check if a binary tree is a full binary tree",
         stmt="A **full** binary tree is one where every internal node has "
              "exactly two children. Decide whether a given tree is full.\n\n"
              "An empty tree and a single leaf are both considered full.",
         inp=TREE_IN, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(is_full(build(s))),
         cases=["1 2 3", "1 2", "1 null 2", "1 2 3 4 5 6 7",
                "1 2 3 4 5", "null", "1", "1 2 3 4 null null 5"]),

    dict(title="Classwork: LC101 Symmetric Tree",
         stmt="Decide whether a binary tree is a **mirror image** of itself: "
              "the left subtree is the mirror of the right subtree.",
         inp=TREE_IN, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(is_symmetric(build(s))),
         cases=["1 2 2 3 4 4 3", "1 2 2 null 3 null 3",
                "1", "null", "1 2 2", "1 2 3", "5 4 4 3 2 2 3",
                "1 2 2 3 null null 3"]),

    # ---- LEC-15 ------------------------------------------------------------
    dict(title="Classwork: Left view of a binary tree (GfG)",
         stmt="Print the **left view** of a binary tree: the nodes you would "
              "see looking at the tree from the left side, one per level from "
              "top to bottom.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(left_view(build(s))), cases=TREES),

    # ---- LEC-16 ------------------------------------------------------------
    dict(title="Classwork: Swap the left and right children of the root only",
         stmt="Given a binary tree, swap the root's left and right children "
              "in place and print the resulting tree. The rest of the tree "
              "stays as it was.",
         inp=TREE_IN, out=SER_OUT, cons=CONS,
         solve=lambda s: serialize(swap_root_children(build(s))), cases=TREES),

    dict(title="Classwork: LC100 Same Tree",
         stmt="Given two binary trees, decide whether they are the **same** "
              "tree: identical shape and identical values at every "
              "corresponding position.",
         inp=TREE_IN2, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(is_same(*two(s))),
         cases=["1 2 3\n1 2 3",
                "1 2 3\n1 3 2",
                "1 2\n1 null 2",
                "null\nnull",
                "1\n1",
                "5 3 8 2 4 7 9\n5 3 8 2 4 7 9",
                "1 2 3 4\n1 2 3 4 5",
                "10 5 15\n10 5 15"]),

    # ---- LEC-17 ------------------------------------------------------------
    dict(title="Classwork: Find the sum of all leaf nodes in a binary tree",
         stmt="Print the sum of the values of every **leaf** node in a binary "
              "tree (a leaf is a node with no children). The sum of an empty "
              "tree is 0.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(sum_leaves(build(s))), cases=TREES),

    dict(title="Classwork: LC124 Binary Tree Maximum Path Sum",
         stmt="A path in a binary tree is any non-empty sequence of nodes in "
              "which each pair of consecutive nodes is connected by an edge, "
              "and no node appears twice. The path need not pass through the "
              "root. Print the maximum sum of the values on any such path.",
         inp=TREE_IN, out=NUM_OUT,
         cons="- `1 <= N <= 3 * 10^4`\n- `-1000 <= node value <= 1000`",
         solve=lambda s: str(max_path_sum(build(s))),
         cases=["1 2 3", "-10 9 20 null null 15 7",
                "1", "-3", "2 -1", "-2 -1", "5 4 8 11 null 13 4 7 2 null null null 1",
                "1 -2 -3 1 3 -2 null -1"]),

    # ---- LEC-18 ------------------------------------------------------------
    dict(title="Classwork: Search whether a value exists in a binary tree",
         stmt="Given a binary tree and a target value, decide whether the "
              "value occurs anywhere in the tree.",
         inp=TREE_IN + TARGET_LINE_2, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(contains_value(build(rows(s)[0]),
                                                 int(rows(s)[1]))),
         cases=["1 2 3\n2", "1 2 3\n4", "null\n0", "1\n1",
                "5 3 8 2 4 7 9\n7", "5 3 8 2 4 7 9\n10",
                "-5 -3 8 0 null null 12\n0",
                "10 5 15 3 7 null 18\n3"]),

    dict(title="Classwork: LCA using root-to-node paths (GfG)",
         stmt="Given a binary tree and two node values, find their **lowest "
              "common ancestor** by recording the root-to-node path of each "
              "value and comparing them until they diverge. Both values are "
              "guaranteed to be present and distinct.",
         inp=TREE_IN + "\n\nA second line contains the two node values, "
                       "separated by a space.",
         out=NUM_OUT, cons=CONS,
         solve=lambda s: str(lca_via_paths(build(rows(s)[0]),
                                           *ints(rows(s)[1]))),
         cases=["3 5 1 6 2 0 8 null null 7 4\n5 1",
                "3 5 1 6 2 0 8 null null 7 4\n5 4",
                "1 2\n1 2",
                "1 2 3\n2 3",
                "5 3 8 2 4 7 9\n2 4",
                "5 3 8 2 4 7 9\n2 9",
                "1 2 null 3 null 4\n3 4",
                "10 5 15 3 7 null 18\n3 18"]),

    # ---- LEC-19 ------------------------------------------------------------
    dict(title="Classwork: Build a binary tree from a level-order array and print inorder",
         stmt="Given a binary tree described in level order, build the tree "
              "in memory and print its **inorder** traversal.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: inorder(s), cases=TREES),

    # ---- LEC-20 ------------------------------------------------------------
    dict(title="Classwork: Count the total number of nodes in a binary tree",
         stmt="Print the total number of nodes in a binary tree. An empty "
              "tree has 0 nodes.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(sum(1 for _ in iter_nodes(build(s)))),
         cases=TREES),

    dict(title="Classwork: LC297 Serialize and Deserialize Binary Tree",
         stmt="Serialize a binary tree to a string in level order using the "
              "token `null` for a missing child, and drop the trailing "
              "`null` tokens. Then deserialize that string back into a tree "
              "and print it in the same format, so a correct round trip "
              "reproduces the input.",
         inp=TREE_IN,
         out="A single line: the serialized tree in level order with `null` "
             "for a missing child, trailing `null` tokens omitted.",
         cons=CONS,
         solve=lambda s: serialize(build(s)),
         cases=TREES),

    # ---- LEC-21 ------------------------------------------------------------
    dict(title="Classwork: Print the inorder of a BST and verify it is sorted",
         stmt="Given a BST, print its **inorder** traversal on one line and "
              "then `true` or `false` on the next line indicating whether the "
              "traversal is strictly increasing.\n\n"
              "An empty BST prints an empty first line and `true`.",
         inp=BST_IN,
         out="Two lines: the inorder values on line 1, and `true` / `false` "
             "on line 2.",
         cons=BST_CONS,
         solve=lambda s: "%s\n%s" % (fmt(in_list(build(s))),
                                     fmt_bool(is_sorted(in_list(build(s))))),
         cases=BSTS),

    # ---- LEC-22 ------------------------------------------------------------
    dict(title="Classwork: Check if an inorder traversal array is strictly increasing",
         stmt="Given a sequence of integers, decide whether it is strictly "
              "increasing (each value greater than the previous). This is "
              "the standard test for the inorder traversal of a valid BST "
              "with distinct keys.",
         inp=SIZED_ARR_IN, out=BOOL_OUT,
         cons="- `0 <= n <= 10^5`\n- `-10^9 <= value <= 10^9`",
         solve=lambda s: fmt_bool(is_sorted(ints(rows(s)[1]) if len(rows(s)) > 1 else [])),
         cases=["5\n1 2 3 4 5",
                "5\n1 2 2 3 4",
                "3\n5 3 8",
                "1\n42",
                "0\n",
                "4\n-10 -3 0 5",
                "4\n-10 -3 0 -5",
                "6\n1 2 3 4 3 5"]),

    # ---- LEC-23 ------------------------------------------------------------
    dict(title="Classwork: Find the inorder successor of a node using the inorder array",
         stmt="Given the inorder traversal of a BST as a sorted array and a "
              "key value, print the key's **inorder successor**: the smallest "
              "value strictly greater than the key. Print `null` if there is "
              "none.",
         inp=SIZED_ARR_IN + "\n\nA final line contains the key value.",
         out="A single line: the successor's value, or `null`.",
         cons="- `1 <= n <= 10^5`\n- the array is sorted increasing",
         solve=lambda s: (lambda r: "null" if r is None else str(r))(
             inorder_successor_array(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=["5\n1 3 5 7 9\n5",
                "5\n1 3 5 7 9\n9",
                "5\n1 3 5 7 9\n0",
                "5\n1 3 5 7 9\n4",
                "1\n42\n42",
                "3\n-5 0 5\n-5",
                "6\n2 4 6 8 10 12\n6",
                "4\n1 2 3 4\n10"]),

    # ---- LEC-24 ------------------------------------------------------------
    dict(title="Classwork: Find the ceiling of a key in a BST (GfG)",
         stmt="Given a BST and a key, print the **ceiling** of the key: the "
              "smallest value in the BST that is `>=` the key. Print `-1` if "
              "there is none.",
         inp=BST_IN_KEY, out="A single line: the ceiling value, or `-1`.",
         cons=BST_CONS,
         solve=lambda s: (lambda r: "-1" if r is None else str(r))(
             bst_ceiling(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [4, 8, 2, 9, 6, 11, 5, 45, 22])),

    dict(title="Classwork: LC173 Binary Search Tree Iterator",
         stmt="Simulate an inorder iterator over a BST. Support two "
              "operations:\n\n"
              "- `next` -- return the next value in inorder.\n"
              "- `hasNext` -- return `true` if there is another value, "
              "`false` otherwise.\n\n"
              "If `next` is called after the iterator is exhausted, print "
              "`null`.",
         inp=BST_IN + "\n\nA second line contains an integer `q`. Each of "
                      "the next `q` lines is one operation, either `next` or "
                      "`hasNext`.",
         out="One line per operation: the returned value for `next` "
             "(or `null`), and `true` / `false` for `hasNext`.",
         cons=BST_CONS + "\n- `1 <= q <= 10^5`",
         solve=lambda s: bst_iterator_run(rows(s)),
         cases=["2 1 3\n5\nhasNext\nnext\nnext\nnext\nhasNext",
                "8 3 10 1 6 null 14 null null 4 7 13\n7\n"
                    "next\nnext\nhasNext\nnext\nnext\nnext\nhasNext",
                "5\n3\nnext\nhasNext\nnext",
                "5 3 8 2 4 7 9\n8\nnext\nnext\nnext\nnext\nnext\nnext\nnext\nhasNext",
                "null\n2\nhasNext\nnext",
                "10 5 15 3 7 null 18\n4\nnext\nnext\nnext\nhasNext",
                "20 10 30 5 15 25 35 1\n5\nnext\nnext\nnext\nnext\nhasNext",
                "50 30 70 20 40 60 80\n4\nnext\nhasNext\nnext\nnext"]),

    # ---- LEC-25 ------------------------------------------------------------
    dict(title="Classwork: Print all BST keys in decreasing order (reverse inorder)",
         stmt="Given a BST, print all its keys in **decreasing** order.",
         inp=BST_IN, out=SEQ_OUT, cons=BST_CONS,
         solve=lambda s: fmt(bst_reverse_inorder(build(s))), cases=BSTS),

    dict(title="Classwork: LC653 Two Sum IV - Input is a BST",
         stmt="Given a BST and a target integer, decide whether **two "
              "different** nodes have values that add up to the target.",
         inp=BST_IN + TARGET_LINE_2, out=BOOL_OUT, cons=BST_CONS,
         solve=lambda s: fmt_bool(two_sum_bst(build(rows(s)[0]),
                                              int(rows(s)[1]))),
         cases=with_key(BSTS, [9, 10, 5, 18, 12, 22, 11, 90, 40])),

    dict(title="Classwork: LC938 Range Sum of BST",
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

    dict(title="Classwork: LC669 Trim a Binary Search Tree",
         stmt="Given a BST and an inclusive range `[lo, hi]`, remove every "
              "node whose value falls outside the range so that the result "
              "is still a valid BST, and print it.",
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

    # ---- LEC-26 ------------------------------------------------------------
    dict(title="Classwork: Sort activities by end time and print the sorted order",
         stmt="Given a list of activities, each with a start and a finish "
              "time, sort them by finish time (ties broken by earlier start) "
              "and print the sorted list.",
         inp=IV_IN,
         out="One line per activity: two integers `start end` separated by a "
             "space, in the sorted order.",
         cons="- `1 <= n <= 10^5`\n- `0 <= start < finish <= 10^9`",
         solve=lambda s: "\n".join("%d %d" % (a, b) for a, b in
                                    sort_activities([tuple(ints(r)) for r in
                                                     rows(s)[1:1 + int(rows(s)[0])]])),
         cases=IV_CASES),

    # ---- LEC-27 ------------------------------------------------------------
    dict(title="Classwork: Given sorted intervals, check whether any two overlap",
         stmt="You are given intervals already sorted by start time. Decide "
              "whether any two of them overlap (touching endpoints, like "
              "`[1,3]` and `[3,5]`, do **not** count as overlapping).",
         inp=IV_IN, out=BOOL_OUT,
         cons="- `1 <= n <= 10^5`\n- intervals are sorted by start time",
         solve=lambda s: fmt_bool(any_overlap_sorted(
             sorted([tuple(ints(r)) for r in
                     rows(s)[1:1 + int(rows(s)[0])]]))),
         cases=IV_CASES),

    # ---- LEC-28 ------------------------------------------------------------
    dict(title="Classwork: Sort items by value/weight ratio and print the order",
         stmt="Given a list of items, each with a value and a weight, sort "
              "them in **decreasing order of value/weight ratio** (ties "
              "broken by higher value, then lower weight) and print them in "
              "that order.",
         inp="The first line contains an integer `n`. Each of the next `n` "
             "lines contains two integers describing one item: its value and "
             "its weight.",
         out="One line per item: two integers `value weight` separated by a "
             "space, in the sorted order.",
         cons="- `1 <= n <= 10^5`\n- weights are positive",
         solve=lambda s: "\n".join(
             "%d %d" % (v, w) for v, w in
             value_weight_order([tuple(ints(r)) for r in
                                 rows(s)[1:1 + int(rows(s)[0])]])),
         cases=["3\n60 10\n100 20\n120 30",
                "4\n10 2\n20 5\n30 10\n40 4",
                "2\n50 5\n100 20",
                "1\n42 7",
                "5\n5 1\n4 1\n3 1\n2 1\n1 1",
                "3\n60 10\n60 20\n60 5",
                "3\n1 100\n2 100\n3 100",
                "4\n100 10\n80 8\n60 6\n40 4"]),

    dict(title="Classwork: Minimum cost to connect ropes (GfG)",
         stmt="Given the lengths of `n` ropes, repeatedly join the two "
              "shortest ropes into one. Every join costs the sum of the two "
              "rope lengths. Print the minimum total cost to join every rope "
              "into a single rope.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `1 <= length <= 10^4`",
         solve=lambda s: str(min_cost_ropes(ints(rows(s)[1]))),
         cases=["4\n4 3 2 6",
                "3\n1 2 3",
                "5\n1 2 3 4 5",
                "2\n10 20",
                "1\n7",
                "6\n5 5 5 5 5 5",
                "4\n1 1 1 1",
                "5\n8 4 6 12 5"]),

    # ---- LEC-29 ------------------------------------------------------------
    dict(title="Classwork: LC605 Can Place Flowers",
         stmt="A flowerbed is a row of 0/1 slots; `1` means already planted, "
              "`0` empty. No two adjacent slots may hold flowers. Decide "
              "whether at least `k` more flowers can be planted.",
         inp=SIZED_ARR_IN + "\n\nA final line contains the integer `k`.",
         out=BOOL_OUT,
         cons="- `1 <= n <= 2 * 10^4`\n- each slot is 0 or 1\n- `0 <= k <= n`",
         solve=lambda s: fmt_bool(can_place_flowers(ints(rows(s)[1]),
                                                    int(rows(s)[2]))),
         cases=["5\n1 0 0 0 1\n1",
                "5\n1 0 0 0 1\n2",
                "3\n0 0 0\n2",
                "1\n0\n1",
                "1\n1\n0",
                "4\n0 0 1 0\n1",
                "7\n1 0 0 0 0 0 1\n2",
                "2\n0 0\n1"]),

    # ---- LEC-30 ------------------------------------------------------------
    dict(title="Classwork: LC1005 Maximize Sum Of Array After K Negations",
         stmt="Given an integer array and an integer `k`, choose any element "
              "(the same one may be chosen more than once) and negate it, up "
              "to `k` times total. Print the largest possible sum of the "
              "array after these negations.",
         inp=SIZED_ARR_IN + "\n\nA final line contains the integer `k`.",
         out=NUM_OUT,
         cons="- `1 <= n <= 10^4`\n- `-100 <= value <= 100`\n- `1 <= k <= 10^4`",
         solve=lambda s: str(maximize_after_k_neg(ints(rows(s)[1]),
                                                   int(rows(s)[2]))),
         cases=["4\n4 2 3 -1 \n2".replace(" \n", "\n"),
                "3\n3 -1 0 \n2".replace(" \n", "\n"),
                "5\n2 -3 -1 5 -4 \n2".replace(" \n", "\n"),
                "1\n-5\n1",
                "1\n5\n2",
                "3\n1 2 3\n1",
                "4\n-8 3 -5 -3\n6",
                "5\n0 0 0 0 0\n5"]),

    dict(title="Classwork: LC767 Reorganize String",
         stmt="Rearrange a string so that no two adjacent characters are the "
              "same. If it is impossible, print an empty line. If several "
              "arrangements are possible any one of them may be printed; the "
              "grader accepts any correct arrangement.",
         inp="A single line: the input string, lowercase letters only.",
         out="A single line: a valid arrangement, or an empty line if there "
             "is none.",
         cons="- `1 <= length <= 500`\n- lowercase English letters",
         solve=lambda s: reorganize_string(s.strip()),
         cases=["aab", "aaab", "aabb", "aabbcc", "a", "aa",
                "vvvlo", "baaba"]),

    dict(title="Classwork: LC621 Task Scheduler",
         stmt="You are given a list of task labels and a cooldown `n`: after "
              "running any task the same task cannot be run again for `n` "
              "intervals. Each task takes one interval. Print the minimum "
              "number of intervals to complete every task.",
         inp="The first line contains an integer `m` and an integer `n` "
             "separated by a space. The second line contains `m` uppercase "
             "letters separated by spaces -- the task labels.",
         out=NUM_OUT,
         cons="- `1 <= m <= 10^4`\n- `0 <= n <= 100`",
         solve=lambda s: str(task_scheduler(rows(s)[1].split(),
                                             ints(rows(s)[0])[1])),
         cases=["6 2\nA A A B B B",
                "6 0\nA A A B B B",
                "6 2\nA B C D E F",
                "10 2\nA A A A B B C C D E",
                "1 5\nA",
                "8 1\nA A A B B C C D",
                "3 100\nA A A",
                "5 2\nA B A B A"]),

    # ---- LEC-31 ------------------------------------------------------------
    dict(title="Classwork: Compute the nth Fibonacci iteratively with two variables",
         stmt="Print the `n`-th Fibonacci number `F(n)` using an iterative "
              "loop that keeps only the previous two values.\n\n"
              "`F(0) = 0`, `F(1) = 1`, `F(k) = F(k-1) + F(k-2)` for `k >= 2`.",
         inp="A single line containing the integer `n`.",
         out=NUM_OUT,
         cons="- `0 <= n <= 90`\n- Auxiliary space `O(1)`",
         solve=lambda s: str(fib_iter(int(s.strip()))),
         cases=["0", "1", "2", "10", "20", "30", "45", "50"]),

    # ---- LEC-32 ------------------------------------------------------------
    dict(title="Classwork: Draw the DP table by hand for making change of a small amount",
         stmt="Given a set of coin denominations and a target amount, print "
              "the minimum-coins DP row `dp[0], dp[1], ..., dp[amount]`, "
              "where `dp[i]` is the fewest coins that add up to `i`. Print "
              "`x` for any amount that cannot be reached with the given "
              "denominations.",
         inp="The first line contains the amount `A` and the number of "
             "denominations `k`, separated by a space. The second line "
             "contains the `k` denominations, separated by spaces.",
         out="A single line with `A + 1` tokens: `dp[0] dp[1] ... dp[A]`, "
             "using `x` for an unreachable amount.",
         cons="- `1 <= A <= 100`\n- `1 <= k <= 10`\n- `1 <= denomination`",
         solve=lambda s: coin_change_dp_row(ints(rows(s)[1]),
                                             ints(rows(s)[0])[0]),
         cases=["5 2\n1 2",
                "11 3\n1 2 5",
                "3 2\n2 5",
                "7 1\n1",
                "0 1\n5",
                "6 2\n3 6",
                "10 3\n1 5 10",
                "4 2\n2 3"]),

    dict(title="Classwork: Minimum number of coins (GfG)",
         stmt="Given a set of coin denominations and a target amount, print "
              "the minimum number of coins that add up to the amount, or "
              "`-1` if it cannot be made. Every denomination may be used "
              "any number of times.",
         inp="The first line contains the denominations, space separated. "
             "The second line contains the target amount.",
         out="A single line: the number of coins, or `-1`.",
         cons="- `1 <= amount <= 10^4`\n- denominations are positive",
         solve=lambda s: str(min_coins_dp(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 2 5\n11",
                "2\n3",
                "1 5 10\n18",
                "1 2 5 10\n27",
                "1\n7",
                "5 10\n15",
                "3 5 7\n13",
                "2 5 10\n1"]),

    # ---- LEC-33 ------------------------------------------------------------
    dict(title="Classwork: LC674 Longest Continuous Increasing Subsequence",
         stmt="Given an integer array, print the length of the longest "
              "**strictly increasing contiguous** run.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^4`\n- `-10^9 <= value <= 10^9`",
         solve=lambda s: str(longest_cont_inc(ints(rows(s)[1]))),
         cases=["5\n1 3 5 4 7",
                "4\n2 2 2 2",
                "6\n1 2 3 2 3 4",
                "1\n42",
                "5\n5 4 3 2 1",
                "5\n1 2 3 4 5",
                "6\n-2 -1 0 -3 -2 -1",
                "3\n10 20 30"]),

    # ---- LEC-34 ------------------------------------------------------------
    dict(title="Classwork: LC1480 Running Sum of 1d Array",
         stmt="Given an integer array `a`, print its **running sum**: for "
              "every index `i`, output `a[0] + a[1] + ... + a[i]`.",
         inp=SIZED_ARR_IN, out=SEQ_OUT,
         cons="- `1 <= n <= 10^3`\n- `-10^6 <= value <= 10^6`",
         solve=lambda s: fmt(running_sum(ints(rows(s)[1]))),
         cases=["4\n1 2 3 4",
                "5\n1 1 1 1 1",
                "1\n5",
                "3\n3 1 2 10 1".split("\n")[0] + "\n3 1 2",
                "6\n-1 -2 -3 -4 -5 -6",
                "4\n10 20 30 40",
                "5\n0 0 0 0 0",
                "3\n-5 5 -5"]),

    # ---- LEC-35 ------------------------------------------------------------
    dict(title="Classwork: Generate all subsets of a 3-element array and print their sums",
         stmt="Given three integers, list the sum of each of the eight "
              "subsets (including the empty subset). Print the sums in "
              "**subset-index order**: subset `mask` corresponds to "
              "`mask = 0..7`, taking element `i` when bit `i` of `mask` is "
              "set.",
         inp="A single line with three integers separated by spaces.",
         out="One line per subset: the subset's sum, in mask order 0..7.",
         cons="- `-10^4 <= each value <= 10^4`",
         solve=lambda s: "\n".join(str(x) for x in subset_sums(ints(s))),
         cases=["1 2 3", "5 5 5", "-1 -2 -3", "0 0 0",
                "10 20 30", "7 -3 2", "100 200 300", "1 1 -1"]),

    dict(title="Classwork: LC91 Decode Ways",
         stmt="A message is encoded as a string of digits using the mapping "
              "`1 -> A, 2 -> B, ..., 26 -> Z`. Print the number of ways to "
              "decode the message.\n\n"
              "A leading `0`, or an unreachable `0` (one that cannot pair "
              "with the digit before it to form `10` or `20`), gives 0 ways.",
         inp="A single line containing the digit string.",
         out=NUM_OUT,
         cons="- `1 <= length <= 100`\n- digits `0`..`9`",
         solve=lambda s: str(decode_ways(s.strip())),
         cases=["12", "226", "0", "06", "10", "11106", "27", "111111"]),

    # ---- LEC-36 ------------------------------------------------------------
    dict(title="Classwork: Solve 0/1 knapsack for n=3 by drawing the DP table by hand",
         stmt="Given a small 0/1 knapsack instance with `n` items and "
              "capacity `W`, print the full `(n + 1) x (W + 1)` DP table "
              "`dp[i][c]` -- the best value achievable using only the first "
              "`i` items with capacity `c` -- one row per line, values "
              "separated by spaces.",
         inp="The first line contains `n` and `W`, separated by a space. "
             "Each of the next `n` lines contains an item's weight and value "
             "separated by a space.",
         out="`n + 1` lines, each with `W + 1` space-separated integers.",
         cons="- `1 <= n <= 5`\n- `1 <= W <= 20`",
         solve=lambda s: knap_dp_table(*parse_kn(s)),
         cases=["3 4\n1 15\n3 20\n4 30",
                "3 5\n2 3\n3 4\n4 5",
                "2 4\n1 1\n2 3",
                "1 3\n2 5",
                "3 6\n1 6\n2 10\n3 12",
                "4 5\n2 1\n2 2\n2 3\n2 4",
                "2 10\n5 6\n3 4",
                "3 7\n1 1\n4 5\n3 4"]),

    # ---- LEC-37 ------------------------------------------------------------
    dict(title="Classwork: Minimum coins for amount N using only coin 1 (trace the recurrence)",
         stmt="Print the minimum number of coins required to make the amount "
              "`N` using **only** coins of denomination `1`. The recurrence "
              "collapses to `dp[i] = dp[i - 1] + 1`, so the answer is "
              "always `N`.",
         inp="A single line containing the non-negative integer `N`.",
         out=NUM_OUT,
         cons="- `0 <= N <= 10^6`",
         solve=lambda s: str(int(s.strip())),
         cases=["0", "1", "2", "5", "10", "100", "999", "1000000"]),

    # ---- LEC-38 ------------------------------------------------------------
    dict(title="Classwork: Count matching characters at the same index in two strings",
         stmt="Given two strings, print how many positions `i` (from the "
              "start, up to the shorter length) have the same character in "
              "both strings.",
         inp="Two lines, one string each.",
         out=NUM_OUT,
         cons="- `0 <= each length <= 10^5`",
         solve=lambda s: str(match_at_index(*rows(s)[:2] +
                                             [""] * (2 - len(rows(s))))),
         cases=["abcdef\nabcxef",
                "hello\nworld",
                "same\nsame",
                "abc\nabcd",
                "abc\nxyz",
                "a\na",
                "aaa\nbbb",
                "openai\nopenat"]),

    # ---- LEC-39 ------------------------------------------------------------
    dict(title="Classwork: Check whether a string is a palindrome using two pointers",
         stmt="Given a string, decide whether it reads the same forwards and "
              "backwards. The check is character-for-character; case and "
              "punctuation matter.",
         inp="A single line containing the string.",
         out=BOOL_OUT,
         cons="- `0 <= length <= 10^5`",
         solve=lambda s: fmt_bool(is_palindrome_two_ptr(s.strip("\n"))),
         cases=["racecar", "hello", "a", "", "aa", "ab",
                "abba", "abcba"]),

    # ---- LEC-40 ------------------------------------------------------------
    dict(title="Classwork: Split an array at every index and print both halves' sums",
         stmt="Given an integer array of length `n`, for each split index "
              "`i` from `1` to `n - 1`, print the sum of the left half "
              "`a[0..i-1]` and the sum of the right half `a[i..n-1]`.",
         inp=SIZED_ARR_IN,
         out="One line per split index: two integers `leftSum rightSum` "
             "separated by a space. Print nothing when `n < 2`.",
         cons="- `1 <= n <= 10^4`\n- `-10^6 <= value <= 10^6`",
         solve=lambda s: split_sums(ints(rows(s)[1]) if len(rows(s)) > 1
                                    else []),
         cases=["5\n1 2 3 4 5",
                "4\n10 20 30 40",
                "1\n42",
                "2\n7 3",
                "6\n-1 -2 -3 4 5 6",
                "3\n0 0 0",
                "5\n5 5 5 5 5",
                "4\n-10 10 -10 10"]),
]


# ------------------------------------------------------ classwork title order
# The exact list of classwork problems in the sheet for LEC-11 to LEC-40,
# in the order they appear. Duplicates are kept for reference; dedupe below.
SHEET_TITLES = [
    # LEC-11 Trees & DFS
    "Classwork: Build a 3-node binary tree manually and print root, left, right",
    "Classwork: LC94 Binary Tree Inorder Traversal",
    "Classwork: LC144 Binary Tree Preorder Traversal",
    "Classwork: LC145 Binary Tree Postorder Traversal",
    # LEC-12 Iterative & BFS
    "Classwork: Print all nodes level by level into one list using BFS",
    "Classwork: LC102 Binary Tree Level Order Traversal",
    "Classwork: LC199 Binary Tree Right Side View",
    "Classwork: LC94 Inorder Traversal (iterative)",
    # LEC-13 Height & Diameter
    "Classwork: Count the number of levels in a binary tree",
    "Classwork: LC104 Maximum Depth of Binary Tree",
    "Classwork: LC111 Minimum Depth of Binary Tree",
    "Classwork: LC543 Diameter of Binary Tree",
    # LEC-14 Balanced & Views
    "Classwork: Check if a binary tree is a full binary tree",
    "Classwork: LC110 Balanced Binary Tree",
    "Classwork: LC101 Symmetric Tree",
    "Classwork: LC199 Binary Tree Right Side View",
    # LEC-15 Advanced Views
    "Classwork: Left view of a binary tree (GfG)",
    "Classwork: Top view of a binary tree (GfG)",
    "Classwork: Boundary traversal of a binary tree (GfG)",
    "Classwork: LC987 Vertical Order Traversal of a Binary Tree",
    # LEC-16 Invert & Symmetric
    "Classwork: Swap the left and right children of the root only",
    "Classwork: LC226 Invert Binary Tree",
    "Classwork: LC101 Symmetric Tree",
    "Classwork: LC100 Same Tree",
    # LEC-17 Path Sum
    "Classwork: Find the sum of all leaf nodes in a binary tree",
    "Classwork: LC112 Path Sum",
    "Classwork: LC113 Path Sum II",
    "Classwork: LC124 Binary Tree Maximum Path Sum",
    # LEC-18 LCA
    "Classwork: Search whether a value exists in a binary tree",
    "Classwork: LC236 Lowest Common Ancestor of a Binary Tree",
    "Classwork: LCA using root-to-node paths (GfG)",
    "Classwork: Distance between two nodes via LCA (GfG)",
    # LEC-19 Construct & Flatten
    "Classwork: Build a binary tree from a level-order array and print inorder",
    "Classwork: LC105 Construct Binary Tree from Preorder and Inorder",
    "Classwork: LC106 Construct Binary Tree from Inorder and Postorder",
    "Classwork: LC114 Flatten Binary Tree to Linked List",
    # LEC-20 Serialize & Utilities
    "Classwork: Count the total number of nodes in a binary tree",
    "Classwork: LC222 Count Complete Tree Nodes",
    "Classwork: LC863 All Nodes Distance K in Binary Tree",
    "Classwork: LC297 Serialize and Deserialize Binary Tree",
    # LEC-21 BST Search & Insert
    "Classwork: Print the inorder of a BST and verify it is sorted",
    "Classwork: LC700 Search in a Binary Search Tree",
    "Classwork: Iterative BST search (GfG)",
    "Classwork: LC701 Insert into a Binary Search Tree",
    # LEC-22 Validate & Min Diff
    "Classwork: Check if an inorder traversal array is strictly increasing",
    "Classwork: LC530 Minimum Absolute Difference in BST",
    "Classwork: LC501 Find Mode in Binary Search Tree",
    "Classwork: LC98 Validate Binary Search Tree",
    # LEC-23 Delete & Kth
    "Classwork: Find the inorder successor of a node using the inorder array",
    "Classwork: LC450 Delete Node in a BST",
    "Classwork: LC230 Kth Smallest Element in a BST",
    "Classwork: Kth largest element in a BST (GfG)",
    # LEC-24 LCA, Build, Iterator
    "Classwork: Find the ceiling of a key in a BST (GfG)",
    "Classwork: LC108 Convert Sorted Array to Binary Search Tree",
    "Classwork: LC235 Lowest Common Ancestor of a BST",
    "Classwork: LC173 Binary Search Tree Iterator",
    # LEC-25 BST Advanced
    "Classwork: Print all BST keys in decreasing order (reverse inorder)",
    "Classwork: LC653 Two Sum IV - Input is a BST",
    "Classwork: LC938 Range Sum of BST",
    "Classwork: LC669 Trim a Binary Search Tree",
    # LEC-26 Greedy & Intervals
    "Classwork: Sort activities by end time and print the sorted order",
    "Classwork: N meetings in one room (GfG)",
    "Classwork: LC435 Non-overlapping Intervals",
    "Classwork: Maximum number of activities selected (GfG)",
    # LEC-27 Merge Intervals
    "Classwork: Given sorted intervals, check whether any two overlap",
    "Classwork: LC56 Merge Intervals",
    "Classwork: LC57 Insert Interval",
    "Classwork: Minimum number of platforms (GfG)",
    # LEC-28 Knapsack & Jobs
    "Classwork: Sort items by value/weight ratio and print the order",
    "Classwork: Fractional Knapsack (GfG)",
    "Classwork: Job Sequencing Problem (GfG)",
    "Classwork: Minimum cost to connect ropes (GfG)",
    # LEC-29 Jump Family
    "Classwork: LC605 Can Place Flowers",
    "Classwork: LC55 Jump Game",
    "Classwork: LC134 Gas Station",
    "Classwork: LC135 Candy",
    # LEC-30 Greedy Patterns
    "Classwork: LC1005 Maximize Sum Of Array After K Negations",
    "Classwork: LC767 Reorganize String",
    "Classwork: LC621 Task Scheduler",
    "Classwork: Minimum cost to connect ropes (GfG)",
    # LEC-31 DP Intro & 1D
    "Classwork: Compute the nth Fibonacci iteratively with two variables",
    "Classwork: LC509 Fibonacci Number",
    "Classwork: LC70 Climbing Stairs",
    "Classwork: LC198 House Robber",
    # LEC-32 Coin Change
    "Classwork: Draw the DP table by hand for making change of a small amount",
    "Classwork: LC322 Coin Change",
    "Classwork: LC518 Coin Change II",
    "Classwork: Minimum number of coins (GfG)",
    # LEC-33 LIS / LCS
    "Classwork: LC674 Longest Continuous Increasing Subsequence",
    "Classwork: LC300 Longest Increasing Subsequence",
    "Classwork: LC1143 Longest Common Subsequence",
    "Classwork: Longest Increasing Subsequence in O(n log n) (GfG)",
    # LEC-34 Grid DP
    "Classwork: LC1480 Running Sum of 1d Array",
    "Classwork: LC62 Unique Paths",
    "Classwork: LC64 Minimum Path Sum",
    "Classwork: LC63 Unique Paths II",
    # LEC-35 Subsequence DP
    "Classwork: Generate all subsets of a 3-element array and print their sums",
    "Classwork: Subset Sum (GfG)",
    "Classwork: LC416 Partition Equal Subset Sum",
    "Classwork: LC91 Decode Ways",
    # LEC-36 0/1 Knapsack
    "Classwork: Solve 0/1 knapsack for n=3 by drawing the DP table by hand",
    "Classwork: 0/1 Knapsack (GfG)",
    "Classwork: LC416 Partition Equal Subset Sum",
    "Classwork: LC494 Target Sum",
    # LEC-37 Unbounded Knapsack
    "Classwork: Minimum coins for amount N using only coin 1 (trace the recurrence)",
    "Classwork: Unbounded Knapsack (GfG)",
    "Classwork: Rod Cutting (GfG)",
    "Classwork: LC322 Coin Change",
    # LEC-38 Edit Distance
    "Classwork: Count matching characters at the same index in two strings",
    "Classwork: LC583 Delete Operation for Two Strings",
    "Classwork: LC712 Minimum ASCII Delete Sum for Two Strings",
    "Classwork: LC72 Edit Distance",
    # LEC-39 LCS Variants
    "Classwork: Check whether a string is a palindrome using two pointers",
    "Classwork: LC516 Longest Palindromic Subsequence",
    "Classwork: Matrix Chain Multiplication (GfG)",
    "Classwork: LC1092 Shortest Common Supersequence",
    # LEC-40 Partition DP
    "Classwork: Split an array at every index and print both halves' sums",
    "Classwork: Matrix Chain Multiplication (GfG)",
    "Classwork: LC132 Palindrome Partitioning II",
    "Classwork: LC312 Burst Balloons",
]


# ---------------------------------------------------------- build & emit ----
def classwork_only(problems):
    return [p for p in problems if p["title"].startswith("Classwork:")]


def build_index():
    """title -> dict, first-occurrence wins."""
    index = {}
    for p in (classwork_only(make_md.PROBLEMS)
              + classwork_only(make_md.PROBLEMS_21_30)
              + classwork_only(make_md.PROBLEMS_GREEDY)
              + classwork_only(dp_problems.PROBLEMS)
              + NEW_PROBLEMS):
        index.setdefault(p["title"], p)
    return index


# -------------------------------------------------- HackerRank id overrides
# Titles that would otherwise match multiple live HackerRank challenges, and
# the one we want editor.py to actually update. Each of these was verified by
# reading the HR challenge list and picking the canonical (non-" 1"/" 2"
# suffix, Classwork-not-Homework) version.
HR_ID_OVERRIDE = {
    "Classwork: LC199 Binary Tree Right Side View":              591603,
    "Classwork: LC101 Symmetric Tree":                           591616,
    "Classwork: LC100 Same Tree":                                591631,
    "Classwork: LC124 Binary Tree Maximum Path Sum":             591639,
    "Classwork: LC700 Search in a Binary Search Tree":           591709,
    "Classwork: LC701 Insert into a Binary Search Tree":         591710,
    "Classwork: LC653 Two Sum IV - Input is a BST":              591721,
    "Classwork: LC938 Range Sum of BST":                         591722,
    "Classwork: LC669 Trim a Binary Search Tree":                591949,
    "Classwork: Minimum cost to connect ropes (GfG)":            591017,
    "Classwork: LC767 Reorganize String":                        591015,
    "Classwork: LC621 Task Scheduler":                           591016,
    "Classwork: Minimum number of coins (GfG)":                  591025,
    "Classwork: LC416 Partition Equal Subset Sum":               591042,
    "Classwork: Matrix Chain Multiplication (GfG)":              591072,
}


# -------------------------------------------------------- explanations ----
# One entry per problem title. A value can be:
#   - a plain string (used ONLY for Sample 1),
#   - a list of strings (index i is the explanation for Sample i+1; None skips),
#   - a callable f(case, output) -> str (used for every sample it's asked for).
# Explanations describe what the output MEANS for the given input in plain
# English. They deliberately avoid algorithm names, code hints, or how-to
# steps: the goal is comprehension, not a solution walkthrough.

def _fmt_first_line(s):
    return s.splitlines()[0] if s else ""


EXPLANATIONS = {
    # ------------------------------------------------------------ LEC-11 ----
    "Classwork: Build a 3-node binary tree manually and print root, left, right":
        lambda c, o: (
            "The three inputs `%s` are the root, left child, and right child "
            "in that order. Each one is printed on its own line."
            % " ".join(c.split())),

    "Classwork: LC94 Binary Tree Inorder Traversal":
        lambda c, o: (
            "Reading the tree left-subtree, root, right-subtree lists the "
            "values in this order: `%s`." % o.replace("\n", " ")),

    "Classwork: LC144 Binary Tree Preorder Traversal":
        lambda c, o: (
            "Reading the tree root, left-subtree, right-subtree lists the "
            "values in this order: `%s`." % o.replace("\n", " ")),

    "Classwork: LC145 Binary Tree Postorder Traversal":
        lambda c, o: (
            "Reading the tree left-subtree, right-subtree, root lists the "
            "values in this order: `%s`." % o.replace("\n", " ")),

    # ------------------------------------------------------------ LEC-12 ----
    "Classwork: Print all nodes level by level into one list using BFS":
        lambda c, o: (
            "Visiting the tree level by level, from the top down and left to "
            "right at each level, produces the flat list `%s`." % o),

    "Classwork: LC102 Binary Tree Level Order Traversal":
        lambda c, o: (
            "One line per level, top to bottom. Each line lists the values "
            "on that level from left to right."),

    "Classwork: LC199 Binary Tree Right Side View":
        lambda c, o: (
            "Standing on the right, at each level you only see the rightmost "
            "value. Reading top to bottom gives `%s`." % o),

    "Classwork: LC94 Inorder Traversal (iterative)":
        lambda c, o: (
            "Same left-root-right order as the recursive inorder traversal, "
            "producing `%s`." % o),

    # ------------------------------------------------------------ LEC-13 ----
    "Classwork: Count the number of levels in a binary tree":
        lambda c, o: (
            "The deepest node in the tree sits at level `%s` counting from "
            "level 1 at the root, so the tree has `%s` levels." % (o, o)),

    "Classwork: LC104 Maximum Depth of Binary Tree":
        lambda c, o: (
            "The longest root-to-leaf path passes through `%s` nodes." % o),

    "Classwork: LC111 Minimum Depth of Binary Tree":
        lambda c, o: (
            "The shortest root-to-leaf path passes through `%s` nodes." % o),

    "Classwork: LC543 Diameter of Binary Tree":
        lambda c, o: (
            "The longest path between any two nodes uses `%s` edges." % o),

    # ------------------------------------------------------------ LEC-14 ----
    "Classwork: Check if a binary tree is a full binary tree":
        lambda c, o: (
            "A tree is `full` when every non-leaf has exactly two children. "
            "Here the answer is `%s`." % o),

    "Classwork: LC110 Balanced Binary Tree":
        lambda c, o: (
            "A tree is `balanced` when the left and right heights differ by "
            "at most 1 at every node. Here the answer is `%s`." % o),

    "Classwork: LC101 Symmetric Tree":
        lambda c, o: (
            "The tree is symmetric when its left subtree is the mirror of "
            "its right subtree. Here the answer is `%s`." % o),

    # ------------------------------------------------------------ LEC-15 ----
    "Classwork: Left view of a binary tree (GfG)":
        lambda c, o: (
            "Standing on the left, at each level you only see the leftmost "
            "value. Reading top to bottom gives `%s`." % o),

    "Classwork: Top view of a binary tree (GfG)":
        lambda c, o: (
            "Looking straight down, each vertical column shows the topmost "
            "value. Reading columns left to right gives `%s`." % o),

    "Classwork: Boundary traversal of a binary tree (GfG)":
        lambda c, o: (
            "Starting at the root, walking down the left edge, across the "
            "leaves, and up the right edge without repeating a node gives "
            "`%s`." % o),

    "Classwork: LC987 Vertical Order Traversal of a Binary Tree":
        lambda c, o: (
            "Each line is one vertical column, printed left to right. Within "
            "a column, higher nodes come first, then smaller values first."),

    # ------------------------------------------------------------ LEC-16 ----
    "Classwork: Swap the left and right children of the root only":
        lambda c, o: (
            "Only the root's two children are swapped; every other node "
            "stays where it was. The new tree in level order is `%s`." % o),

    "Classwork: LC226 Invert Binary Tree":
        lambda c, o: (
            "Every node's children are swapped, flipping the tree "
            "horizontally. The result in level order is `%s`." % o),

    "Classwork: LC100 Same Tree":
        lambda c, o: (
            "Two trees are the `same` when they share the exact same shape "
            "and the same value at every position. Here the answer is `%s`."
            % o),

    # ------------------------------------------------------------ LEC-17 ----
    "Classwork: Find the sum of all leaf nodes in a binary tree":
        lambda c, o: (
            "Adding up every value that has no children gives `%s`." % o),

    "Classwork: LC112 Path Sum":
        lambda c, o: (
            "`%s`: there %s a path from the root down to a leaf whose "
            "values add up to the given target."
            % (o, "is" if o == "true" else "is no")),

    "Classwork: LC113 Path Sum II":
        lambda c, o: (
            "Every printed line is one root-to-leaf path whose values sum "
            "to the target."),

    "Classwork: LC124 Binary Tree Maximum Path Sum":
        lambda c, o: (
            "Considering every path in the tree (which does not need to "
            "pass through the root), the largest possible sum of the "
            "values on that path is `%s`." % o),

    # ------------------------------------------------------------ LEC-18 ----
    "Classwork: Search whether a value exists in a binary tree":
        lambda c, o: (
            "The target value %s in the tree, so the answer is `%s`."
            % ("appears somewhere" if o == "true" else "does not appear",
               o)),

    "Classwork: LC236 Lowest Common Ancestor of a Binary Tree":
        lambda c, o: (
            "The deepest node that has both target nodes in its subtree is "
            "`%s`." % o),

    "Classwork: LCA using root-to-node paths (GfG)":
        lambda c, o: (
            "The two root-to-node paths share a common prefix and then "
            "diverge; the last shared node is `%s`, the lowest common "
            "ancestor." % o),

    "Classwork: Distance between two nodes via LCA (GfG)":
        lambda c, o: (
            "The number of edges on the path between the two nodes, going "
            "through their lowest common ancestor, is `%s`." % o),

    # ------------------------------------------------------------ LEC-19 ----
    "Classwork: Build a binary tree from a level-order array and print inorder":
        lambda c, o: (
            "After building the tree from the level-order tokens, the "
            "left-root-right walk produces `%s`." % o),

    "Classwork: LC105 Construct Binary Tree from Preorder and Inorder":
        lambda c, o: (
            "Preorder tells us the root; inorder tells us which values fall "
            "in the left subtree and which in the right. The rebuilt tree "
            "in level order is `%s`." % o),

    "Classwork: LC106 Construct Binary Tree from Inorder and Postorder":
        lambda c, o: (
            "Postorder tells us the root (the last value); inorder splits "
            "the remaining values into left and right subtrees. The rebuilt "
            "tree in level order is `%s`." % o),

    "Classwork: LC114 Flatten Binary Tree to Linked List":
        lambda c, o: (
            "Reading the tree in preorder gives `%s`; each node is chained "
            "to the next via its right pointer." % o),

    # ------------------------------------------------------------ LEC-20 ----
    "Classwork: Count the total number of nodes in a binary tree":
        lambda c, o: "The tree has `%s` nodes in all." % o,

    "Classwork: LC222 Count Complete Tree Nodes":
        lambda c, o: "The complete tree has `%s` nodes in all." % o,

    "Classwork: LC863 All Nodes Distance K in Binary Tree":
        lambda c, o: (
            "Every value listed sits exactly `k` edges away from the target "
            "node, whether that path goes down, up, or around the tree."),

    "Classwork: LC297 Serialize and Deserialize Binary Tree":
        lambda c, o: (
            "Serializing the tree and then rebuilding it from that string "
            "reproduces the same tree, so the output equals the input "
            "(with trailing `null` tokens trimmed)."),

    # ------------------------------------------------------------ LEC-21 ----
    "Classwork: Print the inorder of a BST and verify it is sorted":
        lambda c, o: (
            "Line 1 is the left-root-right walk of the BST. Line 2 says "
            "whether that sequence is strictly increasing."),

    "Classwork: LC700 Search in a Binary Search Tree":
        lambda c, o: (
            "If the key is present, the subtree rooted at it is printed; "
            "otherwise the output is `null`."),

    "Classwork: Iterative BST search (GfG)":
        lambda c, o: (
            "Walking down the BST from the root -- left when the target is "
            "smaller, right when larger -- either finds the key or runs off "
            "the tree. Here the answer is `%s`." % o),

    "Classwork: LC701 Insert into a Binary Search Tree":
        lambda c, o: (
            "The key is placed at the first empty spot that keeps the tree "
            "a valid BST. If the key already exists, the tree is unchanged."),

    # ------------------------------------------------------------ LEC-22 ----
    "Classwork: Check if an inorder traversal array is strictly increasing":
        lambda c, o: (
            "Each element is compared to the previous one. The sequence "
            "is strictly increasing: `%s`." % o),

    "Classwork: LC530 Minimum Absolute Difference in BST":
        lambda c, o: (
            "Looking at every pair of BST values, the smallest absolute "
            "difference is `%s`." % o),

    "Classwork: LC501 Find Mode in Binary Search Tree":
        lambda c, o: (
            "The value(s) that appear the most often are listed in "
            "increasing order: `%s`." % o),

    "Classwork: LC98 Validate Binary Search Tree":
        lambda c, o: (
            "For a valid BST, every left descendant is strictly smaller and "
            "every right descendant strictly larger than the node. Here the "
            "answer is `%s`." % o),

    # ------------------------------------------------------------ LEC-23 ----
    "Classwork: Find the inorder successor of a node using the inorder array":
        lambda c, o: (
            "In the sorted array, the first value larger than the key is "
            "`%s` (or `null` if no such value exists)." % o),

    "Classwork: LC450 Delete Node in a BST":
        lambda c, o: (
            "The key is removed while the BST property is preserved. If the "
            "key is absent, the tree is printed unchanged."),

    "Classwork: LC230 Kth Smallest Element in a BST":
        lambda c, o: (
            "Listing the BST values in increasing order, the `k`-th one is "
            "`%s`." % o),

    "Classwork: Kth largest element in a BST (GfG)":
        lambda c, o: (
            "Listing the BST values in decreasing order, the `k`-th one is "
            "`%s`." % o),

    # ------------------------------------------------------------ LEC-24 ----
    "Classwork: Find the ceiling of a key in a BST (GfG)":
        lambda c, o: (
            "The smallest BST value that is greater than or equal to the "
            "key is `%s` (or `-1` if every value is smaller)." % o),

    "Classwork: LC108 Convert Sorted Array to Binary Search Tree":
        lambda c, o: (
            "Picking the middle element as the root, and repeating for the "
            "two halves, keeps the tree balanced. Result in level order: "
            "`%s`." % o),

    "Classwork: LC235 Lowest Common Ancestor of a BST":
        lambda c, o: (
            "The first node encountered going from the root down where the "
            "two target values split into different subtrees is `%s`." % o),

    "Classwork: LC173 Binary Search Tree Iterator":
        lambda c, o: (
            "The iterator visits the BST values in increasing order. Each "
            "`next` returns the following value; `hasNext` reports whether "
            "any values remain."),

    # ------------------------------------------------------------ LEC-25 ----
    "Classwork: Print all BST keys in decreasing order (reverse inorder)":
        lambda c, o: (
            "Reading the BST right-root-left lists the values from largest "
            "to smallest: `%s`." % (o if o else "(nothing, the tree is empty)")),

    "Classwork: LC653 Two Sum IV - Input is a BST":
        lambda c, o: (
            "%s two different BST values that add up to the target, so the "
            "answer is `%s`."
            % ("There exist" if o == "true" else "There are no", o)),

    "Classwork: LC938 Range Sum of BST":
        lambda c, o: (
            "Adding up every BST value that falls inside `[lo, hi]` gives "
            "`%s`." % o),

    "Classwork: LC669 Trim a Binary Search Tree":
        lambda c, o: (
            "Every node whose value falls outside `[lo, hi]` is dropped; the "
            "remaining nodes still form a valid BST. Result in level order: "
            "`%s`." % o),

    # ------------------------------------------------------------ LEC-26 ----
    "Classwork: Sort activities by end time and print the sorted order":
        lambda c, o: (
            "The activities are re-listed in increasing order of finish "
            "time, breaking ties by earlier start time."),

    "Classwork: N meetings in one room (GfG)":
        lambda c, o: (
            "Only one meeting can run at a time. The largest number of "
            "non-overlapping meetings you can fit is `%s`." % o),

    "Classwork: LC435 Non-overlapping Intervals":
        lambda c, o: (
            "You must remove `%s` interval(s) so that no two of the "
            "remaining ones overlap." % o),

    "Classwork: Maximum number of activities selected (GfG)":
        lambda c, o: (
            "The largest number of activities that can share the single "
            "resource without overlapping is `%s`." % o),

    # ------------------------------------------------------------ LEC-27 ----
    "Classwork: Given sorted intervals, check whether any two overlap":
        lambda c, o: (
            "Walking through the intervals in order, the answer is `%s`: "
            "%s two intervals whose ranges overlap."
            % (o, "there are" if o == "true" else "there are no")),

    "Classwork: LC56 Merge Intervals":
        lambda c, o: (
            "Overlapping intervals are combined into a single interval "
            "covering both. The final list is printed in increasing order "
            "of start time."),

    "Classwork: LC57 Insert Interval":
        lambda c, o: (
            "The new interval is added and merged with any existing "
            "intervals it overlaps."),

    "Classwork: Minimum number of platforms (GfG)":
        lambda c, o: (
            "At the busiest moment, `%s` trains are at the station "
            "simultaneously, so `%s` platforms are needed." % (o, o)),

    # ------------------------------------------------------------ LEC-28 ----
    "Classwork: Sort items by value/weight ratio and print the order":
        lambda c, o: (
            "The items are re-listed in decreasing order of the "
            "value-to-weight ratio."),

    "Classwork: Fractional Knapsack (GfG)":
        lambda c, o: (
            "Filling the sack with the most `value per unit weight` first, "
            "and breaking the last item to exactly fill the capacity, gives "
            "the maximum total value `%s`." % o),

    "Classwork: Job Sequencing Problem (GfG)":
        lambda c, o: (
            "The two numbers are how many jobs get done and the total "
            "profit earned by scheduling each one no later than its "
            "deadline: `%s`." % o),

    "Classwork: Minimum cost to connect ropes (GfG)":
        lambda c, o: (
            "Each join costs the sum of the two ropes being joined. "
            "Repeatedly joining the two shortest ropes keeps that cost "
            "small; the total is `%s`." % o),

    # ------------------------------------------------------------ LEC-29 ----
    "Classwork: LC605 Can Place Flowers":
        lambda c, o: (
            "Given the no-adjacent-flowers rule, `%s` more flowers can be "
            "planted (the requested number %s that limit)."
            % (o, "does not exceed" if o == "true" else "exceeds")),

    "Classwork: LC55 Jump Game":
        lambda c, o: (
            "Following the jump lengths from index 0, the last index %s "
            "reachable, so the answer is `%s`."
            % ("is" if o == "true" else "is not", o)),

    "Classwork: LC134 Gas Station":
        lambda c, o: (
            "Starting the loop at station `%s` keeps the tank non-negative "
            "the whole way (or `-1` if no starting station works)." % o),

    "Classwork: LC135 Candy":
        lambda c, o: (
            "Every child gets at least one candy, and a child with a "
            "higher rating than a neighbour gets more candy than that "
            "neighbour. The smallest total that satisfies both is `%s`."
            % o),

    # ------------------------------------------------------------ LEC-30 ----
    "Classwork: LC1005 Maximize Sum Of Array After K Negations":
        lambda c, o: (
            "After up to `k` sign flips (spent first on the most negative "
            "values, then, if `k` is still positive, wasted on the "
            "current smallest value), the largest possible sum is `%s`."
            % o),

    "Classwork: LC767 Reorganize String":
        lambda c, o: (
            "A valid rearrangement has no two neighbouring characters "
            "equal. If none is possible the output is empty; otherwise "
            "any valid one is accepted."),

    "Classwork: LC621 Task Scheduler":
        lambda c, o: (
            "Given the cooldown rule between equal tasks, `%s` intervals "
            "(including any needed idle slots) are enough to run every "
            "task." % o),

    # ------------------------------------------------------------ LEC-31 ----
    "Classwork: Compute the nth Fibonacci iteratively with two variables":
        lambda c, o: (
            "`F(0) = 0`, `F(1) = 1`, and each later value is the sum of "
            "the previous two. `F(%s) = %s`." % (c.strip(), o)),

    "Classwork: LC509 Fibonacci Number":
        lambda c, o: (
            "Same Fibonacci definition: `F(0) = 0`, `F(1) = 1`, next is "
            "the sum of the previous two. `F(%s) = %s`."
            % (c.strip(), o)),

    "Classwork: LC70 Climbing Stairs":
        lambda c, o: (
            "You may climb 1 or 2 steps at a time. There are `%s` distinct "
            "ways to reach step `%s`." % (o, c.strip())),

    "Classwork: LC198 House Robber":
        lambda c, o: (
            "Robbing two neighbouring houses is not allowed. The largest "
            "total you can take from a valid selection is `%s`." % o),

    # ------------------------------------------------------------ LEC-32 ----
    "Classwork: Draw the DP table by hand for making change of a small amount":
        lambda c, o: (
            "Position `i` in the row is the fewest coins that make amount "
            "`i`. `x` means the amount cannot be made with the given "
            "denominations. Row: `%s`." % o),

    "Classwork: LC322 Coin Change":
        lambda c, o: (
            "The smallest number of coins that adds up to the target "
            "amount is `%s` (or `-1` if it cannot be made)." % o),

    "Classwork: LC518 Coin Change II":
        lambda c, o: (
            "The number of distinct combinations of coins that add up to "
            "the target amount is `%s`." % o),

    "Classwork: Minimum number of coins (GfG)":
        lambda c, o: (
            "Using each denomination any number of times, the smallest "
            "count of coins that sums to the amount is `%s` (or `-1` if "
            "the amount cannot be made)." % o),

    # ------------------------------------------------------------ LEC-33 ----
    "Classwork: LC674 Longest Continuous Increasing Subsequence":
        lambda c, o: (
            "Scanning left to right, the longest run of values where each "
            "is strictly greater than the previous is `%s` long." % o),

    "Classwork: LC300 Longest Increasing Subsequence":
        lambda c, o: (
            "Picking values from the array in order (not necessarily "
            "adjacent) so that each is strictly greater than the previous, "
            "the longest such pick has length `%s`." % o),

    "Classwork: LC1143 Longest Common Subsequence":
        lambda c, o: (
            "The longest sequence of characters that appears in both "
            "strings in the same relative order (not necessarily adjacent) "
            "has length `%s`." % o),

    "Classwork: Longest Increasing Subsequence in O(n log n) (GfG)":
        lambda c, o: (
            "Same problem as the classic Longest Increasing Subsequence, "
            "answer `%s`; the constraint here is that a fast solution is "
            "expected." % o),

    # ------------------------------------------------------------ LEC-34 ----
    "Classwork: LC1480 Running Sum of 1d Array":
        lambda c, o: (
            "Position `i` in the output is the sum of the first `i + 1` "
            "values of the input array: `%s`." % o),

    "Classwork: LC62 Unique Paths":
        lambda c, o: (
            "Only right and down moves are allowed. There are `%s` "
            "distinct paths from the top-left to the bottom-right." % o),

    "Classwork: LC64 Minimum Path Sum":
        lambda c, o: (
            "Moving only right or down and summing the grid values along "
            "the way, the smallest possible total is `%s`." % o),

    "Classwork: LC63 Unique Paths II":
        lambda c, o: (
            "Right/down moves are still the only ones allowed, but "
            "obstacles cannot be entered. Total distinct paths: `%s`." % o),

    # ------------------------------------------------------------ LEC-35 ----
    "Classwork: Generate all subsets of a 3-element array and print their sums":
        lambda c, o: (
            "For each subset index `mask` from 0 to 7 (in binary), "
            "including element `i` when bit `i` of `mask` is 1, the "
            "resulting subset sum is printed on its own line."),

    "Classwork: Subset Sum (GfG)":
        lambda c, o: (
            "Some subset of the array adds up exactly to the target "
            "value, so the answer is `%s`."
            % (o if o in ("true", "false") else o)),

    "Classwork: LC416 Partition Equal Subset Sum":
        lambda c, o: (
            "The array %s be split into two groups with equal sums, so "
            "the answer is `%s`."
            % ("can" if o == "true" else "cannot", o)),

    "Classwork: LC91 Decode Ways":
        lambda c, o: (
            "Using the mapping `1 -> A, 2 -> B, ..., 26 -> Z`, the digit "
            "string can be decoded in `%s` distinct ways." % o),

    # ------------------------------------------------------------ LEC-36 ----
    "Classwork: Solve 0/1 knapsack for n=3 by drawing the DP table by hand":
        lambda c, o: (
            "Row `i` of the table is `dp[i][0..W]`: the best value using "
            "only the first `i` items with capacity `c`. The bottom-right "
            "entry is the final answer."),

    "Classwork: 0/1 Knapsack (GfG)":
        lambda c, o: (
            "Each item is either fully taken or left, and the sack cannot "
            "exceed the capacity. The largest total value achievable is "
            "`%s`." % o),

    "Classwork: LC494 Target Sum":
        lambda c, o: (
            "Assigning a `+` or `-` sign to every value, the number of "
            "sign choices that sum to the target is `%s`." % o),

    # ------------------------------------------------------------ LEC-37 ----
    "Classwork: Minimum coins for amount N using only coin 1 (trace the recurrence)":
        lambda c, o: (
            "With only 1-coin denominations available, the number of "
            "coins needed for amount `%s` is exactly `%s`."
            % (c.strip(), o)),

    "Classwork: Unbounded Knapsack (GfG)":
        lambda c, o: (
            "Each item can be taken any number of times; the sack cannot "
            "exceed the capacity. The largest total value achievable is "
            "`%s`." % o),

    "Classwork: Rod Cutting (GfG)":
        lambda c, o: (
            "Splitting a rod of length `n` into any number of pieces of "
            "any lengths, the largest total price achievable is `%s`."
            % o),

    # ------------------------------------------------------------ LEC-38 ----
    "Classwork: Count matching characters at the same index in two strings":
        lambda c, o: (
            "Comparing position by position, `%s` position(s) hold the "
            "same character in both strings." % o),

    "Classwork: LC583 Delete Operation for Two Strings":
        lambda c, o: (
            "Deleting `%s` character(s) in total (from either string) "
            "makes the two strings equal." % o),

    "Classwork: LC712 Minimum ASCII Delete Sum for Two Strings":
        lambda c, o: (
            "Choosing which characters to delete to make the two strings "
            "equal, the smallest total ASCII value of the deleted "
            "characters is `%s`." % o),

    "Classwork: LC72 Edit Distance":
        lambda c, o: (
            "The smallest number of single-character insertions, "
            "deletions, or substitutions that turn one string into the "
            "other is `%s`." % o),

    # ------------------------------------------------------------ LEC-39 ----
    "Classwork: Check whether a string is a palindrome using two pointers":
        lambda c, o: (
            "Comparing the string character by character from the outside "
            "in, the answer is `%s`." % o),

    "Classwork: LC516 Longest Palindromic Subsequence":
        lambda c, o: (
            "Picking characters from the string in order (not necessarily "
            "adjacent) so they read the same forwards and backwards, the "
            "longest such pick has length `%s`." % o),

    "Classwork: Matrix Chain Multiplication (GfG)":
        lambda c, o: (
            "By choosing the best order to multiply the matrices, the "
            "smallest possible total number of scalar multiplications is "
            "`%s`." % o),

    "Classwork: LC1092 Shortest Common Supersequence":
        lambda c, o: (
            "The shortest string that has both input strings as "
            "subsequences has length equal to the length of the printed "
            "answer."),

    # ------------------------------------------------------------ LEC-40 ----
    "Classwork: Split an array at every index and print both halves' sums":
        lambda c, o: (
            "For every split index from 1 to `n-1`, the first number is "
            "the sum of the elements before the split and the second is "
            "the sum of the elements from the split onward."),

    "Classwork: LC132 Palindrome Partitioning II":
        lambda c, o: (
            "The smallest number of cuts needed so that every piece of "
            "the string is a palindrome is `%s`." % o),

    "Classwork: LC312 Burst Balloons":
        lambda c, o: (
            "Choosing the order in which to burst the balloons to "
            "maximise the running score, the largest possible total is "
            "`%s`." % o),
}


# ---------------------------------------------------------- local emit -----
# Local copy of make_md.emit that also drops a plain-language `**Explanation N**`
# after the first `N_EXPLAIN_CASES` sample outputs whenever EXPLANATIONS knows
# about the title. Keeps the WHY, not the HOW: no algorithmic hints, only what
# the input means and what the output is saying about it.
N_EXPLAIN_CASES = 2


def _explain_for(title, idx, case, output):
    """Return the explanation string for sample `idx` (1-indexed) of `title`,
    or "" when nothing is registered. An entry may be a plain string (only
    Sample 1 explained), a list of strings (one per sample; `None` skips),
    or a callable `f(case, output)` used for every sample it is asked for."""
    entry = EXPLANATIONS.get(title)
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
    lines = ["# DSA-301 challenges", "",
             "Generated by make_classwork_missing_md.py. Sample outputs are "
             "computed from the reference solutions, not written by hand.",
             "", "---", ""]
    for p in problems:
        lines.append("## %s" % p["title"])
        hr_id = HR_ID_OVERRIDE.get(p["title"]) or p.get("hr_id")
        if hr_id:
            lines.append("<!-- hackerrank_id: %s -->" % hr_id)
        lines.append("")
        diff = SHELL_DIFFICULTY.get(p["title"])
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
                    # editor.py's parse_md looks for this exact heading and
                    # passes the body through to mark_samples so HackerRank
                    # renders it in the sample-test-case "Explanation" panel.
                    lines.append("**Sample Explanation %d**" % i)
                    lines.append(expl)
            lines.append("")
        lines.append("---")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


# Titles that don't yet have a HackerRank challenge shell. Pass
# --missing-only to emit just these into DSA301_classwork_shells_todo.md,
# a reference file you can read while creating the shells on HackerRank.
# Once the shells exist, the main file (DSA301_classwork_missing.md) is
# what editor.py --apply --tests writes into them.
SHELLS_TO_CREATE = {
    "Classwork: Build a 3-node binary tree manually and print root, left, right",
    "Classwork: Print all nodes level by level into one list using BFS",
    "Classwork: Count the number of levels in a binary tree",
    "Classwork: Check if a binary tree is a full binary tree",
    "Classwork: Left view of a binary tree (GfG)",
    "Classwork: Swap the left and right children of the root only",
    "Classwork: Find the sum of all leaf nodes in a binary tree",
    "Classwork: Search whether a value exists in a binary tree",
    "Classwork: Build a binary tree from a level-order array and print inorder",
    "Classwork: Count the total number of nodes in a binary tree",
    "Classwork: Print the inorder of a BST and verify it is sorted",
    "Classwork: Check if an inorder traversal array is strictly increasing",
    "Classwork: Find the inorder successor of a node using the inorder array",
    "Classwork: Find the ceiling of a key in a BST (GfG)",
    "Classwork: Print all BST keys in decreasing order (reverse inorder)",
    "Classwork: Sort activities by end time and print the sorted order",
    "Classwork: Given sorted intervals, check whether any two overlap",
    "Classwork: Sort items by value/weight ratio and print the order",
    "Classwork: LC605 Can Place Flowers",
    "Classwork: LC1005 Maximize Sum Of Array After K Negations",
    "Classwork: Compute the nth Fibonacci iteratively with two variables",
    "Classwork: Draw the DP table by hand for making change of a small amount",
    "Classwork: LC674 Longest Continuous Increasing Subsequence",
    "Classwork: LC1480 Running Sum of 1d Array",
    "Classwork: Generate all subsets of a 3-element array and print their sums",
    "Classwork: Solve 0/1 knapsack for n=3 by drawing the DP table by hand",
    "Classwork: Minimum coins for amount N using only coin 1 (trace the recurrence)",
    "Classwork: Count matching characters at the same index in two strings",
    "Classwork: Check whether a string is a palindrome using two pointers",
    "Classwork: Split an array at every index and print both halves' sums",
}

# The difficulty label per the curriculum sheet, for every classwork row.
# Deduped by title -- if the sheet lists the same problem in two lectures with
# the same difficulty, one entry covers both. Any title not in this dict has no
# `**Difficulty**:` line rendered.
SHELL_DIFFICULTY = {
    # ---- LEC-11 (all Easy) --------------------------------------------------
    "Classwork: Build a 3-node binary tree manually and print root, left, right": "Easy",
    "Classwork: LC94 Binary Tree Inorder Traversal": "Easy",
    "Classwork: LC144 Binary Tree Preorder Traversal": "Easy",
    "Classwork: LC145 Binary Tree Postorder Traversal": "Easy",
    # ---- LEC-12 -------------------------------------------------------------
    "Classwork: Print all nodes level by level into one list using BFS": "Easy",
    "Classwork: LC102 Binary Tree Level Order Traversal": "Medium",
    "Classwork: LC199 Binary Tree Right Side View": "Medium",
    "Classwork: LC94 Inorder Traversal (iterative)": "Medium",
    # ---- LEC-13 -------------------------------------------------------------
    "Classwork: Count the number of levels in a binary tree": "Easy",
    "Classwork: LC104 Maximum Depth of Binary Tree": "Easy",
    "Classwork: LC111 Minimum Depth of Binary Tree": "Easy",
    "Classwork: LC543 Diameter of Binary Tree": "Medium",
    # ---- LEC-14 -------------------------------------------------------------
    "Classwork: Check if a binary tree is a full binary tree": "Easy",
    "Classwork: LC110 Balanced Binary Tree": "Easy",
    "Classwork: LC101 Symmetric Tree": "Easy",
    # LC199 duplicate -- already listed above as Medium.
    # ---- LEC-15 -------------------------------------------------------------
    "Classwork: Left view of a binary tree (GfG)": "Easy",
    "Classwork: Top view of a binary tree (GfG)": "Medium",
    "Classwork: Boundary traversal of a binary tree (GfG)": "Hard",
    "Classwork: LC987 Vertical Order Traversal of a Binary Tree": "Hard",
    # ---- LEC-16 -------------------------------------------------------------
    "Classwork: Swap the left and right children of the root only": "Easy",
    "Classwork: LC226 Invert Binary Tree": "Easy",
    "Classwork: LC100 Same Tree": "Easy",
    # ---- LEC-17 -------------------------------------------------------------
    "Classwork: Find the sum of all leaf nodes in a binary tree": "Easy",
    "Classwork: LC112 Path Sum": "Easy",
    "Classwork: LC113 Path Sum II": "Medium",
    "Classwork: LC124 Binary Tree Maximum Path Sum": "Hard",
    # ---- LEC-18 -------------------------------------------------------------
    "Classwork: Search whether a value exists in a binary tree": "Easy",
    "Classwork: LC236 Lowest Common Ancestor of a Binary Tree": "Medium",
    "Classwork: LCA using root-to-node paths (GfG)": "Medium",
    "Classwork: Distance between two nodes via LCA (GfG)": "Medium",
    # ---- LEC-19 -------------------------------------------------------------
    "Classwork: Build a binary tree from a level-order array and print inorder": "Easy",
    "Classwork: LC105 Construct Binary Tree from Preorder and Inorder": "Medium",
    "Classwork: LC106 Construct Binary Tree from Inorder and Postorder": "Medium",
    "Classwork: LC114 Flatten Binary Tree to Linked List": "Medium",
    # ---- LEC-20 -------------------------------------------------------------
    "Classwork: Count the total number of nodes in a binary tree": "Easy",
    "Classwork: LC222 Count Complete Tree Nodes": "Medium",
    "Classwork: LC863 All Nodes Distance K in Binary Tree": "Medium",
    "Classwork: LC297 Serialize and Deserialize Binary Tree": "Hard",
    # ---- LEC-21 -------------------------------------------------------------
    "Classwork: Print the inorder of a BST and verify it is sorted": "Easy",
    "Classwork: LC700 Search in a Binary Search Tree": "Easy",
    "Classwork: Iterative BST search (GfG)": "Easy",
    "Classwork: LC701 Insert into a Binary Search Tree": "Medium",
    # ---- LEC-22 -------------------------------------------------------------
    "Classwork: Check if an inorder traversal array is strictly increasing": "Easy",
    "Classwork: LC530 Minimum Absolute Difference in BST": "Easy",
    "Classwork: LC501 Find Mode in Binary Search Tree": "Easy",
    "Classwork: LC98 Validate Binary Search Tree": "Medium",
    # ---- LEC-23 -------------------------------------------------------------
    "Classwork: Find the inorder successor of a node using the inorder array": "Easy",
    "Classwork: LC450 Delete Node in a BST": "Medium",
    "Classwork: LC230 Kth Smallest Element in a BST": "Medium",
    "Classwork: Kth largest element in a BST (GfG)": "Medium",
    # ---- LEC-24 -------------------------------------------------------------
    "Classwork: Find the ceiling of a key in a BST (GfG)": "Easy",
    "Classwork: LC108 Convert Sorted Array to Binary Search Tree": "Easy",
    "Classwork: LC235 Lowest Common Ancestor of a BST": "Medium",
    "Classwork: LC173 Binary Search Tree Iterator": "Medium",
    # ---- LEC-25 -------------------------------------------------------------
    "Classwork: Print all BST keys in decreasing order (reverse inorder)": "Easy",
    "Classwork: LC653 Two Sum IV - Input is a BST": "Easy",
    "Classwork: LC938 Range Sum of BST": "Easy",
    "Classwork: LC669 Trim a Binary Search Tree": "Medium",
    # ---- LEC-26 -------------------------------------------------------------
    "Classwork: Sort activities by end time and print the sorted order": "Easy",
    "Classwork: N meetings in one room (GfG)": "Medium",
    "Classwork: LC435 Non-overlapping Intervals": "Medium",
    "Classwork: Maximum number of activities selected (GfG)": "Medium",
    # ---- LEC-27 -------------------------------------------------------------
    "Classwork: Given sorted intervals, check whether any two overlap": "Easy",
    "Classwork: LC56 Merge Intervals": "Medium",
    "Classwork: LC57 Insert Interval": "Medium",
    "Classwork: Minimum number of platforms (GfG)": "Medium",
    # ---- LEC-28 -------------------------------------------------------------
    "Classwork: Sort items by value/weight ratio and print the order": "Easy",
    "Classwork: Fractional Knapsack (GfG)": "Medium",
    "Classwork: Job Sequencing Problem (GfG)": "Medium",
    "Classwork: Minimum cost to connect ropes (GfG)": "Medium",
    # ---- LEC-29 -------------------------------------------------------------
    "Classwork: LC605 Can Place Flowers": "Easy",
    "Classwork: LC55 Jump Game": "Medium",
    "Classwork: LC134 Gas Station": "Medium",
    "Classwork: LC135 Candy": "Hard",
    # ---- LEC-30 -------------------------------------------------------------
    "Classwork: LC1005 Maximize Sum Of Array After K Negations": "Easy",
    "Classwork: LC767 Reorganize String": "Medium",
    "Classwork: LC621 Task Scheduler": "Medium",
    # ---- LEC-31 -------------------------------------------------------------
    "Classwork: Compute the nth Fibonacci iteratively with two variables": "Easy",
    "Classwork: LC509 Fibonacci Number": "Easy",
    "Classwork: LC70 Climbing Stairs": "Easy",
    "Classwork: LC198 House Robber": "Medium",
    # ---- LEC-32 -------------------------------------------------------------
    "Classwork: Draw the DP table by hand for making change of a small amount": "Easy",
    "Classwork: LC322 Coin Change": "Medium",
    "Classwork: LC518 Coin Change II": "Medium",
    "Classwork: Minimum number of coins (GfG)": "Medium",
    # ---- LEC-33 -------------------------------------------------------------
    "Classwork: LC674 Longest Continuous Increasing Subsequence": "Easy",
    "Classwork: LC300 Longest Increasing Subsequence": "Medium",
    "Classwork: LC1143 Longest Common Subsequence": "Medium",
    "Classwork: Longest Increasing Subsequence in O(n log n) (GfG)": "Hard",
    # ---- LEC-34 -------------------------------------------------------------
    "Classwork: LC1480 Running Sum of 1d Array": "Easy",
    "Classwork: LC62 Unique Paths": "Medium",
    "Classwork: LC64 Minimum Path Sum": "Medium",
    "Classwork: LC63 Unique Paths II": "Medium",
    # ---- LEC-35 -------------------------------------------------------------
    "Classwork: Generate all subsets of a 3-element array and print their sums": "Easy",
    "Classwork: Subset Sum (GfG)": "Medium",
    "Classwork: LC416 Partition Equal Subset Sum": "Medium",
    "Classwork: LC91 Decode Ways": "Medium",
    # ---- LEC-36 -------------------------------------------------------------
    "Classwork: Solve 0/1 knapsack for n=3 by drawing the DP table by hand": "Easy",
    "Classwork: 0/1 Knapsack (GfG)": "Medium",
    "Classwork: LC494 Target Sum": "Medium",
    # ---- LEC-37 -------------------------------------------------------------
    "Classwork: Minimum coins for amount N using only coin 1 (trace the recurrence)": "Easy",
    "Classwork: Unbounded Knapsack (GfG)": "Medium",
    "Classwork: Rod Cutting (GfG)": "Medium",
    # ---- LEC-38 -------------------------------------------------------------
    "Classwork: Count matching characters at the same index in two strings": "Easy",
    "Classwork: LC583 Delete Operation for Two Strings": "Medium",
    "Classwork: LC712 Minimum ASCII Delete Sum for Two Strings": "Medium",
    "Classwork: LC72 Edit Distance": "Hard",
    # ---- LEC-39 -------------------------------------------------------------
    "Classwork: Check whether a string is a palindrome using two pointers": "Easy",
    "Classwork: LC516 Longest Palindromic Subsequence": "Medium",
    "Classwork: Matrix Chain Multiplication (GfG)": "Hard",
    "Classwork: LC1092 Shortest Common Supersequence": "Hard",
    # ---- LEC-40 -------------------------------------------------------------
    "Classwork: Split an array at every index and print both halves' sums": "Easy",
    "Classwork: LC132 Palindrome Partitioning II": "Hard",
    "Classwork: LC312 Burst Balloons": "Hard",
}


def main():
    missing_only = "--missing-only" in sys.argv[1:]

    index = build_index()

    # Sheet-order, deduped: keeping the first sighting of each title.
    seen = set()
    ordered_titles = []
    missing = []
    for t in SHEET_TITLES:
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
        problems = [index[t] for t in ordered_titles if t in SHELLS_TO_CREATE]
        out_name = "DSA301_classwork_shells_todo.md"
    else:
        problems = [index[t] for t in ordered_titles]
        out_name = "DSA301_classwork_missing.md"

    # Runtime sanity: run each solve on every case so a broken lambda blows
    # up here rather than silently producing empty output in the MD.
    for p in problems:
        for c in p["cases"]:
            p["solve"](c)

    # Warn (but do not fail) if a problem has no explanation registered --
    # this makes it easy to spot which ones still need one.
    unexplained = [p["title"] for p in problems
                   if p["title"] not in EXPLANATIONS]
    if unexplained:
        print("no explanation registered for %d problem(s):"
              % len(unexplained))
        for t in unexplained:
            print("  %s" % t)

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        out_name)
    emit_with_explanations(path, problems, links=True)

    print("wrote %s" % os.path.basename(path))
    print("  %d classwork problems (deduped from %d sheet rows)"
          % (len(problems), len(SHEET_TITLES)))
    print("  %d total test cases" % sum(len(p["cases"]) for p in problems))
    print("  %d problems with an explanation"
          % (len(problems) - len(unexplained)))


if __name__ == "__main__":
    main()
