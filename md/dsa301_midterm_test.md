# DSA-301 Mid-Term Test (15 challenges)

Author-ready markdown for `automator.py`. Fifteen problems for the DSA-301 Mid-Term Test contest. Each challenge carries 10 sample I/O pairs; run `tools/hr_mark_samples.py --md dsa301_midterm_test.md --apply` to flag the first two as samples. **Ensure ONLY C++14 and Java 8 are enabled on each challenge — unselect every other language (Python 3, etc.)** before publishing. Tree problems (Q4, Q5, Q8, Q9, Q10, Q11) ship with Head Code / Solution Template / Tail Code boilerplate in both C++14 and Java 8 — paste them into the HackerRank admin **Head Code / Body / Tail Code** slots after upload (the automator does not parse boilerplate blocks).

Difficulty per challenge (set in the HackerRank admin UI after upload; the automator does not set this field):

| # | Title | Difficulty |
|---|-------|-----------|
| Q1 | Midterm: Contains Duplicate | Easy |
| Q2 | Midterm: Valid Anagram | Easy |
| Q3 | Midterm: Binary Search | Easy |
| Q4 | Midterm: Inorder Traversal of a Binary Tree | Easy |
| Q5 | Midterm: Minimum Depth of a Binary Tree | Easy |
| Q6 | Midterm: Merge Intervals | Medium |
| Q7 | Midterm: Next Greater Element | Medium |
| Q8 | Midterm: Level Order Traversal of a Binary Tree | Medium |
| Q9 | Midterm: Validate Binary Search Tree | Medium |
| Q10 | Midterm: Diameter of a Binary Tree | Medium |
| Q11 | Midterm: Lowest Common Ancestor of a Binary Tree | Medium |
| Q12 | Midterm: Search in a Rotated Sorted Array | Medium |
| Q13 | Midterm: Lower Bound in a Sorted Array | Medium |
| Q14 | Midterm: Sort Characters by Frequency | Hard |
| Q15 | Midterm: Kth Largest Element in an Array | Hard |

**Tree input convention (Q4, Q5, Q8, Q9, Q10, Q11)**: a binary tree is encoded on one line as a space-separated level-order sequence of tokens, where each token is either an integer value or the literal `null` for an absent child. The first token is the root. Reading proceeds level-by-level: for each non-null node in order, the next two tokens are its left and right children. The provided Head Code parses this format and hands the user a `TreeNode* root` (C++) / `TreeNode root` (Java).

---

## Midterm: Contains Duplicate
**Difficulty**: Easy

**Problem Statement**
Given an integer array `nums`, determine whether any value appears at least twice. Print `1` if any element appears more than once, otherwise print `0`.

**Input Format**
- Line 1: a single integer `N` — the size of the array.
- Line 2: `N` space-separated integers — the array elements.

**Output Format**
A single integer: `1` if a duplicate exists, else `0`.

**Constraints**
- `1 <= N <= 300000`
- `-10^9 <= nums[i] <= 10^9`

**Sample Input 0**
```
4
1 2 3 1
```

**Sample Output 0**
```
1
```

**Sample Explanation 0**
The value `1` appears twice in the array (at indices 0 and 3), so a duplicate exists. Output is `1` (true).

**Sample Input 1**
```
4
1 2 3 4
```

**Sample Output 1**
```
0
```

**Sample Explanation 1**
Every value appears exactly once. No duplicate exists, so the output is `0`.

**Sample Input 2**
```
10
1 1 1 3 3 4 3 2 4 2
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
1
7
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
2
5 5
```

**Sample Output 4**
```
1
```

**Sample Input 5**
```
6
-1 -2 -3 -4 -5 -1
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
5
0 0 0 0 0
```

**Sample Output 6**
```
1
```

**Sample Input 7**
```
5
1000000000 -1000000000 999999999 -999999999 0
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
8
10 20 30 40 50 60 70 10
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
3
2 4 6
```

**Sample Output 9**
```
0
```

**Tags**
Hashmap, Set, Arrays

---

## Midterm: Valid Anagram
**Difficulty**: Easy

**Problem Statement**
Given two strings `s` and `t`, determine whether `t` is an anagram of `s`. Two strings are anagrams if they contain exactly the same characters with the same multiplicity. Print `1` if they are anagrams, else `0`.

**Input Format**
- Line 1: string `s`.
- Line 2: string `t`.

**Output Format**
A single integer: `1` if `t` is an anagram of `s`, else `0`.

**Constraints**
- `1 <= |s|, |t| <= 300000`
- Both strings consist of lowercase English letters only.

**Sample Input 0**
```
anagram
nagaram
```

**Sample Output 0**
```
1
```

**Sample Explanation 0**
`anagram` and `nagaram` are made of the same multiset of letters (a×3, n, g, r, m), just in a different order. They are anagrams, so the answer is `1`.

**Sample Input 1**
```
rat
car
```

**Sample Output 1**
```
0
```

**Sample Explanation 1**
`rat` uses r,a,t while `car` uses c,a,r. The letter counts differ, so they are not anagrams.

**Sample Input 2**
```
listen
silent
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
a
a
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
ab
a
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
abcd
dcba
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
aabbcc
abcabc
```

**Sample Output 6**
```
1
```

**Sample Input 7**
```
hello
world
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
night
thing
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
aaaa
aaab
```

