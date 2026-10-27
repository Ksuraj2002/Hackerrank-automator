# Driver Code (LeetCode-style) - Tree problems

One section per tree challenge in the DSA-301 classwork + homework contests.
Each section has six fenced blocks: `**C++ Head**`, `**C++ Body**`, `**C++ Tail**`,
`**Java Head**`, `**Java Body**`, `**Java Tail**`.

Push with:

    python editor.py driver_code_trees.md --boilerplate --apply

---

## Classwork: Build a 3-node binary tree manually and print root, left, right

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;
```

**C++ Body**
```cpp
/*
 * Print the three input values on three separate lines: root, left, right.
 */
void printThree(int root, int left, int right) {
    // Print each value on its own line, in order: root, left, right.
    // Write your code here.
}
```

**C++ Tail**
```cpp
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int a, b, c;
    cin >> a >> b >> c;
    printThree(a, b, c);
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

public class Solution {
```

**Java Body**
```java
    /*
     * Print the three input values on three separate lines: root, left, right.
     */
    static void printThree(int root, int left, int right) {
        // Print each value on its own line, in order: root, left, right.
        // Write your code here.
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        printThree(a, b, c);
    }
}
```

---

## Classwork: LC94 Binary Tree Inorder Traversal

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
 * Return the inorder (left-root-right) traversal of the tree as a list of values.
 */
vector<int> inorderTraversal(TreeNode* root) {
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
    vector<int> ans = inorderTraversal(root);
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
     * Return the inorder (left-root-right) traversal of the tree as a list of values.
     */
    static List<Integer> inorderTraversal(TreeNode root) {
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
        List<Integer> ans = inorderTraversal(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC144 Binary Tree Preorder Traversal

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
 * Return the preorder (root-left-right) traversal of the tree as a list of values.
 */
vector<int> preorderTraversal(TreeNode* root) {
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
    vector<int> ans = preorderTraversal(root);
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
     * Return the preorder (root-left-right) traversal of the tree as a list of values.
     */
    static List<Integer> preorderTraversal(TreeNode root) {
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
        List<Integer> ans = preorderTraversal(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC145 Binary Tree Postorder Traversal

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
 * Return the postorder (left-right-root) traversal of the tree as a list of values.
 */
vector<int> postorderTraversal(TreeNode* root) {
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
    vector<int> ans = postorderTraversal(root);
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
     * Return the postorder (left-right-root) traversal of the tree as a list of values.
     */
    static List<Integer> postorderTraversal(TreeNode root) {
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
        List<Integer> ans = postorderTraversal(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC102 Binary Tree Level Order Traversal

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
 * Return the level-order traversal grouped by level (one list per level).
 */
vector<vector<int>> levelOrder(TreeNode* root) {
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
    vector<vector<int>> ans = levelOrder(root);
    for (const auto& row : ans) {
        for (size_t i = 0; i < row.size(); ++i) { if (i) cout << ' '; cout << row[i]; }
        cout << "\n";
    }
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
     * Return the level-order traversal grouped by level (one list per level).
     */
    static List<List<Integer>> levelOrder(TreeNode root) {
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
        List<List<Integer>> ans = levelOrder(root);
        StringBuilder sb = new StringBuilder();
        for (List<Integer> row : ans) {
            for (int i = 0; i < row.size(); i++) { if (i > 0) sb.append(' '); sb.append(row.get(i)); }
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}
```

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

## Classwork: LC94 Inorder Traversal (iterative)

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
 * Return the inorder traversal using an explicit stack (no recursion).
 */
vector<int> inorderTraversalIter(TreeNode* root) {
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
    vector<int> ans = inorderTraversalIter(root);
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
     * Return the inorder traversal using an explicit stack (no recursion).
     */
    static List<Integer> inorderTraversalIter(TreeNode root) {
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
        List<Integer> ans = inorderTraversalIter(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: Count the number of levels in a binary tree

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
 * Return how many distinct levels the tree has. An empty tree has 0 levels.
 */
int countLevels(TreeNode* root) {
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
    cout << countLevels(root) << "\n";
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
     * Return how many distinct levels the tree has. An empty tree has 0 levels.
     */
    static int countLevels(TreeNode root) {
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
        System.out.println(countLevels(root));
    }
}
```

---

## Classwork: LC104 Maximum Depth of Binary Tree

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
 * Return the maximum depth: number of nodes on the longest root-to-leaf path.
 */
int maxDepth(TreeNode* root) {
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
    cout << maxDepth(root) << "\n";
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
     * Return the maximum depth: number of nodes on the longest root-to-leaf path.
     */
    static int maxDepth(TreeNode root) {
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
        System.out.println(maxDepth(root));
    }
}
```

---

## Classwork: LC111 Minimum Depth of Binary Tree

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
 * Return the minimum depth: number of nodes on the shortest root-to-leaf path.
 */
int minDepth(TreeNode* root) {
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
    cout << minDepth(root) << "\n";
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
     * Return the minimum depth: number of nodes on the shortest root-to-leaf path.
     */
    static int minDepth(TreeNode root) {
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
        System.out.println(minDepth(root));
    }
}
```

---

## Classwork: LC543 Diameter of Binary Tree

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
 * Return the diameter of the tree, measured in EDGES.
 */
int diameterOfBinaryTree(TreeNode* root) {
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
    cout << diameterOfBinaryTree(root) << "\n";
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
     * Return the diameter of the tree, measured in EDGES.
     */
    static int diameterOfBinaryTree(TreeNode root) {
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
        System.out.println(diameterOfBinaryTree(root));
    }
}
```

---

## Classwork: Check if a binary tree is a full binary tree

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
 * Return true if every internal node has exactly two children.
 */
bool isFullTree(TreeNode* root) {
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
    cout << (isFullTree(root) ? "true" : "false") << "\n";
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
     * Return true if every internal node has exactly two children.
     */
    static boolean isFullTree(TreeNode root) {
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
        System.out.println(isFullTree(root) ? "true" : "false");
    }
}
```

---

## Classwork: LC110 Balanced Binary Tree

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
 * Return true if for every node, |height(left) - height(right)| <= 1.
 */
bool isBalanced(TreeNode* root) {
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
    cout << (isBalanced(root) ? "true" : "false") << "\n";
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
     * Return true if for every node, |height(left) - height(right)| <= 1.
     */
    static boolean isBalanced(TreeNode root) {
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
        System.out.println(isBalanced(root) ? "true" : "false");
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

## Classwork: Left view of a binary tree (GfG)

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
 * Return the leftmost value at each level, from the top down.
 */
vector<int> leftView(TreeNode* root) {
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
    vector<int> ans = leftView(root);
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
     * Return the leftmost value at each level, from the top down.
     */
    static List<Integer> leftView(TreeNode root) {
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
        List<Integer> ans = leftView(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: Top view of a binary tree (GfG)

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
 * Return the top view: leftmost-to-rightmost, one value per vertical column.
 */
vector<int> topView(TreeNode* root) {
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
    vector<int> ans = topView(root);
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
     * Return the top view: leftmost-to-rightmost, one value per vertical column.
     */
    static List<Integer> topView(TreeNode root) {
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
        List<Integer> ans = topView(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: Boundary traversal of a binary tree (GfG)

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
 * Return the anti-clockwise boundary: root, left boundary, leaves, right boundary.
 */
vector<int> boundaryTraversal(TreeNode* root) {
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
    vector<int> ans = boundaryTraversal(root);
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
     * Return the anti-clockwise boundary: root, left boundary, leaves, right boundary.
     */
    static List<Integer> boundaryTraversal(TreeNode root) {
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
        List<Integer> ans = boundaryTraversal(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC987 Vertical Order Traversal of a Binary Tree

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
 * Return the vertical order traversal, grouped by column left to right.
 */
vector<vector<int>> verticalTraversal(TreeNode* root) {
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
    vector<vector<int>> ans = verticalTraversal(root);
    for (const auto& row : ans) {
        for (size_t i = 0; i < row.size(); ++i) { if (i) cout << ' '; cout << row[i]; }
        cout << "\n";
    }
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
     * Return the vertical order traversal, grouped by column left to right.
     */
    static List<List<Integer>> verticalTraversal(TreeNode root) {
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
        List<List<Integer>> ans = verticalTraversal(root);
        StringBuilder sb = new StringBuilder();
        for (List<Integer> row : ans) {
            for (int i = 0; i < row.size(); i++) { if (i > 0) sb.append(' '); sb.append(row.get(i)); }
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}
```

---

## Classwork: Swap the left and right children of the root only

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
 * Swap only the root's two children (in place) and return the tree.
 */
TreeNode* swapRootChildren(TreeNode* root) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = swapRootChildren(root);
    cout << serializeTree(out) << "\n";
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
     * Swap only the root's two children (in place) and return the tree.
     */
    static TreeNode swapRootChildren(TreeNode root) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = swapRootChildren(root);
        System.out.println(serializeTree(out));
    }
}
```

---

## Classwork: LC226 Invert Binary Tree

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
 * Swap every node's two children (in place) and return the tree.
 */
TreeNode* invertTree(TreeNode* root) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = invertTree(root);
    cout << serializeTree(out) << "\n";
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
     * Swap every node's two children (in place) and return the tree.
     */
    static TreeNode invertTree(TreeNode root) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = invertTree(root);
        System.out.println(serializeTree(out));
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

## Classwork: Find the sum of all leaf nodes in a binary tree

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
 * Return the sum of values of every leaf node. Empty tree sums to 0.
 */
int sumOfLeaves(TreeNode* root) {
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
    cout << sumOfLeaves(root) << "\n";
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
     * Return the sum of values of every leaf node. Empty tree sums to 0.
     */
    static int sumOfLeaves(TreeNode root) {
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
        System.out.println(sumOfLeaves(root));
    }
}
```

---

## Classwork: LC112 Path Sum

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
 * Return true if some root-to-leaf path's values sum exactly to `target`.
 */
bool hasPathSum(TreeNode* root, int target) {
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    cout << (hasPathSum(root, target) ? "true" : "false") << "\n";
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
     * Return true if some root-to-leaf path's values sum exactly to `target`.
     */
    static boolean hasPathSum(TreeNode root, int target) {
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(hasPathSum(root, target) ? "true" : "false");
    }
}
```

---

## Classwork: LC113 Path Sum II

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
 * Return every root-to-leaf path (as int lists) whose values sum to `target`.
 */
vector<vector<int>> pathSum(TreeNode* root, int target) {
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    vector<vector<int>> ans = pathSum(root, target);
    for (const auto& p : ans) {
        for (size_t i = 0; i < p.size(); ++i) { if (i) cout << ' '; cout << p[i]; }
        cout << "\n";
    }
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
     * Return every root-to-leaf path (as int lists) whose values sum to `target`.
     */
    static List<List<Integer>> pathSum(TreeNode root, int target) {
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        List<List<Integer>> ans = pathSum(root, target);
        StringBuilder sb = new StringBuilder();
        for (List<Integer> p : ans) {
            for (int i = 0; i < p.size(); i++) { if (i > 0) sb.append(' '); sb.append(p.get(i)); }
            sb.append('\n');
        }
        System.out.print(sb.toString());
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

## Classwork: Search whether a value exists in a binary tree

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
 * Return true if `target` appears anywhere in the tree.
 */
bool containsValue(TreeNode* root, int target) {
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    cout << (containsValue(root, target) ? "true" : "false") << "\n";
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
     * Return true if `target` appears anywhere in the tree.
     */
    static boolean containsValue(TreeNode root, int target) {
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(containsValue(root, target) ? "true" : "false");
    }
}
```

---

## Classwork: LC236 Lowest Common Ancestor of a Binary Tree

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
 * Return the value of the LCA of nodes with values `p` and `q`.
 */
int lcaValue(TreeNode* root, int p, int q) {
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
    int p, q; cin >> p >> q;
    TreeNode* root = buildTree(line);
    cout << lcaValue(root, p, q) << "\n";
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
     * Return the value of the LCA of nodes with values `p` and `q`.
     */
    static int lcaValue(TreeNode root, int p, int q) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(lcaValue(root, p, q));
    }
}
```

---

## Classwork: LCA using root-to-node paths (GfG)

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
 * Return the LCA value by comparing the two root-to-node paths.
 */
int lcaByPaths(TreeNode* root, int p, int q) {
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
    int p, q; cin >> p >> q;
    TreeNode* root = buildTree(line);
    cout << lcaByPaths(root, p, q) << "\n";
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
     * Return the LCA value by comparing the two root-to-node paths.
     */
    static int lcaByPaths(TreeNode root, int p, int q) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(lcaByPaths(root, p, q));
    }
}
```

