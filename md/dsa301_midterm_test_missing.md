# DSA-301 Mid-Term Test — missing 2

Subset of dsa301_midterm_test.md containing only the two challenges the first automator run skipped (Binary Search, LCA).

## Midterm: Binary Search
**Difficulty**: Easy

**Problem Statement**
Given a sorted (non-decreasing) array of integers `nums` and a target value `target`, return the 0-based index of `target` in the array. If the target does not exist, return `-1`. Your algorithm must run in `O(log N)` time.

**Input Format**
- Line 1: two space-separated integers `N` (size of the array) and `target`.
- Line 2: `N` space-separated integers — the sorted array elements.

**Output Format**
A single integer — the 0-based index of `target`, or `-1` if not present.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order.

**Sample Input 0**
```
6 9
-1 0 3 5 9 12
```

**Sample Output 0**
```
4
```

**Sample Explanation 0**
The target `9` is located at index `4` of the sorted array.

**Sample Input 1**
```
6 2
-1 0 3 5 9 12
```

**Sample Output 1**
```
-1
```

**Sample Explanation 1**
The target `2` is not present anywhere in the array, so we return `-1`.

**Sample Input 2**
```
1 5
5
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
1 5
3
```

**Sample Output 3**
```
-1
```

**Sample Input 4**
```
5 1
1 2 3 4 5
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
5 5
1 2 3 4 5
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
5 3
1 2 3 4 5
```

**Sample Output 6**
```
2
```

**Sample Input 7**
```
7 -4
-10 -7 -4 -1 2 5 8
```

**Sample Output 7**
```
2
```

**Sample Input 8**
```
8 100
1 2 3 4 5 6 7 8
```

**Sample Output 8**
```
-1
```

**Sample Input 9**
```
6 7
1 3 5 7 9 11
```

**Sample Output 9**
```
3
```

**Tags**
Binary Search, Arrays

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