**Sample Output 9**
```
0
```

**Tags**
Hashmap, Frequency Counting, Strings

---

## Midterm: Binary Search
**Difficulty**: Easy

**Problem Statement**
Given a sorted (non-decreasing) array of integers `nums` and a batch of `Q` queries, for each query report the 0-based index of the target in `nums`, or `-1` if the target is absent.

**Input Format**
- Line 1: two space-separated integers `N` (size of the array) and `Q` (number of queries).
- Line 2: `N` space-separated integers — the sorted array elements.
- Line 3: `Q` space-separated integers — the targets, one per query.

**Output Format**
A single line of `Q` space-separated integers — the answer for each query in order.

**Constraints**
- `1 <= N <= 200000`
- `1 <= Q <= 200000`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order.

**Sample Input 0**
```
6 2
-1 0 3 5 9 12
9 2
```

**Sample Output 0**
```
4 -1
```

**Sample Explanation 0**
Target `9` sits at index 4, and `2` is not present (`-1`).

**Sample Input 1**
```
6 3
-1 0 3 5 9 12
-1 12 7
```

**Sample Output 1**
```
0 5 -1
```

**Sample Explanation 1**
Target `-1` is at index 0, `12` is at index 5, and `7` is not present.

**Sample Input 2**
```
1 2
5
5 3
```

**Sample Output 2**
```
0 -1
```

**Sample Input 3**
```
5 3
1 2 3 4 5
1 5 3
```

**Sample Output 3**
```
0 4 2
```

**Sample Input 4**
```
7 2
-10 -7 -4 -1 2 5 8
-4 100
```

**Sample Output 4**
```
2 -1
```

**Sample Input 5**
```
5 5
1 2 3 4 5
1 2 3 4 5
```

**Sample Output 5**
```
0 1 2 3 4
```

**Sample Input 6**
```
6 1
1 3 5 7 9 11
7
```

**Sample Output 6**
```
3
```

**Sample Input 7**
```
8 2
1 2 3 4 5 6 7 8
8 100
```

**Sample Output 7**
```
7 -1
```

**Sample Input 8**
```
3 4
-1000000000 0 1000000000
-1000000000 0 1000000000 42
```

**Sample Output 8**
```
0 1 2 -1
```

**Sample Input 9**
```
10 3
1 1 2 2 3 3 4 4 5 5
1 3 6
```

**Sample Output 9**
```
0 4 -1
```

**Tags**
Binary Search, Arrays

---

## Midterm: Inorder Traversal of a Binary Tree
**Difficulty**: Easy

**Problem Statement**
Given the root of a binary tree, return the inorder traversal (left, root, right) of its node values, space-separated on one line. If the tree is empty, print an empty line.

**Input Format**
A single line containing the level-order serialization of the tree (see the "Tree input convention" at the top of this file). Tokens are space-separated; `null` denotes an absent node.

**Output Format**
A single line with the inorder traversal of the node values, separated by single spaces. Print an empty line if the tree is empty.

**Constraints**
- `0 <= number of nodes <= 100000`
- `-10^9 <= Node.val <= 10^9`

**Sample Input 0**
```
1 null 2 3
```

**Sample Output 0**
```
1 3 2
```

**Sample Explanation 0**
The tree looks like: root `1`, no left child, right child `2`, whose left child is `3`. Inorder visits left, root, right. For root `1`: no left, visit `1`, then recurse into right subtree rooted at `2` (whose inorder is `3 2`). Final order: `1 3 2`.

**Sample Input 1**
```

```

**Sample Output 1**
```

```

**Sample Explanation 1**
The input line is empty, so the tree has no nodes. The inorder traversal is also empty.

**Sample Input 2**
```
1
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
1 2 3 4 5 6 7
```

**Sample Output 3**
```
4 2 5 1 6 3 7
```

**Sample Input 4**
```
5 3 8 1 4 7 9
```

**Sample Output 4**
```
1 3 4 5 7 8 9
```

**Sample Input 5**
```
1 2 null 3 null 4
```

**Sample Output 5**
```
4 3 2 1
```

**Sample Input 6**
```
1 null 2 null 3 null 4
```

**Sample Output 6**
```
1 2 3 4
```

**Sample Input 7**
```
10 5 15 null null 12 20
```

**Sample Output 7**
```
5 10 12 15 20
```

**Sample Input 8**
```
-1 -2 -3
```

**Sample Output 8**
```
-2 -1 -3
```

**Sample Input 9**
```
7 3 9 1 5 8 10
```

**Sample Output 9**
```
1 3 5 7 8 9 10
```

**Tags**
Binary Tree, DFS, Recursion

**Boilerplate (C++14)** — NOT parsed by the automator. Paste into HackerRank admin **Head Code / Body / Tail Code** slots after upload.

Head Code:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode* buildTree(const string& line) {
    vector<string> toks;
    {
        stringstream ss(line);
        string t;
        while (ss >> t) toks.push_back(t);
    }
    if (toks.empty() || toks[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(toks[0]));
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < toks.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->left = new TreeNode(stoi(toks[i]));
                q.push(node->left);
            }
            ++i;
        }
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->right = new TreeNode(stoi(toks[i]));
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}
```

Solution Template (the user writes only this):
```cpp
vector<int> inorderTraversal(TreeNode* root) {
    // Write your code here
    return {};
}
```

Tail Code:
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    vector<int> ans = inorderTraversal(root);
    for (size_t i = 0; i < ans.size(); ++i) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << endl;
    return 0;
}
```

