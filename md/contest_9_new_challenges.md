# Contest Additions — 9 New Challenges

Nine problems formatted for `automator.py`. Section headers and `Sample Input N` / `Sample Output N` fenced blocks match the parser. Boilerplate for tree problems (Q2, Q5, Q7) is placed at the end of each such challenge and is NOT parsed by the automator — paste it manually into the HackerRank admin **Head Code / Body / Tail Code** areas for the relevant languages after upload.

Run:

```
python automator.py contest_9_new_challenges.md
```

After upload, for every challenge:
1. Enable **C++14** and **Java 8** (and Python 3 where applicable).
2. **Set the difficulty** in the admin UI according to the table below (the automator does not set this field).
3. For the three tree problems, paste the provided Head/Solution/Tail code into the C++14 and Java 8 boilerplate slots.
4. Mark the first two test cases as **Sample** (or run `tools/hr_mark_samples.py --md contest_9_new_challenges.md --apply`).
5. Set weight 10 on cases 2..9 so the total score is 100. Publish.

**Difficulty per challenge** (HackerRank admin only exposes Easy / Medium / Hard; the intended curriculum-level label appears in parentheses and is the value to record in the source-of-truth curriculum sheet):

| # | Title | HackerRank Difficulty | Curriculum Label |
|---|-------|-----------------------|------------------|
| Q1 | Frequency Counter | Easy | Easy |
| Q2 | Height of Binary Tree | Easy | Easy |
| Q3 | Longest Subarray with Sum K | Easy | Easy |
| Q4 | Valid Parentheses | Easy | Easy |
| Q5 | Iterative Preorder Traversal | Easy | Easy-Medium |
| Q6 | K-th Largest Element | Medium | Medium |
| Q7 | Maximum Path Sum (Root to Leaf) in Binary Tree | Medium | Medium-Hard |
| Q8 | First and Last Occurrence | Easy | Easy-Medium |
| Q9 | Split Array to Minimize Cost | Hard | Hard |

Tree-input convention (used by Q2, Q5, Q7): tokens describe the binary tree in level order. The first token is the root. For every non-null node processed in level order, the next two tokens are its left and right children. The letter `N` marks a null child, which has no further tokens for its own children.

---

## Frequency Counter

**Difficulty**: Easy (curriculum: Easy)

**Problem Statement**
You are given `N` integers. For each distinct value in the input, print the value together with the number of times it appears in the array. Print exactly one distinct value per line, in strictly increasing order of the value.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, a_2, ..., a_N`.

**Output Format**
For every distinct value `v` that appears in the input, print a line containing `v` and its frequency, separated by a single space. Values must appear in increasing order.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= a_i <= 10^9`

**Tags**
Arrays, Counting

**Sample Input 0**
```
5
1 2 2 3 1
```

**Sample Output 0**
```
1 2
2 2
3 1
```

**Sample Input 1**
```
6
4 4 4 4 4 4
```

**Sample Output 1**
```
4 6
```

**Sample Input 2**
```
5
-1 -1 0 1 1
```

**Sample Output 2**
```
-1 2
0 1
1 2
```

**Sample Input 3**
```
1
100
```

**Sample Output 3**
```
100 1
```

**Sample Input 4**
```
3
5 3 5
```

**Sample Output 4**
```
3 1
5 2
```

**Sample Input 5**
```
7
1000000000 -1000000000 0 0 0 1000000000 -1000000000
```

**Sample Output 5**
```
-1000000000 2
0 3
1000000000 2
```

**Sample Input 6**
```
4
7 7 7 7
```

**Sample Output 6**
```
7 4
```

**Sample Input 7**
```
6
1 2 3 4 5 6
```

**Sample Output 7**
```
1 1
2 1
3 1
4 1
5 1
6 1
```

**Sample Input 8**
```
5
2 1 3 1 2
```

**Sample Output 8**
```
1 2
2 2
3 1
```

**Sample Input 9**
```
8
5 5 4 4 3 3 2 2
```

