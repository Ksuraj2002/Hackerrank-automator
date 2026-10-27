#!/usr/bin/env python3
"""
dp_problems.py -- LEC 31-40, the dynamic programming block.

Imported by make_md.py, which writes the markdown. Self-contained: it defines
its own small helpers so there is no circular import.

Exports PROBLEMS (the write-ups) and SANITY (answers worked out by hand, which
gate generation).
"""

from collections import Counter

# ---------------------------------------------------------------- helpers ----
def rows(s):
    return s.split("\n")


def ints(s):
    return [int(x) for x in s.split()]


def fmt(xs):
    return " ".join(str(x) for x in xs)


def fmt_bool(b):
    return "true" if b else "false"


def grid_of(s, start=1):
    """First line 'm n', then m rows."""
    m = ints(rows(s)[start - 1])[0]
    return [ints(rows(s)[start + i]) for i in range(m)]


NUM_OUT = "A single line containing one integer."
BOOL_OUT = "A single line: `true` or `false`."
SEQ_OUT = "A single line: the values separated by single spaces."
ARR_IN = "A single line of space-separated integers."
STR_IN = "A single line containing the string."
TWO_STR_IN = "Two lines, one string each."
GRID_IN = ("The first line contains `m` and `n`. Each of the next `m` lines "
           "contains `n` integers.")
SLOW = "- Exponential recursion will time out; memoise or tabulate."


# ------------------------------------------------------------- solutions ----
def climb(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def rob(a):
    take = skip = 0
    for x in a:
        take, skip = skip + x, max(skip, take)
    return max(take, skip)


def rob2(a):
    if len(a) == 1:
        return a[0]
    return max(rob(a[1:]), rob(a[:-1]))


def min_cost_climb(a):
    p = q = 0
    for x in a:
        p, q = q, min(p, q) + x
    return min(p, q)


def decode_ways(s):
    if not s or s[0] == "0":
        return 0
    prev, cur = 1, 1
    for i in range(1, len(s)):
        nxt = 0
        if s[i] != "0":
            nxt += cur
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            nxt += prev
        prev, cur = cur, nxt
    return cur


def coin_change_min(coins, amt):
    INF = float("inf")
    dp = [0] + [INF] * amt
    for i in range(1, amt + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amt] if dp[amt] != INF else -1


def coin_change_ways(coins, amt):
    dp = [1] + [0] * amt
    for c in coins:
        for i in range(c, amt + 1):
            dp[i] += dp[i - c]
    return dp[amt]


def comb_sum4(nums, target):
    dp = [1] + [0] * target
    for i in range(1, target + 1):
        for x in nums:
            if x <= i:
                dp[i] += dp[i - x]
    return dp[target]


def perfect_squares(n):
    dp = [0] + [float("inf")] * n
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]


def lis(a):
    if not a:
        return 0
    dp = [1] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] \
                else max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(a)][len(b)]


def count_lis(a):
    n = len(a)
    if n == 0:
        return 0
    length = [1] * n
    count = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
    best = max(length)
    return sum(c for l, c in zip(length, count) if l == best)


def lcsubstr(a, b):
    best = 0
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                best = max(best, dp[i][j])
    return best


def ncr(n, r):
    if r < 0 or r > n:
        return 0
    out = 1
    for i in range(r):
        out = out * (n - i) // (i + 1)
    return out


def unique_paths(m, n):
    return ncr(m + n - 2, m - 1)


def min_path_sum(g):
    m, n = len(g), len(g[0])
    dp = [row[:] for row in g]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            best = float("inf")
            if i:
                best = min(best, dp[i - 1][j])
            if j:
                best = min(best, dp[i][j - 1])
            dp[i][j] += best
    return dp[m - 1][n - 1]


def unique_paths_obstacles(g):
    m, n = len(g), len(g[0])
    if g[0][0] == 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                dp[i][j] = 0
                continue
            if i:
                dp[i][j] += dp[i - 1][j]
            if j:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]


def triangle_min(tri):
    dp = tri[-1][:]
    for i in range(len(tri) - 2, -1, -1):
        dp = [tri[i][j] + min(dp[j], dp[j + 1]) for j in range(len(tri[i]))]
    return dp[0]


def falling_path(g):
    n = len(g)
    dp = g[0][:]
    for i in range(1, n):
        nxt = []
        for j in range(n):
            best = dp[j]
            if j:
                best = min(best, dp[j - 1])
            if j + 1 < n:
                best = min(best, dp[j + 1])
            nxt.append(g[i][j] + best)
        dp = nxt
    return min(dp)


def maximal_square(g):
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    best = 0
    for i in range(m):
        for j in range(n):
            if g[i][j]:
                dp[i][j] = 1 + (min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                                if i and j else 0)
                best = max(best, dp[i][j])
    return best * best


def subset_sum(a, t):
    dp = [False] * (t + 1)
    dp[0] = True
    for x in a:
        for i in range(t, x - 1, -1):
            dp[i] = dp[i] or dp[i - x]
    return dp[t]


def count_subsets(a, t):
    dp = [0] * (t + 1)
    dp[0] = 1
    for x in a:
        for i in range(t, x - 1, -1):
            dp[i] += dp[i - x]
    return dp[t]