**Boilerplate (Java 8)** — same convention as the C++ version above.

Head Code:
```java
import java.util.*;
import java.io.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        String[] toks = line.trim().split("\\s+");
        if (toks.length == 0 || toks[0].isEmpty() || toks[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(toks[0]));
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < toks.length) {
            TreeNode node = q.poll();
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.left);
                }
                i++;
            }
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.right);
                }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static List<Integer> inorderTraversal(TreeNode root) {
        // Write your code here
        return new ArrayList<>();
    }
```

Tail Code:
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        List<Integer> ans = inorderTraversal(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
    }
}
```

---

## Midterm: Minimum Depth of a Binary Tree
**Difficulty**: Easy

**Problem Statement**
Given the root of a binary tree, return its minimum depth: the number of nodes on the shortest path from the root to the nearest leaf. A leaf is a node with no children. If the tree is empty, print `0`.

**Input Format**
A single line containing the level-order serialization of the tree (see the "Tree input convention" at the top of this file).

**Output Format**
A single integer — the minimum depth of the tree.

**Constraints**
- `0 <= number of nodes <= 100000`
- `-10^9 <= Node.val <= 10^9`

**Sample Input 0**
```
3 9 20 null null 15 7
```

**Sample Output 0**
```
2
```

**Sample Explanation 0**
The root `3` has two children, `9` (a leaf) and `20`. The shortest root-to-leaf path is `3 -> 9`, which has 2 nodes, so the minimum depth is `2`.

**Sample Input 1**
```
2 null 3 null 4 null 5 null 6
```

**Sample Output 1**
```
5
```

**Sample Explanation 1**
The tree is a right-leaning chain of 5 nodes (`2 -> 3 -> 4 -> 5 -> 6`). The only leaf is `6`, reached at depth `5`.

**Sample Input 2**
```

```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
1
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
1 2
```

**Sample Output 4**
```
2
```

**Sample Input 5**
```
1 null 2
```

**Sample Output 5**
```
2
```

**Sample Input 6**
```
1 2 3 4 5 6 7
```

**Sample Output 6**
```
3
```

**Sample Input 7**
```
10 5 15 null null 12 20
```

**Sample Output 7**
```
2
```

**Sample Input 8**
```
1 2 null 3 null 4 null 5
```

**Sample Output 8**
```
5
```

**Sample Input 9**
```
5 3 8 1 null null 9
```

**Sample Output 9**
```
3
```

**Tags**
Binary Tree, BFS, DFS

**Boilerplate (C++14)** — NOT parsed by the automator.

Head Code:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode* buildTree(const string& line) {
    vector<string> toks;
    {
        stringstream ss(line);
        string t;
        while (ss >> t) toks.push_back(t);
    }
    if (toks.empty() || toks[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(toks[0]));
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < toks.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->left = new TreeNode(stoi(toks[i]));
                q.push(node->left);
            }
            ++i;
        }
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->right = new TreeNode(stoi(toks[i]));
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}
```

Solution Template:
```cpp
int minDepth(TreeNode* root) {
    // Write your code here
    return 0;
}
```

Tail Code:
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << minDepth(root) << endl;
    return 0;
}
```

**Boilerplate (Java 8)**

Head Code:
```java
import java.util.*;
import java.io.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        String[] toks = line.trim().split("\\s+");
        if (toks.length == 0 || toks[0].isEmpty() || toks[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(toks[0]));
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < toks.length) {
            TreeNode node = q.poll();
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.left);
                }
                i++;
            }
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.right);
                }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static int minDepth(TreeNode root) {
        // Write your code here
        return 0;
    }
```