**Sample Output 9**
```
2 2
3 2
4 2
5 2
```

---

## Height of Binary Tree

**Difficulty**: Easy (curriculum: Easy)

**Problem Statement**
You are given a binary tree. The height of a binary tree is defined as the number of nodes on the longest path that starts at the root and ends at any leaf. A tree consisting of a single node has height `1`; an empty tree has height `0`.

Print the height of the given tree.

**Input Format**
- Line 1: an integer `N`, the number of tokens in the level-order description.
- Line 2: `N` space-separated tokens describing the tree in level order (see the "Tree-input convention" note at the top of the file). The letter `N` represents a null (missing) child.

**Output Format**
A single integer — the height of the tree.

**Constraints**
- `1 <= N <= 10^5`
- Each numeric token fits in a 32-bit signed integer.

**Tags**
Trees, Recursion

**Sample Input 0**
```
7
1 2 3 N N 4 5
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
1
42
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
3
5 N N
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
7
1 2 3 4 5 6 7
```

**Sample Output 3**
```
3
```

**Sample Input 4**
```
5
1 2 N 3 N
```

**Sample Output 4**
```
3
```

**Sample Input 5**
```
3
1 N 2
```

**Sample Output 5**
```
2
```

**Sample Input 6**
```
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

**Sample Output 6**
```
4
```

**Sample Input 7**
```
9
10 20 30 N N 40 N N 50
```

**Sample Output 7**
```
4
```

**Sample Input 8**
```
11
-5 -10 -15 0 N N 20 N N N 30
```

**Sample Output 8**
```
4
```

**Sample Input 9**
```
5
1 2 4 8 16
```

**Sample Output 9**
```
3
```

**Boilerplate (C++14)**

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

static TreeNode* buildTree(const vector<string>& tokens) {
    if (tokens.empty() || tokens[0] == "N") return nullptr;
    TreeNode* root = new TreeNode(stoi(tokens[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < tokens.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < tokens.size()) {
            if (tokens[i] != "N") { cur->left = new TreeNode(stoi(tokens[i])); q.push(cur->left); }
            i++;
        }
        if (i < tokens.size()) {
            if (tokens[i] != "N") { cur->right = new TreeNode(stoi(tokens[i])); q.push(cur->right); }
            i++;
        }
    }
    return root;
}
```

Solution Template (the user writes only this):
```cpp
int height(TreeNode* root) {
    // Write your code here
    return 0;
}
```

Tail Code:
```cpp
int main() {
    int n; if (!(cin >> n)) return 0;
    vector<string> tokens(n);
    for (int i = 0; i < n; i++) cin >> tokens[i];
    TreeNode* root = buildTree(tokens);
    cout << height(root) << endl;
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
    static TreeNode buildTree(String[] tokens) {
        if (tokens.length == 0 || tokens[0].equals("N")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tokens[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tokens.length) {
            TreeNode cur = q.poll();
            if (i < tokens.length) {
                if (!tokens[i].equals("N")) { cur.left = new TreeNode(Integer.parseInt(tokens[i])); q.add(cur.left); }
                i++;
            }
            if (i < tokens.length) {
                if (!tokens[i].equals("N")) { cur.right = new TreeNode(Integer.parseInt(tokens[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static int height(TreeNode root) {
        // Write your code here
        return 0;
    }
```

