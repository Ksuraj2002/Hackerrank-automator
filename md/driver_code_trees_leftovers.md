# Driver Code -- leftover tree challenges

The seven tree sections whose titles were ambiguous on HackerRank (or where no HR challenge exists yet). Each ambiguous one carries a `<!-- hackerrank_id: X -->` override pinning it to the right copy.

Push with:

    python editor.py driver_code_trees_leftovers.md --boilerplate --apply

---

## Classwork: LC199 Binary Tree Right Side View
<!-- hackerrank_id: 591603 -->

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
 * Return the rightmost value at each level, from the top down.
 */
vector<int> rightSideView(TreeNode* root) {
    // Write your code here.
    return {};
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> t; string x;
    while (ss >> x) t.push_back(x);
    if (t.empty() || t[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "null") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    vector<int> ans = rightSideView(root);
    for (size_t i = 0; i < ans.size(); ++i) { if (i) cout << ' '; cout << ans[i]; }
    cout << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the rightmost value at each level, from the top down.
     */
    static List<Integer> rightSideView(TreeNode root) {
        // Write your code here.
        return new ArrayList<>();
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        line = line.trim();
        if (line.isEmpty()) return null;
        String[] tok = line.split("\\s+");
        if (tok.length == 0 || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.left = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.left); }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.right = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        List<Integer> ans = rightSideView(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---


## Classwork: LC101 Symmetric Tree
<!-- hackerrank_id: 591616 -->

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
 * Return true if the tree's left subtree is the mirror of its right subtree.
 */
bool isSymmetric(TreeNode* root) {
    // Write your code here.
    return false;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> t; string x;
    while (ss >> x) t.push_back(x);
    if (t.empty() || t[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "null") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << (isSymmetric(root) ? "true" : "false") << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return true if the tree's left subtree is the mirror of its right subtree.
     */
    static boolean isSymmetric(TreeNode root) {
        // Write your code here.
        return false;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        line = line.trim();
        if (line.isEmpty()) return null;
        String[] tok = line.split("\\s+");
        if (tok.length == 0 || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.left = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.left); }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.right = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        System.out.println(isSymmetric(root) ? "true" : "false");
    }
}
```

---


## Classwork: LC100 Same Tree
<!-- hackerrank_id: 591631 -->

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
 * Return true if two trees have identical shape AND identical values.
 */
bool isSameTree(TreeNode* a, TreeNode* b) {
    // Write your code here.
    return false;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> t; string x;
    while (ss >> x) t.push_back(x);
    if (t.empty() || t[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "null") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string la, lb;
    getline(cin, la);
    getline(cin, lb);
    TreeNode* a = buildTree(la);
    TreeNode* b = buildTree(lb);
    cout << (isSameTree(a, b) ? "true" : "false") << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return true if two trees have identical shape AND identical values.
     */
    static boolean isSameTree(TreeNode a, TreeNode b) {
        // Write your code here.
        return false;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        line = line.trim();
        if (line.isEmpty()) return null;
        String[] tok = line.split("\\s+");
        if (tok.length == 0 || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.left = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.left); }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.right = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String la = br.readLine();
        String lb = br.readLine();
        TreeNode a = buildTree(la);
        TreeNode b = buildTree(lb);
        System.out.println(isSameTree(a, b) ? "true" : "false");
    }
}
```

---


## Classwork: LC124 Binary Tree Maximum Path Sum
<!-- hackerrank_id: 591639 -->

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
 * Return the maximum sum over any path (need not pass through root).
 */
int maxPathSum(TreeNode* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> t; string x;
    while (ss >> x) t.push_back(x);
    if (t.empty() || t[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "null") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << maxPathSum(root) << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the maximum sum over any path (need not pass through root).
     */
    static int maxPathSum(TreeNode root) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        line = line.trim();
        if (line.isEmpty()) return null;
        String[] tok = line.split("\\s+");
        if (tok.length == 0 || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.left = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.left); }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.right = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        System.out.println(maxPathSum(root));
    }
}
```

---


## Homework: Find the sum of all node values in a binary tree

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
 * Return the sum of every node's value. Empty tree sums to 0.
 */
int sumOfAllNodes(TreeNode* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> t; string x;
    while (ss >> x) t.push_back(x);
    if (t.empty() || t[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "null") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << sumOfAllNodes(root) << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the sum of every node's value. Empty tree sums to 0.
     */
    static int sumOfAllNodes(TreeNode root) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        line = line.trim();
        if (line.isEmpty()) return null;
        String[] tok = line.split("\\s+");
        if (tok.length == 0 || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.left = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.left); }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.right = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        System.out.println(sumOfAllNodes(root));
    }
}
```

---


## Homework: LC100 Same Tree
<!-- hackerrank_id: 591618 -->

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
 * Return true if two trees are structurally and value-wise identical.
 */
bool isSameTreeHW(TreeNode* a, TreeNode* b) {
    // Write your code here.
    return false;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> t; string x;
    while (ss >> x) t.push_back(x);
    if (t.empty() || t[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "null") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string la, lb;
    getline(cin, la);
    getline(cin, lb);
    TreeNode* a = buildTree(la);
    TreeNode* b = buildTree(lb);
    cout << (isSameTreeHW(a, b) ? "true" : "false") << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return true if two trees are structurally and value-wise identical.
     */
    static boolean isSameTreeHW(TreeNode a, TreeNode b) {
        // Write your code here.
        return false;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        line = line.trim();
        if (line.isEmpty()) return null;
        String[] tok = line.split("\\s+");
        if (tok.length == 0 || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.left = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.left); }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.right = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String la = br.readLine();
        String lb = br.readLine();
        TreeNode a = buildTree(la);
        TreeNode b = buildTree(lb);
        System.out.println(isSameTreeHW(a, b) ? "true" : "false");
    }
}
```

---


## Homework: LC129 Sum Root to Leaf Numbers
<!-- hackerrank_id: 591641 -->

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
 * Sum the integers formed by concatenating digits on each root-to-leaf path.
 */
int sumNumbers(TreeNode* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> t; string x;
    while (ss >> x) t.push_back(x);
    if (t.empty() || t[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(t[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "null") { cur->left = new TreeNode(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") { cur->right = new TreeNode(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    cout << sumNumbers(root) << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Sum the integers formed by concatenating digits on each root-to-leaf path.
     */
    static int sumNumbers(TreeNode root) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    static TreeNode buildTree(String line) {
        if (line == null) return null;
        line = line.trim();
        if (line.isEmpty()) return null;
        String[] tok = line.split("\\s+");
        if (tok.length == 0 || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.left = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.left); }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) { cur.right = new TreeNode(Integer.parseInt(tok[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        System.out.println(sumNumbers(root));
    }
}
```

---