---

## Classwork: Distance between two nodes via LCA (GfG)

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
 * Return the number of EDGES on the path between the two node values.
 */
int distanceBetween(TreeNode* root, int p, int q) {
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
    int p, q; cin >> p >> q;
    TreeNode* root = buildTree(line);
    cout << distanceBetween(root, p, q) << "\n";
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
     * Return the number of EDGES on the path between the two node values.
     */
    static int distanceBetween(TreeNode root, int p, int q) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(distanceBetween(root, p, q));
    }
}
```

---

## Classwork: Build a binary tree from a level-order array and print inorder

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
 * Return the inorder traversal of the tree that the input encodes.
 */
vector<int> inorderFromLevel(TreeNode* root) {
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
    vector<int> ans = inorderFromLevel(root);
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
     * Return the inorder traversal of the tree that the input encodes.
     */
    static List<Integer> inorderFromLevel(TreeNode root) {
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
        List<Integer> ans = inorderFromLevel(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC105 Construct Binary Tree from Preorder and Inorder

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
 * Rebuild the tree from its preorder + inorder traversals. Return the root.
 */
TreeNode* buildFromPreIn(vector<int>& preorder, vector<int>& inorder) {
    // Write your code here.
    return nullptr;
}
```

**C++ Tail**
```cpp
static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

static vector<int> readInts(const string& line) {
    stringstream ss(line);
    vector<int> v; int x;
    while (ss >> x) v.push_back(x);
    return v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string la, lb;
    getline(cin, la);
    getline(cin, lb);
    vector<int> A = readInts(la);
    vector<int> B = readInts(lb);
    TreeNode* root = buildFromPreIn(A, B);
    cout << serializeTree(root) << "\n";
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
     * Rebuild the tree from its preorder + inorder traversals. Return the root.
     */
    static TreeNode buildFromPreIn(int[] preorder, int[] inorder) {
        // Write your code here.
        return null;
    }
```

**Java Tail**
```java
    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    static int[] readInts(String line) {
        if (line == null) return new int[0];
        line = line.trim();
        if (line.isEmpty()) return new int[0];
        String[] tok = line.split("\\s+");
        int[] a = new int[tok.length];
        for (int i = 0; i < tok.length; i++) a[i] = Integer.parseInt(tok[i]);
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] A = readInts(br.readLine());
        int[] B = readInts(br.readLine());
        TreeNode root = buildFromPreIn(A, B);
        System.out.println(serializeTree(root));
    }
}
```

---

## Classwork: LC106 Construct Binary Tree from Inorder and Postorder

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
 * Rebuild the tree from its inorder + postorder traversals. Return the root.
 */
TreeNode* buildFromInPost(vector<int>& inorder, vector<int>& postorder) {
    // Write your code here.
    return nullptr;
}
```

**C++ Tail**
```cpp
static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

static vector<int> readInts(const string& line) {
    stringstream ss(line);
    vector<int> v; int x;
    while (ss >> x) v.push_back(x);
    return v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string la, lb;
    getline(cin, la);
    getline(cin, lb);
    vector<int> A = readInts(la);
    vector<int> B = readInts(lb);
    TreeNode* root = buildFromInPost(A, B);
    cout << serializeTree(root) << "\n";
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
     * Rebuild the tree from its inorder + postorder traversals. Return the root.
     */
    static TreeNode buildFromInPost(int[] inorder, int[] postorder) {
        // Write your code here.
        return null;
    }
```

**Java Tail**
```java
    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    static int[] readInts(String line) {
        if (line == null) return new int[0];
        line = line.trim();
        if (line.isEmpty()) return new int[0];
        String[] tok = line.split("\\s+");
        int[] a = new int[tok.length];
        for (int i = 0; i < tok.length; i++) a[i] = Integer.parseInt(tok[i]);
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] A = readInts(br.readLine());
        int[] B = readInts(br.readLine());
        TreeNode root = buildFromInPost(A, B);
        System.out.println(serializeTree(root));
    }
}
```

---

## Classwork: LC114 Flatten Binary Tree to Linked List

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
 * Flatten the tree in preorder (left=null, right=next) and return the values.
 */
vector<int> flattenAndCollect(TreeNode* root) {
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
    vector<int> ans = flattenAndCollect(root);
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
     * Flatten the tree in preorder (left=null, right=next) and return the values.
     */
    static List<Integer> flattenAndCollect(TreeNode root) {
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
        List<Integer> ans = flattenAndCollect(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: Count the total number of nodes in a binary tree

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
 * Return the total number of nodes. Empty tree has 0.
 */
int countNodes(TreeNode* root) {
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
    cout << countNodes(root) << "\n";
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
     * Return the total number of nodes. Empty tree has 0.
     */
    static int countNodes(TreeNode root) {
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
        System.out.println(countNodes(root));
    }
}
```

---

## Classwork: LC222 Count Complete Tree Nodes

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
 * Return the number of nodes in a complete tree in better than O(N).
 */