Tail Code:
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        System.out.println(minDepth(root));
    }
}
```

---

## Midterm: Merge Intervals
**Difficulty**: Medium

**Problem Statement**
Given a collection of intervals `[start, end]`, merge all overlapping intervals and return the resulting list of pairwise non-overlapping intervals, sorted by start. Two intervals touching at a shared endpoint (for example `[1,4]` and `[4,6]`) are considered overlapping and must be merged into `[1,6]`.

**Input Format**
- Line 1: a single integer `N` — the number of intervals.
- Next `N` lines: each contains two space-separated integers `start` and `end` describing an interval.

**Output Format**
Print the merged intervals, one per line, each as two space-separated integers. Intervals must be printed in non-decreasing order of start.

**Constraints**
- `1 <= N <= 300000`
- `-10^9 <= start <= end <= 10^9`

**Sample Input 0**
```
4
1 3
2 6
8 10
15 18
```

**Sample Output 0**
```
1 6
8 10
15 18
```

**Sample Explanation 0**
`[1,3]` and `[2,6]` overlap (since `2 <= 3`) and merge into `[1,6]`. `[8,10]` and `[15,18]` do not overlap with any other interval, so they remain as-is.

**Sample Input 1**
```
2
1 4
4 5
```

**Sample Output 1**
```
1 5
```

**Sample Explanation 1**
`[1,4]` and `[4,5]` touch at the shared endpoint `4`. The problem treats a shared endpoint as overlapping, so they merge into `[1,5]`.

**Sample Input 2**
```
1
5 7
```

**Sample Output 2**
```
5 7
```

**Sample Input 3**
```
3
1 10
2 3
4 5
```

**Sample Output 3**
```
1 10
```

**Sample Input 4**
```
3
5 6
1 2
3 4
```

**Sample Output 4**
```
1 2
3 4
5 6
```

**Sample Input 5**
```
4
-5 -1
-3 0
1 2
4 5
```

**Sample Output 5**
```
-5 0
1 2
4 5
```

**Sample Input 6**
```
2
1 1
1 1
```

**Sample Output 6**
```
1 1
```

**Sample Input 7**
```
5
1 4
0 2
3 5
6 7
7 8
```

**Sample Output 7**
```
0 5
6 8
```

**Sample Input 8**
```
3
-10 10
-20 -15
20 25
```

**Sample Output 8**
```
-20 -15
-10 10
20 25
```

**Sample Input 9**
```
4
1 3
5 7
2 4
6 8
```

**Sample Output 9**
```
1 4
5 8
```

**Tags**
Sorting, Greedy, Intervals

---

## Midterm: Next Greater Element
**Difficulty**: Medium

**Problem Statement**
Given an array `nums` of integers, for each element find the next greater element to its right — the first element strictly greater than it that appears later in the array. If no such element exists, use `-1`. Print all results space-separated on a single line, in the original order.

**Input Format**
- Line 1: a single integer `N` — the size of the array.
- Line 2: `N` space-separated integers — the array elements.

**Output Format**
A single line of `N` space-separated integers: the next greater element for each position, or `-1` where none exists.

**Constraints**
- `1 <= N <= 300000`
- `-10^9 <= nums[i] <= 10^9`

**Sample Input 0**
```
4
4 5 2 25
```

**Sample Output 0**
```
5 25 25 -1
```

**Sample Explanation 0**
For `4`, the next greater value on its right is `5`. For `5`, the next greater is `25`. For `2`, it is `25`. `25` has no greater value to its right, so the answer there is `-1`.

**Sample Input 1**
```
5
13 7 6 12 10
```

**Sample Output 1**
```
-1 12 12 -1 -1
```

**Sample Explanation 1**
`13` has no greater value to its right, so `-1`. Both `7` and `6` are followed by `12`. `12` and `10` are followed only by smaller values, so `-1` for each.

**Sample Input 2**
```
1
7
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
5
1 2 3 4 5
```

**Sample Output 3**
```
2 3 4 5 -1
```

**Sample Input 4**
```
5
5 4 3 2 1
```

**Sample Output 4**
```
-1 -1 -1 -1 -1
```

**Sample Input 5**
```
6
2 2 2 2 2 2
```

**Sample Output 5**
```
-1 -1 -1 -1 -1 -1
```

**Sample Input 6**
```
6
11 13 21 3 9 4
```

**Sample Output 6**
```
13 21 -1 9 -1 -1
```

**Sample Input 7**
```
3
-1 -2 -3
```

**Sample Output 7**
```
-1 -1 -1
```

**Sample Input 8**
```
3
-3 -2 -1
```

**Sample Output 8**
```
-2 -1 -1
```

**Sample Input 9**
```
7
6 8 0 1 3 4 7
```

**Sample Output 9**
```
8 -1 1 3 4 7 -1
```

**Tags**
Monotonic Stack, Arrays

---

## Midterm: Level Order Traversal of a Binary Tree
**Difficulty**: Medium

**Problem Statement**
Given the root of a binary tree, print its level-order traversal. Nodes within the same level are separated by single spaces; levels are separated by newlines. If the tree is empty, print nothing.

**Input Format**
A single line containing the level-order serialization of the tree (see the "Tree input convention" at the top of this file).

**Output Format**
Print each level of the tree on its own line, with the values on that level separated by single spaces.

**Constraints**
- `0 <= number of nodes <= 100000`
- `-10^9 <= Node.val <= 10^9`

**Sample Input 0**
```
3 9 20 null null 15 7
```

**Sample Output 0**
```
3
9 20
15 7
```

**Sample Explanation 0**
Level 1 is just the root `3`. Level 2 contains `3`'s children: `9` and `20`. Level 3 contains the grandchildren that exist: `15` and `7` (both children of `20`).

**Sample Input 1**
```
1
```

**Sample Output 1**
```
1
```

**Sample Explanation 1**
The tree has only one node, the root `1`. There is a single level, printed on its own line.

**Sample Input 2**
```

```

**Sample Output 2**
```

```

**Sample Input 3**
```
1 2 3 4 5 6 7
```

**Sample Output 3**
```
1
2 3
4 5 6 7
```

**Sample Input 4**
```
1 null 2 null 3
```

**Sample Output 4**
```
1
2
3
```

**Sample Input 5**
```
1 2 null 3 null 4
```

**Sample Output 5**
```
1
2
3
4
```

**Sample Input 6**
```
10 5 15 3 7 12 20
```

**Sample Output 6**
```
10
5 15
3 7 12 20
```

**Sample Input 7**
```
-1 -2 -3 -4 -5
```

**Sample Output 7**
```
-1
-2 -3
-4 -5
```

**Sample Input 8**
```
1 2 3 null 4 null 5
```

**Sample Output 8**
```
1
2 3
4 5
```

**Sample Input 9**
```
50 30 70 20 40 60 80
```

**Sample Output 9**
```
50
30 70
20 40 60 80
```

**Tags**
Binary Tree, BFS

**Boilerplate (C++14)** — NOT parsed by the automator.

Head Code:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode* buildTree(const string& line) {
    vector<string> toks;
    {
        stringstream ss(line);
        string t;
        while (ss >> t) toks.push_back(t);
    }
    if (toks.empty() || toks[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(toks[0]));
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < toks.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->left = new TreeNode(stoi(toks[i]));
                q.push(node->left);
            }
            ++i;
        }
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->right = new TreeNode(stoi(toks[i]));
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}
```

