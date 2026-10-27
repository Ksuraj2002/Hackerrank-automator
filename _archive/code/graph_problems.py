#!/usr/bin/env python3
"""
graph_problems.py -- LEC 41-50: graphs, backtracking, two pointers.

Imported by make_md.py. Self-contained, like dp_problems.py.

CONVENTIONS, stated in every relevant problem so the expected output is never
ambiguous:
  * nodes are 0-indexed
  * unweighted graph input: first line "n m", then m lines "u v"
  * weighted graph input:   first line "n m", then m lines "u v w"
  * grid input:             first line "m n", then m rows
  * where a problem admits several valid answers (topological order, subsets,
    permutations), the statement demands the lexicographically smallest, or the
    full set in lexicographic order, so there is exactly one correct output.
"""

import heapq
from collections import Counter, defaultdict, deque


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
    m = ints(rows(s)[start - 1])[0]
    return [ints(rows(s)[start + i]) for i in range(m)]


def char_grid(s, start=1):
    m = ints(rows(s)[start - 1])[0]
    return [list(rows(s)[start + i].strip()) for i in range(m)]


def edges_of(s):
    """First line 'n m', then m lines 'u v'. Returns (n, [(u,v)])."""
    n, m = ints(rows(s)[0])
    return n, [tuple(ints(rows(s)[1 + i])) for i in range(m)]


def wedges_of(s):
    """First line 'n m', then m lines 'u v w'."""
    n, m = ints(rows(s)[0])
    return n, [tuple(ints(rows(s)[1 + i])) for i in range(m)]


def adj_undirected(n, es):
    g = [[] for _ in range(n)]
    for u, v in es:
        g[u].append(v)
        g[v].append(u)
    return g


NUM_OUT = "A single line containing one integer."
BOOL_OUT = "A single line: `true` or `false`."
SEQ_OUT = "A single line: the values separated by single spaces."
ARR_IN = "A single line of space-separated integers."
STR_IN = "A single line containing the string."
E_IN = ("The first line contains `n` (the number of nodes, numbered `0` to "
        "`n-1`) and `m` (the number of edges). Each of the next `m` lines "
        "contains two node numbers.")
W_IN = ("The first line contains `n` (nodes `0` to `n-1`) and `m`. Each of the "
        "next `m` lines contains `u`, `v` and the edge weight `w`.")
G_IN = ("The first line contains `m` and `n`. Each of the next `m` lines "
        "contains `n` integers.")


# ------------------------------------------------------------- solutions ----
def count_islands(g):
    if not g:
        return 0
    m, n, seen, total = len(g), len(g[0]), set(), 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1 and (i, j) not in seen:
                total += 1
                q = deque([(i, j)])
                seen.add((i, j))
                while q:
                    y, x = q.popleft()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < m and 0 <= nx < n and g[ny][nx] == 1 \
                                and (ny, nx) not in seen:
                            seen.add((ny, nx))
                            q.append((ny, nx))
    return total


def max_island_area(g):
    if not g:
        return 0
    m, n, seen, best = len(g), len(g[0]), set(), 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1 and (i, j) not in seen:
                area, q = 0, deque([(i, j)])
                seen.add((i, j))
                while q:
                    y, x = q.popleft()
                    area += 1
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < m and 0 <= nx < n and g[ny][nx] == 1 \
                                and (ny, nx) not in seen:
                            seen.add((ny, nx))
                            q.append((ny, nx))
                best = max(best, area)
    return best


def count_components(n, es):
    g = adj_undirected(n, es)
    seen, total = set(), 0
    for i in range(n):
        if i not in seen:
            total += 1
            st = [i]
            seen.add(i)
            while st:
                u = st.pop()
                for v in g[u]:
                    if v not in seen:
                        seen.add(v)
                        st.append(v)
    return total


def flood_fill(g, sr, sc, new):
    old = g[sr][sc]
    if old == new:
        return g
    m, n = len(g), len(g[0])
    q = deque([(sr, sc)])
    g[sr][sc] = new
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n and g[ny][nx] == old:
                g[ny][nx] = new
                q.append((ny, nx))
    return g