int countCompleteNodes(TreeNode* root) {
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
    cout << countCompleteNodes(root) << "\n";
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
     * Return the number of nodes in a complete tree in better than O(N).
     */
    static int countCompleteNodes(TreeNode root) {
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
        System.out.println(countCompleteNodes(root));
    }
}
```

---

## Classwork: LC863 All Nodes Distance K in Binary Tree

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
 * Return every value exactly K edges from the target, sorted ascending.
 */
vector<int> distanceK(TreeNode* root, int target, int k) {
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
    int target, k; cin >> target >> k;
    TreeNode* root = buildTree(line);
    vector<int> ans = distanceK(root, target, k);
    sort(ans.begin(), ans.end());
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
     * Return every value exactly K edges from the target, sorted ascending.
     */
    static List<Integer> distanceK(TreeNode root, int target, int k) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int target = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        List<Integer> ans = distanceK(root, target, k);
        Collections.sort(ans);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC297 Serialize and Deserialize Binary Tree

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
 * Serialize the tree, deserialize it back, and return the resulting root.
 */
TreeNode* serializeDeserialize(TreeNode* root) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = serializeDeserialize(root);
    cout << serializeTree(out) << "\n";
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
     * Serialize the tree, deserialize it back, and return the resulting root.
     */
    static TreeNode serializeDeserialize(TreeNode root) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = serializeDeserialize(root);
        System.out.println(serializeTree(out));
    }
}
```

---

## Classwork: Print the inorder of a BST and verify it is sorted

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
 * Return (inorder ints, isStrictlyIncreasing) as a pair to be printed on 2 lines.
 */
pair<vector<int>, bool> inorderAndSorted(TreeNode* root) {
    // Write your code here.
    return {{}, true};
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
    auto pr = inorderAndSorted(root);
    for (size_t i = 0; i < pr.first.size(); ++i) { if (i) cout << ' '; cout << pr.first[i]; }
    cout << "\n" << (pr.second ? "true" : "false") << "\n";
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
     * Return (inorder ints, isStrictlyIncreasing) as a pair to be printed on 2 lines.
     */
    static Object[] inorderAndSorted(TreeNode root) {
        // Return {List<Integer> inorder, Boolean strictlyIncreasing}.
        // Write your code here.
        return new Object[]{new ArrayList<Integer>(), true};
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
        Object[] pr = inorderAndSorted(root);
        @SuppressWarnings("unchecked")
        List<Integer> xs = (List<Integer>) pr[0];
        boolean ok = (Boolean) pr[1];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < xs.size(); i++) { if (i > 0) sb.append(' '); sb.append(xs.get(i)); }
        sb.append('\n').append(ok ? "true" : "false");
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC700 Search in a Binary Search Tree

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
 * Return the subtree rooted at the node whose value equals `key`, or null.
 */
TreeNode* searchBST(TreeNode* root, int key) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    TreeNode* out = searchBST(root, key);
    cout << serializeTree(out) << "\n";
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
     * Return the subtree rooted at the node whose value equals `key`, or null.
     */
    static TreeNode searchBST(TreeNode root, int key) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        TreeNode out = searchBST(root, key);
        System.out.println(serializeTree(out));
    }
}
```

---

## Classwork: Iterative BST search (GfG)

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
 * Return true if `key` is present in the BST. Iterative, O(1) space.
 */
bool iterativeSearchBST(TreeNode* root, int target) {
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    cout << (iterativeSearchBST(root, target) ? "true" : "false") << "\n";
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
     * Return true if `key` is present in the BST. Iterative, O(1) space.
     */
    static boolean iterativeSearchBST(TreeNode root, int target) {
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(iterativeSearchBST(root, target) ? "true" : "false");
    }
}
```

---

## Classwork: LC701 Insert into a Binary Search Tree

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
 * Insert `key` into the BST at the first empty spot; return the root.
 */
TreeNode* insertIntoBST(TreeNode* root, int key) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    TreeNode* out = insertIntoBST(root, key);
    cout << serializeTree(out) << "\n";
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
     * Insert `key` into the BST at the first empty spot; return the root.
     */
    static TreeNode insertIntoBST(TreeNode root, int key) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        TreeNode out = insertIntoBST(root, key);
        System.out.println(serializeTree(out));
    }
}
```

---

## Classwork: Check if an inorder traversal array is strictly increasing

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;
```

**C++ Body**
```cpp
/*
 * Return true if the array is strictly increasing.
 */
bool isStrictlyIncreasing(vector<int>& A) {
    // Write your code here.
    return true;
}
```

**C++ Tail**
```cpp
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    cout << (isStrictlyIncreasing(A) ? "true" : "false") << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

public class Solution {
```

**Java Body**
```java
    /*
     * Return true if the array is strictly increasing.
     */
    static boolean isStrictlyIncreasing(int[] A) {
        // Write your code here.
        return true;
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] A = new int[n];
        if (n > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) A[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(isStrictlyIncreasing(A) ? "true" : "false");
    }
}
```

---

## Classwork: LC530 Minimum Absolute Difference in BST

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
 * Return the smallest |a - b| over any two nodes in the BST.
 */
int getMinimumDifference(TreeNode* root) {
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
    cout << getMinimumDifference(root) << "\n";
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
     * Return the smallest |a - b| over any two nodes in the BST.
     */
    static int getMinimumDifference(TreeNode root) {
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
        System.out.println(getMinimumDifference(root));
    }
}
```

---

## Classwork: LC501 Find Mode in Binary Search Tree

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
 * Return every value with the maximum frequency, sorted ascending.
 */
vector<int> findMode(TreeNode* root) {
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
    vector<int> ans = findMode(root);
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
     * Return every value with the maximum frequency, sorted ascending.
     */
    static List<Integer> findMode(TreeNode root) {
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
        List<Integer> ans = findMode(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC98 Validate Binary Search Tree

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
 * Return true if the tree obeys the BST invariant everywhere.
 */
bool isValidBST(TreeNode* root) {
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
    cout << (isValidBST(root) ? "true" : "false") << "\n";
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
     * Return true if the tree obeys the BST invariant everywhere.
     */
    static boolean isValidBST(TreeNode root) {
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
        System.out.println(isValidBST(root) ? "true" : "false");
    }
}
```

---

## Classwork: Find the inorder successor of a node using the inorder array

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;
```

**C++ Body**
```cpp
/*
 * Return the smallest value strictly greater than `key`, or -2147483648 for null.
 */
int successorInArray(vector<int>& A, int key) {
    // Write your code here.
    return INT_MIN;
}
```

**C++ Tail**
```cpp
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    int key; cin >> key;
    int r = successorInArray(A, key);
    if (r == INT_MIN) cout << "null\n"; else cout << r << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

public class Solution {
```

**Java Body**
```java
    /*
     * Return the smallest value strictly greater than `key`, or -2147483648 for null.
     */
    static int successorInArray(int[] A, int key) {
        // Return Integer.MIN_VALUE to mean "null".
        // Write your code here.
        return Integer.MIN_VALUE;
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] A = new int[n];
        if (n > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) A[i] = Integer.parseInt(st.nextToken());
        }
        int key = Integer.parseInt(br.readLine().trim());
        int r = successorInArray(A, key);
        System.out.println(r == Integer.MIN_VALUE ? "null" : String.valueOf(r));
    }
}
```

---

## Classwork: LC450 Delete Node in a BST

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
 * Delete `key` from the BST if present; return the resulting root.
 */
TreeNode* deleteNode(TreeNode* root, int key) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    TreeNode* out = deleteNode(root, key);
    cout << serializeTree(out) << "\n";
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
     * Delete `key` from the BST if present; return the resulting root.
     */
    static TreeNode deleteNode(TreeNode root, int key) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        TreeNode out = deleteNode(root, key);
        System.out.println(serializeTree(out));
    }
}
```

---

## Classwork: LC230 Kth Smallest Element in a BST

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
 * Return the k-th smallest value (1-indexed) in the BST.
 */
int kthSmallest(TreeNode* root, int k) {
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
    int k; cin >> k;
    TreeNode* root = buildTree(line);
    cout << kthSmallest(root, k) << "\n";
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
     * Return the k-th smallest value (1-indexed) in the BST.
     */
    static int kthSmallest(TreeNode root, int k) {
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
        int k = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(kthSmallest(root, k));
    }
}
```

---

## Classwork: Kth largest element in a BST (GfG)

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
 * Return the k-th largest value (1-indexed) in the BST.
 */
int kthLargest(TreeNode* root, int k) {
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
    int k; cin >> k;
    TreeNode* root = buildTree(line);
    cout << kthLargest(root, k) << "\n";
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
     * Return the k-th largest value (1-indexed) in the BST.
     */
    static int kthLargest(TreeNode root, int k) {
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
        int k = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(kthLargest(root, k));
    }
}
```

---

## Classwork: Find the ceiling of a key in a BST (GfG)

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
 * Return the smallest BST value >= key, or -1 if none.
 */
