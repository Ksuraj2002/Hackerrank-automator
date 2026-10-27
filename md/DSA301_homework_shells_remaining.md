# DSA-301 remaining homework shell(s)

Auto-filtered from DSA301_homework_missing.md. Create these as empty challenges on HackerRank (title + difficulty), then run `python editor.py DSA301_homework_missing.md --apply --tests` to fill in text, tests, samples, and explanations.

---

## Homework: Find the sum of all node values in a binary tree

**Difficulty**: Easy

**Problem Statement**
Given the root of a binary tree, print the sum of every node's value. The sum of an empty tree is 0.

**Input Format**
A single line with the tree in **level order**, values separated by spaces. The token `null` marks a missing child. An empty tree is the single token `null`.

**Output Format**
A single line containing one integer.

**Constraints**
- `0 <= N <= 10^4` nodes
- `-10^4 <= node value <= 10^4`
- Expected time `O(N)`

**Sample Input 1**
```
1 2 3
```
**Sample Output 1**
```
6
```
**Sample Explanation 1**
Adding up every node's value gives `6`.

**Sample Input 2**
```
1 2 3 4 5 null 6 null null 7 8
```
**Sample Output 2**
```
36
```
**Sample Explanation 2**
Adding up every node's value gives `36`.

**Sample Input 3**
```
5 3 8 2 4 7 9
```
**Sample Output 3**
```
38
```

**Sample Input 4**
```
1 null 2 null 3 null 4
```
**Sample Output 4**
```
10
```

**Sample Input 5**
```
1 2 null 3 null 4 null
```
**Sample Output 5**
```
10
```

**Sample Input 6**
```
-5 -3 8 0 null null 12
```
**Sample Output 6**
```
12
```

**Sample Input 7**
```
1 2 3 4 null null 5 6 null null 7
```
**Sample Output 7**
```
28
```

**Sample Input 8**
```
10 5 15 3 7 null 18 1 null 6 8
```
**Sample Output 8**
```
73
```

**Sample Input 9**
```
7
```
**Sample Output 9**
```
7
```

**Sample Input 10**
```
null
```
**Sample Output 10**
```
0
```

---