def can_partition(a):
    s = sum(a)
    return subset_sum(a, s // 2) if s % 2 == 0 else False


def delete_and_earn(a):
    c = Counter(a)
    prev_key, take, skip = None, 0, 0
    for k in sorted(c):
        gain = k * c[k]
        if prev_key is not None and k == prev_key + 1:
            take, skip = skip + gain, max(skip, take)
        else:
            best = max(take, skip)
            take, skip = best + gain, best
        prev_key = k
    return max(take, skip)


def knapsack01(items, cap):
    dp = [0] * (cap + 1)
    for v, w in items:
        for i in range(cap, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    return dp[cap]


def target_sum_ways(a, t):
    total = sum(a)
    if (total + t) % 2 or total < abs(t):
        return 0
    return count_subsets(a, (total + t) // 2)


def min_subset_diff(a):
    total = sum(a)
    half = total // 2
    dp = [False] * (half + 1)
    dp[0] = True
    for x in a:
        for i in range(half, x - 1, -1):
            dp[i] = dp[i] or dp[i - x]
    for i in range(half, -1, -1):
        if dp[i]:
            return total - 2 * i
    return total


def unbounded_knapsack(items, cap):
    dp = [0] * (cap + 1)
    for i in range(1, cap + 1):
        for v, w in items:
            if w <= i:
                dp[i] = max(dp[i], dp[i - w] + v)
    return dp[cap]


def rod_cutting(prices):
    n = len(prices)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j])
    return dp[n]


def ribbon_cut(n, sizes):
    NEG = float("-inf")
    dp = [0] + [NEG] * n
    for i in range(1, n + 1):
        for x in sizes:
            if x <= i and dp[i - x] != NEG:
                dp[i] = max(dp[i], dp[i - x] + 1)
    return dp[n] if dp[n] != NEG else -1


def integer_break(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * max(i - j, dp[i - j]))
    return dp[n]


def edit_distance(a, b):
    dp = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, dp[0] = dp[0], i
        for j in range(1, len(b) + 1):
            cur = dp[j]
            dp[j] = prev if a[i - 1] == b[j - 1] else 1 + min(prev, dp[j], dp[j - 1])
            prev = cur
    return dp[len(b)]


def delete_ops(a, b):
    return len(a) + len(b) - 2 * lcs(a, b)


def ascii_delete_sum(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        dp[i][0] = dp[i - 1][0] + ord(a[i - 1])
    for j in range(1, len(b) + 1):
        dp[0][j] = dp[0][j - 1] + ord(b[j - 1])
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + ord(a[i - 1]),
                               dp[i][j - 1] + ord(b[j - 1]))
    return dp[len(a)][len(b)]


def is_interleave(a, b, c):
    if len(a) + len(b) != len(c):
        return False
    dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
    dp[0][0] = True
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i and dp[i - 1][j] and a[i - 1] == c[i + j - 1]:
                dp[i][j] = True
            if j and dp[i][j - 1] and b[j - 1] == c[i + j - 1]:
                dp[i][j] = True
    return dp[len(a)][len(b)]


def num_distinct(s, t):
    dp = [1] + [0] * len(t)
    for ch in s:
        for j in range(len(t), 0, -1):
            if t[j - 1] == ch:
                dp[j] += dp[j - 1]
    return dp[len(t)]


def one_edit(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) > len(b):
        a, b = b, a
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    if i == len(a):
        return len(a) + 1 == len(b)
    if len(a) == len(b):
        return a[i + 1:] == b[i + 1:]
    return a[i:] == b[i + 1:]


def scs_len(a, b):
    return len(a) + len(b) - lcs(a, b)


def lps(s):
    return lcs(s, s[::-1])


def mcm(dims):
    n = len(dims)
    dp = [[0] * n for _ in range(n)]
    for size in range(2, n):
        for i in range(1, n - size + 1):
            j = i + size - 1
            dp[i][j] = min(dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                           for k in range(i, j))
    return dp[1][n - 1]


def longest_pal_substr(s):
    """Leftmost longest, so the answer is unique."""
    best = ""
    for i in range(len(s)):
        for lo, hi in ((i, i), (i, i + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            cand = s[lo + 1:hi]
            if len(cand) > len(best):
                best = cand
    return best


def count_pal_substrings(s):
    n = 0
    for i in range(len(s)):
        for lo, hi in ((i, i), (i, i + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                n += 1
                lo -= 1
                hi += 1
    return n


def min_insertions_pal(s):
    return len(s) - lps(s)


def min_cut_pal(s):
    n = len(s)
    pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                pal[i][j] = True
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        best = float("inf")
        for j in range(i, n):
            if pal[i][j]:
                best = min(best, 1 + dp[j + 1])
        dp[i] = best
    return dp[0] - 1


def burst_balloons(a):
    v = [1] + list(a) + [1]
    n = len(v)
    dp = [[0] * n for _ in range(n)]
    for size in range(2, n):
        for i in range(n - size):
            j = i + size
            dp[i][j] = max(dp[i][k] + dp[k][j] + v[i] * v[k] * v[j]
                           for k in range(i + 1, j))
    return dp[0][n - 1]


def boolean_paren(s):
    syms, ops = s[::2], s[1::2]
    n = len(syms)
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]
    for i in range(n):
        T[i][i] = 1 if syms[i] == "T" else 0
        F[i][i] = 1 if syms[i] == "F" else 0
    for size in range(2, n + 1):
        for i in range(n - size + 1):
            j = i + size - 1
            for k in range(i, j):
                op = ops[k]
                lt, lf, rt, rf = T[i][k], F[i][k], T[k + 1][j], F[k + 1][j]
                if op == "&":
                    T[i][j] += lt * rt
                    F[i][j] += lt * rf + lf * rt + lf * rf
                elif op == "|":
                    T[i][j] += lt * rt + lt * rf + lf * rt
                    F[i][j] += lf * rf
                else:                                   # ^
                    T[i][j] += lt * rf + lf * rt
                    F[i][j] += lt * rt + lf * rf
    return T[0][n - 1]


def min_cost_cut_stick(n, cuts):
    pts = [0] + sorted(cuts) + [n]
    m = len(pts)
    dp = [[0] * m for _ in range(m)]
    for size in range(2, m):
        for i in range(m - size):
            j = i + size
            dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) \
                + pts[j] - pts[i]
    return dp[0][m - 1]


def partition_max_sum(a, k):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        mx = 0
        for L in range(1, min(k, i) + 1):
            mx = max(mx, a[i - L])
            dp[i] = max(dp[i], dp[i - L] + mx * L)
    return dp[n]


DP_ARR = [
    "1 2 3 1",
    "2 7 9 3 1",
    "5 5 10 100 10 5",
    "2 1 1 2",
    "10 3 2 8 7",
    "1 2 3 4 5",
    "4 1 2 7 5 3",
    "1",
]


def _items(s):
    """First line 'n W', then n lines of 'value weight'."""
    n, cap = ints(rows(s)[0])[0], ints(rows(s)[0])[1]
    return [tuple(ints(rows(s)[1 + i])) for i in range(n)], cap


# -------------------------------------------------------------- write-ups ----
PROBLEMS = [
    # ---- LEC-31 ------------------------------------------------------------
    dict(title="Classwork: LC70 Climbing Stairs",
         stmt="You climb a staircase of `n` steps, taking 1 or 2 steps at a time. Print the number of distinct ways to reach the top.",
         inp="A single line containing `n`.", out=NUM_OUT, cons="- `1 <= n <= 45`",
         solve=lambda s: str(climb(int(s))),
         cases=["2", "3", "5", "10", "20", "45", "4", "1"]),

    dict(title="Classwork: LC198 House Robber",
         stmt="Houses in a row hold money, but robbing two adjacent houses trips the alarm. Print the maximum you can take.",
         inp=ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 100`\n- `0 <= amount <= 400`",
         solve=lambda s: str(rob(ints(s))), cases=DP_ARR),

    dict(title="Classwork: LC509 Fibonacci Number",
         stmt="Print `F(n)`, where `F(0) = 0`, `F(1) = 1`, and each later term is the sum of the previous two.",
         inp="A single line containing `n`.", out=NUM_OUT, cons="- `0 <= n <= 90`",
         solve=lambda s: str(fib(int(s))),
         cases=["2", "3", "10", "30", "50", "90", "1", "0"]),

    dict(title="Homework: LC746 Min Cost Climbing Stairs",
         stmt="Each step costs something to stand on. You may start at index 0 or 1 and climb one or two steps. Print the minimum cost to get past the top.",
         inp=ARR_IN, out=NUM_OUT,
         cons="- `2 <= n <= 1000`\n- `0 <= cost <= 999`",
         solve=lambda s: str(min_cost_climb(ints(s))),
         cases=["10 15 20", "1 100 1 1 1 100 1 1 100 1", "1 2",
                "5 5", "1 2 3 4 5", "10 1 1 10", "2 1 1 2", "0 0 0 0"]),

    dict(title="Homework: LC213 House Robber II",
         stmt="As House Robber, but the houses form a **circle**, so the first and last are adjacent. Print the maximum you can take.",
         inp=ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 100`\n- `0 <= amount <= 1000`",
         solve=lambda s: str(rob2(ints(s))), cases=DP_ARR),

    dict(title="Homework: LC91 Decode Ways",
         stmt="A digit string was produced by mapping `A`-`Z` to `1`-`26`. Print the number of ways to decode it.",
         inp="A single line: the digit string.", out=NUM_OUT,
         cons="- `1 <= length <= 100`\n- digits only",
         solve=lambda s: str(decode_ways(s.strip())),
         cases=["12", "226", "06", "10", "2101", "1111", "27", "100"]),

    # ---- LEC-32 ------------------------------------------------------------
    dict(title="Classwork: LC322 Coin Change",
         stmt="Given denominations and an amount, print the fewest coins that make it, or `-1` if impossible. Coins may be reused freely.",
         inp="The first line contains the denominations. The second line contains the "
             "amount.",
         out="A single line: the minimum number of coins, or `-1`.",
         cons="- `1 <= number of coins <= 12`\n- `0 <= amount <= 10^4`",
         solve=lambda s: str(coin_change_min(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 2 5\n11", "1 3 4\n6", "2\n3", "1 2 5\n100",
                "2 5 10 1\n27", "3 7\n5", "1 5 10 25\n63", "1\n0"]),

    dict(title="Classwork: LC518 Coin Change II",
         stmt="Print the number of **combinations** of coins making the amount. Order does not matter, so `1+2` and `2+1` count once.",
         inp="The first line contains the denominations. The second line contains the "
             "amount.",
         out=NUM_OUT,
         cons="- `1 <= number of coins <= 300`\n- `0 <= amount <= 5000`",
         solve=lambda s: str(coin_change_ways(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 2 5\n5", "1 2 5\n11", "2\n3", "10\n10",
                "2 3 5\n8", "1 2\n4", "5 10 25\n30", "1\n0"]),

    dict(title="Homework: LC377 Combination Sum IV",
         stmt="Print the number of **ordered** sequences of the given numbers summing to the target -- here `1+2` and `2+1` count separately.",
         inp="The first line contains the numbers. The second line contains the target.",
         out=NUM_OUT, cons="- `1 <= n <= 200`\n- `1 <= target <= 1000`",
         solve=lambda s: str(comb_sum4(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 2 3\n4", "9\n3", "1 2 5\n5", "2 3\n7",
                "1 2\n4", "3 5\n8", "1 2 3\n10", "1\n5"]),

    dict(title="Homework: LC279 Perfect Squares",
         stmt="Print the fewest perfect squares that sum to `n`.",
         inp="A single line containing `n`.", out=NUM_OUT, cons="- `1 <= n <= 10^4`",
         solve=lambda s: str(perfect_squares(int(s))),
         cases=["12", "13", "4", "48", "100", "7", "9999", "1"]),

    dict(title="Homework: Number of ways to make change (GfG)",
         stmt="Given denominations and an amount, print the number of distinct combinations making it. Order does not matter.",
         inp="The first line contains the denominations. The second line contains the "
             "amount.",
         out=NUM_OUT,
         cons="- `1 <= number of coins <= 300`\n- `0 <= amount <= 5000`",
         solve=lambda s: str(coin_change_ways(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 2 3\n4", "2 5 3 6\n10", "1 2 5\n5", "5 10\n15",
                "1 2\n3", "3\n7", "1 5 10 25\n30", "1\n0"]),

    # ---- LEC-33 ------------------------------------------------------------
    dict(title="Classwork: LC300 Longest Increasing Subsequence",
         stmt="Print the length of the longest strictly increasing subsequence.",
         inp=ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 2500`\n- Expected time `O(n^2)`",
         solve=lambda s: str(lis(ints(s))),
         cases=["10 9 2 5 3 7 101 18", "0 1 0 3 2 3", "7 7 7 7",
                "1 2 3 4 5", "5 4 3 2 1", "4 10 4 3 8 9", "2 2 3 1 4", "1"]),

    dict(title="Classwork: LC1143 Longest Common Subsequence",
         stmt="Print the length of the longest subsequence common to two strings.",
         inp=TWO_STR_IN, out=NUM_OUT, cons="- `1 <= length <= 1000`\n" + SLOW,
         solve=lambda s: str(lcs(rows(s)[0].strip(), rows(s)[1].strip())),
         cases=["abcde\nace", "abc\nabc", "abc\ndef", "bl\nyby",
                "abcba\nabcbcba", "aggtab\ngxtxayb", "ab\nba", "a\na"]),

    dict(title="Classwork: Longest Increasing Subsequence in O(n log n) (GfG)",
         stmt="Print the length of the longest strictly increasing subsequence, in `O(n log n)`.",
         inp=ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 10^5`\n- Expected time `O(n log n)`",
         solve=lambda s: str(lis(ints(s))),
         cases=["10 9 2 5 3 7 101 18", "0 1 0 3 2 3", "7 7 7 7",
                "1 2 3 4 5", "5 4 3 2 1", "4 10 4 3 8 9",
                "3 1 4 1 5 9 2 6", "1"]),

    dict(title="Homework: LC673 Number of Longest Increasing Subsequence",
         stmt="Print how many longest increasing subsequences the array has.",
         inp=ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 2000`",
         solve=lambda s: str(count_lis(ints(s))),
         cases=["1 3 5 4 7", "2 2 2 2 2", "1 2 4 3 5 4 7 2",
                "1 2 3", "3 2 1", "1 1 2 2 3", "5 4 3 2 1", "1"]),

    dict(title="Homework: LC1035 Uncrossed Lines",
         stmt="Two rows of numbers; connect equal numbers with straight lines that must not cross. Print the maximum number of lines.",
         inp="Two lines, each a list of space-separated integers.", out=NUM_OUT,
         cons="- `1 <= length <= 500`",
         solve=lambda s: str(lcs(ints(rows(s)[0]), ints(rows(s)[1]))),
         cases=["1 4 2\n1 2 4", "2 5 1 2 5\n10 5 2 1 5 2",
                "1 3 7 1 7 5\n1 9 2 5 1", "1 2\n3 4",
                "1 1 1\n1 1", "5 4 3\n3 4 5", "2 5 1\n1 5 2", "1\n1"]),

    dict(title="Homework: Longest common substring (GfG)",
         stmt="Print the length of the longest **contiguous** string appearing in both inputs.",
         inp=TWO_STR_IN, out=NUM_OUT, cons="- `1 <= length <= 1000`",
         solve=lambda s: str(lcsubstr(rows(s)[0].strip(), rows(s)[1].strip())),
         cases=["abcde\nabfce", "abc\nabc", "abc\ndef",
                "geeksforgeeks\ngeeks", "abcdxyz\nxyzabcd", "zzz\nzz",
                "abab\nbaba", "a\na"]),

    # ---- LEC-34 ------------------------------------------------------------
    dict(title="Classwork: LC62 Unique Paths",
         stmt="A robot starts top-left of an `m` by `n` grid and moves only right or down. Print the number of distinct paths to the bottom-right.",
         inp="A single line containing `m` and `n`.", out=NUM_OUT,
         cons="- `1 <= m, n <= 100`",
         solve=lambda s: str(unique_paths(*ints(s))),
         cases=["3 7", "3 2", "2 2", "1 10", "5 5", "3 3", "7 3", "1 1"]),

    dict(title="Classwork: LC64 Minimum Path Sum",
         stmt="Print the minimum sum along a path from top-left to bottom-right of a grid, moving only right or down.",
         inp=GRID_IN, out=NUM_OUT, cons="- `1 <= m, n <= 200`\n- `0 <= value <= 100`",
         solve=lambda s: str(min_path_sum(grid_of(s))),
         cases=["3 3\n1 3 1\n1 5 1\n4 2 1", "2 3\n1 2 3\n4 5 6",
                "1 4\n1 2 3 4", "4 1\n1\n2\n3\n4", "2 2\n1 2\n1 1",
                "3 3\n1 1 1\n1 1 1\n1 1 1", "2 2\n0 0\n0 0", "1 1\n5"]),

    dict(title="Classwork: LC63 Unique Paths II",
         stmt="As Unique Paths, but some cells are blocked, marked `1`. Print the number of paths.",
         inp=GRID_IN + " `0` is free and `1` is an obstacle.", out=NUM_OUT,
         cons="- `1 <= m, n <= 100`",
         solve=lambda s: str(unique_paths_obstacles(grid_of(s))),
         cases=["3 3\n0 0 0\n0 1 0\n0 0 0", "2 2\n0 1\n0 0",
                "1 1\n1", "2 2\n1 0\n0 0",
                "3 3\n0 0 0\n0 0 0\n0 0 0", "2 3\n0 0 0\n0 1 0",
                "3 1\n0\n1\n0", "1 1\n0"]),

    dict(title="Homework: LC120 Triangle",
         stmt="Given a triangle of numbers, print the minimum path sum from top to bottom, where from index `i` you may move to `i` or `i+1` on the next row.",
         inp="The first line contains `n`. Each of the next `n` lines contains one row, "
             "the `i`-th having `i` numbers.",
         out=NUM_OUT, cons="- `1 <= n <= 200`",
         solve=lambda s: str(triangle_min(
             [ints(rows(s)[1 + i]) for i in range(int(rows(s)[0]))])),
         cases=["4\n2\n3 4\n6 5 7\n4 1 8 3", "2\n1\n2 3",
                "3\n1\n2 3\n4 5 6", "3\n-1\n2 3\n1 -1 -3",
                "2\n5\n1 1", "4\n1\n1 1\n1 1 1\n1 1 1 1",
                "3\n10\n1 20\n30 1 2", "1\n-10"]),

    dict(title="Homework: LC931 Minimum Falling Path Sum",
         stmt="Print the minimum sum of a falling path through a square matrix, each step moving down to the same column or either diagonal.",
         inp=GRID_IN + " The matrix is square.", out=NUM_OUT,
         cons="- `1 <= n <= 100`\n- `-100 <= value <= 100`",
         solve=lambda s: str(falling_path(grid_of(s))),
         cases=["3 3\n2 1 3\n6 5 4\n7 8 9", "2 2\n1 2\n3 4",
                "3 3\n-19 57 0\n-40 -5 0\n0 0 0", "2 2\n-1 -1\n-1 -1",
                "3 3\n1 1 1\n1 1 1\n1 1 1",
                "4 4\n1 2 3 4\n4 3 2 1\n1 2 3 4\n4 3 2 1",
                "2 2\n5 1\n1 5", "1 1\n-10"]),

    dict(title="Homework: LC221 Maximal Square",
         stmt="Given a binary matrix, print the **area** of the largest square containing only `1`s.",
         inp=GRID_IN + " Values are `0` or `1`.", out=NUM_OUT,
         cons="- `1 <= m, n <= 300`",
         solve=lambda s: str(maximal_square(grid_of(s))),
         cases=["4 5\n1 0 1 0 0\n1 0 1 1 1\n1 1 1 1 1\n1 0 0 1 0",
                "2 2\n0 1\n1 0", "1 1\n1",
                "3 3\n1 1 1\n1 1 1\n1 1 1", "2 3\n1 1 1\n1 1 1",
                "2 2\n1 1\n1 1", "3 3\n0 0 0\n0 0 0\n0 0 0", "1 1\n0"]),

    # ---- LEC-35 ------------------------------------------------------------
    dict(title="Classwork: Subset Sum (GfG)",
         stmt="Decide whether some subset of the array sums exactly to the target.",
         inp=ARR_IN + "\n\nA second line contains the target sum.", out=BOOL_OUT,
         cons="- `1 <= n <= 100`\n- `0 <= target <= 10^4`\n- values are non-negative",
         solve=lambda s: fmt_bool(subset_sum(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["3 34 4 12 5 2\n9", "3 34 4 12 5 2\n30", "1 2 3\n6",
                "2 4 6\n5", "1 1 1\n2", "5 10 15\n25", "1\n2", "1\n1"]),

    dict(title="Classwork: LC416 Partition Equal Subset Sum",
         stmt="Decide whether the array can be split into two subsets with equal sums.",
         inp=ARR_IN, out=BOOL_OUT, cons="- `1 <= n <= 200`\n- `1 <= value <= 100`",
         solve=lambda s: fmt_bool(can_partition(ints(s))),
         cases=["1 5 11 5", "1 2 3 5", "1 1", "1 2 5",
                "2 2 2 2", "3 3 3 4 5", "1 2 3 4 5 6 7", "1"]),

    dict(title="Homework: Count of subsets with a given sum (GfG)",
         stmt="Print how many subsets sum exactly to the target.\n\nNote the empty subset counts for target 0.",
         inp=ARR_IN + "\n\nA second line contains the target sum.", out=NUM_OUT,
         cons="- `1 <= n <= 100`\n- `0 <= target <= 10^4`\n- values are non-negative",
         solve=lambda s: str(count_subsets(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["2 3 5 6 8 10\n10", "1 2 3 3\n6", "1 1 1\n1",
                "0 0 1\n1", "2 4 6\n6", "1 2 3\n3", "5 5 5\n10", "1\n0"]),

    dict(title="Homework: Maximum sum of non-adjacent elements (GfG)",
         stmt="Print the maximum sum of a subset containing no two adjacent elements.",
         inp=ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- values are non-negative",
         solve=lambda s: str(rob(ints(s))), cases=DP_ARR),

    dict(title="Homework: LC740 Delete and Earn",
         stmt="Taking a number earns its value but deletes every copy of it and every copy of the numbers one above and one below. Print the maximum total.",
         inp=ARR_IN, out=NUM_OUT,
         cons="- `1 <= n <= 2 * 10^4`\n- `1 <= value <= 10^4`",
         solve=lambda s: str(delete_and_earn(ints(s))),
         cases=["3 4 2", "2 2 3 3 3 4", "1 1 1", "1 2 3 4",
                "10 3 3 3 5 5 5 5 8", "1 10 100", "2 4 6 8", "1"]),

    # ---- LEC-36 ------------------------------------------------------------
    dict(title="Classwork: 0/1 Knapsack (GfG)",
         stmt="Each item may be taken whole or not at all. Print the maximum value that fits the capacity.",
         inp="The first line contains `n` and the capacity `W`. Each of the next `n` lines "
             "contains an item's value and weight.",
         out=NUM_OUT, cons="- `1 <= n <= 1000`\n- `1 <= W <= 1000`",
         solve=lambda s: str(knapsack01(*_items(s))),
         cases=["3 50\n60 10\n100 20\n120 30", "1 10\n60 10",
                "1 5\n60 10", "2 5\n10 4\n40 5",
                "4 8\n1 1\n2 2\n5 4\n6 5", "2 3\n5 2\n5 2",
                "3 4\n10 1\n20 2\n30 3", "2 1\n100 2\n1 1"]),

    dict(title="Classwork: LC494 Target Sum",
         stmt="Assign `+` or `-` to every number so the expression equals the target. Print the number of ways.",
         inp=ARR_IN + "\n\nA second line contains the target.", out=NUM_OUT,
         cons="- `1 <= n <= 20`\n- `0 <= value <= 1000`",
         solve=lambda s: str(target_sum_ways(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 1 1 1 1\n3", "1\n1", "1\n2", "1 2 1\n2",
                "0 0 0\n0", "1 2 3\n0", "2 2 2\n2", "1 1\n0"]),

    dict(title="Homework: Count subsets with a given difference (GfG)",
         stmt="Split the array into two subsets whose sums differ by exactly `d`. Print the number of ways.",
         inp=ARR_IN + "\n\nA second line contains the difference `d`.", out=NUM_OUT,
         cons="- `1 <= n <= 100`\n- values are non-negative",
         solve=lambda s: str(target_sum_ways(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 1 2 3\n1", "1 2 3 1 2\n1", "1 1 1 1\n0",
                "1\n1", "1\n0", "2 4 6\n2", "1 2 3\n0", "5 5\n0"]),

    dict(title="Homework: LC1049 Last Stone Weight II",
         stmt="Repeatedly smash any two stones, leaving their difference. Print the smallest possible final weight.",
         inp=ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 30`\n- `1 <= weight <= 100`",
         solve=lambda s: str(min_subset_diff(ints(s))),
         cases=["2 7 4 1 8 1", "31 26 33 21 40", "1 1", "1 2",
                "1 2 3 4 5", "5 5 5", "10 20 30", "1"]),

    dict(title="Homework: Minimum subset-sum difference (GfG)",
         stmt="Split the array into two subsets and print the minimum possible difference between their sums.",
         inp=ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 100`\n- values are non-negative",
         solve=lambda s: str(min_subset_diff(ints(s))),
         cases=["1 6 11 5", "1 4", "1 2 3 4", "10 20 15 5 25",
                "1 1", "8 6 5", "3 1 4 2 2", "1"]),

    # ---- LEC-37 ------------------------------------------------------------
    dict(title="Classwork: Unbounded Knapsack (GfG)",
         stmt="Each item may be taken any number of times. Print the maximum value fitting the capacity.",
         inp="The first line contains `n` and the capacity `W`. Each of the next `n` lines "
             "contains an item's value and weight.",
         out=NUM_OUT, cons="- `1 <= n <= 1000`\n- `1 <= W <= 1000`",
         solve=lambda s: str(unbounded_knapsack(*_items(s))),
         cases=["3 100\n10 5\n30 10\n20 15", "1 10\n5 2",
                "1 5\n10 10", "2 8\n3 2\n5 3", "2 6\n1 1\n10 6",
                "3 10\n1 1\n5 5\n10 10", "1 7\n2 3", "2 4\n4 2\n5 3"]),

    dict(title="Classwork: Rod Cutting (GfG)",
         stmt="A rod of length `n` can be cut into integer pieces, where a piece of length `i` sells for a given price. Print the maximum revenue.",
         inp="A single line: the price for a piece of length 1, 2, ... up to `n`. `n` is "
             "the number of prices.",
         out=NUM_OUT, cons="- `1 <= n <= 1000`",
         solve=lambda s: str(rod_cutting(ints(s))),
         cases=["1 5 8 9 10 17 17 20", "3 5 8 9 10 17 17 20",
                "1 5", "5 1", "1 1 1 1", "2 3 7 8 9", "3 5 8 9", "2"]),

    dict(title="Homework: Maximum ribbon cut (GfG)",
         stmt="Cut a ribbon of length `n` into pieces whose lengths come from a given set, reusing lengths freely. Print the maximum number of pieces, or `-1` if it cannot be cut exactly.",
         inp="The first line contains `n`. The second line contains the allowed piece "
             "lengths.",
         out="A single line: the maximum number of pieces, or `-1`.",
         cons="- `1 <= n <= 5000`",
         solve=lambda s: str(ribbon_cut(int(rows(s)[0]), ints(rows(s)[1]))),
         cases=["5\n5 3 2", "7\n5 3 2", "5\n4 6", "13\n5 3 2",
                "10\n2", "3\n2", "12\n3 4 5", "1\n1"]),

    dict(title="Homework: LC343 Integer Break",
         stmt="Break `n` into at least two positive integers and print the largest possible product of the parts.",
         inp="A single line containing `n`.", out=NUM_OUT, cons="- `2 <= n <= 58`",
         solve=lambda s: str(integer_break(int(s))),
         cases=["2", "10", "3", "4", "8", "11", "58", "5"]),

    # ---- LEC-38 ------------------------------------------------------------
    dict(title="Classwork: LC72 Edit Distance",
         stmt="Print the minimum number of single-character inserts, deletes or replacements to turn the first string into the second.",
         inp=TWO_STR_IN, out=NUM_OUT, cons="- `0 <= length <= 500`",
         solve=lambda s: str(edit_distance(rows(s)[0].strip(), rows(s)[1].strip())),
         cases=["horse\nros", "intention\nexecution", "ab\nba",
                "abc\nabc", "sunday\nsaturday", "a\nb",
                "abcd\nabc", "a\na"]),

    dict(title="Classwork: LC583 Delete Operation for Two Strings",
         stmt="Print the minimum number of character deletions, from either string, needed to make them equal.",
         inp=TWO_STR_IN, out=NUM_OUT, cons="- `1 <= length <= 500`",
         solve=lambda s: str(delete_ops(rows(s)[0].strip(), rows(s)[1].strip())),
         cases=["sea\neat", "leetcode\netco", "ab\nba", "abc\ndef",
                "same\nsame", "abcd\nabc", "xy\nyx", "a\na"]),

    dict(title="Classwork: LC712 Minimum ASCII Delete Sum for Two Strings",
         stmt="Print the smallest possible sum of the ASCII values of the characters you delete to make two strings equal.",
         inp=TWO_STR_IN, out=NUM_OUT,
         cons="- `1 <= length <= 1000`\n- lowercase English letters",
         solve=lambda s: str(ascii_delete_sum(rows(s)[0].strip(), rows(s)[1].strip())),
         cases=["sea\neat", "delete\nleet", "ab\nba", "abc\ndef",
                "same\nsame", "a\nb", "xyz\nxz", "a\na"]),

    dict(title="Homework: LC97 Interleaving String",
         stmt="Decide whether the third string is formed by interleaving the first two, each keeping its own order.",
         inp="Three lines: the two source strings, then the candidate interleaving.",
         out=BOOL_OUT, cons="- `0 <= length <= 100`",
         solve=lambda s: fmt_bool(is_interleave(rows(s)[0].strip(),
                                                rows(s)[1].strip(),
                                                rows(s)[2].strip())),
         cases=["aabcc\ndbbca\naadbbcbcac", "aabcc\ndbbca\naadbbbaccc",
                "a\nb\nab", "a\nb\nba", "abc\ndef\nadbecf",
                "ab\ncd\nabdc", "abc\n\nabc", "a\n\na"]),

    dict(title="Homework: LC115 Distinct Subsequences",
         stmt="Print the number of distinct subsequences of the first string that equal the second.",
         inp=TWO_STR_IN, out=NUM_OUT, cons="- `1 <= length <= 1000`",
         solve=lambda s: str(num_distinct(rows(s)[0].strip(), rows(s)[1].strip())),
         cases=["rabbbit\nrabbit", "babgbag\nbag", "a\nb",
                "aaa\na", "aaa\naa", "abc\nabc", "abcde\nace", "a\na"]),

    dict(title="Homework: LC161 One Edit Distance",
         stmt="Decide whether two strings are exactly one edit apart -- one insert, one delete, or one replace.",
         inp=TWO_STR_IN, out=BOOL_OUT, cons="- `0 <= length <= 10^4`",
         solve=lambda s: fmt_bool(one_edit(rows(s)[0].strip(),
                                          rows(s)[1].strip() if len(rows(s)) > 1 else "")),
         cases=["ab\nacb", "cab\nad", "1203\n1213", "a\na",
                "abc\nabc", "abc\nab", "ab\nba", "a\nb"]),

    # ---- LEC-39 ------------------------------------------------------------
    dict(title="Classwork: LC1092 Shortest Common Supersequence",
         stmt="Print the **length** of the shortest string having both inputs as subsequences.",
         inp=TWO_STR_IN, out=NUM_OUT, cons="- `1 <= length <= 1000`",
         solve=lambda s: str(scs_len(rows(s)[0].strip(), rows(s)[1].strip())),
         cases=["abac\ncab", "aaaaaaaa\naaaaaaaa", "a\nb", "abc\nabc",
                "ab\nba", "geek\neke", "abcd\nxycd", "xy\nyx"]),

    dict(title="Classwork: LC516 Longest Palindromic Subsequence",
         stmt="Print the length of the longest palindromic subsequence.",
         inp=STR_IN, out=NUM_OUT, cons="- `1 <= length <= 1000`",
         solve=lambda s: str(lps(s.strip())),
         cases=["bbbab", "cbbd", "aa", "abc", "agbdba",
                "character", "abcba", "a"]),

    dict(title="Classwork: Matrix Chain Multiplication (GfG)",
         stmt="Given the dimensions of a chain of matrices, print the minimum number of scalar multiplications needed to multiply them all.\n\nWith dimensions `p[0..n]`, matrix `i` is `p[i-1]` by `p[i]`.",
         inp="A single line: the dimension array, space separated.", out=NUM_OUT,
         cons="- `2 <= length of dimension array <= 100`",
         solve=lambda s: str(mcm(ints(s))),
         cases=["40 20 30 10 30", "10 20 30 40 30", "10 20 30",
                "1 2 3 4", "5 4 6 2 7", "1 2 3 4 5",
                "3 3 3 3", "2 3"]),

    dict(title="Homework: LC5 Longest Palindromic Substring",
         stmt="Print the longest palindromic **substring**. If several tie for longest, print the leftmost.",
         inp=STR_IN, out="A single line: the substring.", cons="- `1 <= length <= 1000`",
         solve=lambda s: longest_pal_substr(s.strip()),
         cases=["babad", "cbbd", "ac", "aaaa", "abcba",
                "forgeeksskeegfor", "abb", "a"]),

    dict(title="Homework: LC647 Palindromic Substrings",
         stmt="Print how many palindromic substrings a string contains, counting different positions separately.",
         inp=STR_IN, out=NUM_OUT, cons="- `1 <= length <= 1000`",
         solve=lambda s: str(count_pal_substrings(s.strip())),
         cases=["abc", "aaa", "aa", "abba", "aba",
                "abcba", "aaaa", "a"]),

    dict(title="Homework: LC1312 Minimum Insertion Steps to Make a String Palindrome",
         stmt="Print the fewest characters to insert anywhere to make the string a palindrome.",
         inp=STR_IN, out=NUM_OUT, cons="- `1 <= length <= 500`",
         solve=lambda s: str(min_insertions_pal(s.strip())),
         cases=["zzazz", "mbadm", "leetcode", "ab",
                "aba", "abcd", "abcba", "a"]),

    # ---- LEC-40 ------------------------------------------------------------
    dict(title="Classwork: LC132 Palindrome Partitioning II",
         stmt="Print the minimum number of cuts so every piece of the string is a palindrome.",
         inp=STR_IN, out=NUM_OUT, cons="- `1 <= length <= 2000`",
         solve=lambda s: str(min_cut_pal(s.strip())),
         cases=["aab", "ab", "abbab", "aabb", "abcba",
                "noonabbad", "aaa", "a"]),

    dict(title="Classwork: LC312 Burst Balloons",
         stmt="Bursting a balloon earns the product of it and its two current neighbours, then it is removed. Print the maximum coins obtainable.",
         inp=ARR_IN, out=NUM_OUT, cons="- `1 <= n <= 300`\n- `0 <= value <= 100`",
         solve=lambda s: str(burst_balloons(ints(s))),
         cases=["3 1 5 8", "1 5", "5", "1 2 3",
                "3 1 5", "2 4 6", "1 1 1 1", "1"]),

    dict(title="Homework: Boolean Parenthesization (GfG)",
         stmt="Given a boolean expression of `T` and `F` joined by `&`, `|` and `^`, print the number of ways to parenthesise it so it evaluates to **true**.",
         inp="A single line: the expression, symbols and operators alternating.",
         out=NUM_OUT,
         cons="- `1 <= number of symbols <= 100`\n- operators are `&`, `|`, `^`",
         solve=lambda s: str(boolean_paren(s.strip())),
         cases=["T|T&F^T", "T^F|F", "T&F", "T|F",
                "T^T", "T&T|F", "F", "T"]),

    dict(title="Homework: LC1547 Minimum Cost to Cut a Stick",
         stmt="A stick of length `n` must be cut at given positions, in any order. Each cut costs the length of the piece being cut. Print the minimum total cost.",
         inp="The first line contains `n`. The second line contains the cut positions.",
         out=NUM_OUT, cons="- `2 <= n <= 10^6`\n- `1 <= number of cuts <= 100`",
         solve=lambda s: str(min_cost_cut_stick(int(rows(s)[0]), ints(rows(s)[1]))),
         cases=["7\n1 3 4 5", "9\n5 6 1 4 2", "5\n2", "10\n5",
                "4\n1 2 3", "6\n1 5", "8\n2 4 6", "20\n10 5 15"]),

    dict(title="Homework: LC1043 Partition Array for Maximum Sum",
         stmt="Split the array into contiguous runs of at most `k` elements. Every element in a run becomes that run's maximum. Print the largest possible total.",
         inp=ARR_IN + "\n\nA second line contains `k`.", out=NUM_OUT,
         cons="- `1 <= n <= 500`\n- `1 <= k <= n`\n- `0 <= value <= 10^6`",
         solve=lambda s: str(partition_max_sum(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["1 15 7 9 2 5 10\n3", "1 4 1 5 7 3 6 1 9 9 3\n4",
                "1 2 3\n1", "1 2 3\n3", "5 5 5\n2",
                "1 100 1\n2", "2 1 4 3\n2", "1\n1"]),
]


# ---- answers worked out by hand; generation aborts if one disagrees ---------
SANITY = [
    ("Classwork: LC70 Climbing Stairs", "2", "2"),
    ("Classwork: LC70 Climbing Stairs", "3", "3"),
    ("Classwork: LC70 Climbing Stairs", "5", "8"),
    ("Classwork: LC198 House Robber", "1 2 3 1", "4"),
    ("Classwork: LC198 House Robber", "2 7 9 3 1", "12"),
    ("Classwork: LC509 Fibonacci Number", "10", "55"),
    ("Classwork: LC509 Fibonacci Number", "0", "0"),
    ("Homework: LC746 Min Cost Climbing Stairs", "10 15 20", "15"),
    ("Homework: LC746 Min Cost Climbing Stairs",
     "1 100 1 1 1 100 1 1 100 1", "6"),
    ("Homework: LC213 House Robber II", "1 2 3 1", "4"),
    ("Homework: LC91 Decode Ways", "12", "2"),
    ("Homework: LC91 Decode Ways", "226", "3"),
    ("Homework: LC91 Decode Ways", "06", "0"),
    ("Classwork: LC322 Coin Change", "1 2 5\n11", "3"),
    ("Classwork: LC322 Coin Change", "1 3 4\n6", "2"),
    ("Classwork: LC322 Coin Change", "2\n3", "-1"),
    ("Classwork: LC518 Coin Change II", "1 2 5\n5", "4"),
    ("Classwork: LC518 Coin Change II", "2\n3", "0"),
    ("Homework: LC377 Combination Sum IV", "1 2 3\n4", "7"),
    ("Homework: LC279 Perfect Squares", "12", "3"),
    ("Homework: LC279 Perfect Squares", "13", "2"),
    ("Homework: Number of ways to make change (GfG)", "1 2 3\n4", "4"),
    ("Classwork: LC300 Longest Increasing Subsequence",
     "10 9 2 5 3 7 101 18", "4"),
    ("Classwork: LC300 Longest Increasing Subsequence", "7 7 7 7", "1"),
    ("Classwork: LC1143 Longest Common Subsequence", "abcde\nace", "3"),
    ("Classwork: LC1143 Longest Common Subsequence", "abc\ndef", "0"),
    ("Classwork: Longest Increasing Subsequence in O(n log n) (GfG)",
     "10 9 2 5 3 7 101 18", "4"),
    ("Homework: LC673 Number of Longest Increasing Subsequence",
     "1 3 5 4 7", "2"),
    ("Homework: LC673 Number of Longest Increasing Subsequence",
     "2 2 2 2 2", "5"),
    ("Homework: LC1035 Uncrossed Lines", "1 4 2\n1 2 4", "2"),
    ("Homework: Longest common substring (GfG)", "abcde\nabfce", "2"),
    ("Homework: Longest common substring (GfG)", "geeksforgeeks\ngeeks", "5"),
    ("Classwork: LC62 Unique Paths", "3 7", "28"),
    ("Classwork: LC62 Unique Paths", "3 2", "3"),
    ("Classwork: LC64 Minimum Path Sum", "3 3\n1 3 1\n1 5 1\n4 2 1", "7"),
    ("Classwork: LC64 Minimum Path Sum", "2 3\n1 2 3\n4 5 6", "12"),
    ("Classwork: LC63 Unique Paths II", "3 3\n0 0 0\n0 1 0\n0 0 0", "2"),
    ("Classwork: LC63 Unique Paths II", "1 1\n1", "0"),
    ("Homework: LC120 Triangle", "4\n2\n3 4\n6 5 7\n4 1 8 3", "11"),
    ("Homework: LC931 Minimum Falling Path Sum",
     "3 3\n2 1 3\n6 5 4\n7 8 9", "13"),
    ("Homework: LC221 Maximal Square",
     "4 5\n1 0 1 0 0\n1 0 1 1 1\n1 1 1 1 1\n1 0 0 1 0", "4"),
    ("Homework: LC221 Maximal Square", "2 2\n0 1\n1 0", "1"),
    ("Classwork: Subset Sum (GfG)", "3 34 4 12 5 2\n9", "true"),
    ("Classwork: Subset Sum (GfG)", "3 34 4 12 5 2\n30", "false"),
    ("Classwork: LC416 Partition Equal Subset Sum", "1 5 11 5", "true"),
    ("Classwork: LC416 Partition Equal Subset Sum", "1 2 3 5", "false"),
    ("Homework: Count of subsets with a given sum (GfG)",
     "2 3 5 6 8 10\n10", "3"),
    ("Homework: Maximum sum of non-adjacent elements (GfG)", "1 2 3 1", "4"),
    ("Homework: LC740 Delete and Earn", "3 4 2", "6"),
    ("Homework: LC740 Delete and Earn", "2 2 3 3 3 4", "9"),
    ("Classwork: 0/1 Knapsack (GfG)", "3 50\n60 10\n100 20\n120 30", "220"),
    ("Classwork: 0/1 Knapsack (GfG)", "1 5\n60 10", "0"),
    ("Classwork: LC494 Target Sum", "1 1 1 1 1\n3", "5"),
    ("Classwork: LC494 Target Sum", "1\n2", "0"),
    ("Homework: Count subsets with a given difference (GfG)", "1 1 2 3\n1", "3"),
    ("Homework: LC1049 Last Stone Weight II", "2 7 4 1 8 1", "1"),
    ("Homework: LC1049 Last Stone Weight II", "31 26 33 21 40", "5"),
    ("Homework: Minimum subset-sum difference (GfG)", "1 6 11 5", "1"),
    ("Classwork: Unbounded Knapsack (GfG)",
     "3 100\n10 5\n30 10\n20 15", "300"),
    ("Classwork: Rod Cutting (GfG)", "1 5 8 9 10 17 17 20", "22"),
    ("Classwork: Rod Cutting (GfG)", "3 5 8 9 10 17 17 20", "24"),
    ("Homework: Maximum ribbon cut (GfG)", "5\n5 3 2", "2"),
    ("Homework: Maximum ribbon cut (GfG)", "5\n4 6", "-1"),
    ("Homework: LC343 Integer Break", "2", "1"),
    ("Homework: LC343 Integer Break", "10", "36"),
    ("Classwork: LC72 Edit Distance", "horse\nros", "3"),
    ("Classwork: LC72 Edit Distance", "intention\nexecution", "5"),
    ("Classwork: LC583 Delete Operation for Two Strings", "sea\neat", "2"),
    ("Classwork: LC712 Minimum ASCII Delete Sum for Two Strings",
     "sea\neat", "231"),
    ("Classwork: LC712 Minimum ASCII Delete Sum for Two Strings",
     "delete\nleet", "403"),
    ("Homework: LC97 Interleaving String",
     "aabcc\ndbbca\naadbbcbcac", "true"),
    ("Homework: LC97 Interleaving String",
     "aabcc\ndbbca\naadbbbaccc", "false"),
    ("Homework: LC115 Distinct Subsequences", "rabbbit\nrabbit", "3"),
    ("Homework: LC115 Distinct Subsequences", "babgbag\nbag", "5"),
    ("Homework: LC161 One Edit Distance", "ab\nacb", "true"),
    ("Homework: LC161 One Edit Distance", "cab\nad", "false"),
    ("Homework: LC161 One Edit Distance", "abc\nabc", "false"),
    ("Classwork: LC1092 Shortest Common Supersequence", "abac\ncab", "5"),
    ("Classwork: LC516 Longest Palindromic Subsequence", "bbbab", "4"),
    ("Classwork: LC516 Longest Palindromic Subsequence", "cbbd", "2"),
    ("Classwork: Matrix Chain Multiplication (GfG)", "40 20 30 10 30", "26000"),
    ("Classwork: Matrix Chain Multiplication (GfG)", "10 20 30", "6000"),
    ("Homework: LC5 Longest Palindromic Substring", "babad", "bab"),
    ("Homework: LC5 Longest Palindromic Substring", "cbbd", "bb"),
    ("Homework: LC647 Palindromic Substrings", "abc", "3"),
    ("Homework: LC647 Palindromic Substrings", "aaa", "6"),
    ("Homework: LC1312 Minimum Insertion Steps to Make a String Palindrome",
     "zzazz", "0"),
    ("Homework: LC1312 Minimum Insertion Steps to Make a String Palindrome",
     "mbadm", "2"),
    ("Classwork: LC132 Palindrome Partitioning II", "aab", "1"),
    ("Classwork: LC132 Palindrome Partitioning II", "a", "0"),
    ("Classwork: LC312 Burst Balloons", "3 1 5 8", "167"),
    ("Classwork: LC312 Burst Balloons", "1 5", "10"),
    ("Homework: Boolean Parenthesization (GfG)", "T|T&F^T", "4"),
    ("Homework: Boolean Parenthesization (GfG)", "T^F|F", "2"),
    ("Homework: LC1547 Minimum Cost to Cut a Stick", "7\n1 3 4 5", "16"),
    ("Homework: LC1547 Minimum Cost to Cut a Stick", "9\n5 6 1 4 2", "22"),
    ("Homework: LC1043 Partition Array for Maximum Sum",
     "1 15 7 9 2 5 10\n3", "84"),
    ("Homework: LC1043 Partition Array for Maximum Sum",
     "1 4 1 5 7 3 6 1 9 9 3\n4", "83"),
]