int ceilBST(TreeNode* root, int key) {
    // Write your code here.
    return -1;
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
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    cout << ceilBST(root, key) << "\n";
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
     * Return the smallest BST value >= key, or -1 if none.
     */
    static int ceilBST(TreeNode root, int key) {
        // Write your code here.
        return -1;
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
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(ceilBST(root, key));
    }
}
```

---

## Classwork: LC108 Convert Sorted Array to Binary Search Tree

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
 * Build a height-balanced BST from the sorted array and return the root.
 */
TreeNode* sortedArrayToBST(vector<int>& A) {
    // Write your code here.
    return nullptr;
}
```

**C++ Tail**
```cpp
static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> A; int x;
    while (ss >> x) A.push_back(x);
    TreeNode* root = sortedArrayToBST(A);
    cout << serializeTree(root) << "\n";
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
     * Build a height-balanced BST from the sorted array and return the root.
     */
    static TreeNode sortedArrayToBST(int[] A) {
        // Write your code here.
        return null;
    }
```

**Java Tail**
```java
    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) line = "";
        line = line.trim();
        int[] A;
        if (line.isEmpty()) { A = new int[0]; }
        else {
            String[] tok = line.split("\\s+");
            A = new int[tok.length];
            for (int i = 0; i < tok.length; i++) A[i] = Integer.parseInt(tok[i]);
        }
        TreeNode root = sortedArrayToBST(A);
        System.out.println(serializeTree(root));
    }
}
```

---

## Classwork: LC235 Lowest Common Ancestor of a BST

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
 * Return the LCA value of two nodes in a BST.
 */
int lcaBST(TreeNode* root, int p, int q) {
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
    int p, q; cin >> p >> q;
    TreeNode* root = buildTree(line);
    cout << lcaBST(root, p, q) << "\n";
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
     * Return the LCA value of two nodes in a BST.
     */
    static int lcaBST(TreeNode root, int p, int q) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(lcaBST(root, p, q));
    }
}
```

---

## Classwork: LC173 Binary Search Tree Iterator

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
 * Simulate a BST inorder iterator; the tail feeds it `q` operations.
 */
vector<string> runBSTIterator(TreeNode* root, vector<string>& ops) {
    // Return one output line per op. For 'next', emit an int as string or "null" if empty. For 'hasNext', emit "true"/"false".
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
    int q; cin >> q; cin.ignore();
    vector<string> ops;
    for (int i = 0; i < q; ++i) {
        string op; getline(cin, op);
        while (!op.empty() && (op.back() == '\r' || op.back() == ' ')) op.pop_back();
        ops.push_back(op);
    }
    TreeNode* root = buildTree(line);
    vector<string> out = runBSTIterator(root, ops);
    for (const string& s : out) cout << s << "\n";
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
     * Simulate a BST inorder iterator; the tail feeds it `q` operations.
     */
    static List<String> runBSTIterator(TreeNode root, List<String> ops) {
        // Return one output line per op. For 'next': int-as-string or "null" if empty. For 'hasNext': "true"/"false".
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
        int q = Integer.parseInt(br.readLine().trim());
        List<String> ops = new ArrayList<>();
        for (int i = 0; i < q; i++) ops.add(br.readLine().trim());
        TreeNode root = buildTree(line);
        List<String> out = runBSTIterator(root, ops);
        StringBuilder sb = new StringBuilder();
        for (String s : out) { sb.append(s); sb.append('\n'); }
        System.out.print(sb.toString());
    }
}
```

---

## Classwork: Print all BST keys in decreasing order (reverse inorder)

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
 * Return BST values in DECREASING order.
 */
