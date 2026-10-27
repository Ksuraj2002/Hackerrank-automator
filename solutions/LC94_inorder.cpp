// Classwork: LC94 Binary Tree Inorder Traversal
//
// Reads one line: the tree in level order, space separated, "null" for a
// missing child. An empty tree is the single token "null".
// Prints one line: the inorder traversal, space separated. Empty line for an
// empty tree.
//
// Iterative, with an explicit stack, so a deeply skewed tree cannot overflow
// the call stack.

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    explicit Node(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Level-order tokens -> tree. A "null" token still consumes a slot, which is
// what makes the level-order encoding unambiguous.
Node *buildTree(const vector<string> &t) {
    if (t.empty() || t[0] == "null") return nullptr;

    Node *root = new Node(stoi(t[0]));
    queue<Node *> q;
    q.push(root);

    size_t i = 1;
    while (!q.empty() && i < t.size()) {
        Node *cur = q.front();
        q.pop();

        if (i < t.size()) {
            if (t[i] != "null") {
                cur->left = new Node(stoi(t[i]));
                q.push(cur->left);
            }
            ++i;
        }
        if (i < t.size()) {
            if (t[i] != "null") {
                cur->right = new Node(stoi(t[i]));
                q.push(cur->right);
            }
            ++i;
        }
    }
    return root;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    if (!getline(cin, line)) {
        cout << "\n";
        return 0;
    }

    vector<string> tok;
    {
        istringstream ss(line);
        string w;
        while (ss >> w) tok.push_back(w);
    }

    Node *root = buildTree(tok);

    vector<int> out;
    stack<Node *> st;
    Node *cur = root;
    while (!st.empty() || cur != nullptr) {
        while (cur != nullptr) {
            st.push(cur);
            cur = cur->left;
        }
        cur = st.top();
        st.pop();
        out.push_back(cur->val);
        cur = cur->right;
    }

    for (size_t i = 0; i < out.size(); ++i) {
        if (i) cout << ' ';
        cout << out[i];
    }
    cout << '\n';
    return 0;
}