Solution Template:
```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    // Write your code here
    return {};
}
```

Tail Code:
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    vector<vector<int>> ans = levelOrder(root);
    for (const auto& level : ans) {
        for (size_t i = 0; i < level.size(); ++i) {
            if (i) cout << ' ';
            cout << level[i];
        }
        cout << '\n';
    }
    return 0;
}
```

**Boilerplate (Java 8)**

Head Code:
```java
import java.util.*;
import java.io.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        String[] toks = line.trim().split("\\s+");
        if (toks.length == 0 || toks[0].isEmpty() || toks[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(toks[0]));
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < toks.length) {
            TreeNode node = q.poll();
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.left);
                }
                i++;
            }
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.right);
                }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static List<List<Integer>> levelOrder(TreeNode root) {
        // Write your code here
        return new ArrayList<>();
    }
```

Tail Code:
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        List<List<Integer>> ans = levelOrder(root);
        StringBuilder sb = new StringBuilder();
        for (List<Integer> level : ans) {
            for (int i = 0; i < level.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(level.get(i));
            }
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}
```

---

## Midterm: Validate Binary Search Tree
**Difficulty**: Medium

**Problem Statement**
Given the root of a binary tree, determine whether it is a valid Binary Search Tree. A BST is defined so that for every node:
- All values in the left subtree are strictly less than the node's value.
- All values in the right subtree are strictly greater than the node's value.
- Both left and right subtrees are themselves BSTs.

Print `1` if the tree is a valid BST, else `0`. An empty tree is considered a valid BST.

**Input Format**
A single line containing the level-order serialization of the tree (see the "Tree input convention" at the top of this file).

**Output Format**
A single integer: `1` if the tree is a valid BST, else `0`.

**Constraints**
- `0 <= number of nodes <= 100000`
- `-10^9 <= Node.val <= 10^9`

**Sample Input 0**
```
2 1 3
```

**Sample Output 0**
```
1
```

**Sample Explanation 0**
Left child `1 < 2 = root < 3 = right child`. Every node satisfies the BST invariant, so this is a valid BST — output `1`.

**Sample Input 1**
```
5 1 4 null null 3 6
```

**Sample Output 1**
```
0
```

**Sample Explanation 1**
The right child `4` is less than root `5`. BST requires every value in the right subtree to be strictly greater than the root, so this is not a valid BST — output `0`.

**Sample Input 2**
```

```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
1
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
10 5 15 null null 6 20
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
10 5 15 3 7 12 20
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
2 2 2
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
3 1 5 0 2 4 6
```

**Sample Output 7**
```
1
```

**Sample Input 8**
```
5 4 6 null null 3 7
```

**Sample Output 8**
```
0
```

**Sample Input 9**
```
50 30 70 20 40 60 80
```

**Sample Output 9**
```
1
```

**Tags**
Binary Search Tree, DFS, Recursion

**Boilerplate (C++14)** — NOT parsed by the automator.

Head Code:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode* buildTree(const string& line) {
    vector<string> toks;
    {
        stringstream ss(line);
        string t;
        while (ss >> t) toks.push_back(t);
    }
    if (toks.empty() || toks[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(toks[0]));
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < toks.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->left = new TreeNode(stoi(toks[i]));
                q.push(node->left);
            }
            ++i;
        }
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->right = new TreeNode(stoi(toks[i]));
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}
```

Solution Template:
```cpp
bool isValidBST(TreeNode* root) {
    // Write your code here
    return true;
}
```

Tail Code:
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << (isValidBST(root) ? 1 : 0) << endl;
    return 0;
}
```

**Boilerplate (Java 8)**

Head Code:
```java
import java.util.*;
import java.io.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        String[] toks = line.trim().split("\\s+");
        if (toks.length == 0 || toks[0].isEmpty() || toks[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(toks[0]));
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < toks.length) {
            TreeNode node = q.poll();
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.left);
                }
                i++;
            }
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.right);
                }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static boolean isValidBST(TreeNode root) {
        // Write your code here
        return true;
    }
```

Tail Code:
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        System.out.println(isValidBST(root) ? 1 : 0);
    }
}
```

---

## Midterm: Diameter of a Binary Tree
**Difficulty**: Medium

**Problem Statement**
Given the root of a binary tree, return its diameter: the length (number of edges) of the longest path between any two nodes. The path may or may not pass through the root. If the tree is empty, print `0`.

**Input Format**
A single line containing the level-order serialization of the tree (see the "Tree input convention" at the top of this file).

**Output Format**
A single integer — the diameter of the tree.

**Constraints**
- `0 <= number of nodes <= 100000`
- `-10^9 <= Node.val <= 10^9`