vector<int> reverseInorderBST(TreeNode* root) {
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
    vector<int> ans = reverseInorderBST(root);
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
     * Return BST values in DECREASING order.
     */
    static List<Integer> reverseInorderBST(TreeNode root) {
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
        List<Integer> ans = reverseInorderBST(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Classwork: LC653 Two Sum IV - Input is a BST

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
 * Return true if two DIFFERENT nodes sum to `target`.
 */
bool findTarget(TreeNode* root, int target) {
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    cout << (findTarget(root, target) ? "true" : "false") << "\n";
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
     * Return true if two DIFFERENT nodes sum to `target`.
     */
    static boolean findTarget(TreeNode root, int target) {
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(findTarget(root, target) ? "true" : "false");
    }
}
```

---

## Classwork: LC938 Range Sum of BST

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
 * Return the sum of BST values in [lo, hi].
 */
int rangeSumBST(TreeNode* root, int lo, int hi) {
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
    int lo, hi; cin >> lo >> hi;
    TreeNode* root = buildTree(line);
    cout << rangeSumBST(root, lo, hi) << "\n";
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
     * Return the sum of BST values in [lo, hi].
     */
    static int rangeSumBST(TreeNode root, int lo, int hi) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int lo = Integer.parseInt(st.nextToken());
        int hi = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(rangeSumBST(root, lo, hi));
    }
}
```

---

## Classwork: LC669 Trim a Binary Search Tree

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
 * Remove BST nodes outside [lo, hi] and return the trimmed root.
 */
TreeNode* trimBST(TreeNode* root, int lo, int hi) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int lo, hi; cin >> lo >> hi;
    TreeNode* root = buildTree(line);
    TreeNode* out = trimBST(root, lo, hi);
    cout << serializeTree(out) << "\n";
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
     * Remove BST nodes outside [lo, hi] and return the trimmed root.
     */
    static TreeNode trimBST(TreeNode root, int lo, int hi) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int lo = Integer.parseInt(st.nextToken());
        int hi = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        TreeNode out = trimBST(root, lo, hi);
        System.out.println(serializeTree(out));
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

## Homework: LC589 N-ary Tree Preorder Traversal

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct NaryNode {
    int val;
    vector<NaryNode*> children;
    NaryNode(int v) : val(v) {}
};
```

**C++ Body**
```cpp
/*
 * Return the preorder traversal of an N-ary tree.
 */
vector<int> naryPreorder(NaryNode* root) {
    // Write your code here.
    return {};
}
```

**C++ Tail**
```cpp
static NaryNode* buildNary(int n, vector<int>& vals, vector<int>& parents) {
    if (n <= 0) return nullptr;
    unordered_map<int, NaryNode*> byVal;
    for (int i = 0; i < n; ++i) byVal[vals[i]] = new NaryNode(vals[i]);
    for (int i = 1; i < n; ++i) byVal[parents[i - 1]]->children.push_back(byVal[vals[i]]);
    return byVal[vals[0]];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<int> vals(n), parents(max(0, n - 1));
    for (int i = 0; i < n; ++i) cin >> vals[i];
    for (int i = 0; i < n - 1; ++i) cin >> parents[i];
    NaryNode* root = buildNary(n, vals, parents);
    vector<int> ans = naryPreorder(root);
    for (size_t i = 0; i < ans.size(); ++i) { if (i) cout << ' '; cout << ans[i]; }
    cout << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class NaryNode {
    int val;
    List<NaryNode> children = new ArrayList<>();
    NaryNode(int v) { this.val = v; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the preorder traversal of an N-ary tree.
     */
    static List<Integer> naryPreorder(NaryNode root) {
        // Write your code here.
        return new ArrayList<>();
    }
```

**Java Tail**
```java
    static NaryNode buildNary(int n, int[] vals, int[] parents) {
        if (n <= 0) return null;
        Map<Integer, NaryNode> byVal = new HashMap<>();
        for (int i = 0; i < n; i++) byVal.put(vals[i], new NaryNode(vals[i]));
        for (int i = 1; i < n; i++) byVal.get(parents[i - 1]).children.add(byVal.get(vals[i]));
        return byVal.get(vals[0]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] vals = new int[n];
        if (n > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) vals[i] = Integer.parseInt(st.nextToken());
        }
        int[] parents = new int[Math.max(0, n - 1)];
        if (n >= 2) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n - 1; i++) parents[i] = Integer.parseInt(st.nextToken());
        }
        NaryNode root = buildNary(n, vals, parents);
        List<Integer> ans = naryPreorder(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: Count the total number of nodes recursively

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
 * Return the total number of nodes recursively. Empty tree has 0.
 */
int countNodesRec(TreeNode* root) {
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
    cout << countNodesRec(root) << "\n";
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
     * Return the total number of nodes recursively. Empty tree has 0.
     */
    static int countNodesRec(TreeNode root) {
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
        System.out.println(countNodesRec(root));
    }
}
```

---

## Homework: Print all leaf nodes from left to right

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
 * Return every leaf value in left-to-right order.
 */
vector<int> leafValues(TreeNode* root) {
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
    vector<int> ans = leafValues(root);
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
     * Return every leaf value in left-to-right order.
     */
    static List<Integer> leafValues(TreeNode root) {
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
        List<Integer> ans = leafValues(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: LC993 Cousins in Binary Tree

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
 * Return true if nodes with values x and y have same depth but different parents.
 */
bool isCousins(TreeNode* root, int x, int y) {
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
    int x, y; cin >> x >> y;
    TreeNode* root = buildTree(line);
    cout << (isCousins(root, x, y) ? "true" : "false") << "\n";
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
     * Return true if nodes with values x and y have same depth but different parents.
     */
    static boolean isCousins(TreeNode root, int x, int y) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(isCousins(root, x, y) ? "true" : "false");
    }
}
```

---

## Homework: LC637 Average of Levels in Binary Tree

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
 * Return the average of node values at each level (one double per level).
 */
vector<double> averageOfLevels(TreeNode* root) {
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
    vector<double> ans = averageOfLevels(root);
    cout << fixed << setprecision(5);
    for (double d : ans) cout << d << "\n";
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
     * Return the average of node values at each level (one double per level).
     */
    static List<Double> averageOfLevels(TreeNode root) {
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
        List<Double> ans = averageOfLevels(root);
        StringBuilder sb = new StringBuilder();
        for (double d : ans) sb.append(String.format("%.5f%n", d));
        System.out.print(sb.toString());
    }
}
```

---

## Homework: LC103 Binary Tree Zigzag Level Order Traversal

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
 * Return the level-order traversal with alternating direction per level.
 */
vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
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
    vector<vector<int>> ans = zigzagLevelOrder(root);
    for (const auto& row : ans) {
        for (size_t i = 0; i < row.size(); ++i) { if (i) cout << ' '; cout << row[i]; }
        cout << "\n";
    }
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
     * Return the level-order traversal with alternating direction per level.
     */
    static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
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
        List<List<Integer>> ans = zigzagLevelOrder(root);
        StringBuilder sb = new StringBuilder();
        for (List<Integer> row : ans) {
            for (int i = 0; i < row.size(); i++) { if (i > 0) sb.append(' '); sb.append(row.get(i)); }
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}
```

---

## Homework: LC107 Binary Tree Level Order Traversal II

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
 * Return the level-order traversal from the deepest level up.
 */
vector<vector<int>> levelOrderBottom(TreeNode* root) {
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
    vector<vector<int>> ans = levelOrderBottom(root);
    for (const auto& row : ans) {
        for (size_t i = 0; i < row.size(); ++i) { if (i) cout << ' '; cout << row[i]; }
        cout << "\n";
    }
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
     * Return the level-order traversal from the deepest level up.
     */
    static List<List<Integer>> levelOrderBottom(TreeNode root) {
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
        List<List<Integer>> ans = levelOrderBottom(root);
        StringBuilder sb = new StringBuilder();
        for (List<Integer> row : ans) {
            for (int i = 0; i < row.size(); i++) { if (i > 0) sb.append(' '); sb.append(row.get(i)); }
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}
```

---

## Homework: Find the maximum node value in a binary tree

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
 * Return the maximum value in the tree. Empty tree: return 0.
 */
int maxNodeValue(TreeNode* root) {
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
    cout << maxNodeValue(root) << "\n";
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
     * Return the maximum value in the tree. Empty tree: return 0.
     */
    static int maxNodeValue(TreeNode root) {
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
        System.out.println(maxNodeValue(root));
    }
}
```

---

## Homework: LC559 Maximum Depth of N-ary Tree

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct NaryNode {
    int val;
    vector<NaryNode*> children;
    NaryNode(int v) : val(v) {}
};
```

**C++ Body**
```cpp
/*
 * Return the max depth of an N-ary tree.
 */
int naryMaxDepth(NaryNode* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static NaryNode* buildNary(int n, vector<int>& vals, vector<int>& parents) {
    if (n <= 0) return nullptr;
    unordered_map<int, NaryNode*> byVal;
    for (int i = 0; i < n; ++i) byVal[vals[i]] = new NaryNode(vals[i]);
    for (int i = 1; i < n; ++i) byVal[parents[i - 1]]->children.push_back(byVal[vals[i]]);
    return byVal[vals[0]];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<int> vals(n), parents(max(0, n - 1));
    for (int i = 0; i < n; ++i) cin >> vals[i];
    for (int i = 0; i < n - 1; ++i) cin >> parents[i];
    NaryNode* root = buildNary(n, vals, parents);
    cout << naryMaxDepth(root) << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class NaryNode {
    int val;
    List<NaryNode> children = new ArrayList<>();
    NaryNode(int v) { this.val = v; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the max depth of an N-ary tree.
     */
    static int naryMaxDepth(NaryNode root) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    static NaryNode buildNary(int n, int[] vals, int[] parents) {
        if (n <= 0) return null;
        Map<Integer, NaryNode> byVal = new HashMap<>();
        for (int i = 0; i < n; i++) byVal.put(vals[i], new NaryNode(vals[i]));
        for (int i = 1; i < n; i++) byVal.get(parents[i - 1]).children.add(byVal.get(vals[i]));
        return byVal.get(vals[0]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] vals = new int[n];
        if (n > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) vals[i] = Integer.parseInt(st.nextToken());
        }
        int[] parents = new int[Math.max(0, n - 1)];
        if (n >= 2) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n - 1; i++) parents[i] = Integer.parseInt(st.nextToken());
        }
        NaryNode root = buildNary(n, vals, parents);
        System.out.println(naryMaxDepth(root));
    }
}
```

---

## Homework: Check whether two trees have equal height

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
 * Return true if the two trees have the same height.
 */
bool equalHeight(TreeNode* a, TreeNode* b) {
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
    cout << (equalHeight(a, b) ? "true" : "false") << "\n";
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
     * Return true if the two trees have the same height.
     */
    static boolean equalHeight(TreeNode a, TreeNode b) {
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
        System.out.println(equalHeight(a, b) ? "true" : "false");
    }
}
```

---

## Homework: Count the number of nodes at maximum depth

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
 * Return how many nodes sit at the deepest level.
 */
int countAtMaxDepth(TreeNode* root) {
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
    cout << countAtMaxDepth(root) << "\n";
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
     * Return how many nodes sit at the deepest level.
     */
    static int countAtMaxDepth(TreeNode root) {
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
        System.out.println(countAtMaxDepth(root));
    }
}
```

---

## Homework: Count the number of leaf nodes in a binary tree

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
 * Return the number of leaves. Empty tree has 0.
 */
int countLeafNodes(TreeNode* root) {
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
    cout << countLeafNodes(root) << "\n";
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
     * Return the number of leaves. Empty tree has 0.
     */
    static int countLeafNodes(TreeNode root) {
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
        System.out.println(countLeafNodes(root));
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

## Homework: LC965 Univalued Binary Tree

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
 * Return true if every node has the same value.
 */
bool isUnivalTree(TreeNode* root) {
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
    cout << (isUnivalTree(root) ? "true" : "false") << "\n";
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
     * Return true if every node has the same value.
     */
    static boolean isUnivalTree(TreeNode root) {
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
        System.out.println(isUnivalTree(root) ? "true" : "false");
    }
}
```

---

## Homework: LC872 Leaf-Similar Trees

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
 * Return true if the two trees' leaf sequences (left-to-right) match.
 */
bool leafSimilar(TreeNode* a, TreeNode* b) {
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
    cout << (leafSimilar(a, b) ? "true" : "false") << "\n";
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
     * Return true if the two trees' leaf sequences (left-to-right) match.
     */
    static boolean leafSimilar(TreeNode a, TreeNode b) {
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
        System.out.println(leafSimilar(a, b) ? "true" : "false");
    }
}
```

---

## Homework: Right view of a binary tree (GfG)

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
 * Return the rightmost value at each level from the top down.
 */
vector<int> rightViewHW(TreeNode* root) {
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
    vector<int> ans = rightViewHW(root);
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
     * Return the rightmost value at each level from the top down.
     */
    static List<Integer> rightViewHW(TreeNode root) {
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
        List<Integer> ans = rightViewHW(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: Bottom view of a binary tree (GfG)

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
 * Return the bottom view: leftmost-to-rightmost, bottommost value per column.
 */
vector<int> bottomView(TreeNode* root) {
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
    vector<int> ans = bottomView(root);
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
     * Return the bottom view: leftmost-to-rightmost, bottommost value per column.
     */
    static List<Integer> bottomView(TreeNode root) {
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
        List<Integer> ans = bottomView(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: Diagonal traversal of a binary tree (GfG)

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
 * Return the diagonal traversal (one list per diagonal).
 */
vector<vector<int>> diagonalTraversal(TreeNode* root) {
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
    vector<vector<int>> ans = diagonalTraversal(root);
    for (const auto& row : ans) {
        for (size_t i = 0; i < row.size(); ++i) { if (i) cout << ' '; cout << row[i]; }
        cout << "\n";
    }
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
     * Return the diagonal traversal (one list per diagonal).
     */
    static List<List<Integer>> diagonalTraversal(TreeNode root) {
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
        List<List<Integer>> ans = diagonalTraversal(root);
        StringBuilder sb = new StringBuilder();
        for (List<Integer> row : ans) {
            for (int i = 0; i < row.size(); i++) { if (i > 0) sb.append(' '); sb.append(row.get(i)); }
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}
```

---

## Homework: Morris inorder traversal (O(1) space) (GfG)

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
 * Return the inorder traversal using O(1) space (Morris traversal).
 */
vector<int> morrisInorder(TreeNode* root) {
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
    vector<int> ans = morrisInorder(root);
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
     * Return the inorder traversal using O(1) space (Morris traversal).
     */
    static List<Integer> morrisInorder(TreeNode root) {
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
        List<Integer> ans = morrisInorder(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: LC617 Merge Two Binary Trees

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
 * Overlay two trees: sum where both exist, else use whichever node exists.
 */
TreeNode* mergeTrees(TreeNode* a, TreeNode* b) {
    // Write your code here.
    return a ? a : b;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string la, lb;
    getline(cin, la);
    getline(cin, lb);
    TreeNode* a = buildTree(la);
    TreeNode* b = buildTree(lb);
    TreeNode* out = mergeTrees(a, b);
    cout << serializeTree(out) << "\n";
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
     * Overlay two trees: sum where both exist, else use whichever node exists.
     */
    static TreeNode mergeTrees(TreeNode a, TreeNode b) {
        // Write your code here.
        return a != null ? a : b;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String la = br.readLine();
        String lb = br.readLine();
        TreeNode a = buildTree(la);
        TreeNode b = buildTree(lb);
        TreeNode out = mergeTrees(a, b);
        System.out.println(serializeTree(out));
    }
}
```

---

## Homework: Check if one tree is the mirror of another (GfG)

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
 * Return true if one tree is the mirror image of the other.
 */
bool isMirror(TreeNode* a, TreeNode* b) {
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
    cout << (isMirror(a, b) ? "true" : "false") << "\n";
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
     * Return true if one tree is the mirror image of the other.
     */
    static boolean isMirror(TreeNode a, TreeNode b) {
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
        System.out.println(isMirror(a, b) ? "true" : "false");
    }
}
```

---

## Homework: Convert a tree to its mirror in place (GfG)

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
 * Swap every node's children (in place) and return the tree.
 */
TreeNode* mirrorInPlace(TreeNode* root) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = mirrorInPlace(root);
    cout << serializeTree(out) << "\n";
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
     * Swap every node's children (in place) and return the tree.
     */
    static TreeNode mirrorInPlace(TreeNode root) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = mirrorInPlace(root);
        System.out.println(serializeTree(out));
    }
}
```

---

## Homework: LC951 Flip Equivalent Binary Trees

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
 * Return true if one tree can be flipped into the other by swapping children.
 */
bool flipEquiv(TreeNode* a, TreeNode* b) {
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
    cout << (flipEquiv(a, b) ? "true" : "false") << "\n";
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
     * Return true if one tree can be flipped into the other by swapping children.
     */
    static boolean flipEquiv(TreeNode a, TreeNode b) {
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
        System.out.println(flipEquiv(a, b) ? "true" : "false");
    }
}
```

---

## Homework: LC257 Binary Tree Paths

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
 * Return every root-to-leaf path as a list of strings joined by "->".
 */
vector<string> binaryTreePaths(TreeNode* root) {
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
    vector<string> ans = binaryTreePaths(root);
    for (const string& s : ans) cout << s << "\n";
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
     * Return every root-to-leaf path as a list of strings joined by "->".
     */
    static List<String> binaryTreePaths(TreeNode root) {
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
        List<String> ans = binaryTreePaths(root);
        StringBuilder sb = new StringBuilder();
        for (String s : ans) { sb.append(s); sb.append('\n'); }
        System.out.print(sb.toString());
    }
}
```

---

## Homework: LC437 Path Sum III

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
 * Return the number of downward paths whose values sum to `target`.
 */
int pathSumIII(TreeNode* root, int target) {
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    cout << pathSumIII(root, target) << "\n";
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
     * Return the number of downward paths whose values sum to `target`.
     */
    static int pathSumIII(TreeNode root, int target) {
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(pathSumIII(root, target));
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

## Homework: LC988 Smallest String Starting From Leaf

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
 * Return the lexicographically smallest leaf-to-root string (a=0..z=25).
 */
string smallestFromLeaf(TreeNode* root) {
    // Write your code here.
    return "";
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
    cout << smallestFromLeaf(root) << "\n";
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
     * Return the lexicographically smallest leaf-to-root string (a=0..z=25).
     */
    static String smallestFromLeaf(TreeNode root) {
        // Write your code here.
        return "";
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
        System.out.println(smallestFromLeaf(root));
    }
}
```

---

## Homework: Find the level of a given node in a binary tree

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
 * Return the 1-indexed level of `target`, or -1 if absent.
 */
int levelOfNode(TreeNode* root, int target) {
    // Write your code here.
    return -1;
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    cout << levelOfNode(root, target) << "\n";
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
     * Return the 1-indexed level of `target`, or -1 if absent.
     */
    static int levelOfNode(TreeNode root, int target) {
        // Write your code here.
        return -1;
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(levelOfNode(root, target));
    }
}
```

---

## Homework: LC1650 Lowest Common Ancestor III

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
 * Return the LCA value of two nodes in a binary tree (both present).
 */
int lcaIII(TreeNode* root, int p, int q) {
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
    int p, q; cin >> p >> q;
    TreeNode* root = buildTree(line);
    cout << lcaIII(root, p, q) << "\n";
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
     * Return the LCA value of two nodes in a binary tree (both present).
     */
    static int lcaIII(TreeNode root, int p, int q) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(lcaIII(root, p, q));
    }
}
```

---

## Homework: LC1123 Lowest Common Ancestor of Deepest Leaves

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
 * Return the value of the LCA of all deepest leaves.
 */
int lcaDeepestLeaves(TreeNode* root) {
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
    cout << lcaDeepestLeaves(root) << "\n";
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
     * Return the value of the LCA of all deepest leaves.
     */
    static int lcaDeepestLeaves(TreeNode root) {
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
        System.out.println(lcaDeepestLeaves(root));
    }
}
```

---

## Homework: Kth ancestor of a node in a tree (GfG)

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
 * Return the k-th ancestor of `target`, or -1 if it does not exist.
 */
int kthAncestor(TreeNode* root, int target, int k) {
    // Write your code here.
    return -1;
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
    int t, k; cin >> t >> k;
    TreeNode* root = buildTree(line);
    cout << kthAncestor(root, t, k) << "\n";
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
     * Return the k-th ancestor of `target`, or -1 if it does not exist.
     */
    static int kthAncestor(TreeNode root, int target, int k) {
        // Write your code here.
        return -1;
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(kthAncestor(root, t, k));
    }
}
```

---

## Homework: LC108 Convert Sorted Array to Binary Search Tree

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
 * Build a height-balanced BST from a sorted array of length n; return the root.
 */
TreeNode* sortedArrayToBSTHW(vector<int>& A) {
    // Write your code here.
    return nullptr;
}
```

**C++ Tail**
```cpp
static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    TreeNode* root = sortedArrayToBSTHW(A);
    cout << serializeTree(root) << "\n";
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
     * Build a height-balanced BST from a sorted array of length n; return the root.
     */
    static TreeNode sortedArrayToBSTHW(int[] A) {
        // Write your code here.
        return null;
    }
```

**Java Tail**
```java
    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] A = new int[n];
        if (n > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) A[i] = Integer.parseInt(st.nextToken());
        }
        TreeNode root = sortedArrayToBSTHW(A);
        System.out.println(serializeTree(root));
    }
}
```

---

## Homework: LC889 Construct Binary Tree from Preorder and Postorder

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
 * Rebuild a binary tree from preorder+postorder; return the root.
 */
TreeNode* buildFromPrePost(vector<int>& preorder, vector<int>& postorder) {
    // Write your code here.
    return nullptr;
}
```

**C++ Tail**
```cpp
static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

static vector<int> readInts(const string& line) {
    stringstream ss(line);
    vector<int> v; int x;
    while (ss >> x) v.push_back(x);
    return v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string la, lb;
    getline(cin, la);
    getline(cin, lb);
    vector<int> A = readInts(la);
    vector<int> B = readInts(lb);
    TreeNode* root = buildFromPrePost(A, B);
    cout << serializeTree(root) << "\n";
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
     * Rebuild a binary tree from preorder+postorder; return the root.
     */
    static TreeNode buildFromPrePost(int[] preorder, int[] postorder) {
        // Write your code here.
        return null;
    }
```

**Java Tail**
```java
    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    static int[] readInts(String line) {
        if (line == null) return new int[0];
        line = line.trim();
        if (line.isEmpty()) return new int[0];
        String[] tok = line.split("\\s+");
        int[] a = new int[tok.length];
        for (int i = 0; i < tok.length; i++) a[i] = Integer.parseInt(tok[i]);
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] A = readInts(br.readLine());
        int[] B = readInts(br.readLine());
        TreeNode root = buildFromPrePost(A, B);
        System.out.println(serializeTree(root));
    }
}
```

---

## Homework: LC1008 Construct BST from Preorder Traversal

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
 * Rebuild a BST from its preorder traversal; return the root.
 */
TreeNode* bstFromPreorder(vector<int>& A) {
    // Write your code here.
    return nullptr;
}
```

**C++ Tail**
```cpp
static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> A; int x;
    while (ss >> x) A.push_back(x);
    TreeNode* root = bstFromPreorder(A);
    cout << serializeTree(root) << "\n";
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
     * Rebuild a BST from its preorder traversal; return the root.
     */
    static TreeNode bstFromPreorder(int[] A) {
        // Write your code here.
        return null;
    }
```

**Java Tail**
```java
    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) line = "";
        line = line.trim();
        int[] A;
        if (line.isEmpty()) { A = new int[0]; }
        else {
            String[] tok = line.split("\\s+");
            A = new int[tok.length];
            for (int i = 0; i < tok.length; i++) A[i] = Integer.parseInt(tok[i]);
        }
        TreeNode root = bstFromPreorder(A);
        System.out.println(serializeTree(root));
    }
}
```

---

## Homework: LC426 Convert BST to Sorted Doubly Linked List

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
 * Return the BST values in increasing order (the walk of the resulting DLL).
 */
vector<int> bstToDLL(TreeNode* root) {
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
    vector<int> ans = bstToDLL(root);
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
     * Return the BST values in increasing order (the walk of the resulting DLL).
     */
    static List<Integer> bstToDLL(TreeNode root) {
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
        List<Integer> ans = bstToDLL(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: LC404 Sum of Left Leaves

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
 * Return the sum of every left-leaf value.
 */
int sumOfLeftLeaves(TreeNode* root) {
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
    cout << sumOfLeftLeaves(root) << "\n";
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
     * Return the sum of every left-leaf value.
     */
    static int sumOfLeftLeaves(TreeNode root) {
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
        System.out.println(sumOfLeftLeaves(root));
    }
}
```

---

## Homework: LC662 Maximum Width of Binary Tree

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
 * Return the maximum width of any level (positions between leftmost and rightmost).
 */
int widthOfBinaryTree(TreeNode* root) {
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
    cout << widthOfBinaryTree(root) << "\n";
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
     * Return the maximum width of any level (positions between leftmost and rightmost).
     */
    static int widthOfBinaryTree(TreeNode root) {
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
        System.out.println(widthOfBinaryTree(root));
    }
}
```

---

## Homework: LC116 Populating Next Right Pointers in Each Node

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right, *next;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr), next(nullptr) {}
};
```

**C++ Body**
```cpp
/*
 * Wire each node's `next` to the next node in level order; return the level-by-level values, `#` after each level.
 */
TreeNode* populateNextAndPrint(TreeNode* root) {
    // Wire `next` in place, then return the root. The tail prints level-order with `#` separators.
    // Write your code here.
    return root;
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

static void printLevelsWithNext(TreeNode* root) {
    if (!root) { cout << "#\n"; return; }
    queue<TreeNode*> q; q.push(root);
    bool first = true;
    while (!q.empty()) {
        int sz = (int)q.size();
        for (int i = 0; i < sz; ++i) {
            TreeNode* n = q.front(); q.pop();
            if (!first) cout << ' ';
            cout << n->val;
            first = false;
            if (n->left) q.push(n->left);
            if (n->right) q.push(n->right);
        }
        cout << " #";
        first = false;
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = populateNextAndPrint(root);
    printLevelsWithNext(out);
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right, next;
    TreeNode(int v) { this.val = v; this.left = null; this.right = null; this.next = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Wire each node's `next` to the next node in level order; return the level-by-level values, `#` after each level.
     */
    static TreeNode populateNextAndPrint(TreeNode root) {
        // Wire `next` in place, then return the root.
        // Write your code here.
        return root;
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

    static void printLevelsWithNext(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if (root == null) { System.out.println("#"); return; }
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        boolean first = true;
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                TreeNode n = q.poll();
                if (!first) sb.append(' ');
                sb.append(n.val);
                first = false;
                if (n.left != null) q.add(n.left);
                if (n.right != null) q.add(n.right);
            }
            sb.append(" #");
            first = false;
        }
        System.out.println(sb.toString());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = populateNextAndPrint(root);
        printLevelsWithNext(out);
    }
}
```

---

## Homework: Find the minimum and maximum value in a BST

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
 * Return {min, max} of the BST values on one line.
 */
pair<int,int> minMaxBST(TreeNode* root) {
    // Write your code here.
    return {0, 0};
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
    auto pr = minMaxBST(root);
    cout << pr.first << ' ' << pr.second << "\n";
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
     * Return {min, max} of the BST values on one line.
     */
    static int[] minMaxBST(TreeNode root) {
        // Return new int[]{min, max}.
        // Write your code here.
        return new int[]{0, 0};
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
        int[] pr = minMaxBST(root);
        System.out.println(pr[0] + " " + pr[1]);
    }
}
```

---

## Homework: Count BST nodes lying in a given range (GfG)

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
 * Return how many BST values fall in [lo, hi].
 */
int countBSTInRange(TreeNode* root, int lo, int hi) {
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
    int lo, hi; cin >> lo >> hi;
    TreeNode* root = buildTree(line);
    cout << countBSTInRange(root, lo, hi) << "\n";
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
     * Return how many BST values fall in [lo, hi].
     */
    static int countBSTInRange(TreeNode root, int lo, int hi) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int lo = Integer.parseInt(st.nextToken());
        int hi = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(countBSTInRange(root, lo, hi));
    }
}
```

---

## Homework: Iterative BST insert (GfG)

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
 * Iteratively insert `key` into the BST; return the root.
 */
TreeNode* iterativeInsertBST(TreeNode* root, int key) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    TreeNode* out = iterativeInsertBST(root, key);
    cout << serializeTree(out) << "\n";
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
     * Iteratively insert `key` into the BST; return the root.
     */
    static TreeNode iterativeInsertBST(TreeNode root, int key) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        TreeNode out = iterativeInsertBST(root, key);
        System.out.println(serializeTree(out));
    }
}
```

---

## Homework: Search keys within a range in a BST (GfG)

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
 * Return every BST value in [lo, hi], sorted ascending.
 */
vector<int> keysInRange(TreeNode* root, int lo, int hi) {
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
    int lo, hi; cin >> lo >> hi;
    TreeNode* root = buildTree(line);
    vector<int> ans = keysInRange(root, lo, hi);
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
     * Return every BST value in [lo, hi], sorted ascending.
     */
    static List<Integer> keysInRange(TreeNode root, int lo, int hi) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int lo = Integer.parseInt(st.nextToken());
        int hi = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        List<Integer> ans = keysInRange(root, lo, hi);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: LC897 Increasing Order Search Tree

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
 * Return the BST values in increasing order (the walk of the right-only chain).
 */
vector<int> increasingBST(TreeNode* root) {
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
    vector<int> ans = increasingBST(root);
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
     * Return the BST values in increasing order (the walk of the right-only chain).
     */
    static List<Integer> increasingBST(TreeNode root) {
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
        List<Integer> ans = increasingBST(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: LC783 Minimum Distance Between BST Nodes

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
 * Return the smallest |a - b| across any two BST values.
 */
int minDiffInBST(TreeNode* root) {
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
    cout << minDiffInBST(root) << "\n";
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
     * Return the smallest |a - b| across any two BST values.
     */
    static int minDiffInBST(TreeNode root) {
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
        System.out.println(minDiffInBST(root));
    }
}
```

---

## Homework: LC99 Recover Binary Search Tree

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
 * Recover a BST where two values were swapped; return the root.
 */
TreeNode* recoverTree(TreeNode* root) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = recoverTree(root);
    cout << serializeTree(out) << "\n";
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
     * Recover a BST where two values were swapped; return the root.
     */
    static TreeNode recoverTree(TreeNode root) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = recoverTree(root);
        System.out.println(serializeTree(out));
    }
}
```

---

## Homework: LC255 Verify Preorder Sequence in BST

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;
```

**C++ Body**
```cpp
/*
 * Return true if the sequence could be a valid BST preorder.
 */
bool verifyPreorder(vector<int>& A) {
    // Write your code here.
    return true;
}
```

**C++ Tail**
```cpp
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> A; int x;
    while (cin >> x) A.push_back(x);
    cout << (verifyPreorder(A) ? "true" : "false") << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

public class Solution {
```

**Java Body**
```java
    /*
     * Return true if the sequence could be a valid BST preorder.
     */
    static boolean verifyPreorder(int[] A) {
        // Write your code here.
        return true;
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) line = "";
        line = line.trim();
        int[] A;
        if (line.isEmpty()) { A = new int[0]; }
        else {
            String[] tok = line.split("\\s+");
            A = new int[tok.length];
            for (int i = 0; i < tok.length; i++) A[i] = Integer.parseInt(tok[i]);
        }
        System.out.println(verifyPreorder(A) ? "true" : "false");
    }
}
```

---

## Homework: Find the floor value of a key in a BST (GfG)

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
 * Return the largest BST value <= key, or -1 if none.
 */
int floorBST(TreeNode* root, int key) {
    // Write your code here.
    return -1;
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
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    cout << floorBST(root, key) << "\n";
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
     * Return the largest BST value <= key, or -1 if none.
     */
    static int floorBST(TreeNode root, int key) {
        // Write your code here.
        return -1;
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
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(floorBST(root, key));
    }
}
```

---

## Homework: LC669 Trim a Binary Search Tree

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
 * Remove BST nodes outside [lo, hi] and return the trimmed root.
 */
TreeNode* trimBSTHW(TreeNode* root, int lo, int hi) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int lo, hi; cin >> lo >> hi;
    TreeNode* root = buildTree(line);
    TreeNode* out = trimBSTHW(root, lo, hi);
    cout << serializeTree(out) << "\n";
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
     * Remove BST nodes outside [lo, hi] and return the trimmed root.
     */
    static TreeNode trimBSTHW(TreeNode root, int lo, int hi) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int lo = Integer.parseInt(st.nextToken());
        int hi = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        TreeNode out = trimBSTHW(root, lo, hi);
        System.out.println(serializeTree(out));
    }
}
```

---

## Homework: LC285 Inorder Successor in BST

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
 * Return the successor value, or INT_MIN to represent "null".
 */
int inorderSuccessor(TreeNode* root, int key) {
    // Write your code here.
    return INT_MIN;
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
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    int r = inorderSuccessor(root, key);
    if (r == INT_MIN) cout << "null\n"; else cout << r << "\n";
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
     * Return the successor value, or INT_MIN to represent "null".
     */
    static int inorderSuccessor(TreeNode root, int key) {
        // Write your code here.
        return Integer.MIN_VALUE;
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
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        int r = inorderSuccessor(root, key);
        System.out.println(r == Integer.MIN_VALUE ? "null" : String.valueOf(r));
    }
}
```

---

## Homework: Inorder predecessor in a BST (GfG)

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
 * Return the predecessor value, or INT_MIN to represent "null".
 */
int inorderPredecessor(TreeNode* root, int key) {
    // Write your code here.
    return INT_MIN;
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
    int key; cin >> key;
    TreeNode* root = buildTree(line);
    int r = inorderPredecessor(root, key);
    if (r == INT_MIN) cout << "null\n"; else cout << r << "\n";
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
     * Return the predecessor value, or INT_MIN to represent "null".
     */
    static int inorderPredecessor(TreeNode root, int key) {
        // Write your code here.
        return Integer.MIN_VALUE;
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
        int key = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        int r = inorderPredecessor(root, key);
        System.out.println(r == Integer.MIN_VALUE ? "null" : String.valueOf(r));
    }
}
```

---

## Homework: Count the total nodes and height of a BST

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
 * Return {count, height}; each printed on its own line.
 */
pair<int,int> nodesAndHeight(TreeNode* root) {
    // Write your code here.
    return {0, 0};
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
    auto pr = nodesAndHeight(root);
    cout << pr.first << "\n" << pr.second << "\n";
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
     * Return {count, height}; each printed on its own line.
     */
    static int[] nodesAndHeight(TreeNode root) {
        // Return new int[]{count, height}.
        // Write your code here.
        return new int[]{0, 0};
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
        int[] pr = nodesAndHeight(root);
        System.out.println(pr[0]);
        System.out.println(pr[1]);
    }
}
```

---

## Homework: LC653 Two Sum IV - Input is a BST

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
 * Return true if two different BST values sum to `target`.
 */
bool findTargetHW(TreeNode* root, int target) {
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
    int target; cin >> target;
    TreeNode* root = buildTree(line);
    cout << (findTargetHW(root, target) ? "true" : "false") << "\n";
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
     * Return true if two different BST values sum to `target`.
     */
    static boolean findTargetHW(TreeNode root, int target) {
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
        int target = Integer.parseInt(br.readLine().trim());
        TreeNode root = buildTree(line);
        System.out.println(findTargetHW(root, target) ? "true" : "false");
    }
}
```

---

## Homework: LC938 Range Sum of BST

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
 * Return the sum of BST values in [lo, hi].
 */
int rangeSumBSTHW(TreeNode* root, int lo, int hi) {
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
    int lo, hi; cin >> lo >> hi;
    TreeNode* root = buildTree(line);
    cout << rangeSumBSTHW(root, lo, hi) << "\n";
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
     * Return the sum of BST values in [lo, hi].
     */
    static int rangeSumBSTHW(TreeNode root, int lo, int hi) {
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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int lo = Integer.parseInt(st.nextToken());
        int hi = Integer.parseInt(st.nextToken());
        TreeNode root = buildTree(line);
        System.out.println(rangeSumBSTHW(root, lo, hi));
    }
}
```

---

## Homework: LC109 Convert Sorted List to Binary Search Tree

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
 * Build a height-balanced BST from the sorted values; return the root.
 */
TreeNode* sortedListToBST(vector<int>& A) {
    // Write your code here.
    return nullptr;
}
```

**C++ Tail**
```cpp
static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> A; int x;
    while (ss >> x) A.push_back(x);
    TreeNode* root = sortedListToBST(A);
    cout << serializeTree(root) << "\n";
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
     * Build a height-balanced BST from the sorted values; return the root.
     */
    static TreeNode sortedListToBST(int[] A) {
        // Write your code here.
        return null;
    }
```

**Java Tail**
```java
    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) line = "";
        line = line.trim();
        int[] A;
        if (line.isEmpty()) { A = new int[0]; }
        else {
            String[] tok = line.split("\\s+");
            A = new int[tok.length];
            for (int i = 0; i < tok.length; i++) A[i] = Integer.parseInt(tok[i]);
        }
        TreeNode root = sortedListToBST(A);
        System.out.println(serializeTree(root));
    }
}
```

---

## Homework: Convert a BST into a sorted vector

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
 * Return the BST values in increasing order.
 */
vector<int> bstToSortedVector(TreeNode* root) {
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
    vector<int> ans = bstToSortedVector(root);
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
     * Return the BST values in increasing order.
     */
    static List<Integer> bstToSortedVector(TreeNode root) {
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
        List<Integer> ans = bstToSortedVector(root);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) { if (i > 0) sb.append(' '); sb.append(ans.get(i)); }
        System.out.println(sb.toString());
    }
}
```

