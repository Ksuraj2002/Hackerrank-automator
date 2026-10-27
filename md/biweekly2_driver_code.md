# Biweekly-2 Driver Code — Tree Problems

Three challenges. Each has six fenced blocks: `**C++ Head**`, `**C++ Body**`,
`**C++ Tail**`, `**Java Head**`, `**Java Body**`, `**Java Tail**`.
Head + Body + Tail concatenate (in that order) into a complete compilable
program. Head and Tail are locked on HackerRank; students only edit Body.

Push with:

```
python editor.py biweekly2_driver_code.md --boilerplate --apply
```

Titles match the challenges already in the admin catalog (ids 597930 / 597933 /
597936). The tree-input encoding used by every test case is: level-order tokens
where the letter `N` marks a null child.

---

## Height of Binary Tree

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};
```

**C++ Body**
```cpp
/*
 * Return the height of the tree rooted at `root`.
 * Height = number of nodes on the longest path from root to any leaf.
 * An empty tree has height 0; a single-node tree has height 1.
 */
int height(TreeNode* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const vector<string>& t) {
    if (t.empty() || t[0] == "N") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "N") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "N") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    int n; if (!(cin >> n)) return 0;
    vector<string> tokens(n);
    for (int i = 0; i < n; i++) cin >> tokens[i];
    TreeNode* root = buildTree(tokens);
    cout << height(root) << endl;
    return 0;
}
```

**Java Head**
```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the height of the tree rooted at `root`.
     * Height = number of nodes on the longest path from root to any leaf.
     * An empty tree has height 0; a single-node tree has height 1.
     */
    static int height(TreeNode root) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String[] t) {
        if (t.length == 0 || t[0].equals("N")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(t[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < t.length) {
            TreeNode cur = q.poll();
            if (i < t.length) {
                if (!t[i].equals("N")) { cur.left = new TreeNode(Integer.parseInt(t[i])); q.add(cur.left); }
                i++;
            }
            if (i < t.length) {
                if (!t[i].equals("N")) { cur.right = new TreeNode(Integer.parseInt(t[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] tokens = new String[n];
        for (int i = 0; i < n; i++) tokens[i] = sc.next();
        TreeNode root = buildTree(tokens);
        System.out.println(height(root));
    }
}
```

---

## Iterative Preorder Traversal

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};
```

**C++ Body**
```cpp
/*
 * Return the preorder traversal (Root, Left, Right) of the tree rooted at
 * `root`, as a vector of node values. Implement this iteratively; do not use
 * recursion.
 */
vector<int> preorder(TreeNode* root) {
    // Write your code here.
    return {};
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const vector<string>& t) {
    if (t.empty() || t[0] == "N") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "N") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "N") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    int n; if (!(cin >> n)) return 0;
    vector<string> tokens(n);
    for (int i = 0; i < n; i++) cin >> tokens[i];
    TreeNode* root = buildTree(tokens);
    vector<int> ans = preorder(root);
    for (size_t i = 0; i < ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << endl;
    return 0;
}
```

**Java Head**
```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the preorder traversal (Root, Left, Right) of the tree rooted at
     * `root`, as a list of node values. Implement this iteratively; do not
     * use recursion.
     */
    static List<Integer> preorder(TreeNode root) {
        // Write your code here.
        return new ArrayList<>();
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String[] t) {
        if (t.length == 0 || t[0].equals("N")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(t[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < t.length) {
            TreeNode cur = q.poll();
            if (i < t.length) {
                if (!t[i].equals("N")) { cur.left = new TreeNode(Integer.parseInt(t[i])); q.add(cur.left); }
                i++;
            }
            if (i < t.length) {
                if (!t[i].equals("N")) { cur.right = new TreeNode(Integer.parseInt(t[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] tokens = new String[n];
        for (int i = 0; i < n; i++) tokens[i] = sc.next();
        TreeNode root = buildTree(tokens);
        List<Integer> ans = preorder(root);
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

## Maximum Path Sum (Root to Leaf) in Binary Tree

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};
```

**C++ Body**
```cpp
/*
 * Return the maximum sum over all root-to-leaf paths of the tree rooted at
 * `root`. A leaf is a node with no children. If the tree contains a single
 * node, the answer is that node's value.
 */
long long maxPathSum(TreeNode* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const vector<string>& t) {
    if (t.empty() || t[0] == "N") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "N") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "N") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    int n; if (!(cin >> n)) return 0;
    vector<string> tokens(n);
    for (int i = 0; i < n; i++) cin >> tokens[i];
    TreeNode* root = buildTree(tokens);
    cout << maxPathSum(root) << endl;
    return 0;
}
```

**Java Head**
```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the maximum sum over all root-to-leaf paths of the tree rooted
     * at `root`. A leaf is a node with no children. If the tree contains a
     * single node, the answer is that node's value.
     */
    static long maxPathSum(TreeNode root) {
        // Write your code here.
        return 0L;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String[] t) {
        if (t.length == 0 || t[0].equals("N")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(t[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < t.length) {
            TreeNode cur = q.poll();
            if (i < t.length) {
                if (!t[i].equals("N")) { cur.left = new TreeNode(Integer.parseInt(t[i])); q.add(cur.left); }
                i++;
            }
            if (i < t.length) {
                if (!t[i].equals("N")) { cur.right = new TreeNode(Integer.parseInt(t[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] tokens = new String[n];
        for (int i = 0; i < n; i++) tokens[i] = sc.next();
        TreeNode root = buildTree(tokens);
        System.out.println(maxPathSum(root));
    }
}
```