**Sample Input 0**
```
1 2 3 4 5
```

**Sample Output 0**
```
3
```

**Sample Explanation 0**
The longest path in this tree is `4 -> 2 -> 1 -> 3` (equivalently `5 -> 2 -> 1 -> 3`), which contains 3 edges. The diameter is the number of edges on that longest path.

**Sample Input 1**
```
1 2
```

**Sample Output 1**
```
1
```

**Sample Explanation 1**
The tree is a single edge connecting nodes `1` and `2`. The diameter — the number of edges on the longest path — is `1`.

**Sample Input 2**
```

```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
1
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
1 2 3 4 5 6 7
```

**Sample Output 4**
```
4
```

**Sample Input 5**
```
1 2 null 3 null 4 null 5
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
1 null 2 null 3 null 4 null 5
```

**Sample Output 6**
```
4
```

**Sample Input 7**
```
10 5 15 3 7 null 20
```

**Sample Output 7**
```
4
```

**Sample Input 8**
```
1 2 3 4 null 5 null 6 null null null 7
```

**Sample Output 8**
```
6
```

**Sample Input 9**
```
50 30 70 20 40 60 80 10
```

**Sample Output 9**
```
5
```

**Tags**
Binary Tree, DFS, Recursion

**Boilerplate (C++14)** — NOT parsed by the automator.

Head Code:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode* buildTree(const string& line) {
    vector<string> toks;
    {
        stringstream ss(line);
        string t;
        while (ss >> t) toks.push_back(t);
    }
    if (toks.empty() || toks[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(toks[0]));
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < toks.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->left = new TreeNode(stoi(toks[i]));
                q.push(node->left);
            }
            ++i;
        }
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->right = new TreeNode(stoi(toks[i]));
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}
```

Solution Template:
```cpp
int diameterOfBinaryTree(TreeNode* root) {
    // Write your code here
    return 0;
}
```

Tail Code:
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << diameterOfBinaryTree(root) << endl;
    return 0;
}
```

**Boilerplate (Java 8)**

Head Code:
```java
import java.util.*;
import java.io.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        String[] toks = line.trim().split("\\s+");
        if (toks.length == 0 || toks[0].isEmpty() || toks[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(toks[0]));
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < toks.length) {
            TreeNode node = q.poll();
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.left);
                }
                i++;
            }
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.right);
                }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static int diameterOfBinaryTree(TreeNode root) {
        // Write your code here
        return 0;
    }
```

Tail Code:
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        System.out.println(diameterOfBinaryTree(root));
    }
}
```

---

## Midterm: Lowest Common Ancestor of a Binary Tree
**Difficulty**: Medium

**Problem Statement**
Given the root of a binary tree and two distinct integer values `p` and `q` that are guaranteed to exist in the tree (and node values in the tree are unique), find and print the value of their Lowest Common Ancestor (LCA). The LCA of two nodes is the deepest node that has both of them as descendants (a node is considered a descendant of itself).

**Input Format**
- Line 1: level-order serialization of the tree (see the "Tree input convention" at the top of this file).
- Line 2: two space-separated integers `p` and `q`.

**Output Format**
A single integer — the value stored at the LCA of nodes `p` and `q`.

**Constraints**
- `2 <= number of nodes <= 100000`
- All node values are unique.
- `p != q` and both are present in the tree.
- `-10^9 <= Node.val, p, q <= 10^9`

**Sample Input 0**
```
3 5 1 6 2 0 8 null null 7 4
5 1
```

**Sample Output 0**
```
3
```

**Sample Explanation 0**
`5` lies in the left subtree of root `3`, and `1` is the right child of root `3`. The deepest node that has both as descendants is the root itself, so the LCA is `3`.

**Sample Input 1**
```
3 5 1 6 2 0 8 null null 7 4
5 4
```

**Sample Output 1**
```
5
```

**Sample Explanation 1**
Starting from root `3`, both `5` and `4` lie inside the subtree rooted at `5` (since `4` is reachable as a descendant of `5`). A node counts as a descendant of itself, so the LCA is `5`.

**Sample Input 2**
```
1 2
1 2
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
1 2 3
2 3
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
10 5 15 3 7 12 20
3 7
```

**Sample Output 4**
```
5
```

**Sample Input 5**
```
10 5 15 3 7 12 20
3 20
```

**Sample Output 5**
```
10
```

**Sample Input 6**
```
1 2 null 3 null 4 null 5
3 5
```

**Sample Output 6**
```
3
```

**Sample Input 7**
```
1 2 null 3 null 4 null 5
2 5
```

**Sample Output 7**
```
2
```

**Sample Input 8**
```
50 30 70 20 40 60 80
20 40
```

**Sample Output 8**
```
30
```

**Sample Input 9**
```
50 30 70 20 40 60 80
20 80
```

**Sample Output 9**
```
50
```

**Tags**
Binary Tree, DFS, Recursion

**Boilerplate (C++14)** — NOT parsed by the automator.