---

## Homework: LC538 Convert BST to Greater Tree

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
 * Replace each value with the sum of itself and all larger BST values; return the root.
 */
TreeNode* convertBST(TreeNode* root) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = convertBST(root);
    cout << serializeTree(out) << "\n";
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
     * Replace each value with the sum of itself and all larger BST values; return the root.
     */
    static TreeNode convertBST(TreeNode root) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = convertBST(root);
        System.out.println(serializeTree(out));
    }
}
```

---

## Homework: LC1382 Balance a Binary Search Tree

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
 * Rebuild the BST as a balanced tree with the same values; return the root.
 */
TreeNode* balanceBST(TreeNode* root) {
    // Write your code here.
    return root;
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

static string serializeTree(TreeNode* root) {
    if (!root) return "null";
    vector<string> out;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!n) { out.push_back("null"); continue; }
        out.push_back(to_string(n->val));
        q.push(n->left);
        q.push(n->right);
    }
    while (!out.empty() && out.back() == "null") out.pop_back();
    string s;
    for (size_t i = 0; i < out.size(); ++i) { if (i) s += ' '; s += out[i]; }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    TreeNode* root = buildTree(line);
    TreeNode* out = balanceBST(root);
    cout << serializeTree(out) << "\n";
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
     * Rebuild the BST as a balanced tree with the same values; return the root.
     */
    static TreeNode balanceBST(TreeNode root) {
        // Write your code here.
        return root;
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

    static String serializeTree(TreeNode root) {
        if (root == null) return "null";
        List<String> out = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) { out.add("null"); continue; }
            out.add(String.valueOf(n.val));
            q.add(n.left);
            q.add(n.right);
        }
        int end = out.size();
        while (end > 0 && out.get(end - 1).equals("null")) end--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) { if (i > 0) sb.append(' '); sb.append(out.get(i)); }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        TreeNode root = buildTree(line);
        TreeNode out = balanceBST(root);
        System.out.println(serializeTree(out));
    }
}
```

---

## Homework: LC333 Largest BST Subtree

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
 * Return the number of nodes in the largest subtree that is itself a BST.
 */
int largestBSTSubtree(TreeNode* root) {
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
    cout << largestBSTSubtree(root) << "\n";
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
     * Return the number of nodes in the largest subtree that is itself a BST.
     */
    static int largestBSTSubtree(TreeNode root) {
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
        System.out.println(largestBSTSubtree(root));
    }
}
```

---