Tail Code:
```java
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

## Longest Subarray with Sum K

**Difficulty**: Easy (curriculum: Easy)

**Problem Statement**
You are given an array of `N` integers (values may be positive, negative, or zero) and an integer `K`. Consider every contiguous subarray of the given array and compute its sum. Print the length of the longest contiguous subarray whose sum is exactly `K`. If no contiguous subarray has sum equal to `K`, print `0`.

**Input Format**
- Line 1: two space-separated integers `N` and `K`.
- Line 2: `N` space-separated integers `a_1, a_2, ..., a_N`.

**Output Format**
A single integer — the length of the longest contiguous subarray with sum exactly `K`, or `0` if no such subarray exists.

**Constraints**
- `1 <= N <= 10^5`
- `-10^4 <= a_i <= 10^4`
- `-10^9 <= K <= 10^9`

**Tags**
Arrays, Prefix Sum

**Sample Input 0**
```
5 5
2 3 1 1 -1
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
4 7
1 2 3 4
```

**Sample Output 1**
```
2
```

**Sample Input 2**
```
3 0
1 -1 5
```

**Sample Output 2**
```
2
```

**Sample Input 3**
```
1 5
5
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
1 5
3
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
6 15
10 5 2 7 1 9
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
6 0
1 2 -3 4 5 -6
```

**Sample Output 6**
```
4
```

**Sample Input 7**
```
5 100
10 20 30 40 50
```

**Sample Output 7**
```
4
```

**Sample Input 8**
```
4 -3
1 -2 -1 2
```

**Sample Output 8**
```
2
```

**Sample Input 9**
```
7 6
1 2 3 0 0 0 -6
```

**Sample Output 9**
```
6
```

---

## Valid Parentheses

**Difficulty**: Easy (curriculum: Easy)

**Problem Statement**
You are given a string `S` consisting only of the six characters `(`, `)`, `{`, `}`, `[`, `]`. Decide whether the string is a balanced bracket sequence. A string is balanced when:
- every opening bracket has a matching closing bracket of the same type, and
- brackets close in the reverse order of opening, so a closer never appears while an opener of a different type is still waiting to be closed.

Print `true` if `S` is balanced and `false` otherwise. The empty string is considered balanced.

**Input Format**
A single line containing the string `S`.

**Output Format**
A single line containing `true` or `false`.

**Constraints**
- `1 <= |S| <= 10^5`
- `S` contains only the characters `(`, `)`, `{`, `}`, `[`, `]`.

**Tags**
Strings, Stacks

**Sample Input 0**
```
()[]{}
```

**Sample Output 0**
```
true
```

**Sample Input 1**
```
(]
```

**Sample Output 1**
```
false
```

**Sample Input 2**
```
([{}])
```

**Sample Output 2**
```
true
```

**Sample Input 3**
```
((()))
```

**Sample Output 3**
```
true
```

**Sample Input 4**
```
(
```

**Sample Output 4**
```
false
```

**Sample Input 5**
```
)
```

**Sample Output 5**
```
false
```

**Sample Input 6**
```
{[()]}
```

**Sample Output 6**
```
true
```

**Sample Input 7**
```
[()]{}
```

**Sample Output 7**
```
true
```

**Sample Input 8**
```
([)]
```

**Sample Output 8**
```
false
```

**Sample Input 9**
```
{{[[(())]]}}
```

**Sample Output 9**
```
true
```

---

## Iterative Preorder Traversal

**Difficulty**: Easy (curriculum: Easy-Medium)

**Problem Statement**
You are given a binary tree. Print its preorder traversal on a single line, with values separated by single spaces. Preorder visits every node in the order **Root, then Left subtree, then Right subtree**. Your implementation must be iterative — do not use recursion. If the tree is empty, print an empty line.

**Input Format**
- Line 1: an integer `N`, the number of tokens in the level-order description.
- Line 2: `N` space-separated tokens describing the tree in level order (see the "Tree-input convention" note at the top of the file). The letter `N` represents a null (missing) child.

**Output Format**
A single line containing the preorder traversal of the tree, values separated by single spaces.

**Constraints**
- `1 <= N <= 10^5`
- Each numeric token fits in a 32-bit signed integer.

**Tags**
Trees, Stacks

**Sample Input 0**
```
7
1 2 3 N N 4 5
```

**Sample Output 0**
```
1 2 3 4 5
```

**Sample Input 1**
```
1
42
```

**Sample Output 1**
```
42
```

**Sample Input 2**
```
3
5 N N
```

**Sample Output 2**
```
5
```

**Sample Input 3**
```
3
1 N 2
```

**Sample Output 3**
```
1 2
```

**Sample Input 4**
```
5
1 2 N 3 N
```

**Sample Output 4**
```
1 2 3
```

**Sample Input 5**
```
7
1 2 3 4 5 6 7
```

**Sample Output 5**
```
1 2 4 5 3 6 7
```

**Sample Input 6**
```
5
10 20 30 40 50
```

**Sample Output 6**
```
10 20 40 50 30
```

**Sample Input 7**
```
9
10 20 30 N N 40 N N 50
```

**Sample Output 7**
```
10 20 30 40 50
```

**Sample Input 8**
```
11
5 3 8 1 4 7 9 N N N 2
```

**Sample Output 8**
```
5 3 1 4 2 8 7 9
```

**Sample Input 9**
```
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