Head Code:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode* buildTree(const string& line) {
    vector<string> toks;
    {
        stringstream ss(line);
        string t;
        while (ss >> t) toks.push_back(t);
    }
    if (toks.empty() || toks[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(toks[0]));
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < toks.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->left = new TreeNode(stoi(toks[i]));
                q.push(node->left);
            }
            ++i;
        }
        if (i < toks.size()) {
            if (toks[i] != "null") {
                node->right = new TreeNode(stoi(toks[i]));
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}

static TreeNode* findNode(TreeNode* root, int v) {
    if (!root) return nullptr;
    if (root->val == v) return root;
    TreeNode* l = findNode(root->left, v);
    if (l) return l;
    return findNode(root->right, v);
}
```

Solution Template:
```cpp
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    // Write your code here
    return nullptr;
}
```

Tail Code:
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    int pv, qv;
    cin >> pv >> qv;
    TreeNode* p = findNode(root, pv);
    TreeNode* q = findNode(root, qv);
    TreeNode* ans = lowestCommonAncestor(root, p, q);
    cout << (ans ? ans->val : 0) << endl;
    return 0;
}
```

**Boilerplate (Java 8)**

Head Code:
```java
import java.util.*;
import java.io.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        String[] toks = line.trim().split("\\s+");
        if (toks.length == 0 || toks[0].isEmpty() || toks[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(toks[0]));
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < toks.length) {
            TreeNode node = q.poll();
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.left);
                }
                i++;
            }
            if (i < toks.length) {
                if (!toks[i].equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(toks[i]));
                    q.add(node.right);
                }
                i++;
            }
        }
        return root;
    }

    static TreeNode findNode(TreeNode root, int v) {
        if (root == null) return null;
        if (root.val == v) return root;
        TreeNode l = findNode(root.left, v);
        if (l != null) return l;
        return findNode(root.right, v);
    }
```

Solution Template:
```java
    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Write your code here
        return null;
    }
```

