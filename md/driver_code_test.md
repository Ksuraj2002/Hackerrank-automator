# Driver Code test -- LC94 Inorder Traversal

Push with:

    python editor.py driver_code_test.md --boilerplate --apply --only "LC94 Binary Tree Inorder"

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

// Reads a level-order line ("1 null 2 3") into a TreeNode*.
// A single token "null" (or empty line) means an empty tree.
static TreeNode* buildTree(const string& line) {
    stringstream ss(line);
    vector<string> tok; string t;
    while (ss >> t) tok.push_back(t);
    if (tok.empty() || tok[0] == "null") return nullptr;
    TreeNode* root = new TreeNode(stoi(tok[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < tok.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < tok.size()) {
            if (tok[i] != "null") { cur->left = new TreeNode(stoi(tok[i])); q.push(cur->left); }
            ++i;
        }
        if (i < tok.size()) {
            if (tok[i] != "null") { cur->right = new TreeNode(stoi(tok[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}
```

**C++ Body**
```cpp
/*
 * Return the inorder traversal (left, root, right) of the tree rooted at `root`.
 */
vector<int> inorderTraversal(TreeNode* root) {
    // Write your code here.
    return {};
}
```

**C++ Tail**
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
    cout << '\n';
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
    TreeNode(int v) { val = v; }
}

public class Solution {

    static TreeNode buildTree(String line) {
        if (line == null) return null;
        String[] tok = line.trim().split("\\s+");
        if (tok.length == 0 || tok[0].isEmpty() || tok[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tok[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            TreeNode cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("null")) {
                    cur.left = new TreeNode(Integer.parseInt(tok[i]));
                    q.add(cur.left);
                }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("null")) {
                    cur.right = new TreeNode(Integer.parseInt(tok[i]));
                    q.add(cur.right);
                }
                i++;
            }
        }
        return root;
    }
```

**Java Body**
```java
    /*
     * Return the inorder traversal (left, root, right) of the tree rooted at `root`.
     */
    static List<Integer> inorderTraversal(TreeNode root) {
        // Write your code here.
        return new ArrayList<>();
    }
```

**Java Tail**
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