**Sample Output 9**
```
1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
```

**Boilerplate (C++14)**

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

static TreeNode* buildTree(const vector<string>& tokens) {
    if (tokens.empty() || tokens[0] == "N") return nullptr;
    TreeNode* root = new TreeNode(stoi(tokens[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < tokens.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < tokens.size()) {
            if (tokens[i] != "N") { cur->left = new TreeNode(stoi(tokens[i])); q.push(cur->left); }
            i++;
        }
        if (i < tokens.size()) {
            if (tokens[i] != "N") { cur->right = new TreeNode(stoi(tokens[i])); q.push(cur->right); }
            i++;
        }
    }
    return root;
}
```

Solution Template:
```cpp
vector<int> preorder(TreeNode* root) {
    // Write your code here (iteratively, using a stack)
    return {};
}
```

Tail Code:
```cpp
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
    static TreeNode buildTree(String[] tokens) {
        if (tokens.length == 0 || tokens[0].equals("N")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tokens[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tokens.length) {
            TreeNode cur = q.poll();
            if (i < tokens.length) {
                if (!tokens[i].equals("N")) { cur.left = new TreeNode(Integer.parseInt(tokens[i])); q.add(cur.left); }
                i++;
            }
            if (i < tokens.length) {
                if (!tokens[i].equals("N")) { cur.right = new TreeNode(Integer.parseInt(tokens[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static List<Integer> preorder(TreeNode root) {
        // Write your code here (iteratively, using a stack)
        return new ArrayList<>();
    }
```

Tail Code:
```java
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

## K-th Largest Element

**Difficulty**: Medium (curriculum: Medium)

**Problem Statement**
You are given `N` integers and an integer `K`. Consider the values arranged in non-increasing order (largest first). Print the value at position `K` in that arrangement (1-indexed).

Duplicate values are counted as separate occurrences. For example, in the multiset `[5, 5, 3]` the 1st largest is `5`, the 2nd largest is `5`, and the 3rd largest is `3`.

**Input Format**
- Line 1: two space-separated integers `N` and `K`.
- Line 2: `N` space-separated integers `a_1, a_2, ..., a_N`.

**Output Format**
A single integer — the K-th largest value.

**Constraints**
- `1 <= K <= N <= 10^5`
- `-10^9 <= a_i <= 10^9`

**Tags**
Arrays, Ordering

**Sample Input 0**
```
5 2
3 2 1 5 6
```

**Sample Output 0**
```
5
```

**Sample Input 1**
```
4 1
3 2 3 1
```

**Sample Output 1**
```
3
```

**Sample Input 2**
```
1 1
42
```

**Sample Output 2**
```
42
```

**Sample Input 3**
```
6 4
3 2 1 5 6 4
```

**Sample Output 3**
```
3
```

**Sample Input 4**
```
5 5
7 10 4 3 20
```

**Sample Output 4**
```
3
```

**Sample Input 5**
```
4 2
1 1 1 1
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
6 3
-1 -5 2 3 -2 4
```

**Sample Output 6**
```
2
```

**Sample Input 7**
```
7 6
8 8 5 3 5 3 1
```

**Sample Output 7**
```
3
```

**Sample Input 8**
```
3 2
100 200 50
```

**Sample Output 8**
```
100
```

**Sample Input 9**
```
10 7
15 25 5 35 45 10 20 30 40 50
```

**Sample Output 9**
```
20
```

---

## Maximum Path Sum (Root to Leaf) in Binary Tree

**Difficulty**: Medium (curriculum: Medium-Hard)

**Problem Statement**
You are given a binary tree in which every node holds an integer value (values may be negative, zero, or positive). Consider every path that begins at the root of the tree and ends at some leaf (a node with no children). The sum of a path is the sum of the values of all nodes on that path. Print the maximum such sum over all root-to-leaf paths.

If the tree contains only the root, the answer is the value of the root.

**Input Format**
- Line 1: an integer `N`, the number of tokens in the level-order description.
- Line 2: `N` space-separated tokens describing the tree in level order (see the "Tree-input convention" note at the top of the file). The letter `N` represents a null (missing) child.

**Output Format**
A single integer — the maximum root-to-leaf path sum.

**Constraints**
- `1 <= N <= 10^5`
- `-10^4 <= node value <= 10^4`

**Tags**
Trees, Recursion

**Sample Input 0**
```
7
10 5 -3 3 2 N 11
```

**Sample Output 0**
```
18
```

**Sample Input 1**
```
1
5
```

**Sample Output 1**
```
5
```

**Sample Input 2**
```
3
-5 N N
```

**Sample Output 2**
```
-5
```

**Sample Input 3**
```
5
1 2 3 N N
```

**Sample Output 3**
```
4
```

**Sample Input 4**
```
7
5 -10 20 8 3 -5 4
```

**Sample Output 4**
```
29
```

**Sample Input 5**
```
5
-1 -2 -3 -4 -5
```

**Sample Output 5**
```
-4
```

**Sample Input 6**
```
3
10 5 N
```

**Sample Output 6**
```
15
```

**Sample Input 7**
```
5
1 2 N 3 N
```

**Sample Output 7**
```
6
```

**Sample Input 8**
```
9
1 -2 3 4 5 6 -7 8 -9
```

**Sample Output 8**
```
11
```

**Sample Input 9**
```
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

**Sample Output 9**
```
26
```

**Boilerplate (C++14)**

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

static TreeNode* buildTree(const vector<string>& tokens) {
    if (tokens.empty() || tokens[0] == "N") return nullptr;
    TreeNode* root = new TreeNode(stoi(tokens[0]));
    queue<TreeNode*> q; q.push(root);
    size_t i = 1;
    while (!q.empty() && i < tokens.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < tokens.size()) {
            if (tokens[i] != "N") { cur->left = new TreeNode(stoi(tokens[i])); q.push(cur->left); }
            i++;
        }
        if (i < tokens.size()) {
            if (tokens[i] != "N") { cur->right = new TreeNode(stoi(tokens[i])); q.push(cur->right); }
            i++;
        }
    }
    return root;
}
```

Solution Template:
```cpp
long long maxPathSum(TreeNode* root) {
    // Write your code here
    return 0;
}
```

Tail Code:
```cpp
int main() {
    int n; if (!(cin >> n)) return 0;
    vector<string> tokens(n);
    for (int i = 0; i < n; i++) cin >> tokens[i];
    TreeNode* root = buildTree(tokens);
    cout << maxPathSum(root) << endl;
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
    static TreeNode buildTree(String[] tokens) {
        if (tokens.length == 0 || tokens[0].equals("N")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(tokens[0]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < tokens.length) {
            TreeNode cur = q.poll();
            if (i < tokens.length) {
                if (!tokens[i].equals("N")) { cur.left = new TreeNode(Integer.parseInt(tokens[i])); q.add(cur.left); }
                i++;
            }
            if (i < tokens.length) {
                if (!tokens[i].equals("N")) { cur.right = new TreeNode(Integer.parseInt(tokens[i])); q.add(cur.right); }
                i++;
            }
        }
        return root;
    }
```

Solution Template:
```java
    static long maxPathSum(TreeNode root) {
        // Write your code here
        return 0L;
    }
```

Tail Code:
```java
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

---

## First and Last Occurrence

**Difficulty**: Easy (curriculum: Easy-Medium)

**Problem Statement**
You are given an array of `N` integers sorted in non-decreasing order and an integer `X`. Print two integers on a single line, separated by a single space:
- the smallest index at which `X` appears in the array, and
- the largest index at which `X` appears in the array.

Indices are 0-indexed. If `X` does not appear in the array, print `-1 -1`.

**Input Format**
- Line 1: two space-separated integers `N` and `X`.
- Line 2: `N` space-separated integers `a_1 <= a_2 <= ... <= a_N`.

**Output Format**
A single line containing two space-separated integers: the first and last index of `X` in the array, or `-1 -1` if `X` is not present.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= a_i, X <= 10^9`
- The array is sorted in non-decreasing order.

**Tags**
Arrays, Searching

**Sample Input 0**
```
6 5
1 3 5 5 5 7
```

**Sample Output 0**
```
2 4
```

**Sample Input 1**
```
5 4
1 2 3 5 6
```

**Sample Output 1**
```
-1 -1
```

**Sample Input 2**
```
1 7
7
```

**Sample Output 2**
```
0 0
```

**Sample Input 3**
```
8 2
2 2 2 2 2 2 2 2
```

**Sample Output 3**
```
0 7
```

**Sample Input 4**
```
6 1
1 1 2 3 4 5
```

**Sample Output 4**
```
0 1
```

**Sample Input 5**
```
6 5
1 2 3 4 5 5
```

**Sample Output 5**
```
4 5
```

**Sample Input 6**
```
7 3
1 2 3 3 3 3 4
```

**Sample Output 6**
```
2 5
```

**Sample Input 7**
```
5 10
1 2 3 4 5
```

**Sample Output 7**
```
-1 -1
```

**Sample Input 8**
```
10 6
1 3 5 6 6 6 8 9 10 12
```

**Sample Output 8**
```
3 5
```

**Sample Input 9**
```
4 -5
-10 -5 -5 0
```

**Sample Output 9**
```
1 2
```

---

## Split Array to Minimize Cost

**Difficulty**: Hard (curriculum: Hard)

**Problem Statement**
You are given `N` positive integers arranged in a fixed order and an integer `K`. You must partition the sequence into exactly `K` contiguous, non-empty groups (every element belongs to exactly one group, and the order of elements is preserved). The **cost** of a partition is the largest of the `K` group sums.

Print the smallest possible cost, taken over all valid partitions into exactly `K` groups.

**Input Format**
- Line 1: two space-separated integers `N` and `K`.
- Line 2: `N` space-separated positive integers `a_1, a_2, ..., a_N`.

**Output Format**
A single integer — the minimum possible cost.

**Constraints**
- `1 <= K <= N <= 10^5`
- `1 <= a_i <= 10^4`

**Tags**
Arrays, Searching

**Sample Input 0**
```
5 2
10 20 30 40 50
```

**Sample Output 0**
```
90
```

**Sample Input 1**
```
5 5
1 2 3 4 5
```

**Sample Output 1**
```
5
```

**Sample Input 2**
```
1 1
100
```

**Sample Output 2**
```
100
```

**Sample Input 3**
```
4 2
1 2 3 4
```

**Sample Output 3**
```
6
```

**Sample Input 4**
```
6 3
7 2 5 10 8 3
```

**Sample Output 4**
```
14
```

**Sample Input 5**
```
7 3
5 8 6 3 9 2 7
```

**Sample Output 5**
```
18
```

**Sample Input 6**
```
4 4
5 3 8 2
```

**Sample Output 6**
```
8
```

**Sample Input 7**
```
5 3
1 4 4 3 8
```

**Sample Output 7**
```
8
```

**Sample Input 8**
```
6 1
1 2 3 4 5 6
```

**Sample Output 8**
```
21
```

**Sample Input 9**
```
8 4
10 10 10 10 10 10 10 10
```

**Sample Output 9**
```
20
```

---