Tail Code:
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        StringTokenizer st = new StringTokenizer(br.readLine());
        int pv = Integer.parseInt(st.nextToken());
        int qv = Integer.parseInt(st.nextToken());
        TreeNode p = findNode(root, pv);
        TreeNode q = findNode(root, qv);
        TreeNode ans = lowestCommonAncestor(root, p, q);
        System.out.println(ans == null ? 0 : ans.val);
    }
}
```

---

## Midterm: Search in a Rotated Sorted Array
**Difficulty**: Medium

**Problem Statement**
An array of distinct integers that was originally sorted in strictly ascending order has been rotated at some unknown pivot index. Given the resulting array `nums` and an integer `target`, return the 0-based index of `target`, or `-1` if it is not present.

**Input Format**
- Line 1: two space-separated integers `N` (size of the array) and `target`.
- Line 2: `N` space-separated integers — the rotated array.

**Output Format**
A single integer — the 0-based index of `target`, or `-1` if not present.

**Constraints**
- `1 <= N <= 100000`
- All values in `nums` are distinct.
- `-10^9 <= nums[i], target <= 10^9`

**Sample Input 0**
```
7 0
4 5 6 7 0 1 2
```

**Sample Output 0**
```
4
```

**Sample Explanation 0**
The array was originally `0 1 2 4 5 6 7` and was rotated so it starts at `4`. The target `0` ends up at index `4` of the rotated array.

**Sample Input 1**
```
7 3
4 5 6 7 0 1 2
```

**Sample Output 1**
```
-1
```

**Sample Explanation 1**
The target `3` is not present anywhere in the rotated array, so the answer is `-1`.

**Sample Input 2**
```
1 0
1
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
1 5
5
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
5 3
1 2 3 4 5
```

**Sample Output 4**
```
2
```

**Sample Input 5**
```
5 1
3 4 5 1 2
```

**Sample Output 5**
```
3
```

**Sample Input 6**
```
5 5
3 4 5 1 2
```

**Sample Output 6**
```
2
```

**Sample Input 7**
```
6 4
6 7 8 1 2 3
```

**Sample Output 7**
```
-1
```

**Sample Input 8**
```
6 8
6 7 8 1 2 3
```

**Sample Output 8**
```
2
```

**Sample Input 9**
```
8 15
10 12 15 20 1 3 5 7
```

**Sample Output 9**
```
2
```

**Tags**
Binary Search, Arrays

---

## Midterm: Lower Bound in a Sorted Array
**Difficulty**: Medium

**Problem Statement**
Given a sorted (non-decreasing) array of integers `nums` and a batch of `Q` queries, for each query return the 0-based index of the first element in `nums` that is greater than or equal to the query value (the "lower bound"). If every element is strictly less than the target, return `N`.

**Input Format**
- Line 1: two space-separated integers `N` (size of the array) and `Q` (number of queries).
- Line 2: `N` space-separated integers — the sorted array.
- Line 3: `Q` space-separated integers — the targets.

**Output Format**
A single line of `Q` space-separated integers — the lower-bound index for each target in order.

**Constraints**
- `1 <= N <= 200000`
- `1 <= Q <= 200000`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order.

**Sample Input 0**
```
6 2
1 3 5 7 9 11
4 5
```

**Sample Output 0**
```
2 2
```

**Sample Explanation 0**
The first element `>= 4` is `5` at index 2. The first element `>= 5` is `5` itself, also at index 2.

**Sample Input 1**
```
6 2
1 3 5 7 9 11
0 12
```

**Sample Output 1**
```
0 6
```

**Sample Explanation 1**
`0` is less than every element, so the lower bound is index 0. `12` is greater than every element, so the lower bound is `N = 6`.

**Sample Input 2**
```
1 2
5
5 6
```

**Sample Output 2**
```
0 1
```

**Sample Input 3**
```
5 3
2 2 2 2 2
2 3 1
```

**Sample Output 3**
```
0 5 0
```

**Sample Input 4**
```
7 2
-5 -3 -1 0 2 4 6
0 7
```

**Sample Output 4**
```
3 7
```

**Sample Input 5**
```
8 1
1 2 3 4 5 6 7 8
10
```

**Sample Output 5**
```
8
```

**Sample Input 6**
```
5 2
1 1 1 1 1
0 2
```

**Sample Output 6**
```
0 5
```

**Sample Input 7**
```
3 3
-1000000000 0 1000000000
-1000000000 1 1000000001
```

**Sample Output 7**
```
0 2 3
```

**Sample Input 8**
```
10 1
1 2 3 4 5 6 7 8 9 10
5
```

**Sample Output 8**
```
4
```

**Sample Input 9**
```
4 2
-10 -5 0 5
-10 5
```

**Sample Output 9**
```
0 3
```

**Tags**
Binary Search, Arrays

---

## Midterm: Sort Characters by Frequency
**Difficulty**: Hard

**Problem Statement**
Given a string `s`, rearrange its characters so that characters with a higher frequency appear first. If two characters have the same frequency, break the tie by printing the one with the smaller ASCII code first (deterministic ordering). Return the resulting string.

**Input Format**
A single line containing the string `s`.

**Output Format**
A single line — the rearranged string.

**Constraints**
- `1 <= |s| <= 300000`
- `s` consists of printable ASCII characters without spaces.

**Sample Input 0**
```
tree
```

**Sample Output 0**
```
eert
```

**Sample Explanation 0**
Frequencies: `e`=2, `r`=1, `t`=1. Higher-frequency characters come first, so `e,e` lead. Between `r` and `t` (both frequency 1), the smaller ASCII code `r` (114) comes before `t` (116). Result: `eert`.

**Sample Input 1**
```
cccaaa
```

**Sample Output 1**
```
aaaccc
```

**Sample Explanation 1**
Both `c` and `a` have frequency `3`. On a tie we break by smaller ASCII, and `a` (97) < `c` (99), so all three `a`s come before all three `c`s: `aaaccc`.

**Sample Input 2**
```
Aabb
```

**Sample Output 2**
```
bbAa
```

**Sample Input 3**
```
a
```

**Sample Output 3**
```
a
```

**Sample Input 4**
```
zzzyyx
```

**Sample Output 4**
```
zzzyyx
```

**Sample Input 5**
```
abcabc
```

**Sample Output 5**
```
aabbcc
```

**Sample Input 6**
```
mississippi
```

**Sample Output 6**
```
iiiissssppm
```

**Sample Input 7**
```
aAaA
```

**Sample Output 7**
```
AAaa
```

**Sample Input 8**
```
112233
```

**Sample Output 8**
```
112233
```

**Sample Input 9**
```
raaeaedere
```

**Sample Output 9**
```
eeeeaaarrd
```

**Tags**
Hashmap, Sorting, Strings

---

## Midterm: Kth Largest Element in an Array
**Difficulty**: Hard

**Problem Statement**
Given an integer array `nums` and an integer `k`, return the `k`-th largest element in the array when values are considered with multiplicity. That is, if the array is sorted in non-increasing order, return the element at 0-based index `k-1`.

**Input Format**
- Line 1: two space-separated integers `N` and `k`.
- Line 2: `N` space-separated integers — the array elements.

**Output Format**
A single integer — the k-th largest element.

**Constraints**
- `1 <= k <= N <= 200000`
- `-10^9 <= nums[i] <= 10^9`

**Sample Input 0**
```
6 2
3 2 1 5 6 4
```

**Sample Output 0**
```
5
```

**Sample Explanation 0**
Sorted in non-increasing order: `6, 5, 4, 3, 2, 1`. The 2nd largest element (position `k-1 = 1`) is `5`.

**Sample Input 1**
```
9 4
3 2 3 1 2 4 5 5 6
```

**Sample Output 1**
```
4
```

**Sample Explanation 1**
Sorted in non-increasing order (duplicates kept): `6, 5, 5, 4, 3, 3, 2, 2, 1`. The 4th element is `4`.

**Sample Input 2**
```
1 1
7
```

**Sample Output 2**
```
7
```

**Sample Input 3**
```
5 1
1 2 3 4 5
```

**Sample Output 3**
```
5
```

**Sample Input 4**
```
5 5
1 2 3 4 5
```

**Sample Output 4**
```
1
```

**Sample Input 5**
```
5 3
5 5 5 5 5
```

**Sample Output 5**
```
5
```

**Sample Input 6**
```
6 3
-1 -2 -3 -4 -5 -6
```

**Sample Output 6**
```
-3
```

**Sample Input 7**
```
7 4
10 7 11 5 10 11 3
```

**Sample Output 7**
```
10
```

**Sample Input 8**
```
4 2
1000000000 -1000000000 0 999999999
```

**Sample Output 8**
```
999999999
```

**Sample Input 9**
```
8 6
20 20 10 10 30 30 40 40
```

**Sample Output 9**
```
20
```

**Tags**
Sorting, Heap, Quickselect
