#!/usr/bin/env python3
"""
make_md.py -- generate challenge markdown for editor.py.

    python make_md.py            writes DSA301_LEC11-20.md

Each problem below carries a statement and a reference solution. The sample
outputs are COMPUTED by running that solution over the listed inputs -- they are
never typed by hand. That is the whole point: the original challenges had
hand-made data that was wrong.

SANITY holds a few answers worked out by hand. If a reference solution disagrees
with one, generation aborts rather than emitting bad data.

Only problems written up here are emitted, so editor.py can never overwrite a
live challenge whose replacement has not been authored yet.
"""

import os
import sys

import dp_problems
import graph_problems
import problem_links
from collections import deque

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- tree utils --
class N:
    __slots__ = ("v", "l", "r")

    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


def build(s):
    """Level-order tokens, 'null' for a missing child -> root node."""
    t = s.split()
    if not t or t[0] == "null":
        return None
    root = N(int(t[0]))
    q, i = deque([root]), 1
    while q and i < len(t):
        n = q.popleft()
        if i < len(t):
            x = t[i]; i += 1
            if x != "null":
                n.l = N(int(x)); q.append(n.l)
        if i < len(t):
            x = t[i]; i += 1
            if x != "null":
                n.r = N(int(x)); q.append(n.r)
    return root


def two(s):
    """Two trees, one per line."""
    parts = s.split("\n")
    a = parts[0] if len(parts) > 0 else "null"
    b = parts[1] if len(parts) > 1 else "null"
    return build(a), build(b)


def levels(root):
    out, q = [], deque([root] if root else [])
    while q:
        row = []
        for _ in range(len(q)):
            n = q.popleft()
            row.append(n)
            if n.l: q.append(n.l)
            if n.r: q.append(n.r)
        out.append(row)
    return out


TREE_IN = ("A single line with the tree in **level order**, values separated by "
           "spaces. The token `null` marks a missing child. An empty tree is the "
           "single token `null`.")
TREE_IN2 = ("Two lines, each a tree in **level order** with `null` for a missing "
            "child, exactly as described above.")
SEQ_OUT = ("A single line: the values separated by single spaces. Print an empty "
           "line if there is nothing to output.")
NUM_OUT = "A single line containing one integer."
BOOL_OUT = "A single line: `true` or `false`."
CONS = ("- `0 <= N <= 10^4` nodes\n"
        "- `-10^4 <= node value <= 10^4`\n"
        "- Expected time `O(N)`")

# Illustrative cases FIRST: the leading ones become the visible samples, and an
# empty tree printing an empty line makes a useless first example. Edge cases
# still run, further down.
TREES = [
    "1 2 3",
    "1 2 3 4 5 null 6 null null 7 8",
    "5 3 8 2 4 7 9",
    "1 null 2 null 3 null 4",
    "1 2 null 3 null 4 null",
    "-5 -3 8 0 null null 12",
    "1 2 3 4 null null 5 6 null null 7",
    "10 5 15 3 7 null 18 1 null 6 8",
    "7",
    "null",
]


# ------------------------------------------------------------------ problems --
def leaves(root):
    out = []
    def go(n):
        if not n: return
        if not n.l and not n.r: out.append(n.v)
        go(n.l); go(n.r)
    go(root)
    return out


def depth(n):
    return 0 if not n else 1 + max(depth(n.l), depth(n.r))


def diameter(root):
    best = [0]
    def h(n):
        if not n: return 0
        a, b = h(n.l), h(n.r)
        best[0] = max(best[0], a + b)
        return 1 + max(a, b)
    h(root)
    return best[0]


def min_depth(n):
    if not n: return 0
    if not n.l: return 1 + min_depth(n.r)
    if not n.r: return 1 + min_depth(n.l)
    return 1 + min(min_depth(n.l), min_depth(n.r))


def balanced(root):
    ok = [True]
    def h(n):
        if not n: return 0
        a, b = h(n.l), h(n.r)
        if abs(a - b) > 1: ok[0] = False
        return 1 + max(a, b)
    h(root)
    return ok[0]


def fmt(xs):
    return " ".join(str(x) for x in xs)


def fmt_bool(b):
    return "true" if b else "false"


def inorder(s):
    out, st, cur = [], [], build(s)
    while st or cur:
        while cur:
            st.append(cur); cur = cur.l
        cur = st.pop(); out.append(cur.v); cur = cur.r
    return fmt(out)


def preorder(s):
    root = build(s)
    out, st = [], [root] if root else []
    while st:
        n = st.pop(); out.append(n.v)
        if n.r: st.append(n.r)
        if n.l: st.append(n.l)
    return fmt(out)


def postorder(s):
    root = build(s)
    out, st = [], [root] if root else []
    while st:
        n = st.pop(); out.append(n.v)
        if n.l: st.append(n.l)
        if n.r: st.append(n.r)
    return fmt(reversed(out))


def serialize(root):
    """Level order with 'null' markers, trailing nulls trimmed. Uniquely
    determines the tree, so it is usable as expected output for construction."""
    if not root:
        return "null"
    out, q = [], deque([root])
    while q:
        n = q.popleft()
        if n is None:
            out.append("null")
            continue
        out.append(str(n.v))
        q.append(n.l)
        q.append(n.r)
    while out and out[-1] == "null":
        out.pop()
    return " ".join(out)


def walk_hd(root):
    """(horizontal distance, depth, order, value) for every node, BFS order."""
    res, q, k = [], deque([(root, 0, 0)] if root else []), 0
    while q:
        n, hd, d = q.popleft()
        res.append((hd, d, k, n.v))
        k += 1
        if n.l: q.append((n.l, hd - 1, d + 1))
        if n.r: q.append((n.r, hd + 1, d + 1))
    return res


def top_view(root):
    seen, out = {}, []
    for hd, d, k, v in walk_hd(root):
        if hd not in seen:
            seen[hd] = v
    return [seen[h] for h in sorted(seen)]


def bottom_view(root):
    seen = {}
    for hd, d, k, v in walk_hd(root):
        seen[hd] = v            # later BFS nodes overwrite earlier ones
    return [seen[h] for h in sorted(seen)]


def vertical_order(root):
    """LC987: by column, then row, then value."""
    items = sorted((hd, d, v) for hd, d, k, v in walk_hd(root))
    cols = {}
    for hd, d, v in items:
        cols.setdefault(hd, []).append(v)
    return [cols[h] for h in sorted(cols)]


def diagonal_view(root):
    """Right child stays on the diagonal, left child moves to the next one."""
    groups, q = {}, deque([(root, 0)] if root else [])
    while q:
        n, dg = q.popleft()
        while n:
            groups.setdefault(dg, []).append(n.v)
            if n.l:
                q.append((n.l, dg + 1))
            n = n.r
    return [groups[d] for d in sorted(groups)]


def boundary(root):
    """Root, then left boundary top-down, then leaves L-R, then right boundary
    bottom-up. Leaves are not repeated."""
    if not root:
        return []
    def leaf(n): return n and not n.l and not n.r
    out = [] if leaf(root) else [root.v]

    n = root.l
    while n:
        if not leaf(n): out.append(n.v)
        n = n.l or n.r

    out.extend(leaves(root))

    right, n = [], root.r
    while n:
        if not leaf(n): right.append(n.v)
        n = n.r or n.l
    out.extend(reversed(right))
    return out


def morris_inorder(root):
    out, cur = [], root
    while cur:
        if not cur.l:
            out.append(cur.v); cur = cur.r
        else:
            pre = cur.l
            while pre.r and pre.r is not cur:
                pre = pre.r
            if not pre.r:
                pre.r = cur; cur = cur.l
            else:
                pre.r = None; out.append(cur.v); cur = cur.r
    return out


def invert(n):
    if not n:
        return None
    n.l, n.r = invert(n.r), invert(n.l)
    return n


def mirror_of(a, b):
    if not a and not b: return True
    if not a or not b: return False
    return a.v == b.v and mirror_of(a.l, b.r) and mirror_of(a.r, b.l)


def flip_equiv(a, b):
    if not a and not b: return True
    if not a or not b or a.v != b.v: return False
    return ((flip_equiv(a.l, b.l) and flip_equiv(a.r, b.r)) or
            (flip_equiv(a.l, b.r) and flip_equiv(a.r, b.l)))


def has_path_sum(n, t):
    if not n: return False
    if not n.l and not n.r: return n.v == t
    return has_path_sum(n.l, t - n.v) or has_path_sum(n.r, t - n.v)


def path_sum_all(root, t):
    res, cur = [], []
    def go(n, rem):
        if not n: return
        cur.append(n.v)
        if not n.l and not n.r and rem == n.v:
            res.append(list(cur))
        else:
            go(n.l, rem - n.v); go(n.r, rem - n.v)
        cur.pop()
    go(root, t)
    return res


def path_sum_count(root, t):
    """LC437: any downward path, prefix-sum counting."""
    seen = {0: 1}
    total = [0]
    def go(n, run):
        if not n: return
        run += n.v
        total[0] += seen.get(run - t, 0)
        seen[run] = seen.get(run, 0) + 1
        go(n.l, run); go(n.r, run)
        seen[run] -= 1
    go(root, 0)
    return total[0]


def smallest_from_leaf(root):
    best = [None]
    def go(n, suf):
        if not n: return
        suf = chr(ord('a') + n.v) + suf
        if not n.l and not n.r:
            if best[0] is None or suf < best[0]:
                best[0] = suf
            return
        go(n.l, suf); go(n.r, suf)
    go(root, "")
    return best[0] or ""


def find_lca(n, p, q):
    if not n or n.v == p or n.v == q:
        return n
    a, b = find_lca(n.l, p, q), find_lca(n.r, p, q)
    if a and b: return n
    return a or b


def depth_of(n, v, d=0):
    if not n: return -1
    if n.v == v: return d
    left = depth_of(n.l, v, d + 1)
    return left if left != -1 else depth_of(n.r, v, d + 1)


def dist_between(root, p, q):
    a = find_lca(root, p, q)
    return depth_of(a, p) + depth_of(a, q)


def lca_deepest(root):
    def go(n):
        if not n: return 0, None
        dl, al = go(n.l)
        dr, ar = go(n.r)
        if dl == dr: return dl + 1, n
        return (dl + 1, al) if dl > dr else (dr + 1, ar)
    return go(root)[1]


def from_pre_in(pre, ino):
    pos = {v: i for i, v in enumerate(ino)}
    it = [0]
    def go(lo, hi):
        if lo > hi: return None
        v = pre[it[0]]; it[0] += 1
        n = N(v); m = pos[v]
        n.l = go(lo, m - 1); n.r = go(m + 1, hi)
        return n
    return go(0, len(ino) - 1)


def from_in_post(ino, post):
    pos = {v: i for i, v in enumerate(ino)}
    it = [len(post) - 1]
    def go(lo, hi):
        if lo > hi: return None
        v = post[it[0]]; it[0] -= 1
        n = N(v); m = pos[v]
        n.r = go(m + 1, hi); n.l = go(lo, m - 1)
        return n
    return go(0, len(ino) - 1)


def from_pre_post(pre, post):
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


def bst_from_pre(pre):
    it = [0]
    def go(lo, hi):
        if it[0] >= len(pre): return None
        v = pre[it[0]]
        if v < lo or v > hi: return None
        it[0] += 1
        n = N(v)
        n.l = go(lo, v - 1)
        n.r = go(v + 1, hi)
        return n
    return go(-10 ** 9, 10 ** 9)


def flatten_pre(root):
    out = []
    st = [root] if root else []
    while st:
        n = st.pop(); out.append(n.v)
        if n.r: st.append(n.r)
        if n.l: st.append(n.l)
    return out


def count_complete(root):
    def h(n, left):
        d = 0
        while n:
            d += 1
            n = n.l if left else n.r
        return d
    if not root: return 0
    if h(root, True) == h(root, False):
        return 2 ** h(root, True) - 1
    return 1 + count_complete(root.l) + count_complete(root.r)


def max_width(root):
    best, q = 0, deque([(root, 0)] if root else [])
    while q:
        n_items = len(q)
        first = last = None
        for i in range(n_items):
            n, idx = q.popleft()
            if i == 0: first = idx
            last = idx
            if n.l: q.append((n.l, idx * 2))
            if n.r: q.append((n.r, idx * 2 + 1))
        best = max(best, last - first + 1)
    return best


def nodes_distance_k(root, target, k):
    par = {}
    def link(n, p):
        if not n: return
        par[n.v] = p
        link(n.l, n); link(n.r, n)
    link(root, None)

    start = None
    for n in iter_nodes(root):
        if n.v == target:
            start = n
    if not start:
        return []
    seen, q, out = {start.v}, deque([(start, 0)]), []
    while q:
        n, d = q.popleft()
        if d == k:
            out.append(n.v)
            continue
        for nxt in (n.l, n.r, par.get(n.v)):
            if nxt and nxt.v not in seen:
                seen.add(nxt.v)
                q.append((nxt, d + 1))
    return sorted(out)


def rows(s):
    return s.split("\n")


def ints(s):
    return [int(x) for x in s.split()]


# ------------------------------------------------------------------ BST utils --
def bst_find(n, k):
    while n:
        if n.v == k: return n
        n = n.l if k < n.v else n.r
    return None


def bst_insert(root, k):
    if not root: return N(k)
    n = root
    while True:
        if k < n.v:
            if not n.l:
                n.l = N(k); return root
            n = n.l
        elif k > n.v:
            if not n.r:
                n.r = N(k); return root
            n = n.r
        else:
            return root


def bst_delete(n, k):
    if not n: return None
    if k < n.v:
        n.l = bst_delete(n.l, k)
    elif k > n.v:
        n.r = bst_delete(n.r, k)
    else:
        if not n.l: return n.r
        if not n.r: return n.l
        s = n.r
        while s.l: s = s.l
        n.v = s.v
        n.r = bst_delete(n.r, s.v)
    return n


def in_list(root):
    out, st, cur = [], [], root
    while st or cur:
        while cur:
            st.append(cur); cur = cur.l
        cur = st.pop(); out.append(cur.v); cur = cur.r
    return out


def is_bst(root):
    prev = [None]
    ok = [True]
    def go(n):
        if not n or not ok[0]: return
        go(n.l)
        if prev[0] is not None and n.v <= prev[0]: ok[0] = False
        prev[0] = n.v
        go(n.r)
    go(root)
    return ok[0]


def min_abs_diff(root):
    xs = in_list(root)
    return min((b - a for a, b in zip(xs, xs[1:])), default=0)


def modes(root):
    xs = in_list(root)
    if not xs: return []
    counts = {}
    for x in xs:
        counts[x] = counts.get(x, 0) + 1
    hi = max(counts.values())
    return sorted(k for k, c in counts.items() if c == hi)


def recover_bst(root):
    """Exactly two nodes are swapped; put them back."""
    xs = in_list(root)
    srt = sorted(xs)
    bad = [i for i, (a, b) in enumerate(zip(xs, srt)) if a != b]
    if len(bad) == 2:
        a, b = xs[bad[0]], xs[bad[1]]
        for n in iter_nodes(root):
            if n.v == a: n.v = b
            elif n.v == b: n.v = a
    return root


def verify_preorder_bst(pre):
    st, lower = [], float("-inf")
    for v in pre:
        if v < lower: return False
        while st and v > st[-1]:
            lower = st.pop()
        st.append(v)
    return True


def kth_smallest(root, k):
    xs = in_list(root)
    return xs[k - 1] if 1 <= k <= len(xs) else None


def kth_largest(root, k):
    xs = in_list(root)
    return xs[-k] if 1 <= k <= len(xs) else None


def successor(root, k):
    res, n = None, root
    while n:
        if k < n.v:
            res = n.v; n = n.l
        else:
            n = n.r
    return res


def predecessor(root, k):
    res, n = None, root
    while n:
        if k > n.v:
            res = n.v; n = n.r
        else:
            n = n.l
    return res


def bst_lca(root, p, q):
    n = root
    while n:
        if p < n.v and q < n.v: n = n.l
        elif p > n.v and q > n.v: n = n.r
        else: return n.v
    return None


def sorted_to_bst(xs):
    def go(lo, hi):
        if lo > hi: return None
        m = (lo + hi) // 2
        n = N(xs[m])
        n.l = go(lo, m - 1)
        n.r = go(m + 1, hi)
        return n
    return go(0, len(xs) - 1)


def greater_tree(root):
    run = [0]
    def go(n):
        if not n: return
        go(n.r)
        run[0] += n.v
        n.v = run[0]
        go(n.l)
    go(root)
    return root


def largest_bst_subtree(root):
    """Returns the node count of the largest subtree that is a valid BST."""
    best = [0]
    def go(n):
        # (is_bst, size, min, max)
        if not n:
            return True, 0, float("inf"), float("-inf")
        lb, ls, lmin, lmax = go(n.l)
        rb, rs, rmin, rmax = go(n.r)
        if lb and rb and lmax < n.v < rmin:
            size = ls + rs + 1
            best[0] = max(best[0], size)
            return True, size, min(lmin, n.v), max(rmax, n.v)
        return False, 0, float("-inf"), float("inf")
    go(root)
    return best[0]


def range_values(root, lo, hi):
    return [v for v in in_list(root) if lo <= v <= hi]


BSTS = [
    "null",
    "8",
    "2 1 3",
    "8 3 10",
    "5 3 8 2 4 7 9",
    "10 5 15 3 7 null 18",
    "8 3 10 1 6 null 14 null null 4 7 13",
    "50 30 70 20 40 60 80",
    "20 10 30 5 15 25 35 1",
]


# New display order for the 9 entries of BSTS: illustrative first, degenerate
# ("8", "null") last. Applied to the (tree, key) PAIRS so every pairing that was
# chosen deliberately survives the reordering.
_BST_ORDER = [4, 6, 5, 2, 3, 7, 8, 1, 0]


def with_key(trees, keys):
    pairs = list(zip(trees, keys))
    if len(pairs) == len(_BST_ORDER):
        pairs = [pairs[i] for i in _BST_ORDER]
    return ["%s\n%s" % (t, k) for t, k in pairs]


