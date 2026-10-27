# Reference Solutions (C++14) — Biweekly-2 New Problems

Reference solutions for the 9 challenges in [contest_9_new_challenges.md](contest_9_new_challenges.md).

- Standalone problems (Q1, Q3, Q4, Q6, Q8, Q9) are full `int main()` programs that read the raw input and print the answer directly.
- Tree problems (Q2, Q5, Q7) are only the **Body** function — they assume the boilerplate `TreeNode` + input-parsing already sits in Head and Tail (see [biweekly2_driver_code.md](../hackerrank-editor/biweekly2_driver_code.md)).

Each solution below has been reasoned against every one of the 10 sample cases in the MD; verify locally before publishing to be safe.

---

## Q1 — Frequency Counter

`std::map<int,int>` keeps keys sorted in ascending order, so iterating it once prints the required "increasing value" order for free.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    map<int, int> freq;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        freq[x]++;
    }
    for (auto& kv : freq) {
        cout << kv.first << ' ' << kv.second << '\n';
    }
    return 0;
}
```

Complexity: O(N log N).

---

## Q2 — Height of Binary Tree (Body only)

```cpp
int height(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(height(root->left), height(root->right));
}
```

Complexity: O(N).

---

## Q3 — Longest Subarray with Sum K

Prefix-sum trick: at each index `i`, if some earlier prefix `p` had value `pref[i] - K`, then the subarray from `p+1..i` sums to K. Remembering only the **earliest** occurrence of each prefix value gives the longest subarray.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    cin >> n >> k;

    unordered_map<long long, int> firstIdx;
    firstIdx[0] = -1;                 // empty prefix ends before index 0

    long long pref = 0;
    int best = 0;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        pref += x;

        auto it = firstIdx.find(pref - k);
        if (it != firstIdx.end()) {
            best = max(best, i - it->second);
        }
        // Keep only the earliest index of each prefix so the window stays maximal
        firstIdx.emplace(pref, i);
    }
    cout << best << '\n';
    return 0;
}
```

Complexity: O(N) average.

---

## Q4 — Valid Parentheses

Classic stack scan: push openers, pop and match on closers.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    if (!(cin >> s)) { cout << "true\n"; return 0; }   // empty string is balanced

    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty()) { cout << "false\n"; return 0; }
            char top = st.top();
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{')) {
                cout << "false\n";
                return 0;
            }
            st.pop();
        }
    }
    cout << (st.empty() ? "true" : "false") << '\n';
    return 0;
}
```

Complexity: O(|S|).

---

## Q5 — Iterative Preorder Traversal (Body only)

Stack-based DFS. Push right first, then left, so left is processed next.

```cpp
vector<int> preorder(TreeNode* root) {
    vector<int> out;
    if (!root) return out;

    stack<TreeNode*> st;
    st.push(root);
    while (!st.empty()) {
        TreeNode* cur = st.top(); st.pop();
        out.push_back(cur->val);
        if (cur->right) st.push(cur->right);   // pushed first, popped later
        if (cur->left)  st.push(cur->left);    // pushed second, popped next
    }
    return out;
}
```

Complexity: O(N).

---

## Q6 — K-th Largest Element

Maintain a min-heap of size K. After scanning all N values, the top is the K-th largest.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    priority_queue<int, vector<int>, greater<int>> pq;   // min-heap
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        pq.push(x);
        if ((int)pq.size() > k) pq.pop();
    }
    cout << pq.top() << '\n';
    return 0;
}
```

Complexity: O(N log K).

---

## Q7 — Maximum Path Sum, Root to Leaf (Body only)

Recurse into whichever children exist. A leaf's answer is its own value; an internal node's answer is `val + max(children answers)`. Care not to treat a null child as a leaf with sum 0.

```cpp
long long maxPathSum(TreeNode* root) {
    if (!root) return 0;                          // called only from a parent with only one child
    if (!root->left && !root->right) return root->val;

    long long best = LLONG_MIN;
    if (root->left)  best = max(best, maxPathSum(root->left));
    if (root->right) best = max(best, maxPathSum(root->right));
    return root->val + best;
}
```

Complexity: O(N).

---

## Q8 — First and Last Occurrence

`lower_bound` gives the first index whose value is `>= X`; `upper_bound` gives the first index whose value is `> X`. Their difference is the count of `X`s.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    cin >> n >> x;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    auto lo = lower_bound(a.begin(), a.end(), x);
    auto hi = upper_bound(a.begin(), a.end(), x);

    if (lo == a.end() || *lo != x) {
        cout << "-1 -1\n";
    } else {
        cout << (lo - a.begin()) << ' ' << (hi - a.begin() - 1) << '\n';
    }
    return 0;
}
```

Complexity: O(log N).

---

## Q9 — Split Array to Minimize Cost

Binary search on the answer (the largest allowed group sum). The answer lies in `[max(a_i), sum(a_i)]`. For a candidate `cap`, greedily grow groups from left to right — start a new group whenever adding the next element would exceed `cap`. Fewer or equal groups than K means `cap` is achievable.

```cpp
#include <bits/stdc++.h>
using namespace std;

static bool feasible(const vector<int>& a, int k, long long cap) {
    long long cur = 0;
    int groups = 1;
    for (int x : a) {
        if ((long long)x > cap) return false;
        if (cur + x > cap) {
            groups++;
            cur = x;
            if (groups > k) return false;
        } else {
            cur += x;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    long long total = 0, maxv = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        total += a[i];
        maxv   = max(maxv, (long long)a[i]);
    }

    long long lo = maxv, hi = total;
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (feasible(a, k, mid)) hi = mid;
        else                     lo = mid + 1;
    }
    cout << lo << '\n';
    return 0;
}
```

Complexity: O(N log(sum(a))).
