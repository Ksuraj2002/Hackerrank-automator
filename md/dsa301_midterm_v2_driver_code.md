# DSA-301 Mid-Term Test Batch 2 — Driver Code (tree challenges)

Six fenced blocks per challenge: `**C++ Head**`, `**C++ Body**`, `**C++ Tail**`, `**Java Head**`, `**Java Body**`, `**Java Tail**`. Head + Body + Tail concatenate (in that order) to a complete compilable file. Head and Tail are locked; students only edit Body.

Push with:

```
python code/editor.py md/dsa301_midterm_v2_driver_code.md --boilerplate --apply
```

Titles below MUST match the HackerRank challenge titles exactly (as uploaded by `automator.py` from `dsa301_midterm_test_v2.md`). Covers the five tree problems in this contest: Q4, Q5, Q8, Q9, Q10.

---

## Midterm: Binary Tree Preorder Traversal

**C++ Head**
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

**C++ Body**
```cpp
vector<int> preorderTraversal(TreeNode* root) {
    // Write your code here
    return {};
}
```

**C++ Tail**
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    vector<int> ans = preorderTraversal(root);
    for (size_t i = 0; i < ans.size(); ++i) {
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

**Java Body**
```java
    static List<Integer> preorderTraversal(TreeNode root) {
        // Write your code here
        return new ArrayList<>();
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        List<Integer> ans = preorderTraversal(root);
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

## Midterm: Invert Binary Tree

**C++ Head**
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

static string serialize(TreeNode* root) {
    if (!root) return "";
    vector<string> out;
    vector<TreeNode*> order;
    order.push_back(root);
    size_t idx = 0;
    while (idx < order.size()) {
        TreeNode* n = order[idx++];
        if (!n) continue;
        order.push_back(n->left);
        order.push_back(n->right);
    }
    for (TreeNode* n : order) out.push_back(n ? to_string(n->val) : string("null"));
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) {
        if (i) s += ' ';
        s += out[i];
    }
    return s;
}
```

**C++ Body**
```cpp
TreeNode* invertTree(TreeNode* root) {
    // Write your code here
    return root;
}
```

**C++ Tail**
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* inv = invertTree(root);
    cout << serialize(inv) << endl;
    return 0;
}
```

**Java Head**
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

    static String serialize(TreeNode root) {
        if (root == null) return "";
        List<TreeNode> order = new ArrayList<>();
        order.add(root);
        int idx = 0;
        while (idx < order.size()) {
            TreeNode n = order.get(idx++);
            if (n == null) continue;
            order.add(n.left);
            order.add(n.right);
        }
        List<String> out = new ArrayList<>();
        for (TreeNode n : order) out.add(n == null ? "null" : Integer.toString(n.val));
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) {
            if (i > 0) sb.append(' ');
            sb.append(out.get(i));
        }
        return sb.toString();
    }
```

**Java Body**
```java
    static TreeNode invertTree(TreeNode root) {
        // Write your code here
        return root;
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        TreeNode inv = invertTree(root);
        System.out.println(serialize(inv));
    }
}
```

---

## Midterm: Zigzag Level Order Traversal of a Binary Tree

**C++ Head**
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

**C++ Body**
```cpp
vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    // Write your code here
    return {};
}
```

**C++ Tail**
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    vector<vector<int>> ans = zigzagLevelOrder(root);
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

**Java Head**
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

**Java Body**
```java
    static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        // Write your code here
        return new ArrayList<>();
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        List<List<Integer>> ans = zigzagLevelOrder(root);
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

## Midterm: Validate Binary Search Tree v2

**C++ Head**
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

**C++ Body**
```cpp
bool isValidBST(TreeNode* root) {
    // Write your code here
    return true;
}
```

**C++ Tail**
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << (isValidBST(root) ? 1 : 0) << endl;
    return 0;
}
```

**Java Head**
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

**Java Body**
```java
    static boolean isValidBST(TreeNode root) {
        // Write your code here
        return true;
    }
```

**Java Tail**
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

## Midterm: Kth Smallest Element in a BST

**C++ Head**
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

**C++ Body**
```cpp
int kthSmallest(TreeNode* root, int k) {
    // Write your code here
    return 0;
}
```

**C++ Tail**
```cpp
int main() {
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    int k;
    cin >> k;
    cout << kthSmallest(root, k) << endl;
    return 0;
}
```

**Java Head**
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

**Java Body**
```java
    static int kthSmallest(TreeNode root, int k) {
        // Write your code here
        return 0;
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line == null ? "" : line);
        int k = Integer.parseInt(br.readLine().trim());
        System.out.println(kthSmallest(root, k));
    }
}
```
