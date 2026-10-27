# Driver Code (LeetCode-style)

One section per contest challenge. Each has six fenced blocks:
`**C++ Head**`, `**C++ Body**`, `**C++ Tail**`, `**Java Head**`, `**Java Body**`, `**Java Tail**`.

Head + Body + Tail concatenate (in that order) to a complete compilable file.
Head and Tail are locked on HackerRank; students only edit Body.

Push with:

```
python editor.py driver_code.md --boilerplate --apply
```

---

## Count Leaf Nodes

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(nullptr), right(nullptr) {}
};
```

**C++ Body**
```cpp
/*
 * Return the number of leaf nodes in the tree rooted at `root`.
 * A leaf has both children null.
 */
int countLeaves(Node* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static Node* buildTree(const vector<string>& t) {
    if (t.empty() || t[0] == "-1") return nullptr;
    Node* root = new Node(stoi(t[0]));
    queue<Node*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        Node* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "-1") { cur->left = new Node(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "-1") { cur->right = new Node(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<string> tok(n);
    for (int i = 0; i < n; ++i) cin >> tok[i];
    Node* root = buildTree(tok);
    cout << countLeaves(root) << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class Node {
    int val;
    Node left, right;
    Node(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the number of leaf nodes in the tree rooted at `root`.
     * A leaf has both children null.
     */
    static int countLeaves(Node root) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    static Node buildTree(String[] tok) {
        if (tok.length == 0 || tok[0].equals("-1")) return null;
        Node root = new Node(Integer.parseInt(tok[0]));
        Queue<Node> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            Node cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("-1")) {
                    cur.left = new Node(Integer.parseInt(tok[i]));
                    q.add(cur.left);
                }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("-1")) {
                    cur.right = new Node(Integer.parseInt(tok[i]));
                    q.add(cur.right);
                }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        String[] tok = br.readLine().trim().split("\\s+");
        Node root = buildTree(tok);
        System.out.println(countLeaves(root));
    }
}
```

---

## LC543 Diameter of Binary Tree

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(nullptr), right(nullptr) {}
};
```

**C++ Body**
```cpp
/*
 * Return the diameter of the tree rooted at `root`, measured in EDGES.
 * The diameter is the length of the longest path between any two nodes;
 * the path may or may not pass through the root.
 */
int diameterOfBinaryTree(Node* root) {
    // Write your code here.
    return 0;
}
```

**C++ Tail**
```cpp
static Node* buildTree(const vector<string>& t) {
    if (t.empty() || t[0] == "-1") return nullptr;
    Node* root = new Node(stoi(t[0]));
    queue<Node*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        Node* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "-1") { cur->left = new Node(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "-1") { cur->right = new Node(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<string> tok(n);
    for (int i = 0; i < n; ++i) cin >> tok[i];
    Node* root = buildTree(tok);
    cout << diameterOfBinaryTree(root) << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class Node {
    int val;
    Node left, right;
    Node(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return the diameter of the tree rooted at `root`, measured in EDGES.
     * The diameter is the length of the longest path between any two nodes;
     * the path may or may not pass through the root.
     */
    static int diameterOfBinaryTree(Node root) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    static Node buildTree(String[] tok) {
        if (tok.length == 0 || tok[0].equals("-1")) return null;
        Node root = new Node(Integer.parseInt(tok[0]));
        Queue<Node> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            Node cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("-1")) {
                    cur.left = new Node(Integer.parseInt(tok[i]));
                    q.add(cur.left);
                }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("-1")) {
                    cur.right = new Node(Integer.parseInt(tok[i]));
                    q.add(cur.right);
                }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        String[] tok = br.readLine().trim().split("\\s+");
        Node root = buildTree(tok);
        System.out.println(diameterOfBinaryTree(root));
    }
}
```

---

## Check if Binary Tree is Height Balanced

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(nullptr), right(nullptr) {}
};
```

**C++ Body**
```cpp
/*
 * Return true if the tree rooted at `root` is height-balanced.
 * A tree is balanced when, for every node, |height(left) - height(right)| <= 1.
 */
bool isBalanced(Node* root) {
    // Write your code here.
    return true;
}
```

**C++ Tail**
```cpp
static Node* buildTree(const vector<string>& t) {
    if (t.empty() || t[0] == "-1") return nullptr;
    Node* root = new Node(stoi(t[0]));
    queue<Node*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        Node* cur = q.front(); q.pop();
        if (i < t.size()) {
            if (t[i] != "-1") { cur->left = new Node(stoi(t[i])); q.push(cur->left); }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "-1") { cur->right = new Node(stoi(t[i])); q.push(cur->right); }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<string> tok(n);
    for (int i = 0; i < n; ++i) cin >> tok[i];
    Node* root = buildTree(tok);
    cout << (isBalanced(root) ? "true" : "false") << "\n";
    return 0;
}
```

**Java Head**
```java
import java.io.*;
import java.util.*;

class Node {
    int val;
    Node left, right;
    Node(int v) { this.val = v; this.left = null; this.right = null; }
}

public class Solution {
```

**Java Body**
```java
    /*
     * Return true if the tree rooted at `root` is height-balanced.
     * A tree is balanced when, for every node, |height(left) - height(right)| <= 1.
     */
    static boolean isBalanced(Node root) {
        // Write your code here.
        return true;
    }
```

**Java Tail**
```java
    static Node buildTree(String[] tok) {
        if (tok.length == 0 || tok[0].equals("-1")) return null;
        Node root = new Node(Integer.parseInt(tok[0]));
        Queue<Node> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tok.length) {
            Node cur = q.poll();
            if (i < tok.length) {
                if (!tok[i].equals("-1")) {
                    cur.left = new Node(Integer.parseInt(tok[i]));
                    q.add(cur.left);
                }
                i++;
            }
            if (i < tok.length) {
                if (!tok[i].equals("-1")) {
                    cur.right = new Node(Integer.parseInt(tok[i]));
                    q.add(cur.right);
                }
                i++;
            }
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        String[] tok = br.readLine().trim().split("\\s+");
        Node root = buildTree(tok);
        System.out.println(isBalanced(root) ? "true" : "false");
    }
}
```

---

## Next Greater Element using Set

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;
```

**C++ Body**
```cpp
/*
 * For each A[i], return the smallest value in A that is strictly greater
 * than A[i]; -1 if none exists.
 * Use std::set for O(log N) per query.
 */
vector<int> nextGreater(vector<int>& A) {
    // Write your code here.
    return {};
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
    vector<int> ans = nextGreater(A);
    for (size_t i = 0; i < ans.size(); ++i) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << "\n";
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
     * For each A[i], return the smallest value in A that is strictly greater
     * than A[i]; -1 if none exists.
     * Use TreeSet for O(log N) per query.
     */
    static int[] nextGreater(int[] A) {
        // Write your code here.
        return new int[A.length];
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = Integer.parseInt(st.nextToken());
        int[] ans = nextGreater(A);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans[i]);
        }
        System.out.println(sb.toString());
    }
}
```

---

## Sum and Count Scores using Map

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;
```

**C++ Body**
```cpp
/*
 * Aggregate (name, score) records. Return a map from name to
 * {total_score, count}. std::map iterates in ascending key order,
 * which gives the required alphabetical output.
 */
map<string, pair<int, int>> aggregate(vector<pair<string, int>>& records) {
    // Write your code here.
    return {};
}
```

**C++ Tail**
```cpp
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<pair<string, int>> records(n);
    for (int i = 0; i < n; ++i) cin >> records[i].first >> records[i].second;
    auto result = aggregate(records);
    for (const auto& kv : result) {
        cout << kv.first << ' ' << kv.second.first << ' ' << kv.second.second << "\n";
    }
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
     * Aggregate (name, score) records. Return a TreeMap from name to
     * int[]{total_score, count}. TreeMap iterates in ascending key order,
     * which gives the required alphabetical output.
     */
    static TreeMap<String, int[]> aggregate(List<String[]> records) {
        // Write your code here.
        // Each record is String[]{name, scoreAsString}.
        return new TreeMap<>();
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        List<String[]> records = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String score = st.nextToken();
            records.add(new String[]{name, score});
        }
        TreeMap<String, int[]> result = aggregate(records);
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, int[]> e : result.entrySet()) {
            sb.append(e.getKey()).append(' ')
              .append(e.getValue()[0]).append(' ')
              .append(e.getValue()[1]).append('\n');
        }
        System.out.print(sb.toString());
    }
}
```

---

## Find the Most Frequent Element using Map

**C++ Head**
```cpp
#include <bits/stdc++.h>
using namespace std;
```

**C++ Body**
```cpp
/*
 * Return the most-frequent element in A. On ties, return the smallest.
 * Use std::map<int,int> to count. std::map iterates in ascending key
 * order, so a single scan with strict '>' on best-count naturally
 * yields the smallest key on ties.
 */
int mostFrequent(vector<int>& A) {
    // Write your code here.
    return 0;
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
    cout << mostFrequent(A) << "\n";
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
     * Return the most-frequent element in A. On ties, return the smallest.
     * Use TreeMap<Integer,Integer> to count. TreeMap iterates in ascending
     * key order, so a single scan with strict '>' on best-count naturally
     * yields the smallest key on ties.
     */
    static int mostFrequent(int[] A) {
        // Write your code here.
        return 0;
    }
```

**Java Tail**
```java
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = Integer.parseInt(st.nextToken());
        System.out.println(mostFrequent(A));
    }
}
```