PROBLEMS = [
    # ---- LEC-11 : DFS traversals -------------------------------------------
    dict(title="Classwork: LC94 Binary Tree Inorder Traversal",
         stmt="Given the root of a binary tree, return the **inorder** traversal of its node values.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS, solve=inorder, cases=TREES),

    dict(title="Classwork: LC144 Binary Tree Preorder Traversal",
         stmt="Given the root of a binary tree, return the **preorder** traversal of its node values.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS, solve=preorder, cases=TREES),

    dict(title="Classwork: LC145 Binary Tree Postorder Traversal",
         stmt="Given the root of a binary tree, return the **postorder** traversal of its node values.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: postorder(s), cases=TREES),

    dict(title="Homework: Count the total number of nodes recursively",
         stmt="Given the root of a binary tree, print the total number of nodes.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(len([1 for _ in iter_nodes(build(s))])), cases=TREES),

    dict(title="Homework: Print all leaf nodes from left to right",
         stmt="Given the root of a binary tree, print the values of all its **leaf** nodes from left to right. A leaf is a node with no children.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(leaves(build(s))), cases=TREES),

    # ---- LEC-12 : BFS -------------------------------------------------------
    dict(title="Classwork: LC102 Binary Tree Level Order Traversal",
         stmt="Given the root of a binary tree, print its **level order** traversal: all values at depth 0, then depth 1, and so on.",
         inp=TREE_IN,
         out="One line per level, values separated by spaces. Print nothing for an "
             "empty tree.",
         cons=CONS,
         solve=lambda s: "\n".join(fmt([n.v for n in row]) for row in levels(build(s))),
         cases=TREES),

    dict(title="Homework: LC103 Binary Tree Zigzag Level Order Traversal",
         stmt="Given the root of a binary tree, print its level order traversal **alternating direction**: the first level left to right, the second right to left, and so on.",
         inp=TREE_IN,
         out="One line per level, values separated by spaces, alternating direction.",
         cons=CONS,
         solve=lambda s: "\n".join(
             fmt([n.v for n in (row if i % 2 == 0 else row[::-1])])
             for i, row in enumerate(levels(build(s)))),
         cases=TREES),

    dict(title="Homework: LC107 Binary Tree Level Order Traversal II",
         stmt="Given the root of a binary tree, print its level order traversal **from the deepest level upwards**.",
         inp=TREE_IN,
         out="One line per level, deepest first, values separated by spaces.",
         cons=CONS,
         solve=lambda s: "\n".join(fmt([n.v for n in row])
                                   for row in reversed(levels(build(s)))),
         cases=TREES),

    dict(title="Homework: LC637 Average of Levels in Binary Tree",
         stmt="Given the root of a binary tree, print the average value of the nodes on each level, from the root downwards.",
         inp=TREE_IN,
         out="One line per level: the average, printed with exactly five decimal "
             "places.",
         cons=CONS,
         solve=lambda s: "\n".join(
             "%.5f" % (sum(n.v for n in row) / float(len(row)))
             for row in levels(build(s))),
         cases=TREES),

    # ---- LEC-13 : depth & diameter -----------------------------------------
    dict(title="Classwork: LC104 Maximum Depth of Binary Tree",
         stmt="Given the root of a binary tree, print its maximum depth: the number of nodes along the longest path from the root down to a leaf.\n\nThe depth of an empty tree is 0.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(depth(build(s))), cases=TREES),

    dict(title="Classwork: LC543 Diameter of Binary Tree",
         stmt="Given the root of a binary tree, print its diameter: the number of **edges** on the longest path between any two nodes. The path need not pass through the root.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(diameter(build(s))), cases=TREES),

    dict(title="Classwork: LC111 Minimum Depth of Binary Tree",
         stmt="Given the root of a binary tree, print its minimum depth: the number of nodes along the shortest path from the root to any **leaf**.\n\nA node with only one child is not a leaf.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(min_depth(build(s))), cases=TREES),

    dict(title="Homework: Count the number of nodes at maximum depth",
         stmt="Given the root of a binary tree, print how many nodes sit at the deepest level.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(len(levels(build(s))[-1]) if build(s) else 0),
         cases=TREES),

    # ---- LEC-14 : balance & views ------------------------------------------
    dict(title="Classwork: LC110 Balanced Binary Tree",
         stmt="Given the root of a binary tree, decide whether it is **height-balanced**: for every node, the heights of its two subtrees differ by at most one.",
         inp=TREE_IN, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(balanced(build(s))), cases=TREES),

    dict(title="Homework: LC965 Univalued Binary Tree",
         stmt="Given the root of a binary tree, decide whether every node holds the same value.\n\nAn empty tree counts as univalued.",
         inp=TREE_IN, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(univalued(build(s))),
         cases=TREES + ["4 4 4 4 4 null 4", "1 1 1 1 1 null 2"]),

    dict(title="Homework: LC872 Leaf-Similar Trees",
         stmt="Two binary trees are **leaf-similar** if their leaf values, read left to right, form the same sequence.",
         inp=TREE_IN2, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(leaves(two(s)[0]) == leaves(two(s)[1])),
         cases=["1 2 3\n1 2 3",
                "3 5 1 6 2 9 8 null null 7 4\n3 5 1 6 7 4 2 null null null null null null 9 8",
                "1 2 3\n1 3 2",
                "null\nnull",
                "1\n1",
                "1 2\n2 2",
                "5 4 6 1 2 null null\n5 1 2 4 6",
                "1 2 3 4 5 6 7\n1 4 5 6 7 null null"]),

    dict(title="Homework: Check whether two trees have equal height",
         stmt="Given two binary trees, decide whether their heights are equal. The height of an empty tree is 0.",
         inp=TREE_IN2, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(depth(two(s)[0]) == depth(two(s)[1])),
         cases=["1 2 3\n4 5 6",
                "1 2 3\n1 null 2 null 3",
                "null\nnull",
                "1\nnull",
                "1 2 null 3\n9 8 7 6",
                "1 2 3 4\n5 6 7 8",
                "1 null 2 null 3 null 4\n1 2 3 4 5 6 7",
                "10 5 15\n7"]),

    # ---- LEC-15 : advanced traversals & views -------------------------------
    dict(title="Classwork: LC987 Vertical Order Traversal of a Binary Tree",
         stmt="Print the **vertical order** traversal of a binary tree.",
         inp=TREE_IN,
         out="One line per column, left to right, values separated by spaces.",
         cons=CONS,
         solve=lambda s: "\n".join(fmt(c) for c in vertical_order(build(s))),
         cases=TREES),

    dict(title="Classwork: Top view of a binary tree (GfG)",
         stmt="Print the **top view** of a binary tree: the nodes you would see looking down from directly above.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(top_view(build(s))), cases=TREES),

    dict(title="Homework: Bottom view of a binary tree (GfG)",
         stmt="Print the **bottom view** of a binary tree: the nodes you would see looking up from directly below.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(bottom_view(build(s))), cases=TREES),

    dict(title="Classwork: Boundary traversal of a binary tree (GfG)",
         stmt="Print the **boundary traversal** of a binary tree, anticlockwise: the root, then the left boundary top-down, then every leaf left to right, then the right boundary bottom-up.\n\nNo node appears twice. A node on a boundary that is also a leaf is printed once, in the leaf run.",
         inp=TREE_IN, out=SEQ_OUT, cons=CONS,
         solve=lambda s: fmt(boundary(build(s))), cases=TREES),

    dict(title="Homework: Diagonal traversal of a binary tree (GfG)",
         stmt="Print the **diagonal traversal** of a binary tree.",
         inp=TREE_IN,
         out="One line per diagonal, values separated by spaces.",
         cons=CONS,
         solve=lambda s: "\n".join(fmt(d) for d in diagonal_view(build(s))),
         cases=TREES),

    dict(title="Homework: Morris inorder traversal (O(1) space) (GfG)",
         stmt="Print the inorder traversal of a binary tree using **Morris traversal**, which uses `O(1)` extra space: no recursion and no stack.",
         inp=TREE_IN, out=SEQ_OUT,
         cons=CONS + "\n- Auxiliary space must be `O(1)`",
         solve=lambda s: fmt(morris_inorder(build(s))), cases=TREES),

    # ---- LEC-16 : invert & mirror -------------------------------------------
    dict(title="Classwork: LC226 Invert Binary Tree",
         stmt="**Invert** a binary tree: swap the left and right child of every node, then print the resulting tree.",
         inp=TREE_IN,
         out="A single line: the inverted tree in level order with `null` for a "
             "missing child, trailing `null` tokens omitted.",
         cons=CONS,
         solve=lambda s: serialize(invert(build(s))), cases=TREES),

    dict(title="Homework: Check if one tree is the mirror of another (GfG)",
         stmt="Given two binary trees, decide whether one is the **mirror image** of the other.",
         inp=TREE_IN2, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(mirror_of(two(s)[0], two(s)[1])),
         cases=["1 2 3\n1 3 2",
                "1 2 3\n1 2 3",
                "null\nnull",
                "1\n1",
                "1 2 null\n1 null 2",
                "1 2 3 4 5\n1 3 2 null null 5 4",
                "5 3 8\n5 8 3",
                "1 2 3\n1 3 4"]),

    dict(title="Homework: Convert a tree to its mirror in place (GfG)",
         stmt="Convert a binary tree into its **mirror** by swapping every node's children in place, then print the result.",
         inp=TREE_IN,
         out="A single line: the mirrored tree in level order with `null` for a "
             "missing child, trailing `null` tokens omitted.",
         cons=CONS,
         solve=lambda s: serialize(invert(build(s))), cases=TREES),

    dict(title="Homework: LC951 Flip Equivalent Binary Trees",
         stmt="Two binary trees are **flip equivalent** if one can be turned into the other by swapping the children of any number of nodes.",
         inp=TREE_IN2, out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(flip_equiv(two(s)[0], two(s)[1])),
         cases=["1 2 3\n1 3 2",
                "1 2 3 4 5 6\n1 3 2 null 6 5 4",
                "null\nnull",
                "1\n1",
                "1 2 3\n1 2 4",
                "1 2 null 3\n1 null 2 null 3",
                "1 2 3 4 null null 5\n1 3 2 5 null null 4",
                "1 2 3\n2 1 3"]),

    # ---- LEC-17 : path sums -------------------------------------------------
    dict(title="Classwork: LC112 Path Sum",
         stmt="Given a binary tree and a target sum, decide whether some **root-to-leaf** path has values adding up exactly to the target.",
         inp=TREE_IN + "\n\nA second line contains the integer target sum.",
         out=BOOL_OUT, cons=CONS,
         solve=lambda s: fmt_bool(has_path_sum(build(rows(s)[0]), int(rows(s)[1]))),
         cases=["5 4 8 11 null 13 4 7 2 null null null 1\n22",
                "1 2 3\n3",
                "1 2 3\n4",
                "null\n0",
                "1\n1",
                "1 2\n1",
                "-2 null -3\n-5",
                "10 5 15 3 7 null 18\n18",
                "1 -2 -3 1 3 -2 null -1\n-1"]),

    dict(title="Classwork: LC113 Path Sum II",
         stmt="Given a binary tree and a target sum, print **every** root-to-leaf path whose values add up to the target.",
         inp=TREE_IN + "\n\nA second line contains the integer target sum.",
         out="One line per qualifying path, values from root to leaf separated by "
             "spaces, in the order the paths are found (left before right). Print "
             "nothing if there are none.",
         cons=CONS,
         solve=lambda s: "\n".join(fmt(p) for p in
                                   path_sum_all(build(rows(s)[0]), int(rows(s)[1]))),
         cases=["5 4 8 11 null 13 4 7 2 null null 5 1\n22",
                "1 2 3\n3",
                "1 2 3\n4",
                "null\n0",
                "1\n1",
                "1 2 2 3 4 4 3\n6",
                "10 5 15 3 7 null 18\n18",
                "0 1 1\n1"]),

    dict(title="Homework: LC437 Path Sum III",
         stmt="Given a binary tree and a target sum, count the paths whose values add up to the target. A path may start and end anywhere, but must run **downwards** only.",
         inp=TREE_IN + "\n\nA second line contains the integer target sum.",
         out=NUM_OUT, cons=CONS,
         solve=lambda s: str(path_sum_count(build(rows(s)[0]), int(rows(s)[1]))),
         cases=["10 5 -3 3 2 null 11 3 -2 null 1\n8",
                "5 4 8 11 null 13 4 7 2 null null 5 1\n22",
                "1 2 3\n3",
                "null\n0",
                "1\n1",
                "0 1 1\n1",
                "1 -1 1 null null null 1\n1",
                "10 5 15 3 7 null 18\n25"]),

    dict(title="Homework: LC988 Smallest String Starting From Leaf",
         stmt="Every node holds a value from 0 to 25, standing for the letters `a` to `z`. Consider the strings formed by reading from a **leaf up to the root**. Print the lexicographically smallest one.",
         inp=TREE_IN, out="A single line: the smallest string.", cons=CONS,
         solve=lambda s: smallest_from_leaf(build(s)),
         cases=["0 1 2 3 4 3 4",
                "25 1 3 1 3 0 2",
                "2 2 1 null 1 0 null 0",
                "0",
                "4 0 1 1",
                "1 2 3 4 5 6 7",
                "0 null 1 null 2",
                "3 1 2"]),

    # ---- LEC-18 : lowest common ancestor ------------------------------------
    dict(title="Classwork: LC236 Lowest Common Ancestor of a Binary Tree",
         stmt="Given a binary tree and two node values, print their **lowest common ancestor**: the deepest node having both as descendants. A node counts as a descendant of itself.",
         inp=TREE_IN + "\n\nA second line contains the two node values, separated "
                       "by a space. Both are present and distinct.",
         out=NUM_OUT, cons=CONS,
         solve=lambda s: str(find_lca(build(rows(s)[0]), *ints(rows(s)[1])).v),
         cases=["3 5 1 6 2 0 8 null null 7 4\n5 1",
                "3 5 1 6 2 0 8 null null 7 4\n5 4",
                "1 2\n1 2",
                "1 2 3\n2 3",
                "5 3 8 2 4 7 9\n2 4",
                "5 3 8 2 4 7 9\n2 9",
                "1 2 null 3 null 4\n3 4",
                "10 5 15 3 7 null 18\n3 18"]),

    dict(title="Classwork: Distance between two nodes via LCA (GfG)",
         stmt="Given a binary tree and two node values, print the number of **edges** on the path between them.",
         inp=TREE_IN + "\n\nA second line contains the two node values, separated "
                       "by a space. Both are present.",
         out=NUM_OUT, cons=CONS,
         solve=lambda s: str(dist_between(build(rows(s)[0]), *ints(rows(s)[1]))),
         cases=["3 5 1 6 2 0 8 null null 7 4\n5 1",
                "3 5 1 6 2 0 8 null null 7 4\n7 8",
                "1 2 3\n2 3",
                "1 2\n1 2",
                "5 3 8 2 4 7 9\n2 9",
                "1 2 null 3 null 4\n1 4",
                "10 5 15 3 7 null 18\n3 18",
                "1\n1 1"]),

    dict(title="Homework: LC1123 Lowest Common Ancestor of Deepest Leaves",
         stmt="Print the value of the lowest common ancestor of **all the deepest leaves** of a binary tree.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(lca_deepest(build(s)).v),
         cases=["3 5 1 6 2 0 8 null null 7 4",
                "1",
                "0 1 3 null 2",
                "1 2 3",
                "1 2 3 4",
                "1 2 3 null 4 null null null 5",
                "5 3 8 2 4 7 9",
                "1 2 null 3 null 4"]),

    # ---- LEC-19 : construct & flatten --------------------------------------
    dict(title="Classwork: LC105 Construct Binary Tree from Preorder and Inorder",
         stmt="Rebuild a binary tree from its **preorder** and **inorder** traversals, then print it.",
         inp="The first line is the preorder traversal, the second the inorder "
             "traversal, both space separated. All values are distinct.",
         out="A single line: the tree in level order with `null` for a missing "
             "child, trailing `null` tokens omitted.",
         cons="- `0 <= N <= 3000`\n- values are distinct\n- Expected time `O(N)`",
         solve=lambda s: serialize(from_pre_in(ints(rows(s)[0]), ints(rows(s)[1]))),
         cases=["3 9 20 15 7\n9 3 15 20 7",
                "1\n1",
                "1 2\n2 1",
                "1 2\n1 2",
                "1 2 4 5 3 6\n4 2 5 1 6 3",
                "5 3 2 4 8 7 9\n2 3 4 5 7 8 9",
                "1 2 3 4\n4 3 2 1",
                "10 5 3 7 15 18\n3 5 7 10 15 18"]),

    dict(title="Classwork: LC106 Construct Binary Tree from Inorder and Postorder",
         stmt="Rebuild a binary tree from its **inorder** and **postorder** traversals, then print it.",
         inp="The first line is the inorder traversal, the second the postorder "
             "traversal, both space separated. All values are distinct.",
         out="A single line: the tree in level order with `null` for a missing "
             "child, trailing `null` tokens omitted.",
         cons="- `0 <= N <= 3000`\n- values are distinct\n- Expected time `O(N)`",
         solve=lambda s: serialize(from_in_post(ints(rows(s)[0]), ints(rows(s)[1]))),
         cases=["9 3 15 20 7\n9 15 7 20 3",
                "1\n1",
                "2 1\n2 1",
                "1 2\n2 1",
                "4 2 5 1 6 3\n4 5 2 6 3 1",
                "2 3 4 5 7 8 9\n2 4 3 7 9 8 5",
                "4 3 2 1\n4 3 2 1",
                "3 5 7 10 15 18\n3 7 5 18 15 10"]),

    dict(title="Homework: LC889 Construct Binary Tree from Preorder and Postorder",
         stmt="Rebuild a binary tree from its **preorder** and **postorder** traversals, then print it.",
         inp="The first line is the preorder traversal, the second the postorder "
             "traversal, both space separated. All values are distinct.",
         out="A single line: the tree in level order with `null` for a missing "
             "child, trailing `null` tokens omitted.",
         cons="- `0 <= N <= 30`\n- values are distinct",
         solve=lambda s: serialize(from_pre_post(ints(rows(s)[0]), ints(rows(s)[1]))),
         cases=["1 2 4 5 3 6 7\n4 5 2 6 7 3 1",
                "1\n1",
                "1 2\n2 1",
                "3 9 20 15 7\n9 15 7 20 3",
                "1 2 3\n2 3 1",
                "5 3 2 4 8 7 9\n2 4 3 7 9 8 5",
                "1 2 4 3\n4 2 3 1",
                "2 1 3\n1 3 2"]),

    dict(title="Homework: LC1008 Construct BST from Preorder Traversal",
         stmt="Rebuild a **binary search tree** from its preorder traversal, then print it.",
         inp="A single line: the preorder traversal, space separated, all values "
             "distinct.",
         out="A single line: the tree in level order with `null` for a missing "
             "child, trailing `null` tokens omitted.",
         cons="- `1 <= N <= 100`\n- values are distinct\n- Expected time `O(N)`",
         solve=lambda s: serialize(bst_from_pre(ints(s))),
         cases=["8 5 1 7 10 12",
                "1",
                "1 2 3",
                "3 2 1",
                "5 3 2 4 8 7 9",
                "10 5 3 7 15 18",
                "2 1 3",
                "50 30 20 40 70 60 80"]),

    dict(title="Classwork: LC114 Flatten Binary Tree to Linked List",
         stmt="Flatten a binary tree into a linked list in **preorder**: every node's left child becomes empty and its right child points to the next node in preorder. Print the resulting sequence.",
         inp=TREE_IN,
         out="A single line: the flattened list from head to tail, values separated "
             "by spaces.",
         cons=CONS,
         solve=lambda s: fmt(flatten_pre(build(s))), cases=TREES),

    # ---- LEC-20 : serialize & utilities ------------------------------------
    dict(title="Classwork: LC222 Count Complete Tree Nodes",
         stmt="Count the nodes of a **complete** binary tree in better than linear time.",
         inp=TREE_IN, out=NUM_OUT,
         cons="- `0 <= N <= 5 * 10^4`\n- the tree is complete\n"
              "- Expected time better than `O(N)`",
         solve=lambda s: str(count_complete(build(s))),
         cases=["1 2 3 4 5 6",
                "null",
                "1",
                "1 2 3",
                "1 2 3 4 5 6 7",
                "1 2 3 4 5",
                "1 2 3 4",
                "1 2 3 4 5 6 7 8 9 10"]),

    dict(title="Homework: LC662 Maximum Width of Binary Tree",
         stmt="Print the **maximum width** of a binary tree: the largest number of positions between the leftmost and rightmost non-empty nodes on any level, counting the empty positions between them.",
         inp=TREE_IN, out=NUM_OUT, cons=CONS,
         solve=lambda s: str(max_width(build(s))),
         cases=["1 3 2 5 3 null 9",
                "1 3 2 5 null null 9 6 null 7",
                "1 3 2 5",
                "null",
                "1",
                "1 null 2 null 3 null 4",
                "1 2 3 4 5 6 7",
                "1 2 null 3 null 4 null 5"]),

    dict(title="Classwork: LC863 All Nodes Distance K in Binary Tree",
         stmt="Given a binary tree, a target node's value and an integer `K`, print the values of all nodes exactly `K` edges away from the target.",
         inp=TREE_IN + "\n\nA second line contains the target node's value and `K`, "
                       "separated by a space.",
         out="A single line: the qualifying values in increasing order, separated by "
             "spaces. Print an empty line if there are none.",
         cons=CONS + "\n- values are distinct",
         solve=lambda s: fmt(nodes_distance_k(build(rows(s)[0]),
                                              *ints(rows(s)[1]))),
         cases=["3 5 1 6 2 0 8 null null 7 4\n5 2",
                "3 5 1 6 2 0 8 null null 7 4\n5 0",
                "3 5 1 6 2 0 8 null null 7 4\n3 3",
                "1\n1 0",
                "1\n1 1",
                "1 2 3\n2 2",
                "5 3 8 2 4 7 9\n5 2",
                "10 5 15 3 7 null 18\n7 3"]),
]


BST_IN = ("A single line with the BST in **level order**, values separated by "
          "spaces, `null` for a missing child. An empty tree is the single token "
          "`null`.")
BST_CONS = ("- `0 <= N <= 10^4` nodes\n"
            "- `-10^4 <= node value <= 10^4`\n"
            "- all values are distinct unless stated otherwise\n"
            "- Expected time `O(H)` where `H` is the height, unless stated otherwise")
SER_OUT = ("A single line: the tree in level order with `null` for a missing "
           "child, trailing `null` tokens omitted.")

PROBLEMS_21_30 = [
    # ---- LEC-21 : search & insert -------------------------------------------
    dict(title="Classwork: LC700 Search in a Binary Search Tree",
         stmt="Given a BST and a key, find the node holding that key and print the subtree rooted at it. Print `null` if the key is absent.",
         inp=BST_IN + "\n\nA second line contains the integer key.",
         out=SER_OUT, cons=BST_CONS,
         solve=lambda s: serialize(bst_find(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [1, 8, 3, 10, 7, 18, 6, 30, 15])),

    dict(title="Classwork: LC701 Insert into a Binary Search Tree",
         stmt="Insert a key into a BST so the result is still a valid BST, then print the tree.",
         inp=BST_IN + "\n\nA second line contains the integer key to insert.",
         out=SER_OUT, cons=BST_CONS,
         solve=lambda s: serialize(bst_insert(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [5, 3, 4, 9, 6, 12, 5, 65, 22])),

    dict(title="Classwork: Iterative BST search (GfG)",
         stmt="Decide whether a key is present in a BST, **without recursion**.",
         inp=BST_IN + "\n\nA second line contains the integer key.",
         out=BOOL_OUT,
         cons=BST_CONS + "\n- Auxiliary space must be `O(1)`",
         solve=lambda s: fmt_bool(bst_find(build(rows(s)[0]), int(rows(s)[1])) is not None),
         cases=with_key(BSTS, [1, 8, 4, 10, 7, 99, 13, 60, 1])),

    dict(title="Homework: Iterative BST insert (GfG)",
         stmt="Insert a key into a BST **without recursion**, then print the tree.",
         inp=BST_IN + "\n\nA second line contains the integer key to insert.",
         out=SER_OUT,
         cons=BST_CONS + "\n- Auxiliary space must be `O(1)`",
         solve=lambda s: serialize(bst_insert(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [7, 9, 2, 11, 1, 4, 15, 45, 33])),

    dict(title="Homework: Search keys within a range in a BST (GfG)",
         stmt="Given a BST and an inclusive range, print every value in that range in increasing order.",
         inp=BST_IN + "\n\nA second line contains the two bounds `lo` and `hi`, "
                      "separated by a space.",
         out=SEQ_OUT, cons=BST_CONS,
         solve=lambda s: fmt(range_values(build(rows(s)[0]), *ints(rows(s)[1]))),
         cases=["null\n0 10", "8\n1 10", "2 1 3\n2 3", "8 3 10\n3 10",
                "5 3 8 2 4 7 9\n3 8", "10 5 15 3 7 null 18\n6 16",
                "8 3 10 1 6 null 14 null null 4 7 13\n4 13",
                "50 30 70 20 40 60 80\n35 75",
                "20 10 30 5 15 25 35 1\n1 20"]),

    dict(title="Homework: Count BST nodes lying in a given range (GfG)",
         stmt="Given a BST and an inclusive range, print how many node values fall inside it.",
         inp=BST_IN + "\n\nA second line contains the two bounds `lo` and `hi`, "
                      "separated by a space.",
         out=NUM_OUT, cons=BST_CONS,
         solve=lambda s: str(len(range_values(build(rows(s)[0]), *ints(rows(s)[1])))),
         cases=["null\n0 10", "8\n1 10", "2 1 3\n1 2", "8 3 10\n1 8",
                "5 3 8 2 4 7 9\n4 9", "10 5 15 3 7 null 18\n3 15",
                "8 3 10 1 6 null 14 null null 4 7 13\n6 14",
                "50 30 70 20 40 60 80\n20 50",
                "20 10 30 5 15 25 35 1\n5 25"]),

    # ---- LEC-22 : validate, min diff, mode ----------------------------------
    dict(title="Classwork: LC98 Validate Binary Search Tree",
         stmt="Decide whether a binary tree is a valid **binary search tree**: every value in a node's left subtree is strictly smaller than the node, and every value in its right subtree strictly larger.",
         inp=TREE_IN, out=BOOL_OUT,
         cons="- `0 <= N <= 10^4`\n- `-10^4 <= node value <= 10^4`\n"
              "- Expected time `O(N)`",
         solve=lambda s: fmt_bool(is_bst(build(s))),
         cases=BSTS + ["5 1 4 null null 3 6", "2 2 2", "10 5 15 null null 6 20",
                       "1 1", "5 4 6 null null 3 7"]),

    dict(title="Classwork: LC530 Minimum Absolute Difference in BST",
         stmt="Print the smallest absolute difference between the values of any two different nodes in a BST.",
         inp=BST_IN, out=NUM_OUT,
         cons=BST_CONS + "\n- at least two nodes",
         solve=lambda s: str(min_abs_diff(build(s))),
         cases=[t for t in BSTS if t not in ("null", "8")] +
               ["4 2 6 1 3", "1 null 5 null null null 3", "236 104 701 null 227 null 911"]),

    dict(title="Classwork: LC501 Find Mode in Binary Search Tree",
         stmt="Print every **mode** of a BST -- the value or values occurring most often. Duplicates are allowed in this tree.\n\nPrint the modes in increasing order.",
         inp="A single line with the tree in level order, `null` for a missing "
             "child. Values may repeat; equal values are placed in the right "
             "subtree.",
         out=SEQ_OUT,
         cons="- `1 <= N <= 10^4`\n- `-10^5 <= node value <= 10^5`",
         solve=lambda s: fmt(modes(build(s))),
         cases=["1 null 2 2", "1", "2 1 3", "6 2 8 1 4 7 9",
                "1 null 2", "5 5 7", "1 null 1 1", "2 2 2 2"]),

    dict(title="Homework: LC99 Recover Binary Search Tree",
         stmt="Exactly two nodes of a BST have had their values swapped by mistake. Restore the tree and print it.",
         inp=BST_IN, out=SER_OUT,
         cons="- `2 <= N <= 10^4`\n- exactly two values are swapped",
         solve=lambda s: serialize(recover_bst(build(s))),
         cases=["1 3 null null 2", "3 1 4 null null 2", "2 3 1",
                "5 3 8 2 4 9 7", "10 5 15 3 7 null 18",
                "8 3 10 1 6 null 14 null null 7 4",
                "20 10 30 5 15 35 25 1", "50 30 70 20 40 80 60"]),

    dict(title="Homework: LC783 Minimum Distance Between BST Nodes",
         stmt="Print the smallest difference between the values of any two different nodes in a BST.",
         inp=BST_IN, out=NUM_OUT,
         cons=BST_CONS + "\n- at least two nodes",
         solve=lambda s: str(min_abs_diff(build(s))),
         cases=["4 2 6 1 3", "1 null 48 12 49", "8 3 10",
                "5 3 8 2 4 7 9", "10 5 15 3 7 null 18",
                "27 null 34 null 58 50 null 44",
                "50 30 70 20 40 60 80", "20 10 30 5 15 25 35 1"]),

    dict(title="Homework: LC255 Verify Preorder Sequence in BST",
         stmt="Given a sequence of distinct integers, decide whether it could be the **preorder** traversal of some BST.",
         inp="A single line: the sequence, space separated, all values distinct.",
         out=BOOL_OUT,
         cons="- `1 <= N <= 10^4`\n- values are distinct\n- Expected time `O(N)`",
         solve=lambda s: fmt_bool(verify_preorder_bst(ints(s))),
         cases=["5 2 1 3 6", "5 2 6 1 3", "1", "1 2 3", "3 2 1",
                "8 5 1 7 10 12", "2 1 3", "40 30 35 80 100", "10 5 1 7 40 50"]),

    # ---- LEC-23 : delete & order statistics ---------------------------------
    dict(title="Classwork: LC450 Delete Node in a BST",
         stmt="Delete a key from a BST and print the resulting tree. If the key is absent, print the tree unchanged.",
         inp=BST_IN + "\n\nA second line contains the integer key to delete.",
         out=SER_OUT, cons=BST_CONS,
         solve=lambda s: serialize(bst_delete(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [1, 8, 1, 8, 3, 10, 3, 30, 10])),

    dict(title="Classwork: LC230 Kth Smallest Element in a BST",
         stmt="Print the `k`-th smallest value in a BST, counting from one.",
         inp=BST_IN + "\n\nA second line contains the integer `k`.",
         out=NUM_OUT,
         cons="- `1 <= k <= N <= 10^4`\n- values are distinct",
         solve=lambda s: str(kth_smallest(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key([t for t in BSTS if t != "null"], [1, 1, 2, 3, 4, 5, 3, 4])),

    dict(title="Classwork: Kth largest element in a BST (GfG)",
         stmt="Print the `k`-th largest value in a BST, counting from one.",
         inp=BST_IN + "\n\nA second line contains the integer `k`.",
         out=NUM_OUT,
         cons="- `1 <= k <= N <= 10^4`\n- values are distinct",
         solve=lambda s: str(kth_largest(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key([t for t in BSTS if t != "null"], [1, 1, 2, 3, 4, 5, 3, 4])),

    dict(title="Homework: LC285 Inorder Successor in BST",
         stmt="Given a BST and a key, print the key's **inorder successor**: the smallest value strictly greater than it. Print `null` if there is none.",
         inp=BST_IN + "\n\nA second line contains the integer key.",
         out="A single line: the successor's value, or `null`.",
         cons=BST_CONS,
         solve=lambda s: (lambda r: "null" if r is None else str(r))(
             successor(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [1, 8, 1, 8, 4, 15, 6, 40, 20])),

    dict(title="Homework: Inorder predecessor in a BST (GfG)",
         stmt="Given a BST and a key, print the key's **inorder predecessor**: the largest value strictly smaller than it. Print `null` if there is none.",
         inp=BST_IN + "\n\nA second line contains the integer key.",
         out="A single line: the predecessor's value, or `null`.",
         cons=BST_CONS,
         solve=lambda s: (lambda r: "null" if r is None else str(r))(
             predecessor(build(rows(s)[0]), int(rows(s)[1]))),
         cases=with_key(BSTS, [1, 8, 3, 10, 7, 18, 13, 60, 25])),

    # ---- LEC-24/25 : LCA, build, advanced -----------------------------------
    dict(title="Classwork: LC235 Lowest Common Ancestor of a BST",
         stmt="Given a BST and two values, print their lowest common ancestor.",
         inp=BST_IN + "\n\nA second line contains the two values, separated by a "
                      "space. Both are present.",
         out=NUM_OUT, cons=BST_CONS,
         solve=lambda s: str(bst_lca(build(rows(s)[0]), *ints(rows(s)[1]))),
         cases=["2 1 3\n1 3", "8 3 10\n3 10", "5 3 8 2 4 7 9\n2 4",
                "5 3 8 2 4 7 9\n2 9", "10 5 15 3 7 null 18\n3 7",
                "8 3 10 1 6 null 14 null null 4 7 13\n4 7",
                "50 30 70 20 40 60 80\n20 40", "20 10 30 5 15 25 35 1\n1 15"]),

    dict(title="Classwork: LC108 Convert Sorted Array to Binary Search Tree",
         stmt="Given a sorted array of distinct integers, build a **height-balanced** BST and print it.",
         inp="A single line: the sorted array, space separated, all values distinct.",
         out=SER_OUT,
         cons="- `1 <= N <= 10^4`\n- the array is sorted in increasing order\n"
              "- Expected time `O(N)`",
         solve=lambda s: serialize(sorted_to_bst(ints(s))),
         cases=["-10 -3 0 5 9", "1 3", "1", "1 2 3", "1 2 3 4 5 6 7",
                "0 1 2 3 4 5", "-5 -1 0 2 8 11", "2 4 6 8 10 12 14 16"]),

    dict(title="Homework: LC109 Convert Sorted List to Binary Search Tree",
         stmt="Given the values of a sorted linked list, build a height-balanced BST and print it.",
         inp="A single line: the list values in order, space separated, all "
             "distinct.",
         out=SER_OUT,
         cons="- `1 <= N <= 2 * 10^4`\n- values are sorted increasing",
         solve=lambda s: serialize(sorted_to_bst(ints(s))),
         cases=["-10 -3 0 5 9", "1 3", "1", "1 2 3", "1 2 3 4 5 6 7",
                "0 1 2 3 4 5", "-5 -1 0 2 8 11", "3 5 7 9 11 13"]),

    dict(title="Homework: LC538 Convert BST to Greater Tree",
         stmt="Replace every node's value with the sum of its own value and all values in the BST greater than it, then print the tree.",
         inp=BST_IN, out=SER_OUT,
         cons="- `0 <= N <= 10^4`\n- values are distinct\n- Expected time `O(N)`",
         solve=lambda s: serialize(greater_tree(build(s))),
         cases=[t for t in BSTS if t != "null"] + ["0 null 1", "1 0 2"]),

    dict(title="Homework: LC1382 Balance a Binary Search Tree",
         stmt="Given a BST, produce a **balanced** BST holding the same values and print it.",
         inp=BST_IN, out=SER_OUT,
         cons="- `1 <= N <= 10^4`\n- values are distinct\n- Expected time `O(N)`",
         solve=lambda s: serialize(sorted_to_bst(in_list(build(s)))),
         cases=[t for t in BSTS if t != "null"] +
               ["1 null 2 null 3 null 4", "4 3 null 2 null 1"]),

    dict(title="Homework: LC333 Largest BST Subtree",
         stmt="Given a binary tree, print the number of nodes in its largest subtree that is itself a valid BST.",
         inp=TREE_IN, out=NUM_OUT,
         cons="- `0 <= N <= 10^4`\n- Expected time `O(N)`",
         solve=lambda s: str(largest_bst_subtree(build(s))),
         cases=["10 5 15 1 8 null 7", "4 2 7 2 3 5 null null null null 1",
                "null", "1", "2 1 3", "5 3 8 2 4 7 9",
                "10 5 15 null null 6 20", "1 2 3 4 5 6 7"]),
]


def iter_nodes(root):
    st = [root] if root else []
    while st:
        n = st.pop()
        yield n
        if n.l: st.append(n.l)
        if n.r: st.append(n.r)


def univalued(root):
    if not root:
        return True
    return all(n.v == root.v for n in iter_nodes(root))


# --- answers worked out by hand; generation aborts if a solution disagrees ----
SANITY = [
    ("Classwork: LC94 Binary Tree Inorder Traversal", "1 2 3", "2 1 3"),
    ("Classwork: LC94 Binary Tree Inorder Traversal", "1 null 2 null 3 null 4", "1 2 3 4"),
    ("Classwork: LC144 Binary Tree Preorder Traversal", "1 2 3", "1 2 3"),
    ("Classwork: LC145 Binary Tree Postorder Traversal", "1 2 3", "2 3 1"),
    ("Classwork: LC104 Maximum Depth of Binary Tree", "1 2 3", "2"),
    ("Classwork: LC104 Maximum Depth of Binary Tree", "null", "0"),
    ("Classwork: LC543 Diameter of Binary Tree", "1 2 3", "2"),
    ("Classwork: LC111 Minimum Depth of Binary Tree", "1 2 null 3", "3"),
    ("Classwork: LC110 Balanced Binary Tree", "1 null 2 null 3 null 4", "false"),
    ("Classwork: LC110 Balanced Binary Tree", "1 2 3", "true"),
    ("Homework: Print all leaf nodes from left to right", "1 2 3", "2 3"),
    ("Homework: Count the total number of nodes recursively", "1 2 3", "3"),
    ("Homework: LC872 Leaf-Similar Trees", "1 2 3\n1 3 2", "false"),

    # LEC-15
    ("Classwork: LC987 Vertical Order Traversal of a Binary Tree", "1 2 3", "2\n1\n3"),
    ("Classwork: Top view of a binary tree (GfG)", "1 2 3", "2 1 3"),
    ("Homework: Bottom view of a binary tree (GfG)", "1 2 3", "2 1 3"),
    ("Classwork: Boundary traversal of a binary tree (GfG)", "1 2 3", "1 2 3"),
    ("Classwork: Boundary traversal of a binary tree (GfG)", "7", "7"),
    ("Homework: Diagonal traversal of a binary tree (GfG)", "1 2 3", "1 3\n2"),
    ("Homework: Morris inorder traversal (O(1) space) (GfG)", "1 2 3", "2 1 3"),
    # LEC-16
    ("Classwork: LC226 Invert Binary Tree", "1 2 3", "1 3 2"),
    ("Homework: Check if one tree is the mirror of another (GfG)", "1 2 3\n1 3 2", "true"),
    ("Homework: Check if one tree is the mirror of another (GfG)", "1 2 3\n1 2 3", "false"),
    ("Homework: Convert a tree to its mirror in place (GfG)", "1 2 3", "1 3 2"),
    ("Homework: LC951 Flip Equivalent Binary Trees", "1 2 3\n1 3 2", "true"),
    ("Homework: LC951 Flip Equivalent Binary Trees", "1 2 3\n1 2 4", "false"),
    # LEC-17
    ("Classwork: LC112 Path Sum", "1 2 3\n3", "true"),
    ("Classwork: LC112 Path Sum", "1 2 3\n4", "true"),
    ("Classwork: LC112 Path Sum", "null\n0", "false"),
    ("Classwork: LC113 Path Sum II", "1 2 3\n3", "1 2"),
    ("Homework: LC437 Path Sum III", "1 2 3\n3", "2"),
    ("Homework: LC988 Smallest String Starting From Leaf", "0 1 2 3 4 3 4", "dba"),
    # LEC-18
    ("Classwork: LC236 Lowest Common Ancestor of a Binary Tree",
     "3 5 1 6 2 0 8 null null 7 4\n5 1", "3"),
    ("Classwork: Distance between two nodes via LCA (GfG)",
     "3 5 1 6 2 0 8 null null 7 4\n5 1", "2"),
    ("Homework: LC1123 Lowest Common Ancestor of Deepest Leaves",
     "3 5 1 6 2 0 8 null null 7 4", "2"),
    # LEC-19
    ("Classwork: LC105 Construct Binary Tree from Preorder and Inorder",
     "3 9 20 15 7\n9 3 15 20 7", "3 9 20 null null 15 7"),
    ("Classwork: LC106 Construct Binary Tree from Inorder and Postorder",
     "9 3 15 20 7\n9 15 7 20 3", "3 9 20 null null 15 7"),
    ("Homework: LC889 Construct Binary Tree from Preorder and Postorder",
     "1 2 4 5 3 6 7\n4 5 2 6 7 3 1", "1 2 3 4 5 6 7"),
    ("Homework: LC1008 Construct BST from Preorder Traversal",
     "8 5 1 7 10 12", "8 5 10 1 7 null 12"),
    ("Classwork: LC114 Flatten Binary Tree to Linked List",
     "1 2 5 3 4 null 6", "1 2 3 4 5 6"),
    # LEC-20
    ("Classwork: LC222 Count Complete Tree Nodes", "1 2 3 4 5 6", "6"),
    ("Homework: LC662 Maximum Width of Binary Tree", "1 3 2 5 3 null 9", "4"),
    ("Classwork: LC863 All Nodes Distance K in Binary Tree",
     "3 5 1 6 2 0 8 null null 7 4\n5 2", "1 4 7"),
]




# ------------------------------------------------------- greedy / intervals --
import heapq


def parse_iv(s, start=1):
    """First line n, then n lines of two integers."""
    r = rows(s)
    n = int(r[start - 1])
    return [tuple(ints(r[start + i])) for i in range(n)]


IV_IN = ("The first line contains an integer `n`. Each of the next `n` lines "
         "contains two integers describing one interval.")
ARR_IN = "A single line of space-separated integers."


def n_meetings(iv):
    """Most non-overlapping meetings; one may start exactly as another ends."""
    last, count = None, 0
    for a, b in sorted(iv, key=lambda x: x[1]):
        if last is None or a >= last:
            count += 1
            last = b
    return count


def erase_overlap(iv):
    """LC435: fewest removals. Touching endpoints do NOT overlap."""
    return len(iv) - n_meetings(iv)


def min_arrows(iv):
    """LC452: closed intervals, so a shared endpoint is still coverable."""
    if not iv:
        return 0
    arrows, end = 0, None
    for a, b in sorted(iv, key=lambda x: x[1]):
        if end is None or a > end:
            arrows += 1
            end = b
    return arrows


def pair_chain(iv):
    """LC646: (a,b) then (c,d) requires b < c STRICTLY."""
    last, count = None, 0
    for a, b in sorted(iv, key=lambda x: x[1]):
        if last is None or a > last:
            count += 1
            last = b
    return count


def merge_iv(iv):
    out = []
    for a, b in sorted(iv):
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def insert_iv(iv, new):
    return merge_iv(list(iv) + [tuple(new)])


def min_platforms(arr, dep):
    arr, dep = sorted(arr), sorted(dep)
    i = j = need = best = 0
    while i < len(arr):
        if arr[i] <= dep[j]:
            need += 1
            i += 1
            best = max(best, need)
        else:
            need -= 1
            j += 1
    return best


def interval_intersections(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        lo, hi = max(a[i][0], b[j][0]), min(a[i][1], b[j][1])
        if lo <= hi:
            out.append([lo, hi])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return out


def car_pooling(trips, cap):
    ev = []
    for num, s, e in trips:
        ev.append((s, num))
        ev.append((e, -num))
    cur = 0
    for _, d in sorted(ev):
        cur += d
        if cur > cap:
            return False
    return True


def fractional_knapsack(items, cap):
    total = 0.0
    for v, w in sorted(items, key=lambda x: -(x[0] / float(x[1]))):
        if cap <= 0:
            break
        take = min(w, cap)
        total += v * (take / float(w))
        cap -= take
    return total


def job_sequencing(jobs):
    """One unit of time per job; schedule each as LATE as its deadline allows."""
    slots = {}
    for jid, dl, pr in sorted(jobs, key=lambda x: -x[2]):
        t = dl
        while t > 0 and t in slots:
            t -= 1
        if t > 0:
            slots[t] = pr
    return len(slots), sum(slots.values())


def assign_cookies(greed, size):
    greed, size = sorted(greed), sorted(size)
    i = j = c = 0
    while i < len(greed) and j < len(size):
        if size[j] >= greed[i]:
            c += 1
            i += 1
        j += 1
    return c


def huffman_cost(freqs):
    """Total bits = the sum of every merge, exactly like joining ropes."""
    if len(freqs) <= 1:
        return 0
    h = list(freqs)
    heapq.heapify(h)
    total = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        total += a + b
        heapq.heappush(h, a + b)
    return total


def min_coins_greedy(coins, amount):
    n = 0
    for c in sorted(coins, reverse=True):
        while amount >= c:
            amount -= c
            n += 1
    return n if amount == 0 else -1


def jump_game(a):
    reach = 0
    for i, x in enumerate(a):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True


def jump_game_ii(a):
    if len(a) <= 1:
        return 0
    jumps = end = far = 0
    for i in range(len(a) - 1):
        far = max(far, i + a[i])
        if i == end:
            jumps += 1
            end = far
    return jumps


def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start, tank = i + 1, 0
    return start


def candy(r):
    n = len(r)
    if n == 0:
        return 0
    out = [1] * n
    for i in range(1, n):
        if r[i] > r[i - 1]:
            out[i] = out[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if r[i] > r[i + 1]:
            out[i] = max(out[i], out[i + 1] + 1)
    return sum(out)


def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    out, start, end = [], 0, 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            out.append(end - start + 1)
            start = i + 1
    return out


def rearrange_no_adjacent(s):
    """Lexicographically smallest arrangement with no two equal neighbours."""
    from collections import Counter
    cnt = Counter(s)
    n = len(s)
    if max(cnt.values()) > (n + 1) // 2:
        return "-1"
    out = []
    for _ in range(n):
        placed = False
        for ch in sorted(cnt):
            if cnt[ch] == 0 or (out and out[-1] == ch):
                continue
            rest = n - len(out) - 1
            tmp = dict(cnt)
            tmp[ch] -= 1
            if tmp and max(tmp.values()) > (rest + 1) // 2:
                continue          # this choice strands a letter later
            out.append(ch)
            cnt[ch] -= 1
            placed = True
            break
        if not placed:
            return "-1"
    return "".join(out)


def max_events(ev):
    """LC1353: one event per day; an event occupies one day inside [s, e]."""
    ev = sorted(ev)
    h, i, day, count = [], 0, 0, 0
    while i < len(ev) or h:
        if not h:
            day = max(day, ev[i][0])
        while i < len(ev) and ev[i][0] <= day:
            heapq.heappush(h, ev[i][1])
            i += 1
        while h and h[0] < day:
            heapq.heappop(h)
        if h:
            heapq.heappop(h)
            count += 1
            day += 1
    return count


def lemonade(bills):
    five = ten = 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if not five:
                return False
            five -= 1
            ten += 1
        else:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


IV_CASES = [
    "3\n1 3\n2 6\n8 10",
    "4\n1 2\n2 3\n3 4\n1 3",
    "4\n10 16\n2 8\n1 6\n7 12",
    "6\n1 2\n3 4\n0 6\n5 7\n8 9\n5 9",
    "5\n1 4\n2 3\n4 6\n8 9\n5 7",
    "2\n1 10\n2 3",
    "3\n1 2\n2 3\n3 4",
    "1\n5 7",
]

ARR_CASES = [
    "2 3 1 1 4",
    "1 0 2",
    "2 4 2 1 5 3",
    "3 2 1 0 4",
    "1 2 2",
    "1 1 1 1",
    "5 9 3 2 1 4",
    "0",
]

PROBLEMS_GREEDY = [
    dict(title="Classwork: N meetings in one room (GfG)",
         stmt="One room, many meeting requests, each with a start and a finish time. Print the largest number of meetings that can be held.\n\nA meeting may start at the exact moment another finishes.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `0 <= start < finish <= 10^9`",
         solve=lambda s: str(n_meetings(parse_iv(s))), cases=IV_CASES),

    dict(title="Classwork: LC435 Non-overlapping Intervals",
         stmt="Print the minimum number of intervals to remove so that the rest do not overlap.\n\nIntervals that merely touch, like `[1,2]` and `[2,3]`, do **not** overlap.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `-5 * 10^4 <= start < end <= 5 * 10^4`",
         solve=lambda s: str(erase_overlap(parse_iv(s))), cases=IV_CASES),

    dict(title="Classwork: Maximum number of activities selected (GfG)",
         stmt="Given activities that all need the same resource, print the maximum number that can be performed.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `0 <= start < finish <= 10^9`",
         solve=lambda s: str(n_meetings(parse_iv(s))), cases=IV_CASES),

    dict(title="Homework: LC452 Minimum Number of Arrows to Burst Balloons",
         stmt="Each balloon spans a closed interval on the x-axis. An arrow shot at `x` bursts every balloon whose interval contains `x`. Print the minimum number of arrows needed.\n\nBecause the intervals are **closed**, a balloon starting exactly at the arrow's position is still burst.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `-2^31 <= start <= end <= 2^31 - 1`",
         solve=lambda s: str(min_arrows(parse_iv(s))), cases=IV_CASES),

    dict(title="Homework: LC646 Maximum Length of Pair Chain",
         stmt="A pair `(c, d)` can follow `(a, b)` only when `b < c` **strictly**. Print the length of the longest chain.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 1000`\n- `-1000 <= a < b <= 1000`",
         solve=lambda s: str(pair_chain(parse_iv(s))), cases=IV_CASES),

    dict(title="Homework: Maximize meetings attended in one room (GfG)",
         stmt="Given meeting times, print how many one person can attend, given they can be in only one meeting at a time.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `0 <= start < finish <= 10^9`",
         solve=lambda s: str(n_meetings(parse_iv(s))), cases=IV_CASES),

    dict(title="Classwork: LC56 Merge Intervals",
         stmt="Merge all overlapping intervals and print the result sorted by start time.\n\nIntervals that merely touch, like `[1,4]` and `[4,5]`, **do** merge here.",
         inp=IV_IN,
         out="One line per merged interval, two integers separated by a space, in "
             "increasing order of start time.",
         cons="- `1 <= n <= 10^4`\n- `0 <= start <= end <= 10^4`",
         solve=lambda s: "\n".join("%d %d" % (a, b) for a, b in merge_iv(parse_iv(s))),
         cases=IV_CASES),

    dict(title="Classwork: LC57 Insert Interval",
         stmt="Given non-overlapping intervals sorted by start time, insert a new interval and print the result, merging where needed.",
         inp=IV_IN + "\n\nA final line contains the two integers of the interval to "
                     "insert.",
         out="One line per interval in the result, two integers separated by a space.",
         cons="- `0 <= n <= 10^4`\n- the input intervals are sorted and non-overlapping",
         solve=lambda s: "\n".join(
             "%d %d" % (a, b) for a, b in
             insert_iv(parse_iv(s), ints(rows(s)[int(rows(s)[0]) + 1]))),
         cases=["2\n1 3\n6 9\n2 5",
                "5\n1 2\n3 5\n6 7\n8 10\n12 16\n4 8",
                "1\n1 5\n2 3",
                "1\n1 5\n6 8",
                "3\n1 2\n4 5\n7 8\n3 6",
                "2\n1 2\n5 6\n3 4",
                "1\n3 5\n1 2",
                "0\n5 7"]),

    dict(title="Classwork: Minimum number of platforms (GfG)",
         stmt="Given train arrival and departure times, print the minimum number of platforms so that no train waits.\n\nA train arriving exactly when another departs still needs its own platform.",
         inp="The first line contains the arrival times, space separated. The second "
             "line contains the departure times, in the same train order.",
         out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- times are integers",
         solve=lambda s: str(min_platforms(ints(rows(s)[0]), ints(rows(s)[1]))),
         cases=["900 940 950 1100 1500 1800\n910 1200 1120 1130 1900 2000",
                "900 1100 1235\n1000 1200 1240",
                "1 5 10\n2 6 11",
                "200 210 300 320 350 500\n230 240 320 430 400 520",
                "1 2 3\n4 5 6",
                "10 20\n30 40",
                "1 1 1\n2 2 2",
                "100\n200"]),

    dict(title="Homework: LC986 Interval List Intersections",
         stmt="Given two lists of closed intervals, each sorted and internally disjoint, print every interval where they intersect.",
         inp="The first line contains `n`, then `n` lines of the first list. The next "
             "line contains `m`, then `m` lines of the second list.",
         out="One line per intersection, two integers separated by a space. Print "
             "nothing if there are none.",
         cons="- `0 <= n, m <= 1000`\n- each list is sorted and disjoint",
         solve=lambda s: "\n".join(
             "%d %d" % (a, b) for a, b in
             interval_intersections(parse_iv(s),
                                    parse_iv(s, start=int(rows(s)[0]) + 2))),
         cases=["4\n0 2\n5 10\n13 23\n24 25\n4\n1 5\n8 12\n15 24\n25 26",
                "1\n1 3\n1\n2 4",
                "2\n1 5\n8 12\n2\n5 10\n11 15",
                "1\n0 10\n3\n1 2\n4 5\n7 8",
                "2\n3 5\n9 20\n2\n4 5\n7 10",
                "1\n5 5\n1\n5 5",
                "1\n1 3\n1\n5 7",
                "0\n1\n1 2"]),

    dict(title="Homework: LC1094 Car Pooling",
         stmt="A car with fixed seating drives east, picking up and dropping off passengers at given points. Decide whether every trip fits within capacity.",
         inp="The first line contains the capacity. The second line contains `n`. Each "
             "of the next `n` lines has three integers: passengers, start, end.",
         out=BOOL_OUT,
         cons="- `1 <= n <= 1000`\n- `1 <= capacity <= 10^5`\n"
              "- `0 <= start < end <= 1000`",
         solve=lambda s: fmt_bool(car_pooling(
             [tuple(ints(r)) for r in rows(s)[2:2 + int(rows(s)[1])]],
             int(rows(s)[0]))),
         cases=["4\n2\n2 1 5\n3 3 7",
                "5\n2\n2 1 5\n3 3 7",
                "4\n2\n2 1 5\n3 5 7",
                "1\n2\n1 0 1\n1 1 2",
                "3\n3\n2 1 5\n3 5 7\n2 7 9",
                "2\n2\n1 0 5\n1 2 3",
                "2\n2\n2 0 5\n1 2 3",
                "1\n1\n1 0 1"]),

    dict(title="Homework: Maximum number of overlapping intervals (GfG)",
         stmt="Given a set of intervals, print the largest number that overlap at any single point.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `0 <= start < end <= 10^9`",
         solve=lambda s: str(min_platforms([a for a, b in parse_iv(s)],
                                          [b for a, b in parse_iv(s)])),
         cases=IV_CASES),

    dict(title="Classwork: Fractional Knapsack (GfG)",
         stmt="Given items with values and weights and a knapsack capacity, print the maximum value obtainable when items may be broken into **fractions**.",
         inp="The first line contains `n` and the capacity `W`. Each of the next `n` "
             "lines contains an item's value and weight.",
         out="A single line: the maximum value, printed with exactly five decimal "
             "places.",
         cons="- `1 <= n <= 10^5`\n- `1 <= W <= 10^9`\n- weights are positive",
         solve=lambda s: "%.5f" % fractional_knapsack(
             [tuple(ints(r)) for r in rows(s)[1:1 + ints(rows(s)[0])[0]]],
             ints(rows(s)[0])[1]),
         cases=["3 50\n60 10\n100 20\n120 30",
                "3 10\n10 2\n20 4\n30 6",
                "2 5\n10 10\n20 10",
                "4 15\n10 2\n5 3\n15 5\n7 7",
                "2 1\n100 50\n1 1",
                "1 10\n60 10",
                "1 5\n10 10",
                "3 100\n1 1\n2 2\n3 3"]),

    dict(title="Classwork: Job Sequencing Problem (GfG)",
         stmt="Each job takes one unit of time, must finish by its deadline, and pays a profit. Print how many jobs can be done and the maximum total profit.",
         inp="The first line contains `n`. Each of the next `n` lines contains a job's "
             "id, deadline and profit.",
         out="A single line: the number of jobs done and the total profit, separated by "
             "a space.",
         cons="- `1 <= n <= 10^5`\n- `1 <= deadline <= n`\n- profits are positive",
         solve=lambda s: "%d %d" % job_sequencing(
             [tuple(ints(r)) for r in rows(s)[1:1 + int(rows(s)[0])]]),
         cases=["4\n1 4 20\n2 1 10\n3 1 40\n4 1 30",
                "5\n1 2 100\n2 1 19\n3 2 27\n4 1 25\n5 1 15",
                "3\n1 1 10\n2 1 20\n3 1 30",
                "3\n1 3 10\n2 3 20\n3 3 30",
                "4\n1 2 5\n2 2 10\n3 1 15\n4 3 20",
                "5\n1 5 1\n2 4 2\n3 3 3\n4 2 4\n5 1 5",
                "2\n1 1 1\n2 2 2",
                "1\n1 1 50"]),

    dict(title="Homework: LC455 Assign Cookies",
         stmt="Each child has a greed value and each cookie a size. A child is content if their cookie is at least their greed. Print the maximum number of content children.",
         inp="The first line contains the children's greed values. The second line "
             "contains the cookie sizes.",
         out=NUM_OUT,
         cons="- `0 <= number of children, cookies <= 5 * 10^4`",
         solve=lambda s: str(assign_cookies(
             ints(rows(s)[0]), ints(rows(s)[1]) if len(rows(s)) > 1 else [])),
         cases=["1 2 3\n1 1", "1 2\n1 2 3", "2 3 4\n1 5 3", "10\n1 2 3",
                "1 1 1\n1 1 1", "1 2 3 4\n4", "5 5 5\n5 5", "1\n1"]),

    dict(title="Homework: Huffman Encoding (GfG)",
         stmt="Given the frequencies of the symbols in a message, print the minimum total number of bits needed to encode it with an optimal prefix code.",
         inp="A single line: the symbol frequencies, space separated.",
         out=NUM_OUT,
         cons="- `1 <= number of symbols <= 10^5`\n- frequencies are positive",
         solve=lambda s: str(huffman_cost(ints(s))),
         cases=["5 9 12 13 16 45", "1 2 3 4 5", "10 20 30", "1 1 2 3 5 8 13",
                "1 1 1 1", "5 5 5 5 5 5", "1 1", "4"]),

    dict(title="Homework: Minimum number of coins (GfG)",
         stmt="Given a set of denominations and an amount, print the minimum number of pieces that make it up, or `-1` if it cannot be made.",
         inp="The first line contains the available denominations, space separated. The "
             "second line contains the amount.",
         out="A single line: the number of pieces, or `-1`.",
         cons="- `1 <= amount <= 10^9`",
         solve=lambda s: str(min_coins_greedy(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 2 5 10 20 50 100 200 500 2000\n121",
                "1 2 5 10 20 50 100 200 500 2000\n43",
                "1 2 5 10 20 50 100 200 500 2000\n999",
                "1 2 5 10 20 50 100 200 500 2000\n70",
                "1 5 10\n18",
                "2 5\n3",
                "1 2 5 10 20 50 100 200 500 2000\n2000",
                "1 2 5 10 20 50 100 200 500 2000\n1"]),

    dict(title="Classwork: LC55 Jump Game",
         stmt="Each entry says how far you may jump forward from that position, starting at the first. Decide whether the last position is reachable.",
         inp=ARR_IN, out=BOOL_OUT,
         cons="- `1 <= n <= 10^4`\n- `0 <= value <= 10^5`",
         solve=lambda s: fmt_bool(jump_game(ints(s))), cases=ARR_CASES),

    dict(title="Classwork: LC134 Gas Station",
         stmt="Stations sit in a circle; each has some gas, and reaching the next costs some gas. Print the index to start from to complete the circuit, or `-1` if impossible.",
         inp="The first line contains the gas at each station. The second line contains "
             "the cost to reach the next station.",
         out="A single line: the starting index, or `-1`.",
         cons="- `1 <= n <= 10^5`\n- values are non-negative",
         solve=lambda s: str(gas_station(ints(rows(s)[0]), ints(rows(s)[1]))),
         cases=["1 2 3 4 5\n3 4 5 1 2",
                "2 3 4\n3 4 3",
                "3 1 1\n1 2 2",
                "6 1 4 3 5\n3 6 1 5 3",
                "2 0 0 0\n0 1 0 0",
                "1 1 1 1\n1 1 1 1",
                "5\n4",
                "4\n5"]),

    dict(title="Classwork: LC135 Candy",
         stmt="Children stand in a line with given ratings. Everyone gets at least one candy, and a child rated higher than a neighbour must get more than that neighbour. Print the minimum total candy.",
         inp=ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 2 * 10^4`\n- `0 <= rating <= 2 * 10^4`",
         solve=lambda s: str(candy(ints(s))), cases=ARR_CASES),

    dict(title="Homework: LC45 Jump Game II",
         stmt="Each entry says how far you may jump forward. The end is always reachable; print the **minimum** number of jumps to get there.",
         inp=ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^4`\n- the last index is always reachable",
         solve=lambda s: str(jump_game_ii(ints(s))),
         cases=["2 3 1 1 4", "2 3 0 1 4", "1 2 3", "5 1 1 1 1",
                "1 1 1 1", "1 2 1 1 1", "2 1", "0"]),

    dict(title="Homework: LC763 Partition Labels",
         stmt="Split a string into as many parts as possible so that no letter appears in more than one part. Print the part sizes in order.",
         inp="A single line: the string, lowercase letters only.",
         out="A single line: the part sizes, space separated.",
         cons="- `1 <= length <= 500`\n- lowercase English letters",
         solve=lambda s: fmt(partition_labels(s.strip())),
         cases=["ababcbacadefegdehijhklij", "eccbbbbdec", "abcabc", "abac",
                "qiejxqfnqceocmy", "aaaa", "abc", "a"]),

    dict(title="Homework: Rearrange characters so that none are adjacent (GfG)",
         stmt="Rearrange a string so no two adjacent characters are the same. Print the **lexicographically smallest** such arrangement, or `-1` if it is impossible.",
         inp="A single line: the string, lowercase letters only.",
         out="A single line: the arrangement, or `-1`.",
         cons="- `1 <= length <= 10^4`\n- lowercase English letters",
         solve=lambda s: rearrange_no_adjacent(s.strip()),
         cases=["aab", "aabb", "aaabc", "aaabbc", "abcabc", "aa", "aaab", "a"]),

    dict(title="Homework: LC1353 Maximum Number of Events That Can Be Attended",
         stmt="Each event can be attended on any single day within its start-to-end range, and only one event per day. Print the maximum number attendable.",
         inp=IV_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- `1 <= start <= end <= 10^5`",
         solve=lambda s: str(max_events(parse_iv(s))),
         cases=["3\n1 2\n2 3\n3 4",
                "4\n1 2\n2 3\n3 4\n1 2",
                "3\n1 4\n4 4\n2 2",
                "5\n1 5\n1 5\n1 5\n2 3\n2 3",
                "2\n1 100000\n1 1",
                "4\n1 1\n1 1\n1 1\n1 1",
                "3\n1 3\n1 3\n1 3",
                "1\n1 1"]),

    dict(title="Homework: LC860 Lemonade Change",
         stmt="Customers queue up paying with a 5, 10 or 20 note for a 5-unit lemonade. You start with no change. Decide whether every customer can be given correct change.",
         inp="A single line: the notes in the order received, space separated.",
         out=BOOL_OUT,
         cons="- `1 <= n <= 10^5`\n- each note is 5, 10 or 20",
         solve=lambda s: fmt_bool(lemonade(ints(s))),
         cases=["5 5 5 10 20", "5 5 10 10 20", "5 10 5 20", "5 5 5 5 20 20",
                "5 5 10", "5 5 20", "5 10 20", "10"]),
]


# --------------------------------------------------- LEC 4-10: arrays, maps --
from collections import Counter


def words(s):
    return s.split()


STR_IN = "A single line containing the string."
WORDS_IN = ("The first line contains an integer `n`. The second line contains `n` "
            "space-separated words.")


def two_sum(a, t):
    seen = {}
    for i, x in enumerate(a):
        if t - x in seen:
            return [seen[t - x], i]
        seen.setdefault(x, i)
    return []


def freq_lines(a):
    c = Counter(a)
    return "\n".join("%s %d" % (k, c[k]) for k in sorted(c))


def first_uniq(s):
    c = Counter(s)
    for i, ch in enumerate(s):
        if c[ch] == 1:
            return i
    return -1


def dup_within_k(a, k):
    seen = {}
    for i, x in enumerate(a):
        if x in seen and i - seen[x] <= k:
            return True
        seen[x] = i
    return False


def subarray_sum_k(a, k):
    run, seen, n = 0, {0: 1}, 0
    for x in a:
        run += x
        n += seen.get(run - k, 0)
        seen[run] = seen.get(run, 0) + 1
    return n


def subarray_div_k(a, k):
    run, seen, n = 0, {0: 1}, 0
    for x in a:
        run = (run + x) % k
        n += seen.get(run, 0)
        seen[run] = seen.get(run, 0) + 1
    return n


def longest_unique(s):
    seen, best, lo = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= lo:
            lo = seen[ch] + 1
        seen[ch] = i
        best = max(best, i - lo + 1)
    return best


def group_anagrams(ws):
    g = {}
    for w in ws:
        g.setdefault("".join(sorted(w)), []).append(w)
    groups = [sorted(v) for v in g.values()]
    return sorted(groups, key=lambda x: x[0])


def longest_consecutive(a):
    s, best = set(a), 0
    for x in s:
        if x - 1 in s:
            continue
        y = x
        while y + 1 in s:
            y += 1
        best = max(best, y - x + 1)
    return best


def largest_zero_sum(a):
    run, first, best = 0, {0: -1}, 0
    for i, x in enumerate(a):
        run += x
        if run in first:
            best = max(best, i - first[run])
        else:
            first[run] = i
    return best


def last_stone(a):
    h = [-x for x in a]
    heapq.heapify(h)
    while len(h) > 1:
        x = -heapq.heappop(h)
        y = -heapq.heappop(h)
        if x != y:
            heapq.heappush(h, -(x - y))
    return -h[0] if h else 0


def k_closest(pts, k):
    return sorted(pts, key=lambda p: (p[0] ** 2 + p[1] ** 2, p[0], p[1]))[:k]


def connect_ropes(a):
    h = list(a)
    heapq.heapify(h)
    total = 0
    while len(h) > 1:
        x = heapq.heappop(h)
        y = heapq.heappop(h)
        total += x + y
        heapq.heappush(h, x + y)
    return total


def top_k_frequent(a, k):
    c = Counter(a)
    return [v for v, _ in sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[:k]]


def top_k_words(ws, k):
    c = Counter(ws)
    return [w for w, _ in sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[:k]]


def sort_by_freq(s):
    c = Counter(s)
    out = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))
    return "".join(ch * n for ch, n in out)


def task_scheduler(tasks, n):
    c = Counter(tasks)
    mx = max(c.values())
    ties = sum(1 for v in c.values() if v == mx)
    return max(len(tasks), (mx - 1) * (n + 1) + ties)


def lower_bound_idx(a, t):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo if lo < len(a) and a[lo] == t else -1


def perms(s):
    import itertools
    return sorted(set("".join(p) for p in itertools.permutations(s)))


def prefix_queries(a, qs):
    pre = [0]
    for x in a:
        pre.append(pre[-1] + x)
    return [pre[r + 1] - pre[l] for l, r in qs]


def ncr(n, r):
    if r < 0 or r > n:
        return 0
    out = 1
    for i in range(r):
        out = out * (n - i) // (i + 1)
    return out


def fact(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def fib(n):
    memo = {0: 0, 1: 1}

    def go(k):
        if k not in memo:
            memo[k] = go(k - 1) + go(k - 2)
        return memo[k]
    return go(n)


def has_cycle(vals, pos):
    """pos is the index the tail links back to, or -1 for no cycle."""
    return pos != -1 and len(vals) > 0


def middle_node(vals):
    return vals[len(vals) // 2] if vals else None


def window_max(a, k):
    from collections import deque as dq
    q, out = dq(), []
    for i, x in enumerate(a):
        while q and a[q[-1]] <= x:
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            out.append(a[q[0]])
    return out


def browser_history(ops):
    """Two-stack browser history. Operations:
      visit URL  -- push current to history (if any), set current, clear future.
      back       -- if history non-empty, push current to future and pop history.
      forward    -- if future non-empty, push current to history and pop future.
    Output: the current URL after each operation, or 'blank' if none loaded."""
    hist, fut, cur = [], [], None
    lines = []
    for op in ops:
        parts = op.split()
        cmd = parts[0] if parts else ""
        if cmd == "visit" and len(parts) >= 2:
            if cur is not None:
                hist.append(cur)
            cur = parts[1]
            fut = []
        elif cmd == "back":
            if hist:
                fut.append(cur)
                cur = hist.pop()
        elif cmd == "forward":
            if fut:
                hist.append(cur)
                cur = fut.pop()
        lines.append(cur if cur is not None else "blank")
    return "\n".join(lines)


ARR_SETS = [
    "2 7 11 15",
    "3 2 4",
    "1 2 3 4 5",
    "4 1 2 1 2",
    "5 5 5 5",
    "1",
    "-1 -2 -3 -4",
    "10 5 2 6 1 9",
]

# LEC-1..LEC-10 classwork uses a size-first array format so a C++ student can
# write `cin >> n; vector<int> a(n); for (int i = 0; i < n; i++) cin >> a[i];`
# without having to read a whole line and split. Bigger LEC files keep the
# original ARR_IN (their I/O is more varied and the size is derivable from
# other tokens on the first line).
SIZED_ARR_IN = ("The first line contains an integer `n`. "
                "The second line contains `n` space-separated integers.")
SIZED_ARR_SETS = ["%d\n%s" % (len(c.split()), c) for c in ARR_SETS]


def sized(cases):
    """Given a list of test-case strings whose FIRST line is a raw array
    (space-separated ints), prepend the array's size as a new first line."""
    out = []
    for c in cases:
        lines = c.split("\n", 1)
        first = lines[0]
        n = len(first.split())
        rest = ("\n" + lines[1]) if len(lines) > 1 else ""
        out.append("%d\n%s%s" % (n, first, rest))
    return out


# --- helpers for homework rows ---------------------------------------------

def sliding_window_max(a, k):
    """Max of every window of size k. Returns a list of n - k + 1 values."""
    from collections import deque
    dq, out = deque(), []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(a[dq[0]])
    return out


def print_umap_by_count(ws):
    """For a list of words, produce lines `<word> <count>` sorted by count
    descending, ties by word ascending."""
    c = Counter(ws)
    keys = sorted(c, key=lambda w: (-c[w], w))
    return "\n".join("%s %d" % (w, c[w]) for w in keys)


def sort_strings_by_length_then_lex(ss):
    return sorted(ss, key=lambda x: (len(x), x))


def single_number(a):
    """LC136 -- xor everything; the unpaired value drops out."""
    x = 0
    for v in a:
        x ^= v
    return x


def good_pairs(a):
    """LC1512 -- number of (i, j) with i < j and a[i] == a[j]."""
    c = Counter(a)
    return sum(v * (v - 1) // 2 for v in c.values())


def max_product_two_minus_one(a):
    """LC1464 -- max (a[i]-1) * (a[j]-1) over i < j."""
    s = sorted(a, reverse=True)
    return (s[0] - 1) * (s[1] - 1)


def k_weakest_rows(mat, k):
    """LC1337 -- k row indices ordered by (soldier count asc, index asc)."""
    idx = sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))
    return idx[:k]


def lucky_integer(a):
    """LC1394 -- largest v where v == frequency(v), or -1."""
    c = Counter(a)
    lucky = [v for v, cnt in c.items() if v == cnt]
    return max(lucky) if lucky else -1


def sorted_stream(lines):
    """`insert <x>` inserts x into a multiset; `smallest` prints the current
    smallest. `remove <x>` removes one occurrence if present."""
    import bisect
    q = int(lines[0])
    data = []
    out = []
    for op in lines[1:1 + q]:
        parts = op.split()
        if parts[0] == "insert":
            bisect.insort(data, int(parts[1]))
        elif parts[0] == "smallest":
            out.append(str(data[0]))
        elif parts[0] == "remove":
            x = int(parts[1])
            i = bisect.bisect_left(data, x)
            if i < len(data) and data[i] == x:
                data.pop(i)
    return "\n".join(out)


def kth_largest_stream(lines):
    """Line 1: k. Line 2: n0 (initial size). Line 3: n0 values on one line
    (empty line when n0 = 0). Line 4: q. Next q lines: `add <val>`.
    Emits one line per `add`: the current k-th largest, or `-` if fewer
    than k values have been seen. The initial fill is silent."""
    import heapq
    k = int(lines[0])
    n0 = int(lines[1])
    init = list(map(int, lines[2].split())) if n0 > 0 else []
    q = int(lines[3])
    h = []
    for v in init:
        if len(h) < k:
            heapq.heappush(h, v)
        elif v > h[0]:
            heapq.heapreplace(h, v)
    out = []
    for op in lines[4:4 + q]:
        v = int(op.split()[1])
        if len(h) < k:
            heapq.heappush(h, v)
        elif v > h[0]:
            heapq.heapreplace(h, v)
        out.append(str(h[0]) if len(h) >= k else "-")
    return "\n".join(out)


def lru_cache_sim(lines):
    """Line 1: capacity. Line 2: q. Then q lines `get <key>` or
    `put <key> <val>`. Emit one line per `get`: the returned value or -1."""
    from collections import OrderedDict
    cap = int(lines[0])
    q = int(lines[1])
    cache = OrderedDict()
    out = []
    for op in lines[2:2 + q]:
        parts = op.split()
        if parts[0] == "get":
            key = int(parts[1])
            if key in cache:
                cache.move_to_end(key)
                out.append(str(cache[key]))
            else:
                out.append("-1")
        elif parts[0] == "put":
            key, val = int(parts[1]), int(parts[2])
            if key in cache:
                cache.move_to_end(key)
            cache[key] = val
            if len(cache) > cap:
                cache.popitem(last=False)
    return "\n".join(out)


def all_o_one(lines):
    """LC432. Ops: `inc <key>`, `dec <key>` (removes if count hits 0),
    `max` prints one key with the highest count (`-` if empty), `min` prints
    one key with the smallest positive count (`-` if empty).
    For determinism, break ties by lexicographic order of the key."""
    q = int(lines[0])
    freq = {}
    out = []
    for op in lines[1:1 + q]:
        parts = op.split()
        cmd = parts[0]
        if cmd == "inc":
            k = parts[1]
            freq[k] = freq.get(k, 0) + 1
        elif cmd == "dec":
            k = parts[1]
            if k in freq:
                freq[k] -= 1
                if freq[k] == 0:
                    del freq[k]
        elif cmd == "max":
            if not freq:
                out.append("-")
            else:
                m = max(freq.values())
                out.append(min(k for k, v in freq.items() if v == m))
        elif cmd == "min":
            if not freq:
                out.append("-")
            else:
                m = min(freq.values())
                out.append(min(k for k, v in freq.items() if v == m))
    return "\n".join(out)


# --- helpers for the remaining classwork rows -------------------------------

def relative_ranks(scores):
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    labels = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    rank = [""] * len(scores)
    for place, i in enumerate(order):
        rank[i] = labels[place] if place < 3 else str(place + 1)
    return "\n".join(rank)


def sort_by_freq_then_desc(a):
    c = Counter(a)
    # Sort keys by (freq asc, value desc), then expand each key freq times.
    keys = sorted(c, key=lambda x: (c[x], -x))
    out = []
    for k in keys:
        out.extend([k] * c[k])
    return out


def reorganize_string(s):
    """Return the lexicographically smallest rearrangement with no two adjacent
    equal characters, or 'impossible' when none exists. At each position tries
    each remaining character in lex order and commits to the first one that
    still leaves the rest of the string arrangeable -- checked by the standard
    condition max(count) <= (remaining_length + 1) // 2."""
    c = Counter(s)
    if c and max(c.values()) > (len(s) + 1) // 2:
        return "impossible"
    out, prev = [], None
    keys = sorted(c)
    for pos in range(len(s)):
        rem_after = len(s) - pos - 1
        for ch in keys:
            if c[ch] == 0 or ch == prev:
                continue
            c[ch] -= 1
            max_rem = max(c.values()) if c else 0
            if max_rem <= (rem_after + 1) // 2:
                out.append(ch)
                prev = ch
                break
            c[ch] += 1
        else:
            return "impossible"                  # guarded by the check above
    return "".join(out)


def median_stream(lines):
    import bisect
    q = int(lines[0])
    data = []
    out = []
    for op in lines[1:1 + q]:
        if op.startswith("add "):
            bisect.insort(data, int(op.split()[1]))
        elif op.strip() == "median":
            n = len(data)
            if n % 2 == 1:
                out.append("%.5f" % data[n // 2])
            else:
                out.append("%.5f" % ((data[n // 2 - 1] + data[n // 2]) / 2))
    return "\n".join(out)


def design_twitter(lines):
    q = int(lines[0])
    tweets_by_user = {}                          # user -> list of (time, tid)
    follows = {}                                 # user -> set of followees
    t = 0
    out = []
    for op in lines[1:1 + q]:
        parts = op.split()
        cmd = parts[0]
        if cmd == "post":
            u, tid = int(parts[1]), int(parts[2])
            tweets_by_user.setdefault(u, []).append((t, tid))
            t += 1
        elif cmd == "follow":
            u, v = int(parts[1]), int(parts[2])
            follows.setdefault(u, set()).add(v)
        elif cmd == "unfollow":
            u, v = int(parts[1]), int(parts[2])
            follows.setdefault(u, set()).discard(v)
        elif cmd == "feed":
            u = int(parts[1])
            people = set(follows.get(u, ())) | {u}
            merged = []
            for p in people:
                merged.extend(tweets_by_user.get(p, ()))
            merged.sort(key=lambda x: -x[0])
            out.append(" ".join(str(tid) for _, tid in merged[:10]))
    return "\n".join(out)


def freq_stack(lines):
    import heapq
    q = int(lines[0])
    freq = {}
    groups = {}                                  # freq -> list of values (LIFO)
    out = []
    for op in lines[1:1 + q]:
        parts = op.split()
        if parts[0] == "push":
            v = int(parts[1])
            freq[v] = freq.get(v, 0) + 1
            groups.setdefault(freq[v], []).append(v)
        else:  # pop
            top = max(groups)
            v = groups[top].pop()
            if not groups[top]:
                del groups[top]
            freq[v] -= 1
            out.append(str(v))
    return "\n".join(out)


# --- helpers for LEC-1..LEC-3 additions ---
def count_gt(a, k):
    return sum(1 for x in a if x > k)


def first_gt(a, k):
    for x in a:
        if x > k:
            return x
    return None


def sort_pairs_ss(pairs):
    return sorted(pairs, key=lambda p: (p[1], p[0]))


def drop_odds(a):
    return [x for x in a if x % 2 == 0]


def distinct_sorted(a):
    return sorted(set(a))


def distinct_first_seen(a):
    seen, out = set(), []
    for x in a:
        if x not in seen:
            seen.add(x); out.append(x)
    return out


def word_freq_lines(ws):
    c = Counter(ws)
    return "\n".join("%s %d" % (w, c[w]) for w in sorted(c))


def browser_history(lines):
    """Line 1 = homepage. Line 2 = number of ops. Then that many op lines:
        visit <url>
        back <steps>
        forward <steps>
    Emits one URL per op: the page you are on after that op."""
    home = lines[0].strip()
    n = int(lines[1])
    history = [home]
    cur = 0
    top = 0                                  # furthest reachable via forward
    out = []
    for op in lines[2:2 + n]:
        parts = op.split()
        cmd = parts[0]
        if cmd == "visit":
            url = parts[1]
            cur += 1
            if cur < len(history):
                history[cur] = url
            else:
                history.append(url)
            top = cur                         # visiting clears forward stack
        elif cmd == "back":
            steps = int(parts[1])
            cur = max(0, cur - steps)
        elif cmd == "forward":
            steps = int(parts[1])
            cur = min(top, cur + steps)
        out.append(history[cur])
    return "\n".join(out)


PROBLEMS_01_10 = [
    # ---- LEC-1 : lambdas ---------------------------------------------------
    dict(title="Classwork: Sum of Two Integers",
         stmt="Print the sum of two integers.",
         inp="A single line with two integers `a` and `b`, separated by a space.",
         out=NUM_OUT,
         cons="- `-10^9 <= a, b <= 10^9`",
         solve=lambda s: str(sum(ints(s))),
         cases=["3 4", "0 0", "-1 5", "-7 -8",
                "100 200", "1000000 2000000", "-1000000 1000000", "1 -1"],
         explains=[
             "The two numbers are 3 and 4. Their sum is 7.",
             "Both numbers are 0. The sum is 0.",
         ]),

    dict(title="Classwork: Sort in Descending Order",
         stmt="Print the elements of an integer array in **decreasing** order.",
         inp=SIZED_ARR_IN, out=SEQ_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt(sorted(ints(rows(s)[1]), reverse=True)),
         cases=SIZED_ARR_SETS,
         explains=[
             "The array is 2, 7, 11, 15. Sorted from biggest to smallest: 15, 11, 7, 2.",
             "The array is 3, 2, 4. Sorted from biggest to smallest: 4, 3, 2.",
         ]),

    dict(title="Count Elements Greater Than K",
         hr_id=590960,   # duplicate title in the account; 596085 is an orphan
         stmt="Print how many elements of an array are strictly greater than a value `k`.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=NUM_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: str(count_gt(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["1 2 3 4 5\n2", "5 5 5\n5", "1\n0",
                      "-3 -1 0 4\n0", "10 20 30\n25", "1 1 1\n1",
                      "-5 -4 -3\n-5", "7 6 5 4 3\n10"]),
         explains=[
             "K is 2. Numbers greater than 2 are 3, 4, and 5. That is 3 numbers.",
             "K is 5. No number is strictly greater than 5, so the count is 0.",
         ]),

    dict(title="Classwork: Add Two Numbers Mixed Types",
         stmt="Print the sum of an integer and a floating-point number. "
              "Print the result with exactly **six** digits after the decimal point.",
         inp="A single line: the integer `a` and the double `b`, separated by a space.",
         out="A single line: `a + b` with 6 digits after the decimal point.",
         cons="- `-10^6 <= a <= 10^6`\n- `-10^6 <= b <= 10^6`",
         solve=lambda s: "%.6f" % (int(s.split()[0]) + float(s.split()[1])),
         cases=["2 3.5", "0 0.0", "-1 1.25", "10 0.1",
                "-5 -2.5", "100 3.1415", "7 0.333333",
                "-1000 1000.0"],
         explains=[
             "The integer is 2 and the decimal is 3.5. Their sum is 5.5.",
             "Both numbers are 0. The sum is 0.0.",
         ]),

    # ---- LEC-2 : more lambdas ----------------------------------------------
    dict(title="Classwork: Square Every Element",
         stmt="Print the square of each element of an integer array, in the same order.",
         inp=SIZED_ARR_IN, out=SEQ_OUT, cons="- `1 <= n <= 10^5`\n- `|value| <= 10^4`",
         solve=lambda s: fmt(x * x for x in ints(rows(s)[1])),
         cases=sized(["1 2 3", "-2 -3 4", "0 0 0", "10",
                      "5 -5", "1 1 1 1", "-10 10 -1 1", "7 8 9"]),
         explains=[
             "Square each: 1x1=1, 2x2=4, 3x3=9.",
             "Square each: -2x-2=4, -3x-3=9, 4x4=16.",
         ]),

    dict(title="Classwork: Use find_if to return the first element greater than K",
         stmt="Print the **first** element of an array that is strictly greater than a "
              "value `k`, in input order. Print `-1` if no such element exists.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out="A single line: the first element greater than `k`, or `-1`.",
         cons="- `1 <= n <= 10^5`",
         solve=lambda s: str(first_gt(ints(rows(s)[1]), int(rows(s)[2])) if
                             first_gt(ints(rows(s)[1]), int(rows(s)[2])) is not None
                             else -1),
         cases=sized(["1 4 2 8 5\n3", "5 5 5\n5", "1 2 3\n0",
                      "10 20 30\n25", "1\n0", "-3 -1 0\n-2",
                      "7 6 5 4\n10", "9 1 8 2\n7"]),
         explains=[
             "K is 3. Going left to right, the first number bigger than 3 is 4.",
             "K is 5. No number is strictly greater than 5, so print -1.",
         ]),

    dict(title="Classwork: Sort Pairs by Second Value",
         stmt="Given a list of integer pairs, print them sorted in increasing order of "
              "their **second** value, breaking ties by the **first** value.",
         inp="The first line contains `n`. Each of the next `n` lines contains two "
             "integers separated by a space.",
         out="One pair per line: the two integers separated by a space.",
         cons="- `1 <= n <= 10^5`",
         solve=lambda s: "\n".join("%d %d" % (a, b) for a, b in
             sort_pairs_ss([tuple(ints(r)) for r in
                            rows(s)[1:1 + int(rows(s)[0])]])),
         cases=["3\n1 5\n2 3\n4 3",
                "1\n7 7",
                "4\n1 2\n3 2\n2 1\n4 1",
                "2\n1 1\n1 1",
                "5\n5 5\n4 4\n3 3\n2 2\n1 1",
                "3\n-1 0\n0 -1\n1 0",
                "2\n9 8\n8 9",
                "4\n1 10\n2 10\n3 10\n4 10"],
         explains=[
             "Sort by second value: (2,3) and (4,3) come first (second value 3). Between them, first value 2 comes before 4. Then (1,5) has second value 5.",
             "Only one pair (7,7), so the output is that pair.",
         ]),

    dict(title="Classwork: Use remove_if + erase to delete all odd numbers from a vector",
         stmt="Print the array with all **odd** values removed. Preserve the order of "
              "the remaining even values.",
         inp=SIZED_ARR_IN, out=SEQ_OUT,
         cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt(drop_odds(ints(rows(s)[1]))),
         cases=sized(["1 2 3 4 5 6", "2 4 6 8", "1 3 5 7",
                      "0 1 2 3", "10", "7",
                      "-1 -2 -3 -4", "1 2 1 2 1 2"]),
         explains=[
             "Odd numbers 1, 3, 5 are removed. Even numbers 2, 4, 6 stay in the same order.",
             "All numbers are already even. Nothing is removed.",
         ]),

    # ---- LEC-3 : STL containers --------------------------------------------
    dict(title="Classwork: Print Distinct Values in Sorted Order",
         stmt="Print the distinct values of an integer array in **increasing** order.",
         inp=SIZED_ARR_IN, out=SEQ_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt(distinct_sorted(ints(rows(s)[1]))),
         cases=sized(["5 2 8 2 5", "1 2 3 4 5", "7 7 7 7",
                      "3 1 2", "10 -5 3 -5 10", "1",
                      "9 8 7 6 5", "4 4 3 3 2 2 1 1"]),
         explains=[
             "The distinct values are 2, 5, and 8. Sorted in increasing order: 2, 5, 8.",
             "All five values are already distinct and in increasing order.",
         ]),

    dict(title="Classwork: Remove duplicates from a vector using a set",
         stmt="Print the array with duplicate values removed. Keep each value at its "
              "**first** position of occurrence.",
         inp=SIZED_ARR_IN, out=SEQ_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt(distinct_first_seen(ints(rows(s)[1]))),
         cases=sized(["1 2 1 3 2 4", "5 5 5 5", "1 2 3 4 5",
                      "3 1 2 1 3 2", "10 -5 3 -5 10", "7",
                      "9 8 7 6", "1 1 2 2 3 3"]),
         explains=[
             "The values in order of first appearance are 1, 2, 3, 4. Repeated occurrences (the second 1 and second 2) are dropped.",
             "All four values are the same. Only the first 5 stays.",
         ]),

    dict(title="Classwork: Count word frequencies from input using unordered_map",
         stmt="Print the number of times each distinct word appears, one word per "
              "line, sorted lexicographically by the word.",
         inp="The first line contains `n`. The second line contains `n` space-"
             "separated words.",
         out="One line per distinct word: the word and its count, separated by a "
             "space, in lexicographic order of the word.",
         cons="- `1 <= n <= 10^5`\n- words contain lowercase English letters only",
         solve=lambda s: word_freq_lines(words(rows(s)[1])),
         cases=["6\napple banana apple cherry banana apple",
                "3\ndog cat dog",
                "1\nhello",
                "4\na a a a",
                "5\nz y x w z",
                "6\nred blue red blue red blue",
                "2\none two",
                "5\ncat dog fish cat fish"],
         explains=[
             "apple appears 3 times, banana 2, cherry 1. Words are printed in alphabetical order.",
             "dog appears 2 times, cat 1. Alphabetical order: cat, then dog.",
         ]),

    dict(title="Classwork: Implement browser back/forward history using two stacks",
         stmt="Simulate a simple browser that supports three operations:\n"
              "\n"
              "- `visit <url>` -- open `<url>`, which becomes the current page and "
              "clears the forward history.\n"
              "- `back <steps>` -- go back `<steps>` pages, but never past the "
              "homepage.\n"
              "- `forward <steps>` -- go forward `<steps>` pages, but never past the "
              "furthest page reached.\n"
              "\n"
              "After each operation, print the URL of the current page.",
         inp="The first line contains the homepage URL. The second line contains an "
             "integer `q`. Each of the next `q` lines contains one operation exactly "
             "as described above.",
         out="One line per operation, in order: the URL of the current page after "
             "that operation.",
         cons="- `1 <= q <= 10^4`\n"
              "- `1 <= steps <= 10^4`\n"
              "- URLs contain visible ASCII characters, no spaces",
         solve=lambda s: browser_history(rows(s)),
         cases=[
             "leetcode.com\n7\nvisit google.com\nvisit facebook.com\nvisit youtube.com\nback 1\nback 1\nforward 1\nvisit linkedin.com",
             "home.com\n3\nvisit a.com\nback 5\nforward 5",
             "start\n1\nvisit only.com",
             "a\n4\nvisit b\nvisit c\nback 1\nforward 1",
             "x.com\n2\nback 3\nforward 3",
             "p\n5\nvisit q\nvisit r\nvisit s\nback 2\nvisit t",
             "root\n3\nvisit child1\nback 1\nvisit child2",
             "h\n6\nvisit a\nvisit b\nback 1\nvisit c\nforward 1\nback 2",
         ],
         explains=[
             "Start at leetcode.com. Visit google, then facebook, then youtube. Go back one page to facebook, then back again to google. Go forward one to facebook. Visit linkedin, which becomes the current page and clears any forward pages.",
             "Start at home.com. Visit a.com. Try to go back 5 pages, but only 1 page back exists — stop at home.com. Try to go forward 5, but only 1 forward exists — stop at a.com.",
         ]),

    # ---- LEC-4 : STL algorithms --------------------------------------------
    dict(title="Classwork: Sum and Maximum",
         stmt="Print the sum of the array on the first line and the maximum value on "
              "the second line.",
         inp=SIZED_ARR_IN, out="Two lines: the sum, then the maximum.",
         cons="- `1 <= n <= 10^5`",
         solve=lambda s: "%d\n%d" % (sum(ints(rows(s)[1])), max(ints(rows(s)[1]))),
         cases=sized(["1 2 3 4 5", "5", "-1 -2 -3",
                      "10 -5 3 8", "0 0 0", "7 7 7 7",
                      "100 200 300", "-10 10 -1 1"]),
         explains=[
             "Sum: 1+2+3+4+5 = 15. Maximum: the biggest value is 5.",
             "Only one number, 5. Both the sum and the maximum are 5.",
         ]),

    dict(title="Classwork: Find the k-th largest element using a priority_queue",
         stmt="Given `n` integers and a value `k`, print the `k`-th largest element.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=NUM_OUT, cons="- `1 <= k <= n <= 10^5`",
         solve=lambda s: str(sorted(ints(rows(s)[1]), reverse=True)[int(rows(s)[2]) - 1]),
         cases=sized(["3 2 1 5 6 4\n2", "1\n1", "3 2 3 1 2 4 5 5 6\n4",
                      "5 5 5 5\n3", "-1 -2 -3\n1", "10 5 2 6 1 9\n5",
                      "1 2\n2", "7 6 5 4 3 2 1\n7"]),
         explains=[
             "Sort from largest: 6, 5, 4, 3, 2, 1. The 2nd largest is 5.",
             "The array has one element, 1. The 1st largest is 1.",
         ]),

    dict(title="Classwork: Binary-search a target in a sorted vector with lower_bound",
         stmt="Given a sorted vector and a target, print the index of the target's first occurrence, or `-1` if it is absent.",
         inp=SIZED_ARR_IN + "\n\nA third line contains the target.",
         out="A single line: the 0-based index, or `-1`.",
         cons="- `1 <= n <= 10^5`\n- the vector is sorted increasing",
         solve=lambda s: str(lower_bound_idx(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["1 3 5 7 9\n5", "1 3 5 7 9\n4", "1 1 1 2\n1", "5\n5",
                      "5\n1", "1 2 3 4 5\n1", "1 2 3 4 5\n5", "2 4 6 8\n7"]),
         explains=[
             "The target 5 is in the array at index 2 (0-based).",
             "The target 4 is not in the array, so print -1.",
         ]),

    dict(title="Classwork: Count distinct elements using sort + unique",
         stmt="Print how many distinct values a vector contains.",
         inp=SIZED_ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: str(len(set(ints(rows(s)[1])))),
         cases=SIZED_ARR_SETS,
         explains=[
             "All 4 values (2, 7, 11, 15) are different. Distinct count is 4.",
             "All 3 values (3, 2, 4) are different. Distinct count is 3.",
         ]),

    dict(title="Homework: Merge k sorted vectors into one using a min-heap",
         stmt="Given `k` sorted vectors, merge them into one sorted vector and print it.",
         inp="The first line contains `k`. Each of the next `k` lines contains one "
             "sorted vector, space separated.",
         out=SEQ_OUT, cons="- `1 <= k <= 100`\n- each vector is sorted increasing",
         solve=lambda s: fmt(sorted(
             x for r in rows(s)[1:1 + int(rows(s)[0])] for x in ints(r))),
         cases=["3\n1 4 5\n1 3 4\n2 6", "1\n1 2 3", "2\n1 2\n3 4",
                "2\n5\n1", "3\n1\n2\n3", "2\n-3 -1\n-2 0",
                "2\n1 1 1\n1 1", "4\n1 5\n2 6\n3 7\n4 8"],
         explains=[
             "Three sorted vectors [1, 4, 5], [1, 3, 4], [2, 6]. All values merged and sorted: 1, 1, 2, 3, 4, 4, 5, 6.",
             "Only one already-sorted list [1, 2, 3]. Output is the same.",
         ]),

    dict(title="Homework: Generate all permutations of a string with next_permutation",
         stmt="Print every distinct permutation of a string in **lexicographic order**, one per line.",
         inp=STR_IN,
         out="One permutation per line, in lexicographic order.",
         cons="- `1 <= length <= 8`\n- lowercase English letters",
         solve=lambda s: "\n".join(perms(s.strip())),
         cases=["abc", "aab", "a", "ab", "aa", "abcd", "aba", "zyx"],
         explains=[
             "All 6 permutations of 'abc' in alphabetical order.",
             "Distinct permutations of 'aab' in alphabetical order: aab, aba, baa.",
         ]),

    dict(title="Homework: Answer range-sum queries using prefix sums (partial_sum)",
         stmt="Given an array and several inclusive index ranges, print the sum over each range.",
         inp=SIZED_ARR_IN + "\n\nThe next line contains `q`. Each of the next `q` lines "
                            "contains two 0-based indices `l` and `r`.",
         out="One line per query: the sum.",
         cons="- `1 <= n <= 10^5`\n- `1 <= q <= 10^5`\n- `0 <= l <= r < n`",
         solve=lambda s: "\n".join(str(x) for x in prefix_queries(
             ints(rows(s)[1]),
             [tuple(ints(r)) for r in rows(s)[3:3 + int(rows(s)[2])]])),
         cases=sized(["1 2 3 4 5\n2\n0 2\n1 3",
                      "1 2 3\n1\n0 2",
                      "5\n1\n0 0",
                      "-1 -2 -3\n2\n0 1\n2 2",
                      "1 1 1 1\n3\n0 0\n0 3\n2 3",
                      "10 20 30\n2\n1 1\n0 1",
                      "2 4 6 8\n1\n1 3",
                      "1 2 3 4 5\n1\n0 4"]),
         explains=[
             "Array [1, 2, 3, 4, 5]. Query 0-2: 1+2+3 = 6. Query 1-3: 2+3+4 = 9.",
             "Array [1, 2, 3]. Query 0-2: 1+2+3 = 6.",
         ]),

    # ---- LEC-5 : recursion & linked lists ----------------------------------
    dict(title="Classwork: Compute factorial and nCr recursively",
         stmt="Print `n!` and then `nCr`.",
         inp="The first line contains `n`. The second line contains `n` and `r` "
             "separated by a space.",
         out="Two lines: the factorial, then `nCr`.",
         cons="- `0 <= n <= 20`\n- `0 <= r <= n`",
         solve=lambda s: "%d\n%d" % (fact(int(rows(s)[0])),
                                     ncr(*ints(rows(s)[1]))),
         cases=["5\n5 2", "0\n0 0", "1\n1 1", "10\n10 5",
                "3\n3 0", "6\n6 3", "20\n20 1", "4\n4 4"],
         explains=[
             "5! = 5x4x3x2x1 = 120. nCr with n=5, r=2 is 10 (ways to pick 2 items from 5).",
             "0! = 1 by definition. 0C0 = 1 (one way to pick 0 items from 0).",
         ]),

    dict(title="Classwork: Reverse a singly linked list iteratively",
         stmt="Given the values of a singly linked list in order, reverse the list and print it.",
         inp="The first line contains an integer `n`. The second line contains the "
             "`n` list values in order, space separated. When `n` is `0` the second "
             "line is empty.",
         out=SEQ_OUT, cons="- `0 <= n <= 10^5`\n- auxiliary space `O(1)`",
         solve=lambda s: fmt(list(reversed(ints(rows(s)[1])))),
         cases=sized(["1 2 3 4 5", "1 2", "1", "5 4 3 2 1",
                      "1 1 1", "-1 -2 -3", "10 20 30 40", "7 7"]),
         explains=[
             "The list is 1 -> 2 -> 3 -> 4 -> 5. Reversed: 5 -> 4 -> 3 -> 2 -> 1.",
             "The list has two nodes 1 and 2. Reversed: 2 first, then 1.",
         ]),

    dict(title="Classwork: Print numbers 1..N and N..1 using recursion",
         stmt="Print the numbers from 1 up to `N`, then from `N` back down to 1, using recursion for both.",
         inp="A single line containing `N`.",
         out="Two lines: the ascending sequence, then the descending sequence, each "
             "space separated.",
         cons="- `1 <= N <= 10^4`",
         solve=lambda s: "%s\n%s" % (fmt(range(1, int(s) + 1)),
                                     fmt(range(int(s), 0, -1))),
         cases=["5", "1", "2", "10", "3", "7", "4", "6"],
         explains=[
             "N=5. First line prints 1 to 5. Second line prints 5 down to 1.",
             "N=1. Both lines just print 1.",
         ]),

    dict(title="Homework: Fibonacci with memoization",
         stmt="Print the `n`-th Fibonacci number, with `F(0) = 0` and `F(1) = 1`.",
         inp="A single line containing `n`.",
         out=NUM_OUT, cons="- `0 <= n <= 90`",
         solve=lambda s: str(fib(int(s))),
         cases=["10", "0", "1", "2", "30", "50", "7", "90"],
         explains=[
             "F(10) = 55 (the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55).",
             "F(0) = 0 by definition.",
         ]),

    dict(title="Homework: Detect a cycle in a linked list (Floyd's algorithm)",
         stmt="Decide whether a singly linked list contains a cycle.",
         inp="The first line contains `n`, the number of nodes. The second line "
             "contains the `n` list values in order, space separated. The third "
             "line contains the 0-based index that the last node links back to, "
             "or `-1` for no cycle.",
         out=BOOL_OUT, cons="- `0 <= n <= 10^4`\n- auxiliary space `O(1)`",
         solve=lambda s: fmt_bool(has_cycle(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["3 2 0 -4\n1", "1 2\n0", "1\n-1", "1 2 3\n-1",
                      "1\n0", "1 2 3 4\n2", "5 6\n-1", "9 8 7\n0"]),
         explains=[
             "The list is 3 -> 2 -> 0 -> -4. The last node links back to index 1 (value 2), which forms a cycle.",
             "The list is 1 -> 2. The last node links back to index 0 (value 1), which forms a cycle.",
         ]),

    dict(title="Homework: Find the middle node of a linked list in one pass",
         stmt="Print the value of the middle node of a singly linked list. With an even number of nodes, print the **second** of the two middle ones.",
         inp=SIZED_ARR_IN.replace("integers", "list values"),
         out=NUM_OUT, cons="- `1 <= n <= 10^5`\n- one pass only",
         solve=lambda s: str(middle_node(ints(rows(s)[1]))),
         cases=sized(["1 2 3 4 5", "1 2 3 4 5 6", "1", "1 2",
                      "10 20 30", "7 7 7 7", "-1 -2 -3", "1 2 3 4"]),
         explains=[
             "The list has 5 nodes. The middle one (position 2) has value 3.",
             "The list has 6 nodes (even count). The two middle nodes are at positions 2 and 3 with values 3 and 4. Print the second one: 4.",
         ]),

    # ---- LEC-6 : hashmap fundamentals --------------------------------------
    dict(title="Classwork: LC1 Two Sum",
         stmt="Given an array and a target, print the indices of the two numbers adding up to the target. Exactly one such pair exists.",
         inp=SIZED_ARR_IN + "\n\nA third line contains the target.",
         out="A single line: the two 0-based indices in increasing order, separated by "
             "a space.",
         cons="- `2 <= n <= 10^4`\n- exactly one valid pair exists",
         solve=lambda s: fmt(two_sum(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["2 7 11 15\n9", "3 2 4\n6", "3 3\n6", "1 2 3 4\n7",
                      "-1 -2 -3\n-5", "0 4 3 0\n0", "1 5 9\n10", "10 20 30\n50"]),
         explains=[
             "The target is 9. Numbers at index 0 and 1 are 2 and 7, and 2 + 7 = 9.",
             "The target is 6. Numbers at index 1 and 2 are 2 and 4, and 2 + 4 = 6.",
         ]),

    dict(title="Classwork: Frequency of elements (GfG)",
         stmt="Print how many times each distinct value appears, in increasing order of value.",
         inp=SIZED_ARR_IN,
         out="One line per distinct value: the value and its count, separated by a "
             "space, in increasing order of value.",
         cons="- `1 <= n <= 10^5`",
         solve=lambda s: freq_lines(ints(rows(s)[1])), cases=SIZED_ARR_SETS,
         explains=[
             "Every value (2, 7, 11, 15) appears exactly once. Print each with count 1, in increasing order.",
             "Every value (2, 3, 4) appears exactly once. Print each with count 1.",
         ]),

    dict(title="Classwork: LC217 Contains Duplicate",
         stmt="Decide whether any value appears more than once.",
         inp=SIZED_ARR_IN, out=BOOL_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt_bool(len(set(ints(rows(s)[1]))) != len(ints(rows(s)[1]))),
         cases=SIZED_ARR_SETS,
         explains=[
             "All 4 values are different. No duplicates.",
             "All 3 values are different. No duplicates.",
         ]),

    dict(title="Homework: LC387 First Unique Character in a String",
         stmt="Print the index of the first character that appears exactly once, or `-1` if there is none.",
         inp=STR_IN,
         out="A single line: the 0-based index, or `-1`.",
         cons="- `1 <= length <= 10^5`\n- lowercase English letters",
         solve=lambda s: str(first_uniq(s.strip())),
         cases=["leetcode", "loveleetcode", "aabb", "z",
                "abcabc", "aabbc", "abab", "cc"],
         explains=[
             "In 'leetcode', the letter 'l' appears once at index 0. It is the first character with count 1.",
             "In 'loveleetcode', the letter 'v' first appears at index 2 and appears only once. It is the first unique character.",
         ]),

    dict(title="Homework: LC242 Valid Anagram",
         stmt="Decide whether two strings are anagrams of each other.",
         inp="Two lines, one string each.",
         out=BOOL_OUT,
         cons="- `1 <= length <= 5 * 10^4`\n- lowercase English letters",
         solve=lambda s: fmt_bool(Counter(rows(s)[0].strip()) ==
                                  Counter(rows(s)[1].strip())),
         cases=["anagram\nnagaram", "rat\ncar", "a\na", "ab\nba",
                "aabb\nbbaa", "abc\nabcd", "listen\nsilent", "aa\nab"],
         explains=[
             "'anagram' and 'nagaram' have the same letters with the same counts. They are anagrams.",
             "'rat' has letters r, a, t while 'car' has c, a, r. Different letter sets, so not anagrams.",
         ]),

    dict(title="Homework: LC219 Contains Duplicate II",
         stmt="Decide whether the array contains two equal values whose indices differ by at most `k`.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=BOOL_OUT, cons="- `1 <= n <= 10^5`\n- `0 <= k <= 10^5`",
         solve=lambda s: fmt_bool(dup_within_k(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["1 2 3 1\n3", "1 0 1 1\n1", "1 2 3 1 2 3\n2", "1 2 3 4\n4",
                      "1 1\n0", "5 5\n1", "1 2 1\n1", "99 99\n2"]),
         explains=[
             "Value 1 is at index 0 and index 3. The distance is 3, which is at most k = 3. Answer: true.",
             "Value 1 is at index 0 and index 2, distance 2. Value 1 is at index 2 and 3, distance 1. Some pair is within k = 1. Answer: true.",
         ]),

    # ---- LEC-7 : subarrays & patterns --------------------------------------
    dict(title="Classwork: LC560 Subarray Sum Equals K",
         stmt="Print the number of contiguous subarrays summing to `k`.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=NUM_OUT, cons="- `1 <= n <= 2 * 10^4`\n- values may be negative",
         solve=lambda s: str(subarray_sum_k(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["1 1 1\n2", "1 2 3\n3", "1\n1", "1 -1 0\n0",
                      "3 4 7 2 -3 1 4 2\n7", "-1 -1 1\n0", "1 2 1 2 1\n3",
                      "0 0 0\n0"]),
         explains=[
             "The array is [1, 1, 1] and k = 2. Subarrays that sum to 2: [1, 1] at positions 0-1 and [1, 1] at positions 1-2. Count is 2.",
             "The array is [1, 2, 3] and k = 3. Subarrays that sum to 3: [3] at position 2, and [1, 2] at positions 0-1. Count is 2.",
         ]),

    dict(title="Classwork: LC49 Group Anagrams",
         stmt="Group words that are anagrams of one another.\n\nFor a deterministic answer, print each group with its words in lexicographic order, and order the groups by their first word.",
         inp=WORDS_IN,
         out="One line per group: the words in lexicographic order, space separated. "
             "Groups are ordered by their first word.",
         cons="- `1 <= n <= 10^4`\n- lowercase English letters",
         solve=lambda s: "\n".join(fmt(g) for g in
                                   group_anagrams(words(rows(s)[1]))),
         cases=["6\neat tea tan ate nat bat", "1\na", "2\nab ba",
                "3\nabc bca cab", "2\nabc def", "4\naa aa bb bb",
                "3\na b c", "5\nlisten silent enlist inlets google"],
         explains=[
             "'eat', 'tea', 'ate' share the same letters (one group). 'tan' and 'nat' share letters (another group). 'bat' is alone. Sorted inside each group and by the first word between groups.",
             "Only one word 'a'. That is one group with just 'a'.",
         ]),

    dict(title="Classwork: LC3 Longest Substring Without Repeating Characters",
         hr_id=591573,   # duplicate title in the account; 592134 is an orphan
         stmt="Print the length of the longest substring containing no repeated character.",
         inp=STR_IN, out=NUM_OUT,
         cons="- `0 <= length <= 5 * 10^4`",
         solve=lambda s: str(longest_unique(s.strip())),
         cases=["abcabcbb", "bbbbb", "pwwkew", "a", "au",
                "dvdf", "abba", "tmmzuxt"],
         explains=[
             "The longest substring without repeats is 'abc' — length 3.",
             "Only one distinct letter 'b'. The longest substring without repeats is a single 'b' — length 1.",
         ]),

    dict(title="Homework: LC974 Subarray Sums Divisible by K",
         stmt="Print the number of contiguous subarrays whose sum is divisible by `k`.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=NUM_OUT, cons="- `1 <= n <= 3 * 10^4`\n- `2 <= k <= 10^4`",
         solve=lambda s: str(subarray_div_k(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["4 5 0 -2 -3 1\n5", "5\n9", "1 2 3\n3", "-1 2 9\n2",
                      "0 0 0\n3", "2 -2 2 -4\n6", "1 1 1\n2", "7 7 7\n7"]),
         explains=[
             "Array [4, 5, 0, -2, -3, 1], k = 5. Seven subarrays have sums divisible by 5 (like [5], [5, 0], [0], and others).",
             "Array [5], k = 9. Only subarray is [5] with sum 5, not divisible by 9. Count is 0.",
         ]),

    dict(title="Homework: LC128 Longest Consecutive Sequence",
         stmt="Print the length of the longest run of consecutive integers present in the array. The values need not be adjacent in the input.",
         inp=SIZED_ARR_IN, out=NUM_OUT, cons="- `0 <= n <= 10^5`",
         solve=lambda s: str(longest_consecutive(ints(rows(s)[1]))),
         cases=sized(["100 4 200 1 3 2", "0 3 7 2 5 8 4 6 0 1", "1", "1 2 0 1",
                      "9 1 4 7 3 -1 0 5 8 -1 6", "5 5 5", "1 3 5 7", "-1 0 1"]),
         explains=[
             "Values 1, 2, 3, 4 are all present and form a run of 4 consecutive integers. Length is 4.",
             "Values 0 through 8 are all present. Longest consecutive run: 0, 1, 2, 3, 4, 5, 6, 7, 8 — length 9.",
         ]),

    dict(title="Homework: Largest subarray with 0 sum (GfG)",
         stmt="Print the length of the longest contiguous subarray summing to zero.",
         inp=SIZED_ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: str(largest_zero_sum(ints(rows(s)[1]))),
         cases=sized(["15 -2 2 -8 1 7 10 23", "1 2 3", "0", "1 -1",
                      "1 0 -1 2", "-1 1 -1 1", "3 -3 3 -3", "1 2 -3 3"]),
         explains=[
             "The subarray [-2, 2, -8, 1, 7] (indices 1 to 5) sums to 0. Its length 5 is the longest.",
             "Array [1, 2, 3]. No subarray sums to zero. Answer is 0.",
         ]),

    # ---- LEC-8 : heaps -----------------------------------------------------
    dict(title="Classwork: LC215 Kth Largest Element in an Array",
         stmt="Print the `k`-th largest element, counting duplicates as separate elements.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=NUM_OUT, cons="- `1 <= k <= n <= 10^5`",
         solve=lambda s: str(sorted(ints(rows(s)[1]), reverse=True)[int(rows(s)[2]) - 1]),
         cases=sized(["3 2 1 5 6 4\n2", "3 2 3 1 2 4 5 5 6\n4", "1\n1",
                      "5 5 5\n2", "-1 -2\n2", "7 6 5 4\n4", "1 2\n1",
                      "10 5 2 6 1 9\n3"]),
         explains=[
             "Sorted from largest: 6, 5, 4, 3, 2, 1. The 2nd largest is 5.",
             "Sorted from largest: 6, 5, 5, 4, 3, 3, 2, 2, 1. Counting duplicates, the 4th largest is 4.",
         ]),

    dict(title="Classwork: Kth smallest element (GfG)",
         stmt="Print the `k`-th smallest element of an array.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=NUM_OUT, cons="- `1 <= k <= n <= 10^5`",
         solve=lambda s: str(sorted(ints(rows(s)[1]))[int(rows(s)[2]) - 1]),
         cases=sized(["7 10 4 3 20 15\n3", "7 10 4 3 20 15\n4", "1\n1",
                      "5 5 5\n2", "-1 -2\n1", "1 2 3 4\n4", "9 8 7\n2",
                      "10 5 2 6 1 9\n5"]),
         explains=[
             "Sorted: 3, 4, 7, 10, 15, 20. The 3rd smallest is 7.",
             "Sorted: 3, 4, 7, 10, 15, 20. The 4th smallest is 10.",
         ]),

    dict(title="Classwork: LC1046 Last Stone Weight",
         stmt="Repeatedly smash the two heaviest stones together: equal weights destroy both, otherwise the difference remains. Print the weight of the last stone left, or `0` if none is.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 30`\n- `1 <= weight <= 1000`",
         solve=lambda s: str(last_stone(ints(rows(s)[1]))),
         cases=sized(["2 7 4 1 8 1", "1", "2 2", "1 3",
                      "10 4 2 10", "1 1 1", "5 5 5 5", "3 7 2"]),
         explains=[
             "Smash the two heaviest (8, 7) -> a stone of weight 1 remains. Continue smashing pairs. In the end one stone of weight 1 is left.",
             "Only one stone with weight 1. Nothing to smash, so the last stone weight is 1.",
         ]),

    dict(title="Homework: LC973 K Closest Points to Origin",
         stmt="Print the `k` points closest to the origin.\n\nFor a deterministic answer, order by distance, then by `x`, then by `y`.",
         inp="The first line contains `n` and `k`. Each of the next `n` lines contains "
             "a point's `x` and `y`.",
         out="One line per point: `x` and `y` separated by a space, ordered by distance "
             "then `x` then `y`.",
         cons="- `1 <= k <= n <= 10^4`",
         solve=lambda s: "\n".join(
             "%d %d" % (x, y) for x, y in
             k_closest([tuple(ints(r)) for r in rows(s)[1:1 + ints(rows(s)[0])[0]]],
                       ints(rows(s)[0])[1])),
         cases=["2 1\n1 3\n-2 2", "3 2\n3 3\n5 -1\n-2 4", "1 1\n0 0",
                "2 2\n1 1\n2 2", "3 1\n1 0\n0 1\n-1 0",
                "4 2\n1 1\n1 -1\n-1 1\n-1 -1", "2 1\n5 5\n1 1",
                "3 3\n0 1\n1 0\n2 2"],
         explains=[
             "Two points, keep 1 closest. Distances: (1, 3) is sqrt(10) away, (-2, 2) is sqrt(8) away. Closer is (-2, 2).",
             "Three points, keep 2 closest. Distances squared: (3, 3) -> 18, (5, -1) -> 26, (-2, 4) -> 20. Two closest are (3, 3) and (-2, 4).",
         ]),

    dict(title="Homework: Minimum cost of ropes (GfG)",
         stmt="Joining two ropes costs the sum of their lengths. Print the minimum total cost of joining every rope into one.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- lengths are positive",
         solve=lambda s: str(connect_ropes(ints(rows(s)[1]))),
         cases=sized(["4 3 2 6", "1 2 3 4 5", "5", "1 1",
                      "10 20 30", "1 2 3", "2 2 2 2", "4 2 7 6 9"]),
         explains=[
             "Ropes [4, 3, 2, 6]. Join 2 + 3 = 5 (cost 5). Then [4, 5, 6]: join 4 + 5 = 9 (cost 9). Then [6, 9]: join 6 + 9 = 15 (cost 15). Total: 5 + 9 + 15 = 29.",
             "Ropes [1, 2, 3, 4, 5]. Join 1 + 2 = 3, then 3 + 3 = 6, then 4 + 5 = 9, then 6 + 9 = 15. Total: 3 + 6 + 9 + 15 = 33.",
         ]),

    # ---- LEC-9 : advanced heaps --------------------------------------------
    dict(title="Classwork: LC347 Top K Frequent Elements",
         stmt="Print the `k` most frequent values.\n\nFor a deterministic answer, order by frequency descending, breaking ties by the smaller value first.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out=SEQ_OUT, cons="- `1 <= n <= 10^5`\n- `1 <= k <= distinct values`",
         solve=lambda s: fmt(top_k_frequent(ints(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["1 1 1 2 2 3\n2", "1\n1", "1 2\n2", "4 4 4 5 5 6\n1",
                      "1 1 2 2 3 3\n3", "5 5 5\n1", "-1 -1 2\n1",
                      "1 2 3 4\n4"]),
         explains=[
             "1 appears 3 times, 2 appears 2 times, 3 appears once. The top 2 most frequent values are 1 and 2.",
             "Only one value 1. It is the top 1 most frequent.",
         ]),

    dict(title="Classwork: LC23 Merge k Sorted Lists",
         stmt="Given `k` sorted lists, merge them into one sorted list and print it.",
         inp="The first line contains `k`. Each of the next `k` lines contains one "
             "sorted list, space separated. A list may be empty.",
         out=SEQ_OUT, cons="- `0 <= k <= 10^4`\n- each list is sorted increasing",
         solve=lambda s: fmt(sorted(
             x for r in rows(s)[1:1 + int(rows(s)[0])] for x in ints(r))),
         cases=["3\n1 4 5\n1 3 4\n2 6", "1\n1", "2\n1 2\n3 4",
                "2\n5\n1", "3\n1\n2\n3", "2\n-3 -1\n-2 0",
                "2\n1 1\n1 1", "4\n1 5\n2 6\n3 7\n4 8"],
         explains=[
             "Three sorted lists: [1, 4, 5], [1, 3, 4], [2, 6]. Merged in sorted order: 1, 1, 2, 3, 4, 4, 5, 6.",
             "Only one list [1]. The merged result is just 1.",
         ]),

    dict(title="Homework: LC378 Kth Smallest Element in a Sorted Matrix",
         stmt="Each row and each column of an `n` by `n` matrix is sorted increasing. Print the `k`-th smallest value overall.",
         inp="The first line contains `n` and `k`. Each of the next `n` lines contains "
             "one row of the matrix.",
         out=NUM_OUT, cons="- `1 <= n <= 300`\n- `1 <= k <= n * n`",
         solve=lambda s: str(sorted(
             x for r in rows(s)[1:1 + ints(rows(s)[0])[0]] for x in ints(r)
         )[ints(rows(s)[0])[1] - 1]),
         cases=["3 8\n1 5 9\n10 11 13\n12 13 15", "1 1\n5",
                "2 2\n1 2\n3 4", "2 4\n1 2\n3 4",
                "3 1\n1 2 3\n4 5 6\n7 8 9", "2 3\n1 1\n1 1",
                "3 5\n1 3 5\n6 7 12\n11 14 14", "2 1\n-5 -4\n-3 -2"],
         explains=[
             "All matrix values sorted: 1, 5, 9, 10, 11, 12, 13, 13, 15. The 8th smallest is 13.",
             "1x1 matrix with the single value 5. The 1st smallest is 5.",
         ]),

    dict(title="Homework: LC692 Top K Frequent Words",
         stmt="Print the `k` most frequent words. Words with equal frequency are ordered lexicographically.",
         inp=WORDS_IN + "\n\nA third line contains `k`.",
         out="A single line: the words, space separated.",
         cons="- `1 <= n <= 10^4`\n- lowercase English letters",
         solve=lambda s: fmt(top_k_words(words(rows(s)[1]), int(rows(s)[2]))),
         cases=["6\ni love leetcode i love coding\n2",
                "9\nthe day is sunny the the the sunny is\n4",
                "1\na\n1", "2\nb a\n2", "3\na a b\n1",
                "4\nz y x w\n2", "5\naa aa bb bb cc\n2",
                "3\nsame same same\n1"],
         explains=[
             "'i' 2 times, 'love' 2, 'leetcode' 1, 'coding' 1. Top 2 by count: 'i' and 'love' tie at 2. Alphabetical tie-break: 'i' first, then 'love'.",
             "'the' 4 times, 'is' 2, 'sunny' 2, 'day' 1. Top 4 by count: 'the' first. 'is' and 'sunny' tie at 2, alphabetical order 'is' before 'sunny'. Then 'day'.",
         ]),

    dict(title="Homework: LC451 Sort Characters By Frequency",
         stmt="Rearrange a string so its characters appear in order of decreasing frequency, with all copies of a character together.\n\nFor a deterministic answer, break ties by the smaller character first.",
         inp=STR_IN,
         out="A single line: the rearranged string.",
         cons="- `1 <= length <= 5 * 10^5`\n- lowercase English letters",
         solve=lambda s: sort_by_freq(s.strip()),
         cases=["tree", "cccaaa", "abb", "a", "aabbcc",
                "abcabcaa", "zzyyx", "mississippi"],
         explains=[
             "In 'tree': 'e' appears 2 times, 'r' 1, 't' 1. Sorted by count descending, tie-broken by the smaller character first: 'e' (count 2), then 'r' (count 1), then 't'. Repeat each: 'ee' + 'r' + 't' = 'eert'.",
             "In 'cccaaa': 'a' 3, 'c' 3. Same count — smaller 'a' first, then 'c'. Result: 'aaaccc'.",
         ]),

    # ---- LEC-10 : hashmaps & heaps combined --------------------------------
    dict(title="Homework: LC621 Task Scheduler",
         stmt="Identical tasks must be separated by at least `n` intervals of cooldown; different tasks may run back to back, and the CPU may idle. Print the minimum number of intervals to finish everything.",
         inp="The first line contains `m`, the number of tasks. The second line "
             "contains the `m` task letters, space separated. The third line "
             "contains `n`, the cooldown.",
         out=NUM_OUT,
         cons="- `1 <= m <= 10^4`\n- `0 <= n <= 100`",
         solve=lambda s: str(task_scheduler(words(rows(s)[1]), int(rows(s)[2]))),
         cases=sized(["A A A B B B\n2", "A A A B B B\n0",
                      "A A A A B C D E F G\n2",
                      "A\n0", "A A\n1", "A B C\n2", "A A B\n2", "A A A B\n3"]),
         explains=[
             "Tasks A A A B B B with cooldown 2. A schedule: A B _ A B _ A B (8 slots, one idle).",
             "Cooldown 0 means tasks can run back to back. All 6 tasks take 6 intervals.",
         ]),

    # ---- Remaining classwork entries -- one per uncovered contest row ------
    dict(title="Classwork: Sum of First N Natural Numbers",
         stmt="Print the sum of the first `N` natural numbers, i.e. "
              "`1 + 2 + 3 + ... + N`.",
         inp="A single line containing the integer `N`.",
         out=NUM_OUT,
         cons="- `0 <= N <= 10^6`",
         solve=lambda s: str(int(s) * (int(s) + 1) // 2),
         cases=["5", "1", "0", "10", "100", "20", "50", "1000"],
         explains=[
             "Sum of 1 + 2 + 3 + 4 + 5 = 15.",
             "N is 1. The only number to add is 1. The sum is 1.",
         ]),

    dict(title="Classwork: Character Frequency",
         stmt="Print how many times each distinct character appears in a string. "
              "Print one line per distinct character, sorted in ascending ASCII order "
              "of the character.",
         inp=STR_IN,
         out="One line per distinct character: the character and its count separated "
             "by a space, in ascending order of the character.",
         cons="- `1 <= length <= 10^5`\n- lowercase English letters",
         solve=lambda s: "\n".join(
             "%s %d" % (ch, cnt) for ch, cnt in
             sorted(Counter(s.strip()).items())),
         cases=["hello", "banana", "aabbcc", "z",
                "abcabc", "programming", "level", "mississippi"],
         explains=[
             "'e' 1, 'h' 1, 'l' 2, 'o' 1. Printed in alphabetical order.",
             "'a' 3, 'b' 1, 'n' 2. Printed in alphabetical order.",
         ]),

    dict(title="Classwork: LC1207 Unique Number of Occurrences",
         stmt="Given an array of integers, decide whether the number of occurrences "
              "of every value is **unique** across the array. Two different values "
              "may not share the same occurrence count.",
         inp=SIZED_ARR_IN,
         out=BOOL_OUT,
         cons="- `1 <= n <= 1000`\n- `-1000 <= value <= 1000`",
         solve=lambda s: fmt_bool(
             len(set(Counter(ints(rows(s)[1])).values())) ==
             len(Counter(ints(rows(s)[1])))),
         cases=sized(["1 2 2 1 1 3", "1 2", "-3 0 1 -3 1 1 1 -3 10 0",
                      "1", "1 1 2 2 3 3", "5 5 5 4 4 3", "7 7 7 7",
                      "1 2 3 4 5"]),
         explains=[
             "1 appears 3 times, 2 appears 2 times, 3 appears 1 time. The counts 3, 2, 1 are all different. Answer: true.",
             "1 appears 1 time and 2 appears 1 time. Both have the same count of 1, so they are not unique. Answer: false.",
         ]),

    dict(title="Classwork: Three Smallest Elements",
         stmt="Print the three smallest elements of an array in **ascending** order.",
         inp=SIZED_ARR_IN,
         out="A single line with the three smallest elements, space separated, in "
             "ascending order.",
         cons="- `3 <= n <= 10^5`",
         solve=lambda s: fmt(sorted(ints(rows(s)[1]))[:3]),
         cases=sized(["7 2 9 1 5 3", "10 20 30", "5 5 5 5 5",
                      "9 8 7 6 5 4 3 2 1", "-1 -2 -3 -4",
                      "100 1 50 2 25 3", "0 0 0 1 1 1",
                      "4 4 3 3 2 2 1 1"]),
         explains=[
             "Sorted: 1, 2, 3, 5, 7, 9. The three smallest are 1, 2, 3.",
             "Only three numbers, so all three are the smallest: 10, 20, 30.",
         ]),

    dict(title="Classwork: LC506 Relative Ranks",
         stmt="You are given the finishing scores of `n` athletes, all distinct. "
              "Print each athlete's placement in the **input order**:\n"
              "\n"
              "- the top score is `Gold Medal`\n"
              "- the second-best is `Silver Medal`\n"
              "- the third-best is `Bronze Medal`\n"
              "- every remaining athlete gets their placement as a plain integer "
              "(4th place prints `4`, and so on)",
         inp=SIZED_ARR_IN,
         out="One line per athlete, in the same order as the input: their placement "
             "label (`Gold Medal` / `Silver Medal` / `Bronze Medal`) or their "
             "numeric placement.",
         cons="- `1 <= n <= 10^4`\n- scores are distinct",
         solve=lambda s: relative_ranks(ints(rows(s)[1])),
         cases=sized(["5 4 3 2 1", "10 3 8 9 4", "50", "100 200",
                      "1 2 3", "5 4 3 2", "9 8 7 6 5 4 3 2 1",
                      "1 10 100 1000 10000"]),
         explains=[
             "Scores from highest: 5 (1st), 4 (2nd), 3 (3rd), 2 (4th), 1 (5th). Print each athlete's place in input order.",
             "Highest score is 10 (Gold). Next is 9 (Silver). Then 8 (Bronze). Then 4 (4th), then 3 (5th). Printed in the original input order.",
         ]),

    dict(title="Classwork: LC1636 Sort Array by Increasing Frequency",
         stmt="Sort the array in **increasing** order of the frequency with which each "
              "value appears. If two values appear the same number of times, print "
              "the one with the **larger** value first. Every occurrence of each "
              "value stays together in the output.",
         inp=SIZED_ARR_IN,
         out=SEQ_OUT,
         cons="- `1 <= n <= 100`\n- `-100 <= value <= 100`",
         solve=lambda s: fmt(sort_by_freq_then_desc(ints(rows(s)[1]))),
         cases=sized(["1 1 2 2 2 3", "2 3 1 3 2", "-1 1 -6 4 5 -6 1 4 1",
                      "5", "1 2 3", "4 4 4 3 3 2 2 2 1",
                      "10 20 20 10 30 30", "1 1 1 2 2 3"]),
         explains=[
             "Frequencies: 1 -> 2, 2 -> 3, 3 -> 1. Sorted by frequency ascending: 3 first (freq 1), then 1 (freq 2), then 2 (freq 3). Each value is repeated its frequency times.",
             "Frequencies: 1 -> 1, 2 -> 2, 3 -> 2. By frequency ascending: 1 (freq 1) first. Then 2 and 3 tie at freq 2 — larger value 3 comes first, then 2.",
         ]),

    dict(title="Classwork: LC767 Reorganize String",
         hr_id=591015,   # duplicate title in the account; 591590 is an orphan
         stmt="Rearrange the characters of a string so that no two adjacent "
              "characters are the same, and print the **lexicographically "
              "smallest** such rearrangement. If no valid rearrangement exists, "
              "print the single word `impossible`.",
         inp=STR_IN,
         out="A single line: the rearranged string, or `impossible`.",
         cons="- `1 <= length <= 500`\n- lowercase English letters",
         solve=lambda s: reorganize_string(s.strip()),
         cases=["aab", "aaab", "aabb", "aaaabc",
                "vvvlo", "baaba", "z", "aabbcc"],
         explains=[
             "Rearrange 'aab' so no two same letters are next to each other: 'aba'. This is the smallest valid arrangement.",
             "'a' appears 3 times in 4 characters. No matter how we arrange them, two a's must touch. So no valid rearrangement exists.",
         ]),

    dict(title="Classwork: LC295 Find Median from Data Stream",
         stmt="Simulate a data stream and answer running-median queries.\n"
              "\n"
              "Two operations are supported:\n"
              "\n"
              "- `add <num>` -- insert the integer `<num>` into the stream.\n"
              "- `median` -- print the current median of every value inserted so "
              "far. When the number of inserted values is even, the median is the "
              "average of the two middle values.\n"
              "\n"
              "Print median values with exactly **five** digits after the decimal "
              "point (e.g. `3.50000`, `4.00000`).",
         inp="The first line contains the integer `q`, the number of operations. "
             "Each of the next `q` lines contains one operation exactly as described "
             "above.",
         out="One line for every `median` operation, in order: the current median "
             "with 5 digits after the decimal point.",
         cons="- `1 <= q <= 5 * 10^4`\n"
              "- at least one `median` follows the first `add`\n"
              "- `-10^5 <= num <= 10^5`",
         solve=lambda s: median_stream(rows(s)),
         cases=[
             "6\nadd 1\nadd 2\nmedian\nadd 3\nmedian\nadd 4",
             "5\nadd 10\nmedian\nadd 20\nadd 30\nmedian",
             "3\nadd 5\nmedian\nmedian",
             "4\nadd -5\nadd 5\nmedian\nmedian",
             "7\nadd 1\nadd 2\nadd 3\nadd 4\nadd 5\nmedian\nmedian",
             "6\nadd 3\nadd 1\nadd 4\nadd 1\nadd 5\nmedian",
             "5\nadd 100\nadd 200\nmedian\nadd 300\nmedian",
             "4\nadd 0\nmedian\nadd 0\nmedian",
         ],
         explains=[
             "Add 1 and 2. Values so far: 1, 2. Median (of even count) is (1+2)/2 = 1.50000. Add 3. Values: 1, 2, 3. Median is the middle value 2.00000.",
             "Add 10. Only value is 10. Median is 10. Add 20 and 30. Values: 10, 20, 30. Median is the middle value 20.",
         ]),

    dict(title="Classwork: LC355 Design Twitter",
         stmt="Simulate a tiny social network with four operations:\n"
              "\n"
              "- `post <user_id> <tweet_id>` -- user posts a tweet. Tweets have "
              "increasing recency in the order they are posted.\n"
              "- `follow <follower_id> <followee_id>` -- follower starts following "
              "followee.\n"
              "- `unfollow <follower_id> <followee_id>` -- follower stops following "
              "followee. A no-op if they were not following.\n"
              "- `feed <user_id>` -- print the ids of the **10 most recent** tweets "
              "posted by the user or by anyone they follow, most recent first. "
              "Print an empty line if there are none.",
         inp="The first line contains the integer `q`, the number of operations. "
             "Each of the next `q` lines contains one operation as described above.",
         out="One line for every `feed` operation, in order: the tweet ids separated "
             "by single spaces, most recent first. An empty feed prints an empty "
             "line.",
         cons="- `1 <= q <= 3 * 10^4`\n"
              "- user ids and tweet ids are positive integers",
         solve=lambda s: design_twitter(rows(s)),
         cases=[
             "7\npost 1 5\nfeed 1\nfollow 1 2\npost 2 6\nfeed 1\nunfollow 1 2\nfeed 1",
             "3\npost 1 10\npost 1 20\nfeed 1",
             "2\nfeed 42\npost 42 1",
             "4\npost 1 1\npost 2 2\nfollow 1 2\nfeed 1",
             "5\npost 1 1\npost 1 2\npost 1 3\npost 1 4\nfeed 1",
             "6\nfollow 1 2\nfollow 1 3\npost 2 20\npost 3 30\nfeed 1\nunfollow 1 2",
             "4\npost 5 100\nfeed 5\nunfollow 5 6\nfeed 5",
             "5\npost 1 1\nfollow 1 1\nfeed 1\nunfollow 1 1\nfeed 1",
         ],
         explains=[
             "User 1 posts tweet 5. Feed shows [5]. User 1 follows user 2. User 2 posts tweet 6. Feed shows [6, 5] (most recent first). User 1 unfollows user 2. Feed shows only user 1's tweets: [5].",
             "User 1 posts tweets 10, then 20. Feed shows both in most-recent-first order: 20 10.",
         ]),

    dict(title="Classwork: LC895 Maximum Frequency Stack",
         stmt="Simulate a specialised stack that always pops the value with the "
              "**highest current frequency**. Ties are broken by picking the value "
              "that was **most recently pushed**. Two operations are supported:\n"
              "\n"
              "- `push <val>` -- push `<val>` onto the stack.\n"
              "- `pop` -- remove and print the value defined above.",
         inp="The first line contains the integer `q`, the number of operations. "
             "Each of the next `q` lines contains one operation as described above.",
         out="One line for every `pop` operation, in order: the value popped.",
         cons="- `1 <= q <= 2 * 10^4`\n"
              "- every `pop` follows at least one `push`",
         solve=lambda s: freq_stack(rows(s)),
         cases=[
             "10\npush 5\npush 7\npush 5\npush 7\npush 4\npush 5\npop\npop\npop\npop",
             "3\npush 1\npush 1\npop",
             "4\npush 9\npush 9\npop\npop",
             "6\npush 1\npush 2\npush 3\npop\npop\npop",
             "5\npush 4\npush 4\npush 4\npop\npop",
             "6\npush 7\npush 7\npush 8\npush 8\npop\npop",
             "4\npush 1\npop\npush 2\npop",
             "8\npush 3\npush 3\npush 5\npush 5\npush 3\npop\npop\npop",
         ],
         explains=[
             "After all pushes: 5 has count 3, 7 has count 2, 4 has count 1. Pop 1: highest count is 5 -> pop 5. Pop 2: 5 and 7 tie at count 2, but 7 was pushed more recently -> pop 7. Pop 3: 5 has count 2 (highest) -> pop 5. Pop 4: 5, 7, 4 all at count 1, and 4 was pushed most recently among them -> pop 4.",
             "Push 1 twice. Pop: value 1 has count 2 (highest) -> pop 1.",
         ]),

    # ---- Remaining homework entries ---------------------------------------

    # LEC-1 lambdas -----------------------------------------------------
    dict(title="Homework: Print Vector Elements",
         stmt="Print every element of an integer array on a single line, "
              "separated by single spaces.",
         inp=SIZED_ARR_IN, out=SEQ_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt(ints(rows(s)[1])),
         cases=SIZED_ARR_SETS,
         explains=[
             "Print the four values in the same order: 2 7 11 15.",
             "Print the three values in the same order: 3 2 4.",
         ]),

    dict(title="Sum of vector using for_each",
         stmt="Print the sum of an integer array.",
         inp=SIZED_ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: str(sum(ints(rows(s)[1]))),
         cases=SIZED_ARR_SETS,
         explains=[
             "Add all values: 2 + 7 + 11 + 15 = 35.",
             "Add all values: 3 + 2 + 4 = 9.",
         ]),

    dict(title="Store and Apply Lambdas using function",
         stmt="Given an integer `x`, apply three fixed functions to it and "
              "print each result on its own line, in this order:\n"
              "\n"
              "1. **double**: `2 * x`\n"
              "2. **square**: `x * x`\n"
              "3. **negate**: `-x`",
         inp="A single line with the integer `x`.",
         out="Three lines: `2 * x`, `x * x`, `-x`.",
         cons="- `-10^4 <= x <= 10^4`",
         solve=lambda s: "%d\n%d\n%d" % (2 * int(s), int(s) ** 2, -int(s)),
         cases=["5", "0", "-3", "10", "7", "-1", "2", "100"],
         explains=[
             "For x = 5: double is 10, square is 25, negate is -5.",
             "For x = 0: all three results are 0.",
         ]),

    dict(title="Filter a Vector Capturing Threshold by Value",
         stmt="Print all elements of an integer array that are **strictly "
              "greater than** a threshold, preserving their input order.",
         inp=SIZED_ARR_IN + "\n\nA third line contains the threshold `t`.",
         out=SEQ_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt(
             x for x in ints(rows(s)[1]) if x > int(rows(s)[2]))
             or "",                                  # empty line for no matches
         cases=sized(["1 5 2 8 3\n3", "5 5 5\n5", "10 20 30\n0",
                      "1 2 3\n5", "1\n0", "-3 -1 0 4\n0",
                      "7 6 5 4 3 2 1\n4", "100 200 300\n150"]),
         explains=[
             "Threshold is 3. Values strictly greater than 3, in original order: 5 and 8.",
             "Threshold is 5. No value is strictly greater than 5. The output is empty.",
         ]),

    # LEC-2 lambdas -----------------------------------------------------
    dict(title="Homework: Sort Strings in Reverse Alphabetical Order",
         stmt="Print a list of strings sorted in **reverse alphabetical** "
              "(lexicographically decreasing) order.",
         inp="The first line contains an integer `n`. The second line contains "
             "`n` space-separated strings.",
         out="A single line: the strings in decreasing lexicographic order, "
             "separated by single spaces.",
         cons="- `1 <= n <= 10^4`\n- lowercase English letters",
         solve=lambda s: " ".join(sorted(words(rows(s)[1]), reverse=True)),
         cases=["3\napple banana cherry", "1\nonly",
                "4\ndog cat fish bird", "2\naa ab",
                "5\nz y x w v", "3\nsame same same",
                "4\nab abc abcd a", "6\nred green blue red green blue"],
         explains=[
             "Sorted in reverse alphabetical order: cherry, banana, apple.",
             "Only one string 'only', so the output is the same.",
         ]),

    dict(title="Homework: Print unordered_map entries sorted by count using a lambda",
         stmt="Given a list of words, for each distinct word print its count "
              "on its own line. Print the entries in order of **decreasing "
              "count**; break ties by ascending lexicographic order of the "
              "word.",
         inp="The first line contains `n`. The second line contains `n` "
             "space-separated words.",
         out="One line per distinct word: the word and its count separated by "
             "a space.",
         cons="- `1 <= n <= 10^5`\n- lowercase English letters",
         solve=lambda s: print_umap_by_count(words(rows(s)[1])),
         cases=["6\napple banana apple cherry banana apple",
                "3\ndog cat dog", "1\nhello", "4\na a a a",
                "5\nz y x w z", "6\nred blue red blue red blue",
                "2\none two", "5\ncat dog fish cat fish"],
         explains=[
             "apple appears 3 times, banana 2, cherry 1. Sorted by count from high to low: apple, banana, cherry.",
             "dog appears 2 times, cat 1. Higher count first: dog, then cat.",
         ]),

    dict(title="Homework: Sort strings by length then lexicographically with one lambda",
         stmt="Sort a list of strings by **length ascending**; break ties by "
              "ascending lexicographic order.",
         inp="The first line contains `n`. The second line contains `n` "
             "space-separated strings.",
         out="A single line: the strings in the required order, separated by "
             "single spaces.",
         cons="- `1 <= n <= 10^4`\n- lowercase English letters",
         solve=lambda s: " ".join(sort_strings_by_length_then_lex(
             words(rows(s)[1]))),
         cases=["4\nbanana kiwi apple fig",
                "3\ncat bat ant", "1\nsolo",
                "5\na bb ccc dddd eeeee",
                "5\neeeee dddd ccc bb a",
                "4\nabc acb bac cab",
                "2\naaaa bbbb", "6\nz y x aa bb cc"],
         explains=[
             "By length ascending: fig (3), kiwi (4), apple (5), banana (6).",
             "All three strings have length 3. Sorted alphabetically: ant, bat, cat.",
         ]),

    dict(title="Homework: Write a function that returns a lambda multiplying by a captured factor",
         stmt="Given a factor `f` and an integer array, print the array with "
              "every element multiplied by `f`, in the same order.",
         inp="The first line contains the factor `f`. " + SIZED_ARR_IN,
         out=SEQ_OUT,
         cons="- `1 <= n <= 10^5`\n- `-10^4 <= f, value <= 10^4`",
         solve=lambda s: fmt(int(rows(s)[0]) * x for x in ints(rows(s)[2])),
         cases=["3\n4\n1 2 3 4",
                "2\n3\n5 6 7",
                "-1\n3\n1 2 3",
                "0\n5\n1 2 3 4 5",
                "10\n1\n7",
                "5\n3\n-1 -2 -3",
                "1\n4\n100 200 300 400",
                "-2\n4\n2 4 6 8"],
         explains=[
             "Factor is 3. Multiply each element by 3: 1x3=3, 2x3=6, 3x3=9, 4x3=12.",
             "Factor is 2. 5x2=10, 6x2=12, 7x2=14.",
         ]),

    # LEC-3 --------------------------------------------------------------
    dict(title="Homework: Sorted Key-Value Pairs",
         stmt="Given `n` key-value pairs, print them sorted by key in "
              "**ascending** order. Keys are integers and are guaranteed "
              "distinct.",
         inp="The first line contains `n`. Each of the next `n` lines "
             "contains one pair: the key and the value separated by a space.",
         out="One pair per line: the key and its value separated by a space, "
             "in ascending order of key.",
         cons="- `1 <= n <= 10^4`",
         solve=lambda s: "\n".join(
             "%d %d" % kv for kv in sorted(
                 tuple(ints(r)) for r in rows(s)[1:1 + int(rows(s)[0])])),
         cases=["3\n5 100\n1 200\n3 300",
                "1\n7 7",
                "4\n10 1\n20 2\n30 3\n40 4",
                "4\n40 4\n30 3\n20 2\n10 1",
                "2\n-5 5\n5 -5",
                "5\n2 20\n4 40\n1 10\n5 50\n3 30",
                "3\n100 1\n50 2\n25 3",
                "2\n1 999\n2 888"],
         explains=[
             "Sort pairs by key: 1 comes first (value 200), then 3 (value 300), then 5 (value 100).",
             "Only one pair (7, 7). Output is the same.",
         ]),

    dict(title="Homework: Maintain a sorted stream with a multiset and query the smallest",
         stmt="Simulate a multiset that supports three operations:\n"
              "\n"
              "- `insert <x>` -- insert the integer `<x>`. Duplicates are "
              "allowed.\n"
              "- `remove <x>` -- remove a single occurrence of `<x>`. Does "
              "nothing if `<x>` is not present.\n"
              "- `smallest` -- print the current smallest value in the "
              "multiset.\n"
              "\n"
              "It is guaranteed that every `smallest` query is issued when at "
              "least one element is present.",
         inp="The first line contains `q`, the number of operations. Each of "
             "the next `q` lines contains one operation as described above.",
         out="One line per `smallest` operation, in order: the current smallest "
             "value.",
         cons="- `1 <= q <= 5 * 10^4`\n- `-10^5 <= x <= 10^5`",
         solve=lambda s: sorted_stream(rows(s)),
         cases=[
             "5\ninsert 3\ninsert 1\ninsert 2\nsmallest\nremove 1",
             "6\ninsert 5\nsmallest\ninsert 2\nsmallest\ninsert 4\nsmallest",
             "3\ninsert 7\nsmallest\nsmallest",
             "5\ninsert 4\ninsert 4\nsmallest\nremove 4\nsmallest",
             "6\ninsert 10\ninsert 20\nremove 10\ninsert 5\nsmallest\nremove 5",
             "4\ninsert -3\ninsert 0\ninsert 3\nsmallest",
             "5\ninsert 1\ninsert 2\nremove 3\nsmallest\nsmallest",
             "3\ninsert 9\ninsert 9\nsmallest",
         ],
         explains=[
             "After inserting 3, 1, 2 the multiset is {1, 2, 3}. Smallest is 1. Then 1 is removed (no query follows).",
             "Insert 5: smallest is 5. Insert 2: smallest is 2. Insert 4: smallest is still 2.",
         ]),

    dict(title="Homework: Compute a fixed-size sliding-window maximum using a deque",
         stmt="Given an integer array and a window size `k`, print the maximum "
              "value over every contiguous window of size `k`, in left-to-right "
              "order. There are exactly `n - k + 1` such windows.",
         inp=SIZED_ARR_IN + "\n\nA third line contains `k`.",
         out="A single line: the maximum of each window, space separated.",
         cons="- `1 <= k <= n <= 10^5`",
         solve=lambda s: fmt(sliding_window_max(ints(rows(s)[1]),
                                                int(rows(s)[2]))),
         cases=sized(["1 3 -1 -3 5 3 6 7\n3",
                      "1\n1",
                      "9 8 7 6 5 4 3 2 1\n3",
                      "1 2 3 4 5\n1",
                      "5 4 3 2 1\n5",
                      "4 4 4 4 4\n2",
                      "-1 -2 -3 -4\n2",
                      "10 5 2 6 1 9\n4"]),
         explains=[
             "Windows of size 3: [1, 3, -1] -> 3, [3, -1, -3] -> 3, [-1, -3, 5] -> 5, [-3, 5, 3] -> 5, [5, 3, 6] -> 6, [3, 6, 7] -> 7.",
             "Only one window of size 1 containing the value 1. Maximum is 1.",
         ]),

    # LEC-4 --------------------------------------------------------------
    dict(title="Homework: Sort Records by Score",
         stmt="You are given `n` records, each with a name and an integer "
              "score. Print the records sorted in **descending** order of "
              "score; break ties by the name in ascending lexicographic order.",
         inp="The first line contains `n`. Each of the next `n` lines contains "
             "one record: the name (no spaces) and the score separated by a "
             "space.",
         out="One record per line: the name and the score separated by a "
             "space, in the required order.",
         cons="- `1 <= n <= 10^4`",
         solve=lambda s: "\n".join(
             "%s %d" % (name, score) for name, score in
             sorted(((r.split()[0], int(r.split()[1]))
                     for r in rows(s)[1:1 + int(rows(s)[0])]),
                    key=lambda x: (-x[1], x[0]))),
         cases=["3\nalice 80\nbob 90\ncarol 80",
                "1\nsolo 100",
                "4\nzoe 50\naaron 50\nmike 70\nnina 60",
                "2\na 1\nb 2",
                "5\ne 5\nd 4\nc 3\nb 2\na 1",
                "3\nx 100\ny 100\nz 100",
                "4\np 10\nq 20\nr 30\ns 40",
                "3\nk1 -5\nk2 -10\nk3 0"],
         explains=[
             "Sort by score descending: bob (90) is highest. Then alice and carol tie at 80. Alphabetical tie-break: alice, then carol.",
             "Only one record.",
         ]),

    # LEC-5 --------------------------------------------------------------
    dict(title="Homework: Contains Value",
         stmt="Given the values of a singly linked list and a target integer, "
              "decide whether the target appears in the list.",
         inp=SIZED_ARR_IN.replace("integers", "list values") +
             "\n\nA third line contains the target.",
         out=BOOL_OUT, cons="- `0 <= n <= 10^5`",
         solve=lambda s: fmt_bool(
             int(rows(s)[2]) in ints(rows(s)[1])),
         cases=sized(["1 2 3 4 5\n3",
                      "1 2 3\n7",
                      "5\n5",
                      "5\n6",
                      "1 1 1 1\n1",
                      "-3 -2 -1\n-2",
                      "10 20 30 40\n25",
                      "7 7 7 7 7\n7"]),
         explains=[
             "The list is 1, 2, 3, 4, 5. Target 3 is in the list. Answer: true.",
             "The list is 1, 2, 3. Target 7 is not in the list. Answer: false.",
         ]),

    # LEC-6 --------------------------------------------------------------
    dict(title="Homework: LC136 Single Number",
         stmt="Every element in the array appears exactly twice except for "
              "one, which appears exactly once. Print the value that appears "
              "only once.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 3 * 10^4`\n- `n` is odd\n"
              "- exactly one value appears once; every other value appears "
              "twice",
         solve=lambda s: str(single_number(ints(rows(s)[1]))),
         cases=sized(["2 2 1", "4 1 2 1 2", "1", "7 3 7 3 5",
                      "-1 -1 9", "6 6 8", "10 20 10 30 20 30 40",
                      "0 1 0 1 2"]),
         explains=[
             "2 appears twice, 1 appears once. The single number is 1.",
             "1 and 2 each appear twice, 4 appears once. The single number is 4.",
         ]),

    # LEC-7 --------------------------------------------------------------
    dict(title="Homework: LC1512 Number of Good Pairs",
         stmt="A pair `(i, j)` is **good** when `i < j` and the two values at "
              "those positions are equal. Print the number of good pairs in "
              "the array.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 100`\n- `1 <= value <= 100`",
         solve=lambda s: str(good_pairs(ints(rows(s)[1]))),
         cases=sized(["1 2 3 1 1 3", "1 1 1 1", "1 2 3",
                      "1", "7 7", "5 5 5 5 5",
                      "1 2 1 2 1 2", "10 20 30 10 20 30"]),
         explains=[
             "1 appears 3 times, giving 3 good pairs. 3 appears 2 times, giving 1 good pair. Total: 3 + 1 = 4.",
             "1 appears 4 times. Number of pairs = 4 x 3 / 2 = 6.",
         ]),

    # LEC-8 --------------------------------------------------------------
    dict(title="Homework: LC1464 Maximum Product of Two Elements in an Array",
         stmt="Choose two distinct indices `i` and `j` and print the maximum "
              "possible value of `(a[i] - 1) * (a[j] - 1)`.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `2 <= n <= 500`\n- `1 <= a[i] <= 10^3`",
         solve=lambda s: str(max_product_two_minus_one(ints(rows(s)[1]))),
         cases=sized(["3 4 5 2", "1 5 4 5", "3 7", "1 1",
                      "10 2 5 20", "100 1", "5 5 5 5",
                      "9 8 7 6 5 4 3 2 1"]),
         explains=[
             "Two largest values are 5 and 4. Product = (5-1) x (4-1) = 4 x 3 = 12.",
             "Two largest values are 5 and 5 (both). Product = (5-1) x (5-1) = 4 x 4 = 16.",
         ]),

    dict(title="Homework: LC703 Kth Largest Element in a Stream",
         stmt="Simulate a running stream that always answers *what is the "
              "`k`-th largest value seen so far?*. Two inputs and one "
              "operation:\n"
              "\n"
              "- Initial `k` and an initial array of values (possibly empty) "
              "are given.\n"
              "- Then `q` operations `add <val>` follow. After each `add`, "
              "print the current `k`-th largest value. If fewer than `k` "
              "values have been seen so far, print `-` instead.",
         inp="The first line contains `k`. "
             "The second line contains `n0`, the size of the initial array. "
             "The third line contains the initial `n0` values, space "
             "separated (empty when `n0 = 0`). "
             "The fourth line contains `q`. Each of the next `q` lines "
             "contains one operation `add <val>`.",
         out="One line per `add`: the `k`-th largest value seen so far, or "
             "`-` if fewer than `k` values have been seen.",
         cons="- `1 <= k <= 10^4`\n- `0 <= n0 <= 10^4`\n- `1 <= q <= 10^4`",
         solve=lambda s: kth_largest_stream(rows(s)),
         cases=[
             "3\n4\n4 5 8 2\n3\nadd 3\nadd 5\nadd 10",
             "1\n0\n\n3\nadd 5\nadd 3\nadd 8",
             "2\n2\n1 1\n3\nadd 1\nadd 2\nadd 3",
             "3\n0\n\n5\nadd 1\nadd 2\nadd 3\nadd 4\nadd 5",
             "1\n1\n7\n2\nadd 3\nadd 9",
             "2\n3\n10 20 30\n2\nadd 5\nadd 25",
             "4\n2\n1 2\n3\nadd 3\nadd 4\nadd 5",
             "3\n5\n5 5 5 5 5\n2\nadd 1\nadd 6",
         ],
         explains=[
             "k = 3, initial values [4, 5, 8, 2]. Top 3 largest are {4, 5, 8}. Add 3: 3 is not among top 3, so 3rd largest stays 4. Add 5: 5 replaces 4, top 3 become {5, 5, 8}, 3rd largest is 5. Add 10: 10 replaces 5, top 3 become {5, 8, 10}, 3rd largest is 5.",
             "k = 1, empty start. Add 5: 1st largest is 5. Add 3: still 5. Add 8: 1st largest becomes 8.",
         ]),

    # LEC-9 --------------------------------------------------------------
    dict(title="Homework: LC1337 The K Weakest Rows in a Matrix",
         stmt="An `m` by `n` binary matrix has `1`s (soldiers) placed to the "
              "left of every `0` (civilians) in each row. Row `i` is "
              "**weaker** than row `j` when it has fewer soldiers; ties are "
              "broken by the smaller index. Print the indices of the `k` "
              "weakest rows, from weakest to strongest.",
         inp="The first line contains `m`, `n`, and `k` separated by spaces. "
             "Each of the next `m` lines contains one row of the matrix: `n` "
             "space-separated `0`/`1` values.",
         out="A single line with the `k` chosen row indices separated by "
             "spaces.",
         cons="- `2 <= m, n <= 100`\n- `1 <= k <= m`",
         solve=lambda s: fmt(k_weakest_rows(
             [ints(r) for r in
              rows(s)[1:1 + ints(rows(s)[0])[0]]],
             ints(rows(s)[0])[2])),
         cases=[
             "5 5 3\n1 1 0 0 0\n1 1 1 1 0\n1 0 0 0 0\n1 1 0 0 0\n1 1 1 1 1",
             "4 4 2\n1 1 1 1\n1 0 0 0\n1 1 0 0\n1 1 1 0",
             "2 2 1\n0 0\n1 1",
             "3 3 2\n1 1 1\n0 0 0\n1 0 0",
             "4 3 3\n0 0 0\n1 1 1\n1 1 0\n1 0 0",
             "3 4 1\n1 1 1 0\n1 1 0 0\n1 0 0 0",
             "5 2 5\n0 0\n1 0\n1 1\n1 1\n1 1",
             "2 3 2\n1 1 0\n1 0 0",
         ],
         explains=[
             "Soldiers per row: row 0 has 2, row 1 has 4, row 2 has 1, row 3 has 2, row 4 has 5. Sorted by (soldiers ascending, index ascending): row 2 (1), row 0 (2), row 3 (2). Top 3 weakest: 2, 0, 3.",
             "Soldiers per row: row 0 has 4, row 1 has 1, row 2 has 2, row 3 has 3. Sorted: row 1 (1), row 2 (2). Top 2 weakest: 1, 2.",
         ]),

    # LEC-10 -------------------------------------------------------------
    dict(title="Homework: LC1394 Find Lucky Integer in an Array",
         stmt="A value `v` is **lucky** in the array when its frequency of "
              "occurrence equals `v`. Print the **largest** lucky value, or "
              "`-1` if the array has none.",
         inp=SIZED_ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 500`\n- `1 <= value <= 500`",
         solve=lambda s: str(lucky_integer(ints(rows(s)[1]))),
         cases=sized(["2 2 3 4", "1 2 2 3 3 3", "2 2 2 3 3",
                      "5", "7 7 7 7 7 7 7", "1 1 2 2 3 3",
                      "4 4 4 4", "5 5 5 5 5 5"]),
         explains=[
             "Value 2 appears 2 times (2 = 2, lucky). 3 appears once (3 != 1), 4 appears once (4 != 1). Largest lucky value: 2.",
             "1 appears 1 time (lucky), 2 appears 2 times (lucky), 3 appears 3 times (lucky). Largest lucky value: 3.",
         ]),

    dict(title="Homework: LC146 LRU Cache",
         stmt="Simulate a **Least Recently Used** cache with a fixed "
              "capacity. Two operations are supported:\n"
              "\n"
              "- `put <key> <value>` -- insert or update `<key>` -> `<value>`. "
              "If the cache is full, the least recently used entry is "
              "evicted first.\n"
              "- `get <key>` -- print the value associated with `<key>`, or "
              "`-1` if `<key>` is not in the cache. `get` and `put` both "
              "mark the touched entry as most recently used.",
         inp="The first line contains the cache capacity. The second line "
             "contains `q`, the number of operations. Each of the next `q` "
             "lines contains one operation as described above.",
         out="One line per `get` operation, in order: the returned value.",
         cons="- `1 <= capacity <= 3 * 10^3`\n- `1 <= q <= 2 * 10^4`\n"
              "- keys and values are non-negative integers",
         solve=lambda s: lru_cache_sim(rows(s)),
         cases=[
             "2\n8\nput 1 1\nput 2 2\nget 1\nput 3 3\nget 2\nput 4 4\nget 1\nget 4",
             "1\n4\nput 1 10\nget 1\nput 2 20\nget 1",
             "2\n3\nget 5\nput 5 100\nget 5",
             "3\n5\nput 1 1\nput 2 2\nput 3 3\nget 1\nget 2",
             "2\n5\nput 1 1\nput 2 2\nget 1\nput 3 3\nget 2",
             "1\n3\nput 1 1\nput 2 2\nget 1",
             "3\n4\nput 1 10\nput 2 20\nput 3 30\nget 2",
             "2\n6\nput 1 1\nput 2 2\nput 1 10\nget 1\nput 3 3\nget 2",
         ],
         explains=[
             "Capacity is 2. put(1, 1) and put(2, 2). get(1) returns 1 (now 1 is most recent). put(3, 3) evicts key 2. get(2) returns -1. put(4, 4) evicts key 1. get(1) returns -1. get(4) returns 4.",
             "Capacity is 1. put(1, 10). get(1) returns 10. put(2, 20) evicts key 1. get(1) returns -1.",
         ]),

    dict(title="Homework: LC432 All O one Data Structure",
         stmt="Maintain a collection of string keys with integer counts and "
              "answer running max/min-count queries. Four operations:\n"
              "\n"
              "- `inc <key>` -- add 1 to the count of `<key>` (inserts it "
              "with count 1 if new).\n"
              "- `dec <key>` -- subtract 1 from the count of `<key>`. If the "
              "count becomes 0 the key is removed.\n"
              "- `max` -- print a key with the **highest** current count. "
              "When several keys share the highest count, print the "
              "lexicographically smallest such key. Print `-` if the "
              "collection is empty.\n"
              "- `min` -- print a key with the **smallest** positive count, "
              "breaking ties lexicographically. Print `-` if the collection "
              "is empty.\n"
              "\n"
              "`dec` is only called on a key that currently has a positive "
              "count.",
         inp="The first line contains `q`, the number of operations. Each of "
             "the next `q` lines contains one operation as described above.",
         out="One line per `max` or `min` operation, in order: the answering "
             "key (or `-` if the collection is empty).",
         cons="- `1 <= q <= 5 * 10^4`\n"
              "- keys are non-empty lowercase strings of length at most 10",
         solve=lambda s: all_o_one(rows(s)),
         cases=[
             "7\ninc a\ninc b\ninc b\nmax\nmin\ndec b\nmin",
             "5\ninc apple\ninc apple\nmax\ndec apple\nmax",
             "3\nmax\nmin\ninc x",
             "6\ninc c\ninc b\ninc a\nmin\nmax\ndec b",
             "4\ninc x\ninc y\ninc x\nmin",
             "5\ninc k\ndec k\nmax\ninc m\nmax",
             "6\ninc p\ninc q\ninc p\ninc q\nmax\nmin",
             "4\ninc apple\ninc banana\nmin\nmax",
         ],
         explains=[
             "After inc a, inc b, inc b: counts are {a: 1, b: 2}. max prints 'b' (highest count 2). min prints 'a' (smallest count 1). dec b: {a: 1, b: 1}. min: tie between a and b at count 1. Alphabetical smallest is 'a'.",
             "inc apple twice: {apple: 2}. max prints 'apple'. dec apple: {apple: 1}. max prints 'apple' again.",
         ]),
]


# --- added: coverage for previously unchecked problems -------------------
SANITY += [
    ("Classwork: LC102 Binary Tree Level Order Traversal", "1 2 3", "1\n2 3"),
    ("Classwork: LC102 Binary Tree Level Order Traversal", "1 2 3 4 5 null 6 null null 7 8", "1\n2 3\n4 5 6\n7 8"),
    ("Homework: LC103 Binary Tree Zigzag Level Order Traversal", "1 2 3", "1\n3 2"),
    ("Homework: LC103 Binary Tree Zigzag Level Order Traversal", "1 2 3 4 5 null 6 null null 7 8", "1\n3 2\n4 5 6\n8 7"),
    ("Homework: LC107 Binary Tree Level Order Traversal II", "1 2 3", "2 3\n1"),
    ("Homework: LC637 Average of Levels in Binary Tree", "1 2 3", "1.00000\n2.50000"),
    ("Homework: Count the number of nodes at maximum depth", "1 2 3", "2"),
    ("Homework: Count the number of nodes at maximum depth", "1 2 3 4 5 null 6 null null 7 8", "2"),
    ("Homework: LC965 Univalued Binary Tree", "4 4 4 4 4 null 4", "true"),
    ("Homework: LC965 Univalued Binary Tree", "1 1 1 1 1 null 2", "false"),
    ("Homework: Check whether two trees have equal height", "1 2 3\n4 5 6", "true"),
    ("Homework: Check whether two trees have equal height", "1 2 3\n1 null 2 null 3", "false"),
    ("Classwork: Boundary traversal of a binary tree (GfG)", "1 2 3 4 5 null 6 null null 7 8", "1 2 4 7 8 6 3"),
    ("Classwork: LC987 Vertical Order Traversal of a Binary Tree", "1 2 3 4 5 null 6 null null 7 8", "4\n2 7\n1 5\n3 8\n6"),
    ("Homework: Diagonal traversal of a binary tree (GfG)", "1 2 3 4 5 null 6 null null 7 8", "1 3 6\n2 5 8\n4 7"),
    ("Classwork: Top view of a binary tree (GfG)", "1 2 3 4 5 null 6 null null 7 8", "4 2 1 3 6"),
    ("Homework: Bottom view of a binary tree (GfG)", "1 2 3 4 5 null 6 null null 7 8", "4 7 5 8 6"),
]

SANITY_21_30 = [
    ("Classwork: LC700 Search in a Binary Search Tree", "5 3 8 2 4 7 9\n7", "7"),
    ("Classwork: LC700 Search in a Binary Search Tree", "8 3 10\n99", "null"),
    ("Classwork: LC701 Insert into a Binary Search Tree", "2 1 3\n4", "2 1 3 null null null 4"),
    ("Classwork: Iterative BST search (GfG)", "8 3 10\n4", "false"),
    ("Classwork: Iterative BST search (GfG)", "8 3 10\n10", "true"),
    ("Homework: Iterative BST insert (GfG)", "2 1 3\n4", "2 1 3 null null null 4"),
    ("Homework: Search keys within a range in a BST (GfG)", "5 3 8 2 4 7 9\n3 8", "3 4 5 7 8"),
    ("Homework: Count BST nodes lying in a given range (GfG)", "5 3 8 2 4 7 9\n3 8", "5"),
    ("Classwork: LC98 Validate Binary Search Tree", "2 1 3", "true"),
    ("Classwork: LC98 Validate Binary Search Tree", "5 1 4 null null 3 6", "false"),
    ("Classwork: LC530 Minimum Absolute Difference in BST", "4 2 6 1 3", "1"),
    ("Classwork: LC501 Find Mode in Binary Search Tree", "1 null 2 2", "2"),
    ("Homework: LC99 Recover Binary Search Tree", "1 3 null null 2", "3 1 null null 2"),
    ("Homework: LC783 Minimum Distance Between BST Nodes", "4 2 6 1 3", "1"),
    ("Homework: LC255 Verify Preorder Sequence in BST", "5 2 1 3 6", "true"),
    ("Homework: LC255 Verify Preorder Sequence in BST", "5 2 6 1 3", "false"),
    ("Classwork: LC450 Delete Node in a BST", "5 3 8 2 4 7 9\n3", "5 4 8 2 null 7 9"),
    ("Classwork: LC230 Kth Smallest Element in a BST", "5 3 8 2 4 7 9\n3", "4"),
    ("Classwork: Kth largest element in a BST (GfG)", "5 3 8 2 4 7 9\n3", "7"),
    ("Homework: LC285 Inorder Successor in BST", "8 3 10 1 6 null 14 null null 4 7 13\n6", "7"),
    ("Homework: LC285 Inorder Successor in BST", "8 3 10\n10", "null"),
    ("Homework: Inorder predecessor in a BST (GfG)", "8 3 10 1 6 null 14 null null 4 7 13\n6", "4"),
    ("Classwork: LC235 Lowest Common Ancestor of a BST", "5 3 8 2 4 7 9\n2 4", "3"),
    ("Classwork: LC108 Convert Sorted Array to Binary Search Tree", "-10 -3 0 5 9", "0 -10 5 null -3 null 9"),
    ("Homework: LC109 Convert Sorted List to Binary Search Tree", "-10 -3 0 5 9", "0 -10 5 null -3 null 9"),
    ("Homework: LC538 Convert BST to Greater Tree", "2 1 3", "5 6 3"),
    ("Homework: LC1382 Balance a Binary Search Tree", "1 null 2 null 3 null 4", "2 1 3 null null null 4"),
    ("Homework: LC333 Largest BST Subtree", "10 5 15 1 8 null 7", "3"),
]

SANITY_GREEDY = [
    ("Classwork: N meetings in one room (GfG)", "6\n1 2\n3 4\n0 6\n5 7\n8 9\n5 9", "4"),
    ("Classwork: LC435 Non-overlapping Intervals", "4\n1 2\n2 3\n3 4\n1 3", "1"),
    ("Classwork: Maximum number of activities selected (GfG)", "3\n1 2\n2 3\n3 4", "3"),
    ("Homework: LC452 Minimum Number of Arrows to Burst Balloons", "4\n10 16\n2 8\n1 6\n7 12", "2"),
    ("Homework: LC646 Maximum Length of Pair Chain", "3\n1 2\n2 3\n3 4", "2"),
    ("Homework: Maximize meetings attended in one room (GfG)", "2\n1 10\n2 3", "1"),
    ("Classwork: LC56 Merge Intervals", "3\n1 3\n2 6\n8 10", "1 6\n8 10"),
    ("Classwork: LC57 Insert Interval", "2\n1 3\n6 9\n2 5", "1 5\n6 9"),
    ("Classwork: Minimum number of platforms (GfG)", "900 940 950 1100 1500 1800\n910 1200 1120 1130 1900 2000", "3"),
    ("Homework: LC986 Interval List Intersections", "1\n1 3\n1\n2 4", "2 3"),
    ("Homework: LC986 Interval List Intersections", "1\n1 3\n1\n5 7", ""),
    ("Homework: LC1094 Car Pooling", "4\n2\n2 1 5\n3 3 7", "false"),
    ("Homework: LC1094 Car Pooling", "5\n2\n2 1 5\n3 3 7", "true"),
    ("Homework: Maximum number of overlapping intervals (GfG)", "3\n1 3\n2 6\n8 10", "2"),
    ("Classwork: Fractional Knapsack (GfG)", "3 50\n60 10\n100 20\n120 30", "240.00000"),
    ("Classwork: Job Sequencing Problem (GfG)", "4\n1 4 20\n2 1 10\n3 1 40\n4 1 30", "2 60"),
    ("Classwork: Job Sequencing Problem (GfG)", "5\n1 2 100\n2 1 19\n3 2 27\n4 1 25\n5 1 15", "2 127"),
    ("Homework: LC455 Assign Cookies", "1 2 3\n1 1", "1"),
    ("Homework: LC455 Assign Cookies", "1 2\n1 2 3", "2"),
    ("Homework: Huffman Encoding (GfG)", "5 9 12 13 16 45", "224"),
    ("Homework: Minimum number of coins (GfG)", "1 2 5 10 20 50 100 200 500 2000\n121", "3"),
    ("Homework: Minimum number of coins (GfG)", "2 5\n3", "-1"),
    ("Classwork: LC55 Jump Game", "2 3 1 1 4", "true"),
    ("Classwork: LC55 Jump Game", "3 2 1 0 4", "false"),
    ("Classwork: LC134 Gas Station", "1 2 3 4 5\n3 4 5 1 2", "3"),
    ("Classwork: LC134 Gas Station", "2 3 4\n3 4 3", "-1"),
    ("Classwork: LC135 Candy", "1 0 2", "5"),
    ("Classwork: LC135 Candy", "1 2 2", "4"),
    ("Homework: LC45 Jump Game II", "2 3 1 1 4", "2"),
    ("Homework: LC763 Partition Labels", "ababcbacadefegdehijhklij", "9 7 8"),
    ("Homework: Rearrange characters so that none are adjacent (GfG)", "aab", "aba"),
    ("Homework: Rearrange characters so that none are adjacent (GfG)", "aaab", "-1"),
    ("Homework: LC1353 Maximum Number of Events That Can Be Attended", "3\n1 2\n2 3\n3 4", "3"),
    ("Homework: LC1353 Maximum Number of Events That Can Be Attended", "4\n1 2\n2 3\n3 4\n1 2", "4"),
    ("Homework: LC860 Lemonade Change", "5 5 5 10 20", "true"),
    ("Homework: LC860 Lemonade Change", "5 5 10 10 20", "false"),
]

SANITY_01_10 = [
    # LEC-1
    ("Classwork: Sum of Two Integers", "3 4", "7"),
    ("Classwork: Sum of Two Integers", "-1 5", "4"),
    ("Classwork: Sort in Descending Order", "4\n2 7 11 15", "15 11 7 2"),
    ("Classwork: Sort in Descending Order", "3\n3 2 4", "4 3 2"),
    ("Count Elements Greater Than K", "5\n1 2 3 4 5\n2", "3"),
    ("Count Elements Greater Than K", "3\n5 5 5\n5", "0"),
    ("Classwork: Add Two Numbers Mixed Types", "2 3.5", "5.500000"),
    ("Classwork: Add Two Numbers Mixed Types", "-1 1.25", "0.250000"),
    # LEC-2
    ("Classwork: Square Every Element", "3\n1 2 3", "1 4 9"),
    ("Classwork: Square Every Element", "3\n-2 -3 4", "4 9 16"),
    ("Classwork: Use find_if to return the first element greater than K", "5\n1 4 2 8 5\n3", "4"),
    ("Classwork: Use find_if to return the first element greater than K", "3\n5 5 5\n5", "-1"),
    ("Classwork: Sort Pairs by Second Value", "3\n1 5\n2 3\n4 3", "2 3\n4 3\n1 5"),
    ("Classwork: Sort Pairs by Second Value", "4\n1 2\n3 2\n2 1\n4 1", "2 1\n4 1\n1 2\n3 2"),
    ("Classwork: Use remove_if + erase to delete all odd numbers from a vector", "6\n1 2 3 4 5 6", "2 4 6"),
    ("Classwork: Use remove_if + erase to delete all odd numbers from a vector", "4\n1 3 5 7", ""),
    # LEC-3
    ("Classwork: Print Distinct Values in Sorted Order", "5\n5 2 8 2 5", "2 5 8"),
    ("Classwork: Print Distinct Values in Sorted Order", "1\n1", "1"),
    ("Classwork: Remove duplicates from a vector using a set", "6\n1 2 1 3 2 4", "1 2 3 4"),
    ("Classwork: Remove duplicates from a vector using a set", "6\n3 1 2 1 3 2", "3 1 2"),
    ("Classwork: Count word frequencies from input using unordered_map",
     "6\napple banana apple cherry banana apple", "apple 3\nbanana 2\ncherry 1"),
    ("Classwork: Count word frequencies from input using unordered_map", "1\nhello", "hello 1"),
    ("Classwork: Implement browser back/forward history using two stacks",
     "leetcode.com\n7\nvisit google.com\nvisit facebook.com\nvisit youtube.com\nback 1\nback 1\nforward 1\nvisit linkedin.com",
     "google.com\nfacebook.com\nyoutube.com\nfacebook.com\ngoogle.com\nfacebook.com\nlinkedin.com"),
    ("Classwork: Implement browser back/forward history using two stacks",
     "home.com\n3\nvisit a.com\nback 5\nforward 5",
     "a.com\nhome.com\na.com"),
    # LEC-4 (new)
    ("Classwork: Sum and Maximum", "5\n1 2 3 4 5", "15\n5"),
    ("Classwork: Sum and Maximum", "3\n-1 -2 -3", "-6\n-1"),
    ("Classwork: Find the k-th largest element using a priority_queue", "6\n3 2 1 5 6 4\n2", "5"),
    ("Classwork: Binary-search a target in a sorted vector with lower_bound", "5\n1 3 5 7 9\n5", "2"),
    ("Classwork: Binary-search a target in a sorted vector with lower_bound", "5\n1 3 5 7 9\n4", "-1"),
    ("Classwork: Binary-search a target in a sorted vector with lower_bound", "4\n1 1 1 2\n1", "0"),
    ("Classwork: Count distinct elements using sort + unique", "5\n4 1 2 1 2", "3"),
    ("Homework: Merge k sorted vectors into one using a min-heap", "3\n1 4 5\n1 3 4\n2 6", "1 1 2 3 4 4 5 6"),
    ("Homework: Generate all permutations of a string with next_permutation", "aab", "aab\naba\nbaa"),
    ("Homework: Answer range-sum queries using prefix sums (partial_sum)", "5\n1 2 3 4 5\n2\n0 2\n1 3", "6\n9"),
    ("Classwork: Compute factorial and nCr recursively", "5\n5 2", "120\n10"),
    ("Classwork: Compute factorial and nCr recursively", "0\n0 0", "1\n1"),
    ("Classwork: Reverse a singly linked list iteratively", "5\n1 2 3 4 5", "5 4 3 2 1"),
    ("Classwork: Print numbers 1..N and N..1 using recursion", "5", "1 2 3 4 5\n5 4 3 2 1"),
    ("Homework: Fibonacci with memoization", "10", "55"),
    ("Homework: Fibonacci with memoization", "0", "0"),
    ("Homework: Detect a cycle in a linked list (Floyd's algorithm)", "4\n3 2 0 -4\n1", "true"),
    ("Homework: Detect a cycle in a linked list (Floyd's algorithm)", "3\n1 2 3\n-1", "false"),
    ("Homework: Find the middle node of a linked list in one pass", "5\n1 2 3 4 5", "3"),
    ("Homework: Find the middle node of a linked list in one pass", "6\n1 2 3 4 5 6", "4"),
    ("Classwork: LC1 Two Sum", "4\n2 7 11 15\n9", "0 1"),
    ("Classwork: LC1 Two Sum", "3\n3 2 4\n6", "1 2"),
    ("Classwork: Frequency of elements (GfG)", "5\n4 1 2 1 2", "1 2\n2 2\n4 1"),
    ("Classwork: LC217 Contains Duplicate", "5\n4 1 2 1 2", "true"),
    ("Classwork: LC217 Contains Duplicate", "5\n1 2 3 4 5", "false"),
    ("Homework: LC387 First Unique Character in a String", "leetcode", "0"),
    ("Homework: LC387 First Unique Character in a String", "loveleetcode", "2"),
    ("Homework: LC387 First Unique Character in a String", "aabb", "-1"),
    ("Homework: LC242 Valid Anagram", "anagram\nnagaram", "true"),
    ("Homework: LC242 Valid Anagram", "rat\ncar", "false"),
    ("Homework: LC219 Contains Duplicate II", "4\n1 2 3 1\n3", "true"),
    ("Homework: LC219 Contains Duplicate II", "6\n1 2 3 1 2 3\n2", "false"),
    ("Classwork: LC560 Subarray Sum Equals K", "3\n1 1 1\n2", "2"),
    ("Classwork: LC560 Subarray Sum Equals K", "3\n1 2 3\n3", "2"),
    ("Classwork: LC49 Group Anagrams", "6\neat tea tan ate nat bat", "ate eat tea\nbat\nnat tan"),
    ("Classwork: LC3 Longest Substring Without Repeating Characters", "abcabcbb", "3"),
    ("Classwork: LC3 Longest Substring Without Repeating Characters", "bbbbb", "1"),
    ("Classwork: LC3 Longest Substring Without Repeating Characters", "pwwkew", "3"),
    ("Homework: LC974 Subarray Sums Divisible by K", "6\n4 5 0 -2 -3 1\n5", "7"),
    ("Homework: LC128 Longest Consecutive Sequence", "6\n100 4 200 1 3 2", "4"),
    ("Homework: Largest subarray with 0 sum (GfG)", "8\n15 -2 2 -8 1 7 10 23", "5"),
    ("Classwork: LC215 Kth Largest Element in an Array", "9\n3 2 3 1 2 4 5 5 6\n4", "4"),
    ("Classwork: Kth smallest element (GfG)", "6\n7 10 4 3 20 15\n3", "7"),
    ("Classwork: LC1046 Last Stone Weight", "6\n2 7 4 1 8 1", "1"),
    ("Classwork: LC1046 Last Stone Weight", "2\n2 2", "0"),
    ("Homework: LC973 K Closest Points to Origin", "2 1\n1 3\n-2 2", "-2 2"),
    ("Homework: Minimum cost of ropes (GfG)", "4\n4 3 2 6", "29"),
    ("Classwork: LC347 Top K Frequent Elements", "6\n1 1 1 2 2 3\n2", "1 2"),
    ("Classwork: LC23 Merge k Sorted Lists", "3\n1 4 5\n1 3 4\n2 6", "1 1 2 3 4 4 5 6"),
    ("Homework: LC378 Kth Smallest Element in a Sorted Matrix", "3 8\n1 5 9\n10 11 13\n12 13 15", "13"),
    ("Homework: LC692 Top K Frequent Words", "6\ni love leetcode i love coding\n2", "i love"),
    ("Homework: LC451 Sort Characters By Frequency", "tree", "eert"),
    ("Homework: LC451 Sort Characters By Frequency", "cccaaa", "aaaccc"),
    ("Homework: LC621 Task Scheduler", "6\nA A A B B B\n2", "8"),
    ("Homework: LC621 Task Scheduler", "6\nA A A B B B\n0", "6"),
    ("Homework: LC621 Task Scheduler", "10\nA A A A B C D E F G\n2", "10"),
    # Remaining classwork
    ("Classwork: Sum of First N Natural Numbers", "5", "15"),
    ("Classwork: Sum of First N Natural Numbers", "10", "55"),
    ("Classwork: Sum of First N Natural Numbers", "0", "0"),
    ("Classwork: Character Frequency", "hello", "e 1\nh 1\nl 2\no 1"),
    ("Classwork: Character Frequency", "banana", "a 3\nb 1\nn 2"),
    ("Classwork: LC1207 Unique Number of Occurrences", "6\n1 2 2 1 1 3", "true"),
    ("Classwork: LC1207 Unique Number of Occurrences", "2\n1 2", "false"),
    ("Classwork: Three Smallest Elements", "6\n7 2 9 1 5 3", "1 2 3"),
    ("Classwork: Three Smallest Elements", "3\n10 20 30", "10 20 30"),
    ("Classwork: LC506 Relative Ranks", "5\n5 4 3 2 1",
     "Gold Medal\nSilver Medal\nBronze Medal\n4\n5"),
    ("Classwork: LC506 Relative Ranks", "5\n10 3 8 9 4",
     "Gold Medal\n5\nBronze Medal\nSilver Medal\n4"),
    ("Classwork: LC1636 Sort Array by Increasing Frequency", "6\n1 1 2 2 2 3",
     "3 1 1 2 2 2"),
    ("Classwork: LC1636 Sort Array by Increasing Frequency", "5\n2 3 1 3 2",
     "1 3 3 2 2"),
    ("Classwork: LC767 Reorganize String", "aab", "aba"),
    ("Classwork: LC767 Reorganize String", "aaab", "impossible"),
    ("Classwork: LC767 Reorganize String", "aabb", "abab"),
    ("Classwork: LC295 Find Median from Data Stream",
     "6\nadd 1\nadd 2\nmedian\nadd 3\nmedian\nadd 4",
     "1.50000\n2.00000"),
    ("Classwork: LC295 Find Median from Data Stream",
     "3\nadd 5\nmedian\nmedian",
     "5.00000\n5.00000"),
    ("Classwork: LC355 Design Twitter",
     "7\npost 1 5\nfeed 1\nfollow 1 2\npost 2 6\nfeed 1\nunfollow 1 2\nfeed 1",
     "5\n6 5\n5"),
    ("Classwork: LC355 Design Twitter",
     "3\npost 1 10\npost 1 20\nfeed 1",
     "20 10"),
    ("Classwork: LC895 Maximum Frequency Stack",
     "10\npush 5\npush 7\npush 5\npush 7\npush 4\npush 5\npop\npop\npop\npop",
     "5\n7\n5\n4"),
    ("Classwork: LC895 Maximum Frequency Stack",
     "3\npush 1\npush 1\npop",
     "1"),
    # Remaining homework
    ("Homework: Print Vector Elements", "4\n2 7 11 15", "2 7 11 15"),
    ("Homework: Print Vector Elements", "1\n1", "1"),
    ("Sum of vector using for_each", "4\n2 7 11 15", "35"),
    ("Sum of vector using for_each", "3\n3 2 4", "9"),
    ("Store and Apply Lambdas using function", "5", "10\n25\n-5"),
    ("Store and Apply Lambdas using function", "-3", "-6\n9\n3"),
    ("Filter a Vector Capturing Threshold by Value", "5\n1 5 2 8 3\n3", "5 8"),
    ("Filter a Vector Capturing Threshold by Value", "3\n5 5 5\n5", ""),
    ("Homework: Sort Strings in Reverse Alphabetical Order",
     "3\napple banana cherry", "cherry banana apple"),
    ("Homework: Sort Strings in Reverse Alphabetical Order",
     "1\nonly", "only"),
    ("Homework: Print unordered_map entries sorted by count using a lambda",
     "6\napple banana apple cherry banana apple",
     "apple 3\nbanana 2\ncherry 1"),
    ("Homework: Print unordered_map entries sorted by count using a lambda",
     "3\ndog cat dog", "dog 2\ncat 1"),
    ("Homework: Sort strings by length then lexicographically with one lambda",
     "4\nbanana kiwi apple fig", "fig kiwi apple banana"),
    ("Homework: Sort strings by length then lexicographically with one lambda",
     "5\na bb ccc dddd eeeee", "a bb ccc dddd eeeee"),
    ("Homework: Write a function that returns a lambda multiplying by a captured factor",
     "3\n4\n1 2 3 4", "3 6 9 12"),
    ("Homework: Write a function that returns a lambda multiplying by a captured factor",
     "0\n5\n1 2 3 4 5", "0 0 0 0 0"),
    ("Homework: Sorted Key-Value Pairs", "3\n5 100\n1 200\n3 300",
     "1 200\n3 300\n5 100"),
    ("Homework: Sorted Key-Value Pairs", "1\n7 7", "7 7"),
    ("Homework: Maintain a sorted stream with a multiset and query the smallest",
     "5\ninsert 3\ninsert 1\ninsert 2\nsmallest\nremove 1", "1"),
    ("Homework: Maintain a sorted stream with a multiset and query the smallest",
     "6\ninsert 5\nsmallest\ninsert 2\nsmallest\ninsert 4\nsmallest",
     "5\n2\n2"),
    ("Homework: Compute a fixed-size sliding-window maximum using a deque",
     "8\n1 3 -1 -3 5 3 6 7\n3", "3 3 5 5 6 7"),
    ("Homework: Compute a fixed-size sliding-window maximum using a deque",
     "1\n1\n1", "1"),
    ("Homework: Sort Records by Score",
     "3\nalice 80\nbob 90\ncarol 80",
     "bob 90\nalice 80\ncarol 80"),
    ("Homework: Sort Records by Score", "1\nsolo 100", "solo 100"),
    ("Homework: Contains Value", "5\n1 2 3 4 5\n3", "true"),
    ("Homework: Contains Value", "3\n1 2 3\n7", "false"),
    ("Homework: LC136 Single Number", "3\n2 2 1", "1"),
    ("Homework: LC136 Single Number", "5\n4 1 2 1 2", "4"),
    ("Homework: LC1512 Number of Good Pairs", "6\n1 2 3 1 1 3", "4"),
    ("Homework: LC1512 Number of Good Pairs", "4\n1 1 1 1", "6"),
    ("Homework: LC1464 Maximum Product of Two Elements in an Array",
     "4\n3 4 5 2", "12"),
    ("Homework: LC1464 Maximum Product of Two Elements in an Array",
     "4\n1 5 4 5", "16"),
    ("Homework: LC703 Kth Largest Element in a Stream",
     "3\n4\n4 5 8 2\n3\nadd 3\nadd 5\nadd 10", "4\n5\n5"),
    ("Homework: LC703 Kth Largest Element in a Stream",
     "1\n0\n\n3\nadd 5\nadd 3\nadd 8", "5\n5\n8"),
    ("Homework: LC1337 The K Weakest Rows in a Matrix",
     "5 5 3\n1 1 0 0 0\n1 1 1 1 0\n1 0 0 0 0\n1 1 0 0 0\n1 1 1 1 1",
     "2 0 3"),
    ("Homework: LC1337 The K Weakest Rows in a Matrix",
     "4 4 2\n1 1 1 1\n1 0 0 0\n1 1 0 0\n1 1 1 0",
     "1 2"),
    ("Homework: LC1394 Find Lucky Integer in an Array", "4\n2 2 3 4", "2"),
    ("Homework: LC1394 Find Lucky Integer in an Array",
     "6\n1 2 2 3 3 3", "3"),
    ("Homework: LC1394 Find Lucky Integer in an Array",
     "5\n2 2 2 3 3", "-1"),
    ("Homework: LC146 LRU Cache",
     "2\n8\nput 1 1\nput 2 2\nget 1\nput 3 3\nget 2\nput 4 4\nget 1\nget 4",
     "1\n-1\n-1\n4"),
    ("Homework: LC146 LRU Cache",
     "1\n4\nput 1 10\nget 1\nput 2 20\nget 1", "10\n-1"),
    ("Homework: LC432 All O one Data Structure",
     "7\ninc a\ninc b\ninc b\nmax\nmin\ndec b\nmin", "b\na\na"),
    ("Homework: LC432 All O one Data Structure",
     "5\ninc apple\ninc apple\nmax\ndec apple\nmax", "apple\napple"),
]

def check(problems, sanity):
    by = {p["title"]: p for p in problems}
    bad = 0
    for title, inp, want in sanity:
        p = by.get(title)
        if not p:
            print("  SANITY refers to a missing problem: %s" % title)
            bad += 1
            continue
        got = p["solve"](inp)
        if got.strip() != want.strip():
            print("  WRONG  %s\n         input %r\n         want %r got %r"
                  % (title, inp, want, got))
            bad += 1
    return bad


def emit(path, problems, links=True, link_only=False):
    lines = ["# DSA-301 challenges", "",
             "Generated by make_md.py. Sample outputs are computed from the "
             "reference solutions, not written by hand.", "", "---", ""]
    for p in problems:
        # In link-only mode a problem that HAS a source becomes a bare pointer:
        # the link is the whole statement and the three format fields are left
        # out entirely, so editor.py writes them empty. A problem with no source
        # keeps its full write-up -- there is nowhere to send the student.
        bare = problem_links.link_only_for(p["title"]) if link_only else ""

        lines.append("## %s" % p["title"])
        # Optional per-problem HackerRank id override, used by editor.py when
        # the title matches more than one live challenge in the account.
        if p.get("hr_id"):
            lines.append("<!-- hackerrank_id: %s -->" % p["hr_id"])
        lines.append("")
        lines.append("**Problem Statement**")
        if bare:
            lines.append(bare)
            lines.append("")
            # Not omitted, and not empty: HackerRank's edit form validates the
            # four boxes as a unit and refuses a save with blank ones. See the
            # note on LINK_ONLY_INP in problem_links.py.
            lines.append("**Input Format**")
            lines.append(problem_links.LINK_ONLY_INP)
            lines.append("")
            lines.append("**Output Format**")
            lines.append(problem_links.LINK_ONLY_OUT)
            lines.append("")
            lines.append("**Constraints**")
            lines.append(problem_links.LINK_ONLY_CONS)
            lines.append("")
        else:
            lines.append(p["stmt"])
            # Most of these problems are LeetCode's or GeeksforGeeks'. Point at
            # the original so a student can read their write-up, and say plainly
            # that the I/O contract here is different -- see problem_links.py.
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
        explains = p.get("explains") or []
        for i, c in enumerate(p["cases"], 1):
            lines.append("**Sample Input %d**" % i)
            lines.append("```")
            lines.append(c)
            lines.append("```")
            lines.append("**Sample Output %d**" % i)
            lines.append("```")
            lines.append(p["solve"](c))
            lines.append("```")
            # Editor.py reads this block and feeds it to mark_samples, which
            # attaches the text to the corresponding test case's Explanation
            # field on HackerRank (visible only when Sample is checked).
            if i - 1 < len(explains) and explains[i - 1]:
                lines.append("**Sample Explanation %d**" % i)
                lines.append(explains[i - 1])
            lines.append("")
        lines.append("---")
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


if __name__ == "__main__":
    FLAGS = ("--no-links", "--link-only")
    argv = sys.argv[1:]
    links = "--no-links" not in argv
    link_only = "--link-only" in argv
    unknown = [a for a in argv if a not in FLAGS]
    if unknown or (link_only and not links):
        print("usage: make_md.py [--no-links | --link-only]")
        print()
        print("  (default)     full write-up, plus a link to the original")
        print("  --no-links    full write-up, no link")
        print("  --link-only   the link IS the statement, so a student reads")
        print("                the problem at the source. The other three")
        print("                boxes get a one-line placeholder. The 16")
        print("                problems with no source keep their write-up.")
        if link_only and not links:
            print()
            print("--link-only and --no-links contradict each other.")
        sys.exit(2)

    # Subsets of PROBLEMS_01_10 emitted into their own files so editor.py can
    # push just those without re-uploading anything else.
    #  - _last10: the ten late-added classwork rows (LEC-5 sum-of-N,
    #    LEC-6 char freq, LC1207, Three Smallest, LC506, LC1636, LC767,
    #    LC295, LC355, LC895) -- still identified by "the last 10 dicts
    #    added to the classwork block", which sit right before the homework
    #    additions.
    #  - _homework: everything whose title starts with "Homework:" plus the
    #    three LEC-1 lambdas that live under short non-standard names in the
    #    homework contest (Sum of vector using for_each, Store and Apply
    #    Lambdas using function, Filter a Vector Capturing Threshold by
    #    Value).
    def _is_homework(title):
        t = title.lower()
        return (t.startswith("homework:")
                or t in ("sum of vector using for_each",
                         "store and apply lambdas using function",
                         "filter a vector capturing threshold by value"))

    HOMEWORK = [p for p in PROBLEMS_01_10 if _is_homework(p["title"])]
    HOMEWORK_TITLES = {p["title"] for p in HOMEWORK}
    HOMEWORK_SANITY = [s for s in SANITY_01_10 if s[0] in HOMEWORK_TITLES]

    # The ten "last classwork" batch sits between the previous classwork
    # entries and the new homework additions -- classwork entries only.
    CLASSWORK = [p for p in PROBLEMS_01_10 if not _is_homework(p["title"])]
    LAST_10 = CLASSWORK[-10:]
    LAST_10_TITLES = {p["title"] for p in LAST_10}
    LAST_10_SANITY = [s for s in SANITY_01_10 if s[0] in LAST_10_TITLES]

    FILES = [
        ("DSA301_LEC11-20.md", PROBLEMS, SANITY),
        ("DSA301_LEC21-30.md", PROBLEMS_21_30 + PROBLEMS_GREEDY,
         SANITY_21_30 + SANITY_GREEDY),
        ("DSA301_LEC01-10.md", PROBLEMS_01_10, SANITY_01_10),
        ("DSA301_LEC01-10_last10.md", LAST_10, LAST_10_SANITY),
        ("DSA301_LEC01-10_homework.md", HOMEWORK, HOMEWORK_SANITY),
        ("DSA301_LEC31-40.md", dp_problems.PROBLEMS,
         dp_problems.SANITY),
        ("DSA301_LEC41-50.md", graph_problems.PROBLEMS,
         graph_problems.SANITY),
    ]

    print("checking reference solutions against hand-worked answers...")
    bad = 0
    for name, probs, sane in FILES:
        n = check(probs, sane)
        print("  %-22s %d checks, %d failed" % (name, len(sane), n))
        bad += n
    if bad:
        print()
        print("%d sanity failure(s). Nothing written." % bad)
        sys.exit(1)

    # Resolve every source link BEFORE writing anything. A title naming LC999,
    # or a new (GfG) problem with no entry in problem_links.py, raises here --
    # same policy as the sanity gate above, and for the same reason.
    if links:
        print()
        print("resolving source links...")
        tot_lc = tot_gfg = tot_none = 0
        try:
            for name, probs, sane in FILES:
                lc, gfg, none = problem_links.summarise(probs)
                print("  %-22s %3d LeetCode, %2d GeeksforGeeks, %2d own"
                      % (name, lc, gfg, none))
                tot_lc += lc; tot_gfg += gfg; tot_none += none
        except problem_links.MissingLink as ex:
            print()
            print("%s -- add it to problem_links.py. Nothing written." % ex)
            sys.exit(1)
        print("  %-22s %3d LeetCode, %2d GeeksforGeeks, %2d own"
              % ("total", tot_lc, tot_gfg, tot_none))
        if link_only:
            print()
            print("  LINK-ONLY: those %d linked problems become a bare link,"
                  % (tot_lc + tot_gfg))
            print("  with a one-line placeholder in the other three boxes --")
            print("  HackerRank refuses a save that leaves them blank. Push")
            print("  these WITH --tests: the samples are the only I/O spec")
            print("  left. The %d own problems keep their write-up." % tot_none)

    print()
    for name, probs, sane in FILES:
        path = emit(os.path.join(OUT_DIR, name), probs, links=links,
                    link_only=link_only)
        print("wrote %-40s %d problems, %d test cases"
              % (os.path.basename(path), len(probs),
                 sum(len(p["cases"]) for p in probs)))