def path_exists(n, es, a, b):
    g = adj_undirected(n, es)
    seen, st = {a}, [a]
    while st:
        u = st.pop()
        if u == b:
            return True
        for v in g[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return a == b


def clone_adj(n, es):
    """Canonical form of the graph: sorted neighbours per node."""
    g = adj_undirected(n, es)
    return [sorted(set(x)) for x in g]


def can_finish(n, prereqs):
    """prereqs are directed edges u -> v meaning u before v."""
    g = [[] for _ in range(n)]
    deg = [0] * n
    for u, v in prereqs:
        g[u].append(v)
        deg[v] += 1
    q = deque(i for i in range(n) if deg[i] == 0)
    done = 0
    while q:
        u = q.popleft()
        done += 1
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    return done == n


def topo_smallest(n, es):
    """Kahn's with a min-heap: the lexicographically smallest valid order."""
    g = [[] for _ in range(n)]
    deg = [0] * n
    for u, v in es:
        g[u].append(v)
        deg[v] += 1
    h = [i for i in range(n) if deg[i] == 0]
    heapq.heapify(h)
    out = []
    while h:
        u = heapq.heappop(h)
        out.append(u)
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(h, v)
    return out if len(out) == n else []


def is_bipartite(n, es):
    g = adj_undirected(n, es)
    colour = [0] * n
    for s in range(n):
        if colour[s]:
            continue
        colour[s] = 1
        q = deque([s])
        while q:
            u = q.popleft()
            for v in g[u]:
                if colour[v] == 0:
                    colour[v] = -colour[u]
                    q.append(v)
                elif colour[v] == colour[u]:
                    return False
    return True


def undirected_cycle(n, es):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in es:
        ru, rv = find(u), find(v)
        if ru == rv:
            return True
        parent[ru] = rv
    return False


def directed_cycle(n, es):
    g = [[] for _ in range(n)]
    for u, v in es:
        g[u].append(v)
    state = [0] * n

    def dfs(u):
        state[u] = 1
        for v in g[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    return any(state[i] == 0 and dfs(i) for i in range(n))


def redundant_connection(n, es):
    """The last edge that closes a cycle."""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    ans = None
    for u, v in es:
        ru, rv = find(u), find(v)
        if ru == rv:
            ans = (u, v)
        else:
            parent[ru] = rv
    return ans


def alien_order(ws):
    """Lexicographically smallest valid letter order, or empty if impossible."""
    letters = set("".join(ws))
    g = defaultdict(set)
    deg = {c: 0 for c in letters}
    for a, b in zip(ws, ws[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in g[x]:
                    g[x].add(y)
                    deg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""
    h = [c for c in deg if deg[c] == 0]
    heapq.heapify(h)
    out = []
    while h:
        c = heapq.heappop(h)
        out.append(c)
        for d in sorted(g[c]):
            deg[d] -= 1
            if deg[d] == 0:
                heapq.heappush(h, d)
    return "".join(out) if len(out) == len(letters) else ""


def dijkstra(n, es, src, directed=False):
    g = [[] for _ in range(n)]
    for u, v, w in es:
        g[u].append((v, w))
        if not directed:
            g[v].append((u, w))
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    h = [(0, src)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(h, (dist[v], v))
    return dist


def network_delay(n, es, src):
    d = dijkstra(n, es, src, directed=True)
    return -1 if any(x == float("inf") for x in d) else max(d)


def min_effort(g):
    m, n = len(g), len(g[0])
    INF = float("inf")
    best = [[INF] * n for _ in range(m)]
    best[0][0] = 0
    h = [(0, 0, 0)]
    while h:
        e, y, x = heapq.heappop(h)
        if e > best[y][x]:
            continue
        if (y, x) == (m - 1, n - 1):
            return e
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n:
                ne = max(e, abs(g[ny][nx] - g[y][x]))
                if ne < best[ny][nx]:
                    best[ny][nx] = ne
                    heapq.heappush(h, (ne, ny, nx))
    return 0


def cheapest_k_stops(n, es, src, dst, k):
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        nxt = dist[:]
        for u, v, w in es:
            if dist[u] != INF and dist[u] + w < nxt[v]:
                nxt[v] = dist[u] + w
        dist = nxt
    return -1 if dist[dst] == INF else dist[dst]


def mst_cost_points(pts):
    """Prim on the complete graph of Manhattan distances."""
    n = len(pts)
    if n <= 1:
        return 0
    INF = float("inf")
    best = [INF] * n
    best[0] = 0
    used = [False] * n
    total = 0
    for _ in range(n):
        u = min((i for i in range(n) if not used[i]), key=lambda i: best[i])
        used[u] = True
        total += best[u]
        for v in range(n):
            if not used[v]:
                d = abs(pts[u][0] - pts[v][0]) + abs(pts[u][1] - pts[v][1])
                if d < best[v]:
                    best[v] = d
    return total


def zero_one_bfs(n, es, src):
    """Edges weigh 0 or 1; a deque replaces the heap."""
    g = [[] for _ in range(n)]
    for u, v, w in es:
        g[u].append((v, w))
        g[v].append((u, w))
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    q = deque([src])
    while q:
        u = q.popleft()
        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w:
                    q.append(v)
                else:
                    q.appendleft(v)
    return dist


def bellman_ford(n, es, src):
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in es:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in es:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None                     # negative cycle
    return dist


def floyd_warshall(n, es):
    INF = float("inf")
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in es:
        d[u][v] = min(d[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


def rotting_oranges(g):
    m, n = len(g), len(g[0])
    q = deque((i, j) for i in range(m) for j in range(n) if g[i][j] == 2)
    fresh = sum(1 for i in range(m) for j in range(n) if g[i][j] == 1)
    mins = 0
    while q and fresh:
        for _ in range(len(q)):
            y, x = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n and g[ny][nx] == 1:
                    g[ny][nx] = 2
                    fresh -= 1
                    q.append((ny, nx))
        mins += 1
    return -1 if fresh else mins


def zero_one_matrix(g):
    m, n = len(g), len(g[0])
    INF = float("inf")
    d = [[0 if g[i][j] == 0 else INF for j in range(n)] for i in range(m)]
    q = deque((i, j) for i in range(m) for j in range(n) if g[i][j] == 0)
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n and d[ny][nx] > d[y][x] + 1:
                d[ny][nx] = d[y][x] + 1
                q.append((ny, nx))
    return d


def shortest_binary_path(g):
    n = len(g)
    if g[0][0] or g[n - 1][n - 1]:
        return -1
    q = deque([(0, 0, 1)])
    seen = {(0, 0)}
    while q:
        y, x, d = q.popleft()
        if (y, x) == (n - 1, n - 1):
            return d
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and not g[ny][nx] \
                        and (ny, nx) not in seen:
                    seen.add((ny, nx))
                    q.append((ny, nx, d + 1))
    return -1


def bridges(n, es):
    g = adj_undirected(n, es)
    disc = [-1] * n
    low = [0] * n
    out = []
    timer = [0]

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        skipped = False
        for v in g[u]:
            if v == parent and not skipped:
                skipped = True
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    out.append(tuple(sorted((u, v))))
            else:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    return sorted(out)


# --- tree DP (input is a level-order tree, as in LEC 11-20) ------------------
class N:
    __slots__ = ("v", "l", "r")

    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


def build(s):
    t = s.split()
    if not t or t[0] == "null":
        return None
    root = N(int(t[0]))
    q, i = deque([root]), 1
    while q and i < len(t):
        n = q.popleft()
        if i < len(t):
            x = t[i]
            i += 1
            if x != "null":
                n.l = N(int(x))
                q.append(n.l)
        if i < len(t):
            x = t[i]
            i += 1
            if x != "null":
                n.r = N(int(x))
                q.append(n.r)
    return root


TREE_IN = ("A single line with the tree in level order, `null` for a missing "
           "child. An empty tree is the single token `null`.")


def rob3(root):
    def go(n):
        if not n:
            return 0, 0                      # (rob this, skip this)
        lr, ls = go(n.l)
        rr, rs = go(n.r)
        return n.v + ls + rs, max(lr, ls) + max(rr, rs)
    return max(go(root))


def min_cameras(root):
    """0 = needs cover, 1 = covered, 2 = has a camera."""
    total = [0]

    def go(n):
        if not n:
            return 1
        l, r = go(n.l), go(n.r)
        if l == 0 or r == 0:
            total[0] += 1
            return 2
        if l == 2 or r == 2:
            return 1
        return 0

    if go(root) == 0:
        total[0] += 1
    return total[0]


def longest_univalue(root):
    best = [0]

    def go(n):
        if not n:
            return 0
        l, r = go(n.l), go(n.r)
        el = l + 1 if n.l and n.l.v == n.v else 0
        er = r + 1 if n.r and n.r.v == n.v else 0
        best[0] = max(best[0], el + er)
        return max(el, er)

    go(root)
    return best[0]


def tree_non_adjacent(root):
    return rob3(root)


# --- backtracking -----------------------------------------------------------
def subsets(a):
    a = sorted(a)
    out = [[]]
    for x in a:
        out += [c + [x] for c in out]
    return sorted(out)


def subsets_unique(a):
    a = sorted(a)
    seen = set()
    out = []
    def go(i, cur):
        key = tuple(cur)
        if key not in seen:
            seen.add(key)
            out.append(list(cur))
        for j in range(i, len(a)):
            cur.append(a[j])
            go(j + 1, cur)
            cur.pop()
    go(0, [])
    return sorted(out)


def permutations_of(a):
    import itertools
    return sorted(set(itertools.permutations(sorted(a))))


def combinations_of(n, k):
    import itertools
    return sorted(itertools.combinations(range(1, n + 1), k))


def combination_sum(a, t):
    a = sorted(set(a))
    out = []
    def go(i, rem, cur):
        if rem == 0:
            out.append(list(cur))
            return
        for j in range(i, len(a)):
            if a[j] <= rem:
                cur.append(a[j])
                go(j, rem - a[j], cur)
                cur.pop()
    go(0, t, [])
    return sorted(out)


def palindrome_partitions(s):
    out = []
    def go(i, cur):
        if i == len(s):
            out.append(list(cur))
            return
        for j in range(i, len(s)):
            piece = s[i:j + 1]
            if piece == piece[::-1]:
                cur.append(piece)
                go(j + 1, cur)
                cur.pop()
    go(0, [])
    return sorted(out)


def word_search(g, word):
    m, n = len(g), len(g[0])

    def go(y, x, k, used):
        if k == len(word):
            return True
        if not (0 <= y < m and 0 <= x < n) or (y, x) in used \
                or g[y][x] != word[k]:
            return False
        used.add((y, x))
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if go(y + dy, x + dx, k + 1, used):
                used.discard((y, x))
                return True
        used.discard((y, x))
        return k + 1 == len(word) and False

    for i in range(m):
        for j in range(n):
            if go(i, j, 0, set()):
                return True
    return False


def n_queens_count(n):
    cols, d1, d2 = set(), set(), set()
    total = [0]

    def go(r):
        if r == n:
            total[0] += 1
            return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            cols.add(c); d1.add(r - c); d2.add(r + c)
            go(r + 1)
            cols.discard(c); d1.discard(r - c); d2.discard(r + c)

    go(0)
    return total[0]


def gen_parens(n):
    out = []
    def go(cur, o, c):
        if len(cur) == 2 * n:
            out.append(cur)
            return
        if o < n:
            go(cur + "(", o + 1, c)
        if c < o:
            go(cur + ")", o, c + 1)
    go("", 0, 0)
    return sorted(out)


def solve_sudoku(g):
    def ok(r, c, v):
        for i in range(9):
            if g[r][i] == v or g[i][c] == v:
                return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if g[i][j] == v:
                    return False
        return True

    def go():
        for r in range(9):
            for c in range(9):
                if g[r][c] == 0:
                    for v in range(1, 10):
                        if ok(r, c, v):
                            g[r][c] = v
                            if go():
                                return True
                            g[r][c] = 0
                    return False
        return True

    go()
    return g


def word_search_ii(g, ws):
    return sorted(w for w in set(ws) if word_search(g, w))


def restore_ip(s):
    out = []
    def go(i, parts):
        if len(parts) == 4:
            if i == len(s):
                out.append(".".join(parts))
            return
        for L in (1, 2, 3):
            if i + L > len(s):
                break
            seg = s[i:i + L]
            if (seg[0] == "0" and L > 1) or int(seg) > 255:
                continue
            go(i + L, parts + [seg])
    go(0, [])
    return sorted(out)


# --- two pointers -----------------------------------------------------------
def min_subarray_len(a, t):
    lo, run, best = 0, 0, float("inf")
    for hi, x in enumerate(a):
        run += x
        while run >= t:
            best = min(best, hi - lo + 1)
            run -= a[lo]
            lo += 1
    return 0 if best == float("inf") else best


def three_sum(a):
    a = sorted(a)
    out = set()
    for i in range(len(a) - 2):
        lo, hi = i + 1, len(a) - 1
        while lo < hi:
            t = a[i] + a[lo] + a[hi]
            if t == 0:
                out.add((a[i], a[lo], a[hi]))
                lo += 1
                hi -= 1
            elif t < 0:
                lo += 1
            else:
                hi -= 1
    return sorted(out)


def min_window(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    missing = len(t)
    best = (float("inf"), 0, 0)
    lo = 0
    for hi, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if hi - lo + 1 < best[0]:
                best = (hi - lo + 1, lo, hi + 1)
            need[s[lo]] += 1
            if need[s[lo]] > 0:
                missing += 1
            lo += 1
    return "" if best[0] == float("inf") else s[best[1]:best[2]]


def char_replacement(s, k):
    cnt = Counter()
    lo, best = 0, 0
    for hi, ch in enumerate(s):
        cnt[ch] += 1
        while (hi - lo + 1) - max(cnt.values()) > k:
            cnt[s[lo]] -= 1
            lo += 1
        best = max(best, hi - lo + 1)
    return best


def max_water(a):
    lo, hi, best = 0, len(a) - 1, 0
    while lo < hi:
        best = max(best, (hi - lo) * min(a[lo], a[hi]))
        if a[lo] < a[hi]:
            lo += 1
        else:
            hi -= 1
    return best


GRIDS01 = [
    "4 5\n1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1",
    "3 3\n1 1 1\n0 1 0\n1 1 1",
    "1 1\n1",
    "1 1\n0",
    "2 2\n1 0\n0 1",
    "3 4\n1 1 0 0\n0 0 1 1\n1 0 0 1",
    "2 3\n0 0 0\n0 0 0",
    "3 3\n1 0 1\n0 1 0\n1 0 1",
]

E_CASES = [
    "5 3\n0 1\n1 2\n3 4",
    "3 2\n0 1\n1 2",
    "4 4\n0 1\n1 2\n2 0\n2 3",
    "2 1\n0 1",
    "1 0",
    "6 4\n0 1\n2 3\n4 5\n0 2",
    "4 2\n0 1\n2 3",
    "5 4\n0 1\n1 2\n2 3\n3 4",
]


PROBLEMS = [
    # ---- LEC-41 : representation & traversal --------------------------------
    dict(title="Classwork: LC200 Number of Islands",
         stmt="A grid of `1`s (land) and `0`s (water). Print the number of islands, where an island is land connected horizontally or vertically.",
         inp=G_IN + " Values are `0` or `1`.", out=NUM_OUT,
         cons="- `1 <= m, n <= 300`",
         solve=lambda s: str(count_islands(grid_of(s))), cases=GRIDS01),

    dict(title="Classwork: LC547 Number of Provinces",
         stmt="Given an undirected graph, print the number of connected components.",
         inp=E_IN, out=NUM_OUT, cons="- `1 <= n <= 200`",
         solve=lambda s: str(count_components(*edges_of(s))), cases=E_CASES),

    dict(title="Classwork: LC133 Clone Graph",
         stmt="Given an undirected graph, build a deep copy and print the copy's adjacency list.",
         inp=E_IN,
         out="One line per node `0` to `n-1`: its neighbours in ascending order, space "
             "separated. An isolated node produces an empty line.",
         cons="- `0 <= n <= 100`",
         solve=lambda s: "\n".join(fmt(x) for x in clone_adj(*edges_of(s))),
         cases=E_CASES),

    dict(title="Homework: LC733 Flood Fill",
         stmt="Starting from one cell, repaint it and every cell reachable from it through equally-coloured horizontal or vertical neighbours.",
         inp=G_IN + "\n\nA final line contains the start row, start column and the new "
                    "colour.",
         out="The repainted grid: `m` lines of `n` integers.",
         cons="- `1 <= m, n <= 50`",
         solve=lambda s: "\n".join(
             fmt(r) for r in flood_fill(grid_of(s),
                                       *ints(rows(s)[1 + ints(rows(s)[0])[0]]))),
         cases=["3 3\n1 1 1\n1 1 0\n1 0 1\n1 1 2",
                "2 2\n0 0\n0 0\n0 0 0",
                "1 1\n0\n0 0 5",
                "2 2\n1 2\n3 4\n0 0 9",
                "3 3\n1 1 1\n1 1 1\n1 1 1\n1 1 2",
                "2 3\n0 1 0\n1 1 1\n1 1 2",
                "1 3\n1 1 1\n0 1 7",
                "3 1\n1\n1\n0\n0 0 4"]),

    dict(title="Homework: LC695 Max Area of Island",
         stmt="Print the number of cells in the largest island, where an island is `1`s connected horizontally or vertically. Print `0` if there is no land.",
         inp=G_IN + " Values are `0` or `1`.", out=NUM_OUT,
         cons="- `1 <= m, n <= 50`",
         solve=lambda s: str(max_island_area(grid_of(s))), cases=GRIDS01),

    dict(title="Homework: LC1971 Find if Path Exists in Graph",
         stmt="Decide whether a path exists between two nodes of an undirected graph.",
         inp=E_IN + "\n\nA final line contains the two node numbers.",
         out=BOOL_OUT, cons="- `1 <= n <= 2 * 10^5`",
         solve=lambda s: fmt_bool(path_exists(
             *edges_of(s), *ints(rows(s)[1 + ints(rows(s)[0])[1]]))),
         cases=["3 2\n0 1\n1 2\n0 2",
                "6 3\n0 1\n0 2\n3 5\n0 5",
                "1 0\n0 0",
                "2 1\n0 1\n0 1",
                "2 0\n0 1",
                "4 2\n0 1\n2 3\n1 3",
                "5 4\n0 1\n1 2\n2 3\n3 4\n0 4",
                "3 1\n0 1\n1 2"]),

    # ---- LEC-42 : cycles & bipartite ---------------------------------------
    dict(title="Classwork: LC207 Course Schedule",
         stmt="Courses have prerequisites: an edge `u v` means `u` must be taken before `v`. Decide whether every course can be finished.",
         inp=E_IN + " Edges are directed `u` to `v`.", out=BOOL_OUT,
         cons="- `1 <= n <= 2000`",
         solve=lambda s: fmt_bool(can_finish(*edges_of(s))), cases=E_CASES),

    dict(title="Classwork: LC785 Is Graph Bipartite?",
         stmt="Decide whether a graph's nodes can be split into two sets so that every edge joins the two sets.",
         inp=E_IN, out=BOOL_OUT, cons="- `1 <= n <= 100`",
         solve=lambda s: fmt_bool(is_bipartite(*edges_of(s))), cases=E_CASES),

    dict(title="Classwork: Detect cycle in an undirected graph (GfG)",
         stmt="Decide whether an undirected graph contains a cycle.",
         inp=E_IN, out=BOOL_OUT, cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt_bool(undirected_cycle(*edges_of(s))), cases=E_CASES),

    dict(title="Homework: Detect cycle in a directed graph (GfG)",
         stmt="Decide whether a directed graph contains a cycle.",
         inp=E_IN + " Edges are directed `u` to `v`.", out=BOOL_OUT,
         cons="- `1 <= n <= 10^5`",
         solve=lambda s: fmt_bool(directed_cycle(*edges_of(s))), cases=E_CASES),

    dict(title="Homework: LC886 Possible Bipartition",
         stmt="Some people dislike each other and must be split into two groups so that nobody shares a group with someone they dislike. Decide whether that is possible.",
         inp=E_IN + " Each edge is a mutual dislike.", out=BOOL_OUT,
         cons="- `1 <= n <= 2000`",
         solve=lambda s: fmt_bool(is_bipartite(*edges_of(s))), cases=E_CASES),

    dict(title="Homework: LC684 Redundant Connection",
         stmt="A tree had one extra edge added, creating exactly one cycle. Print the edge to remove so a tree remains. If several qualify, print the one that appears last in the input.",
         inp=E_IN, out="A single line: the two node numbers of the edge.",
         cons="- `3 <= n <= 1000`\n- exactly one extra edge",
         solve=lambda s: (lambda r: "%d %d" % r if r else "")(
             redundant_connection(*edges_of(s))),
         cases=["3 3\n0 1\n1 2\n2 0",
                "4 4\n0 1\n1 2\n2 3\n1 3",
                "5 5\n0 1\n1 2\n2 3\n3 4\n0 4",
                "3 3\n0 1\n0 2\n1 2",
                "4 4\n0 1\n0 2\n0 3\n1 2",
                "5 5\n0 1\n1 2\n0 2\n3 4\n0 3",
                "4 4\n1 2\n2 3\n3 1\n0 1",
                "6 6\n0 1\n1 2\n2 3\n3 4\n4 5\n0 5"]),

    # ---- LEC-43 : topological sort -----------------------------------------
    dict(title="Classwork: LC210 Course Schedule II",
         stmt="An edge `u v` means `u` must come before `v`. Print an order in which all courses can be taken, or nothing if it is impossible.\n\nIf several orders are valid, print the lexicographically smallest.",
         inp=E_IN + " Edges are directed `u` to `v`.",
         out="A single line: the course order, space separated. Print an empty line if no "
             "valid order exists.",
         cons="- `1 <= n <= 2000`",
         solve=lambda s: fmt(topo_smallest(*edges_of(s))), cases=E_CASES),

    dict(title="Classwork: Topological Sort (GfG)",
         stmt="Print a topological ordering of a directed acyclic graph -- every node before all nodes it points to.\n\nIf several orderings are valid, print the lexicographically smallest.",
         inp=E_IN + " Edges are directed `u` to `v`. The graph is acyclic.",
         out="A single line: the ordering, space separated.",
         cons="- `1 <= n <= 10^4`",
         solve=lambda s: fmt(topo_smallest(*edges_of(s))),
         cases=["6 6\n5 2\n5 0\n4 0\n4 1\n2 3\n3 1",
                "3 2\n0 1\n1 2",
                "4 2\n0 1\n2 3",
                "1 0",
                "5 4\n0 1\n0 2\n1 3\n2 4",
                "2 1\n1 0",
                "6 4\n0 1\n2 3\n4 5\n0 2",
                "5 0"]),

    dict(title="Classwork: Kahn's algorithm for topological sort (GfG)",
         stmt="Produce a topological order using **Kahn's algorithm** specifically: compute in-degrees, start from the nodes with in-degree zero, and reduce in-degrees as you remove nodes.\n\nIf several orderings are valid, print the lexicographically smallest.",
         inp=E_IN + " Edges are directed `u` to `v`.",
         out="A single line: the ordering, space separated, or an empty line if the graph "
             "has a cycle.",
         cons="- `1 <= n <= 10^4`",
         solve=lambda s: fmt(topo_smallest(*edges_of(s))), cases=E_CASES),

    dict(title="Homework: LC269 Alien Dictionary",
         stmt="Given words sorted according to an unknown alphabet, recover the letter order.\n\nPrint the lexicographically smallest valid order, or an empty line if the input is contradictory -- including the case where a word precedes its own prefix.",
         inp="The first line contains `n`. The second line contains `n` space-separated "
             "words.",
         out="A single line: the letters in order, with no separators. Empty line if "
             "impossible.",
         cons="- `1 <= n <= 100`\n- lowercase English letters",
         solve=lambda s: alien_order(rows(s)[1].split()),
         cases=["5\nwrt wrf er ett rftt",
                "2\nz x",
                "3\nz x z",
                "1\nabc",
                "2\nab a",
                "2\nab ac",
                "3\nba bc ac",
                "4\nz y x w"]),

    dict(title="Homework: LC2115 Find All Possible Recipes from Given Supplies",
         stmt="Each recipe needs certain ingredients, which may be supplies you already have or other recipes. Print every recipe you can make.\n\nPrint the makeable recipes in lexicographic order.",
         inp="The first line contains the supplies you have, space separated. The second "
             "line contains `n`, the number of recipes. Each of the next `n` lines contains "
             "a recipe name followed by its ingredients.",
         out="A single line: the makeable recipe names in lexicographic order, space "
             "separated. Empty line if none.",
         cons="- `1 <= n <= 100`",
         solve=lambda s: fmt(_recipes(s)),
         cases=["yeast flour\n1\nbread yeast flour",
                "yeast flour\n2\nbread yeast flour\nsandwich bread meat",
                "yeast flour meat\n2\nbread yeast flour\nsandwich bread meat",
                "flour\n1\nbread yeast flour",
                "a\n1\nb a",
                "a b\n2\nc a\nd c b",
                "x\n2\ny x\nz y",
                "q\n1\nr s"]),

    dict(title="Homework: LC1462 Course Schedule IV",
         stmt="Given prerequisites and a list of queries, answer for each whether one course is a prerequisite of another, directly or indirectly.",
         inp=E_IN + " Edges are directed `u` to `v`.\n\nThe next line contains `q`. Each "
                    "of the next `q` lines contains two node numbers.",
         out="One line per query: `true` or `false`.",
         cons="- `2 <= n <= 100`\n- `1 <= q <= 10^4`",
         solve=lambda s: _reach_queries(s),
         cases=["2 1\n0 1\n2\n0 1\n1 0",
                "3 2\n0 1\n1 2\n2\n0 2\n2 0",
                "3 0\n1\n0 1",
                "4 3\n0 1\n1 2\n2 3\n2\n0 3\n3 0",
                "2 1\n1 0\n1\n1 0",
                "5 4\n0 1\n1 2\n2 3\n3 4\n1\n0 4",
                "3 1\n0 2\n2\n0 2\n0 1",
                "4 2\n0 1\n2 3\n2\n0 3\n2 3"]),

    # ---- LEC-44 : weighted paths & MST -------------------------------------
    dict(title="Classwork: LC743 Network Delay Time",
         stmt="A signal starts at one node and travels along directed weighted edges. Print the time for every node to receive it, or `-1` if some node cannot.",
         inp=W_IN + " Edges are directed `u` to `v`.\n\nA final line contains the source "
                    "node.",
         out="A single line: the time, or `-1`.",
         cons="- `1 <= n <= 100`\n- weights are positive",
         solve=lambda s: str(network_delay(
             *wedges_of(s), int(rows(s)[1 + ints(rows(s)[0])[1]]))),
         cases=["4 3\n1 0 1\n1 2 1\n2 3 1\n1",
                "2 1\n0 1 1\n0",
                "2 1\n0 1 1\n1",
                "3 2\n0 1 2\n1 2 3\n0",
                "1 0\n0",
                "4 4\n0 1 1\n0 2 4\n1 2 2\n2 3 1\n0",
                "3 1\n0 1 5\n0",
                "5 4\n0 1 1\n1 2 1\n2 3 1\n3 4 1\n0"]),

    dict(title="Classwork: LC1631 Path With Minimum Effort",
         stmt="A grid of heights; moving between adjacent cells costs the absolute height difference. A route's effort is its **largest** single step. Print the minimum effort from top-left to bottom-right.",
         inp=G_IN, out=NUM_OUT, cons="- `1 <= m, n <= 100`",
         solve=lambda s: str(min_effort(grid_of(s))),
         cases=["3 3\n1 2 2\n3 8 2\n5 3 5",
                "3 3\n1 2 3\n3 8 4\n5 3 5",
                "1 1\n5",
                "1 4\n1 2 3 4",
                "2 2\n1 10\n10 1",
                "3 1\n1\n5\n9",
                "2 3\n1 1 1\n1 1 1",
                "3 3\n1 2 1\n1 2 1\n1 2 1"]),

    dict(title="Classwork: Dijkstra's shortest path (GfG)",
         stmt="Print the shortest distance from a source to every node of a weighted undirected graph, or `-1` for unreachable nodes.",
         inp=W_IN + "\n\nA final line contains the source node.",
         out="A single line: the distance to node `0`, `1`, ... `n-1`, space separated, "
             "using `-1` for unreachable.",
         cons="- `1 <= n <= 10^4`\n- weights are non-negative",
         solve=lambda s: fmt(-1 if d == float("inf") else d for d in dijkstra(
             *wedges_of(s), int(rows(s)[1 + ints(rows(s)[0])[1]]))),
         cases=["3 2\n0 1 1\n1 2 3\n0",
                "4 3\n0 1 1\n1 2 2\n2 3 3\n0",
                "1 0\n0",
                "4 2\n0 1 5\n2 3 5\n0",
                "3 3\n0 1 4\n0 2 1\n2 1 2\n0",
                "2 1\n0 1 7\n1",
                "5 4\n0 1 1\n1 2 1\n2 3 1\n3 4 1\n2",
                "3 1\n0 1 2\n2"]),

    dict(title="Homework: LC787 Cheapest Flights Within K Stops",
         stmt="Print the cheapest route from source to destination using at most `k` intermediate stops, or `-1` if none exists.",
         inp=W_IN + " Edges are directed `u` to `v`.\n\nA final line contains the source, "
                    "the destination and `k`.",
         out="A single line: the cost, or `-1`.",
         cons="- `1 <= n <= 100`\n- weights are positive",
         solve=lambda s: str(cheapest_k_stops(
             *wedges_of(s), *ints(rows(s)[1 + ints(rows(s)[0])[1]]))),
         cases=["4 4\n0 1 100\n1 2 100\n2 0 100\n1 3 600\n0 3 1",
                "3 3\n0 1 100\n1 2 100\n0 2 500\n0 2 1",
                "3 3\n0 1 100\n1 2 100\n0 2 500\n0 2 0",
                "2 1\n0 1 5\n0 1 0",
                "2 0\n0 1 0",
                "4 3\n0 1 1\n1 2 1\n2 3 1\n0 3 2",
                "4 3\n0 1 1\n1 2 1\n2 3 1\n0 3 1",
                "5 4\n0 1 1\n1 2 1\n2 3 1\n3 4 1\n0 4 3"]),

    dict(title="Homework: LC1584 Min Cost to Connect All Points (MST)",
         stmt="Given points on a plane, print the minimum total cost to connect them all, where connecting two points costs their Manhattan distance.",
         inp="The first line contains `n`. Each of the next `n` lines contains a point's "
             "`x` and `y`.",
         out=NUM_OUT, cons="- `1 <= n <= 1000`",
         solve=lambda s: str(mst_cost_points(
             [tuple(ints(rows(s)[1 + i])) for i in range(int(rows(s)[0]))])),
         cases=["5\n0 0\n2 2\n3 10\n5 2\n7 0",
                "3\n3 12\n-2 5\n-4 1",
                "1\n0 0",
                "2\n0 0\n1 1",
                "4\n0 0\n1 0\n0 1\n1 1",
                "3\n0 0\n0 5\n0 10",
                "2\n-1 -1\n1 1",
                "4\n0 0\n10 0\n0 10\n10 10"]),

    dict(title="Homework: 0/1 BFS shortest path (GfG)",
         stmt="Every edge weighs either 0 or 1. Print the shortest distance from a source to all nodes, or `-1` for unreachable ones.",
         inp=W_IN + " Weights are `0` or `1`.\n\nA final line contains the source node.",
         out="A single line: the distances, space separated, `-1` for unreachable.",
         cons="- `1 <= n <= 10^5`\n- weights are `0` or `1`",
         solve=lambda s: fmt(-1 if d == float("inf") else d for d in zero_one_bfs(
             *wedges_of(s), int(rows(s)[1 + ints(rows(s)[0])[1]]))),
         cases=["4 3\n0 1 0\n1 2 1\n2 3 0\n0",
                "3 2\n0 1 1\n1 2 1\n0",
                "3 2\n0 1 0\n1 2 0\n0",
                "1 0\n0",
                "4 2\n0 1 1\n2 3 1\n0",
                "5 4\n0 1 0\n1 2 1\n2 3 0\n3 4 1\n0",
                "2 1\n0 1 1\n1",
                "3 3\n0 1 1\n1 2 1\n0 2 0\n0"]),

    # ---- LEC-45 : graphs extra ---------------------------------------------
    dict(title="Classwork: Bellman-Ford algorithm (GfG)",
         stmt="Print the shortest distances from a source in a directed graph that may contain **negative** edge weights, or report a negative cycle.",
         inp=W_IN + " Edges are directed and weights may be negative.\n\nA final line "
                    "contains the source node.",
         out="A single line: the distances, space separated, `-1` for unreachable; or the "
             "single word `cycle` if a negative cycle exists.",
         cons="- `1 <= n <= 500`",
         solve=lambda s: _bf_out(s),
         cases=["3 2\n0 1 4\n1 2 -2\n0",
                "3 3\n0 1 1\n1 2 -1\n2 0 -1\n0",
                "1 0\n0",
                "4 3\n0 1 1\n1 2 2\n2 3 3\n0",
                "2 1\n0 1 -5\n0",
                "4 2\n0 1 2\n2 3 2\n0",
                "3 2\n0 1 -1\n1 2 -1\n0",
                "2 2\n0 1 1\n1 0 -3\n0"]),

    dict(title="Classwork: Floyd-Warshall all-pairs shortest path (GfG)",
         stmt="Print the shortest distance between every pair of nodes in a directed weighted graph.",
         inp=W_IN + " Edges are directed `u` to `v`.",
         out="`n` lines of `n` values: the distance matrix, using `-1` where no path "
             "exists.",
         cons="- `1 <= n <= 100`",
         solve=lambda s: "\n".join(
             fmt(-1 if x == float("inf") else x for x in row)
             for row in floyd_warshall(*wedges_of(s))),
         cases=["4 4\n0 1 5\n1 2 3\n2 3 1\n3 0 2",
                "2 1\n0 1 4",
                "1 0",
                "3 2\n0 1 1\n1 2 1",
                "3 3\n0 1 1\n1 2 1\n0 2 5",
                "2 2\n0 1 1\n1 0 1",
                "4 2\n0 1 1\n2 3 1",
                "3 1\n1 2 7"]),

    dict(title="Classwork: LC994 Rotting Oranges",
         stmt="A grid where `0` is empty, `1` is a fresh orange and `2` is rotten. Each minute, rot spreads to fresh oranges horizontally and vertically adjacent to a rotten one. Print the minutes until none are fresh, or `-1` if some never rot.",
         inp=G_IN + " Values are `0`, `1` or `2`.", out=NUM_OUT,
         cons="- `1 <= m, n <= 100`",
         solve=lambda s: str(rotting_oranges(grid_of(s))),
         cases=["3 3\n2 1 1\n1 1 0\n0 1 1",
                "3 3\n2 1 1\n0 1 1\n1 0 1",
                "1 1\n0",
                "1 1\n2",
                "1 1\n1",
                "2 2\n2 1\n1 1",
                "2 3\n2 0 1\n0 0 0",
                "3 3\n2 2 2\n1 1 1\n1 1 1"]),

    dict(title="Homework: LC542 01 Matrix",
         stmt="For each cell of a binary matrix, print its distance to the nearest `0`.",
         inp=G_IN + " Values are `0` or `1`.",
         out="`m` lines of `n` integers: the distance matrix.",
         cons="- `1 <= m, n <= 10^4` cells in total",
         solve=lambda s: "\n".join(fmt(r) for r in zero_one_matrix(grid_of(s))),
         cases=["3 3\n0 0 0\n0 1 0\n0 0 0",
                "3 3\n0 0 0\n0 1 0\n1 1 1",
                "1 1\n0",
                "1 3\n0 1 1",
                "2 2\n0 1\n1 1",
                "3 1\n0\n1\n1",
                "2 3\n0 0 0\n1 1 1",
                "2 2\n0 0\n0 0"]),

    dict(title="Homework: LC1091 Shortest Path in Binary Matrix",
         stmt="In a binary matrix you may step to any of the **eight** neighbours of a clear cell. Print the number of cells on the shortest clear path from top-left to bottom-right, or `-1` if there is none.",
         inp=G_IN + " The matrix is square; `0` is clear and `1` is blocked.",
         out="A single line: the path length in cells, or `-1`.",
         cons="- `1 <= n <= 100`",
         solve=lambda s: str(shortest_binary_path(grid_of(s))),
         cases=["2 2\n0 1\n1 0",
                "3 3\n0 0 0\n1 1 0\n1 1 0",
                "3 3\n1 0 0\n1 1 0\n1 1 0",
                "1 1\n0",
                "1 1\n1",
                "2 2\n0 0\n0 0",
                "3 3\n0 1 1\n1 1 1\n1 1 0",
                "4 4\n0 0 0 0\n1 1 1 0\n0 0 0 0\n0 1 1 0"]),

    dict(title="Homework: LC1192 Critical Connections in a Network",
         stmt="Print every **bridge** of an undirected graph -- an edge whose removal disconnects it.",
         inp=E_IN,
         out="One line per bridge: two node numbers, smaller first. Lines sorted "
             "ascending. Empty output if there are none.",
         cons="- `1 <= n <= 10^5`",
         solve=lambda s: "\n".join("%d %d" % e for e in bridges(*edges_of(s))),
         cases=["4 4\n0 1\n1 2\n2 0\n1 3",
                "2 1\n0 1",
                "3 3\n0 1\n1 2\n2 0",
                "1 0",
                "5 4\n0 1\n1 2\n2 3\n3 4",
                "4 3\n0 1\n1 2\n2 3",
                "6 6\n0 1\n1 2\n2 0\n3 4\n4 5\n5 3",
                "4 4\n0 1\n1 2\n2 3\n3 0"]),

    # ---- LEC-46 : tree DP --------------------------------------------------
    dict(title="Classwork: LC337 House Robber III",
         stmt="Houses form a binary tree, and robbing a node forbids robbing its children. Print the maximum money.",
         inp=TREE_IN, out=NUM_OUT, cons="- `0 <= nodes <= 10^4`",
         solve=lambda s: str(rob3(build(s))),
         cases=["3 2 3 null 3 null 1", "3 4 5 1 3 null 1", "1",
                "null", "1 2 3", "4 1 null 2 null 3",
                "5 1 1 5 5 null 5", "2 1 3"]),

    dict(title="Homework: LC968 Binary Tree Cameras",
         stmt="A camera on a node monitors itself, its parent and its children. Print the minimum number of cameras to monitor every node.",
         inp=TREE_IN, out=NUM_OUT, cons="- `1 <= nodes <= 1000`",
         solve=lambda s: str(min_cameras(build(s))),
         cases=["0 0 null 0 0", "0 0 null null 0 0 null null 0 0",
                "0", "0 0", "0 0 0", "0 0 0 0 0 0 0",
                "0 null 0 null 0", "0 0 null 0"]),

    dict(title="Homework: LC687 Longest Univalue Path",
         stmt="Print the number of **edges** on the longest path where every node holds the same value. The path need not pass through the root.",
         inp=TREE_IN, out=NUM_OUT, cons="- `0 <= nodes <= 10^4`",
         solve=lambda s: str(longest_univalue(build(s))),
         cases=["5 4 5 1 1 null 5", "1 4 5 4 4 null 5", "1",
                "null", "1 1 1", "1 2 3",
                "1 1 1 1 1 1 1", "2 2 null 2 null 2"]),

    dict(title="Homework: Maximum sum of non-adjacent nodes in a tree (GfG)",
         stmt="Choose nodes of a binary tree so that no chosen node is the parent of another, maximising the total. Print that total.",
         inp=TREE_IN, out=NUM_OUT, cons="- `1 <= nodes <= 10^4`",
         solve=lambda s: str(tree_non_adjacent(build(s))),
         cases=["11 1 2", "1 2 3 4 5", "1", "10 5 5",
                "3 2 3 null 3 null 1", "1 2 3 4 null null 5",
                "5 10 5", "4 1 1 2 2"]),

    # ---- LEC-47 : backtracking foundations ---------------------------------
    dict(title="Classwork: LC78 Subsets",
         stmt="Print every subset of a set of distinct integers.\n\nThe empty subset is an empty line.",
         inp=ARR_IN + " The values are distinct.",
         out="One subset per line, values ascending and space separated. Lines sorted "
             "ascending.",
         cons="- `1 <= n <= 10`",
         solve=lambda s: "\n".join(fmt(x) for x in subsets(ints(s))),
         cases=["1 2 3", "0", "1 2", "3 1 2",
                "1", "1 2 3 4", "5 6", "2 4 6"]),

    dict(title="Classwork: LC46 Permutations",
         stmt="Print every permutation of a list of distinct integers, in lexicographic order.",
         inp=ARR_IN + " The values are distinct.",
         out="One permutation per line, values space separated, lines in lexicographic "
             "order.",
         cons="- `1 <= n <= 6`",
         solve=lambda s: "\n".join(fmt(p) for p in permutations_of(ints(s))),
         cases=["1 2 3", "0 1", "1", "3 1 2",
                "1 2", "2 4 6", "1 2 3 4", "5 6 7"]),

    dict(title="Classwork: LC77 Combinations",
         stmt="Print every combination of `k` numbers chosen from `1` to `n`, in lexicographic order.",
         inp="A single line containing `n` and `k`.",
         out="One combination per line, values ascending and space separated, lines in "
             "lexicographic order.",
         cons="- `1 <= k <= n <= 10`",
         solve=lambda s: "\n".join(fmt(c) for c in combinations_of(*ints(s))),
         cases=["4 2", "1 1", "3 3", "5 1",
                "4 3", "3 2", "5 4", "2 2"]),

    dict(title="Homework: LC90 Subsets II",
         stmt="Print every **distinct** subset of a list that may contain duplicates.",
         inp=ARR_IN + " Values may repeat.",
         out="One subset per line, values ascending and space separated. Lines sorted "
             "ascending; the empty subset is an empty line.",
         cons="- `1 <= n <= 10`",
         solve=lambda s: "\n".join(fmt(x) for x in subsets_unique(ints(s))),
         cases=["1 2 2", "0", "1 1", "1 2 3",
                "2 1 2", "1 1 1", "4 4 4 1", "1 2"]),

    dict(title="Homework: LC39 Combination Sum",
         stmt="Given distinct candidates and a target, print every combination summing to the target. A candidate may be used any number of times.",
         inp=ARR_IN + " The candidates are distinct.\n\nA second line contains the target.",
         out="One combination per line, values ascending and space separated, lines "
             "sorted.",
         cons="- `1 <= n <= 30`\n- `1 <= target <= 40`",
         solve=lambda s: "\n".join(fmt(c) for c in combination_sum(
             ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["2 3 6 7\n7", "2 3 5\n8", "2\n1", "1\n3",
                "3 5\n8", "2 4\n6", "7\n7", "2 3\n5"]),

    dict(title="Homework: LC131 Palindrome Partitioning",
         stmt="Print every way to cut a string so that every piece is a palindrome.",
         inp=STR_IN,
         out="One partition per line: the pieces in order, space separated. Lines sorted "
             "ascending.",
         cons="- `1 <= length <= 12`\n- lowercase English letters",
         solve=lambda s: "\n".join(fmt(p) for p in palindrome_partitions(s.strip())),
         cases=["aab", "a", "ab", "aba", "aaa",
                "abba", "abc", "aabb"]),

    # ---- LEC-48 : backtracking on grids ------------------------------------
    dict(title="Classwork: LC79 Word Search",
         stmt="Decide whether a word can be spelt in a grid of letters by moving between horizontally or vertically adjacent cells, using each cell at most once.",
         inp="The first line contains `m` and `n`. Each of the next `m` lines contains `n` "
             "letters with no spaces.\n\nA final line contains the word.",
         out=BOOL_OUT, cons="- `1 <= m, n <= 6`\n- lowercase English letters",
         solve=lambda s: fmt_bool(word_search(
             char_grid(s), rows(s)[1 + ints(rows(s)[0])[0]].strip())),
         cases=["3 4\nabce\nsfcs\nadee\nabcced",
                "3 4\nabce\nsfcs\nadee\nsee",
                "3 4\nabce\nsfcs\nadee\nabcb",
                "1 1\na\na",
                "1 1\na\nb",
                "2 2\nab\ncd\nabdc",
                "2 2\nab\ncd\nacdb",
                "1 3\nabc\nabc"]),

    dict(title="Classwork: LC51 N-Queens",
         stmt="Place `n` queens on an `n` by `n` board so no two attack each other. Print the **number** of distinct arrangements.",
         inp="A single line containing `n`.", out=NUM_OUT, cons="- `1 <= n <= 9`",
         solve=lambda s: str(n_queens_count(int(s))),
         cases=["4", "1", "2", "3", "5", "6", "8", "9"]),

    dict(title="Classwork: LC22 Generate Parentheses",
         stmt="Print every well-formed string of `n` pairs of parentheses, in lexicographic order.",
         inp="A single line containing `n`.",
         out="One string per line, in lexicographic order.", cons="- `1 <= n <= 8`",
         solve=lambda s: "\n".join(gen_parens(int(s))),
         cases=["3", "1", "2", "4", "5", "6", "7", "8"]),

    dict(title="Homework: LC37 Sudoku Solver",
         stmt="Solve a 9 by 9 Sudoku, where `0` marks an empty cell, and print the completed grid.\n\nThe puzzle has exactly one solution.",
         inp="Nine lines of nine integers, `0` for empty.",
         out="Nine lines of nine integers: the solved grid.",
         cons="- exactly one solution exists",
         solve=lambda s: "\n".join(fmt(r) for r in solve_sudoku(
             [ints(r) for r in rows(s)[:9]])),
         cases=["5 3 0 0 7 0 0 0 0\n6 0 0 1 9 5 0 0 0\n0 9 8 0 0 0 0 6 0\n"
                "8 0 0 0 6 0 0 0 3\n4 0 0 8 0 3 0 0 1\n7 0 0 0 2 0 0 0 6\n"
                "0 6 0 0 0 0 2 8 0\n0 0 0 4 1 9 0 0 5\n0 0 0 0 8 0 0 7 9",
                "1 2 3 4 5 6 7 8 0\n4 5 6 7 8 9 1 2 3\n7 8 9 1 2 3 4 5 6\n"
                "2 3 1 5 6 4 8 9 7\n5 6 4 8 9 7 2 3 1\n8 9 7 2 3 1 5 6 4\n"
                "3 1 2 6 4 5 9 7 8\n6 4 5 9 7 8 3 1 2\n9 7 8 3 1 2 6 4 5"]),

    dict(title="Homework: LC212 Word Search II",
         stmt="Given a letter grid and a list of words, print every word that can be spelt in the grid by moving between adjacent cells, using each cell at most once per word.\n\nPrint the found words in lexicographic order.",
         inp="The first line contains `m` and `n`. Each of the next `m` lines contains `n` "
             "letters with no spaces. The next line contains `k`, then a line of `k` "
             "space-separated words.",
         out="A single line: the found words in lexicographic order, space separated. "
             "Empty line if none.",
         cons="- `1 <= m, n <= 6`\n- `1 <= k <= 20`",
         solve=lambda s: fmt(word_search_ii(
             char_grid(s),
             rows(s)[2 + ints(rows(s)[0])[0]].split())),
         cases=["4 4\noaan\netae\nihkr\niflv\n2\noath pea",
                "4 4\noaan\netae\nihkr\niflv\n4\noath pea eat rain",
                "1 1\na\n1\na",
                "1 1\na\n1\nb",
                "2 2\nab\ncd\n2\nab cd",
                "2 2\nab\ncd\n1\nabcd",
                "1 3\nabc\n2\nabc cba",
                "2 3\nabc\ndef\n2\nadd ad"]),

    dict(title="Homework: LC93 Restore IP Addresses",
         stmt="Print every valid IP address that can be formed by inserting three dots into a digit string.\n\nPrint the addresses in lexicographic order.",
         inp="A single line: the digit string.",
         out="One address per line, in lexicographic order. Empty output if none.",
         cons="- `1 <= length <= 20`\n- digits only",
         solve=lambda s: "\n".join(restore_ip(s.strip())),
         cases=["25525511135", "0000", "101023", "1111",
                "010010", "1", "255255255255", "123456789012"]),

    # ---- LEC-49 : two pointers & sliding window -----------------------------
    dict(title="Classwork: LC209 Minimum Size Subarray Sum",
         stmt="Print the length of the shortest contiguous subarray whose sum is at least the target, or `0` if there is none.",
         inp=ARR_IN + "\n\nA second line contains the target.", out=NUM_OUT,
         cons="- `1 <= n <= 10^5`\n- values are positive",
         solve=lambda s: str(min_subarray_len(ints(rows(s)[0]), int(rows(s)[1]))),
         cases=["2 3 1 2 4 3\n7", "1 4 4\n4", "1 1 1 1 1 1 1 1\n11",
                "1\n1", "1\n2", "5 1 3\n5", "1 2 3 4 5\n11",
                "10 2 3\n6"]),

    dict(title="Classwork: LC15 3Sum",
         stmt="Print every distinct triplet summing to zero.",
         inp=ARR_IN,
         out="One triplet per line, values ascending and space separated. Lines sorted "
             "ascending. Empty output if there are none.",
         cons="- `3 <= n <= 3000`",
         solve=lambda s: "\n".join(fmt(t) for t in three_sum(ints(s))),
         cases=["-1 0 1 2 -1 -4", "0 1 1", "0 0 0", "-2 0 1 1 2",
                "1 2 3", "0 0 0 0", "-1 -1 2", "3 0 -2 -1 1 2"]),

    dict(title="Homework: LC76 Minimum Window Substring",
         stmt="Print the shortest substring of the first string containing every character of the second, including repeats. Print an empty line if there is none.",
         inp="Two lines: the string, then the required characters.",
         out="A single line: the substring, or an empty line.",
         cons="- `1 <= length <= 10^5`",
         solve=lambda s: min_window(rows(s)[0].strip(), rows(s)[1].strip()),
         cases=["ADOBECODEBANC\nABC", "a\na", "a\naa", "ab\nb",
                "abc\nd", "aa\naa", "bba\nab", "cabwefgewcwaefgcf\ncae"]),

    dict(title="Homework: LC424 Longest Repeating Character Replacement",
         stmt="You may change at most `k` characters. Print the length of the longest substring that can then consist of one repeated character.",
         inp="The first line contains the string. The second line contains `k`.",
         out=NUM_OUT,
         cons="- `1 <= length <= 10^5`\n- uppercase English letters",
         solve=lambda s: str(char_replacement(rows(s)[0].strip(), int(rows(s)[1]))),
         cases=["ABAB\n2", "AABABBA\n1", "A\n0", "A\n1",
                "AAAA\n2", "ABCDE\n1", "ABBB\n0", "AABA\n0"]),

    dict(title="Homework: LC11 Container With Most Water",
         stmt="Each value is the height of a vertical line. Print the largest area of water held between two lines.",
         inp=ARR_IN, out=NUM_OUT, cons="- `2 <= n <= 10^5`",
         solve=lambda s: str(max_water(ints(s))),
         cases=["1 8 6 2 5 4 8 3 7", "1 1", "4 3 2 1 4", "1 2 1",
                "2 3 4 5 18 17 6", "1 2 3 4 5", "5 4 3 2 1", "1 3 2 5 25 24 5"]),
]


# --- helpers used by a couple of the write-ups above -------------------------
def _recipes(s):
    have = set(rows(s)[0].split())
    n = int(rows(s)[1])
    recipes = {}
    for i in range(n):
        parts = rows(s)[2 + i].split()
        recipes[parts[0]] = parts[1:]
    made, changed = set(), True
    while changed:
        changed = False
        for name, need in recipes.items():
            if name not in made and all(x in have or x in made for x in need):
                made.add(name)
                changed = True
    return sorted(made)


def _reach_queries(s):
    n, m = ints(rows(s)[0])
    es = [tuple(ints(rows(s)[1 + i])) for i in range(m)]
    reach = [[False] * n for _ in range(n)]
    for u, v in es:
        reach[u][v] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
    q = int(rows(s)[1 + m])
    out = []
    for i in range(q):
        a, b = ints(rows(s)[2 + m + i])
        out.append(fmt_bool(reach[a][b]))
    return "\n".join(out)


def _bf_out(s):
    n, m = ints(rows(s)[0])
    es = [tuple(ints(rows(s)[1 + i])) for i in range(m)]
    src = int(rows(s)[1 + m])
    d = bellman_ford(n, es, src)
    if d is None:
        return "cycle"
    return fmt(-1 if x == float("inf") else x for x in d)


SANITY = [
    ("Classwork: LC200 Number of Islands",
     "4 5\n1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1", "3"),
    ("Classwork: LC200 Number of Islands", "1 1\n0", "0"),
    ("Classwork: LC547 Number of Provinces", "5 3\n0 1\n1 2\n3 4", "2"),
    ("Classwork: LC547 Number of Provinces", "1 0", "1"),
    ("Classwork: LC133 Clone Graph", "3 2\n0 1\n1 2", "1\n0 2\n1"),
    ("Homework: LC733 Flood Fill",
     "3 3\n1 1 1\n1 1 0\n1 0 1\n1 1 2", "2 2 2\n2 2 0\n2 0 1"),
    ("Homework: LC695 Max Area of Island",
     "4 5\n1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1", "4"),
    ("Homework: LC1971 Find if Path Exists in Graph", "3 2\n0 1\n1 2\n0 2", "true"),
    ("Homework: LC1971 Find if Path Exists in Graph",
     "6 3\n0 1\n0 2\n3 5\n0 5", "false"),
    ("Classwork: LC207 Course Schedule", "3 2\n0 1\n1 2", "true"),
    ("Classwork: LC207 Course Schedule", "4 4\n0 1\n1 2\n2 0\n2 3", "false"),
    ("Classwork: LC785 Is Graph Bipartite?", "4 4\n0 1\n1 2\n2 0\n2 3", "false"),
    ("Classwork: LC785 Is Graph Bipartite?", "2 1\n0 1", "true"),
    ("Classwork: Detect cycle in an undirected graph (GfG)",
     "4 4\n0 1\n1 2\n2 0\n2 3", "true"),
    ("Classwork: Detect cycle in an undirected graph (GfG)", "3 2\n0 1\n1 2", "false"),
    ("Homework: Detect cycle in a directed graph (GfG)",
     "4 4\n0 1\n1 2\n2 0\n2 3", "true"),
    ("Homework: Detect cycle in a directed graph (GfG)", "3 2\n0 1\n1 2", "false"),
    ("Homework: LC886 Possible Bipartition", "2 1\n0 1", "true"),
    ("Homework: LC684 Redundant Connection", "3 3\n0 1\n1 2\n2 0", "2 0"),
    ("Homework: LC684 Redundant Connection", "4 4\n0 1\n1 2\n2 3\n1 3", "1 3"),
    ("Classwork: LC210 Course Schedule II", "3 2\n0 1\n1 2", "0 1 2"),
    ("Classwork: LC210 Course Schedule II", "4 4\n0 1\n1 2\n2 0\n2 3", ""),
    ("Classwork: Topological Sort (GfG)",
     "6 6\n5 2\n5 0\n4 0\n4 1\n2 3\n3 1", "4 5 0 2 3 1"),
    ("Classwork: Kahn's algorithm for topological sort (GfG)",
     "3 2\n0 1\n1 2", "0 1 2"),
    ("Homework: LC269 Alien Dictionary", "2\nz x", "zx"),
    ("Homework: LC269 Alien Dictionary", "3\nz x z", ""),
    ("Homework: LC269 Alien Dictionary", "2\nab a", ""),
    ("Homework: LC2115 Find All Possible Recipes from Given Supplies",
     "yeast flour\n1\nbread yeast flour", "bread"),
    ("Homework: LC2115 Find All Possible Recipes from Given Supplies",
     "flour\n1\nbread yeast flour", ""),
    ("Homework: LC1462 Course Schedule IV",
     "2 1\n0 1\n2\n0 1\n1 0", "true\nfalse"),
    ("Homework: LC1462 Course Schedule IV",
     "3 2\n0 1\n1 2\n2\n0 2\n2 0", "true\nfalse"),
    ("Classwork: LC743 Network Delay Time",
     "4 3\n1 0 1\n1 2 1\n2 3 1\n1", "2"),
    ("Classwork: LC743 Network Delay Time", "2 1\n0 1 1\n1", "-1"),
    ("Classwork: LC1631 Path With Minimum Effort",
     "3 3\n1 2 2\n3 8 2\n5 3 5", "2"),
    ("Classwork: LC1631 Path With Minimum Effort", "1 1\n5", "0"),
    ("Classwork: Dijkstra's shortest path (GfG)", "3 2\n0 1 1\n1 2 3\n0", "0 1 4"),
    ("Classwork: Dijkstra's shortest path (GfG)", "4 2\n0 1 5\n2 3 5\n0",
     "0 5 -1 -1"),
    ("Homework: LC787 Cheapest Flights Within K Stops",
     "4 4\n0 1 100\n1 2 100\n2 0 100\n1 3 600\n0 3 1", "700"),
    ("Homework: LC787 Cheapest Flights Within K Stops",
     "3 3\n0 1 100\n1 2 100\n0 2 500\n0 2 0", "500"),
    ("Homework: LC1584 Min Cost to Connect All Points (MST)",
     "5\n0 0\n2 2\n3 10\n5 2\n7 0", "20"),
    ("Homework: LC1584 Min Cost to Connect All Points (MST)", "1\n0 0", "0"),
    ("Homework: 0/1 BFS shortest path (GfG)",
     "4 3\n0 1 0\n1 2 1\n2 3 0\n0", "0 0 1 1"),
    ("Classwork: Bellman-Ford algorithm (GfG)", "3 2\n0 1 4\n1 2 -2\n0", "0 4 2"),
    ("Classwork: Bellman-Ford algorithm (GfG)",
     "3 3\n0 1 1\n1 2 -1\n2 0 -1\n0", "cycle"),
    ("Classwork: Floyd-Warshall all-pairs shortest path (GfG)",
     "2 1\n0 1 4", "0 4\n-1 0"),
    ("Classwork: LC994 Rotting Oranges",
     "3 3\n2 1 1\n1 1 0\n0 1 1", "4"),
    ("Classwork: LC994 Rotting Oranges",
     "3 3\n2 1 1\n0 1 1\n1 0 1", "-1"),
    ("Classwork: LC994 Rotting Oranges", "1 1\n0", "0"),
    ("Homework: LC542 01 Matrix",
     "3 3\n0 0 0\n0 1 0\n1 1 1", "0 0 0\n0 1 0\n1 2 1"),
    ("Homework: LC1091 Shortest Path in Binary Matrix", "2 2\n0 1\n1 0", "2"),
    ("Homework: LC1091 Shortest Path in Binary Matrix",
     "3 3\n1 0 0\n1 1 0\n1 1 0", "-1"),
    ("Homework: LC1192 Critical Connections in a Network",
     "4 4\n0 1\n1 2\n2 0\n1 3", "1 3"),
    ("Homework: LC1192 Critical Connections in a Network",
     "3 3\n0 1\n1 2\n2 0", ""),
    ("Classwork: LC337 House Robber III", "3 2 3 null 3 null 1", "7"),
    ("Classwork: LC337 House Robber III", "3 4 5 1 3 null 1", "9"),
    ("Homework: LC968 Binary Tree Cameras", "0 0 null 0 0", "1"),
    ("Homework: LC968 Binary Tree Cameras",
     "0 0 null null 0 0 null null 0 0", "2"),
    ("Homework: LC687 Longest Univalue Path", "5 4 5 1 1 null 5", "2"),
    ("Homework: LC687 Longest Univalue Path", "1 4 5 4 4 null 5", "2"),
    ("Homework: Maximum sum of non-adjacent nodes in a tree (GfG)",
     "11 1 2", "11"),
    ("Classwork: LC78 Subsets", "1 2",
     "\n1\n1 2\n2"),
    ("Classwork: LC46 Permutations", "1 2", "1 2\n2 1"),
    ("Classwork: LC77 Combinations", "4 2",
     "1 2\n1 3\n1 4\n2 3\n2 4\n3 4"),
    ("Homework: LC90 Subsets II", "1 1", "\n1\n1 1"),
    ("Homework: LC39 Combination Sum", "2 3\n5", "2 3"),
    ("Homework: LC131 Palindrome Partitioning", "aab", "a a b\naa b"),
    ("Classwork: LC79 Word Search",
     "3 4\nabce\nsfcs\nadee\nabcced", "true"),
    ("Classwork: LC79 Word Search",
     "3 4\nabce\nsfcs\nadee\nabcb", "false"),
    ("Classwork: LC51 N-Queens", "4", "2"),
    ("Classwork: LC51 N-Queens", "1", "1"),
    ("Classwork: LC51 N-Queens", "2", "0"),
    ("Classwork: LC51 N-Queens", "8", "92"),
    ("Classwork: LC22 Generate Parentheses", "2", "(())\n()()"),
    ("Homework: LC93 Restore IP Addresses", "0000", "0.0.0.0"),
    ("Homework: LC93 Restore IP Addresses", "1", ""),
    ("Classwork: LC209 Minimum Size Subarray Sum", "2 3 1 2 4 3\n7", "2"),
    ("Classwork: LC209 Minimum Size Subarray Sum", "1\n2", "0"),
    ("Classwork: LC15 3Sum", "-1 0 1 2 -1 -4", "-1 -1 2\n-1 0 1"),
    ("Classwork: LC15 3Sum", "1 2 3", ""),
    ("Homework: LC76 Minimum Window Substring", "ADOBECODEBANC\nABC", "BANC"),
    ("Homework: LC76 Minimum Window Substring", "a\naa", ""),
    ("Homework: LC424 Longest Repeating Character Replacement", "ABAB\n2", "4"),
    ("Homework: LC424 Longest Repeating Character Replacement", "AABABBA\n1", "4"),
    ("Homework: LC11 Container With Most Water", "1 8 6 2 5 4 8 3 7", "49"),
    ("Homework: LC11 Container With Most Water", "1 1", "1"),
]
