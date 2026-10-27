# DSA-301 Bi-Weekly Test 1 (6 challenges)

Author-ready markdown for `automator.py`. Six problems for the DSA-301 Bi-Weekly Test 1 contest (Due Sat, Sep 26, 2026; 120 minutes; max marks 300). Each challenge carries 10 sample I/O pairs; run `tools/hr_mark_samples.py --md dsa301_biweekly_test_1.md --apply` to flag the first two as samples. Ensure C++14, Java 8 and Python 3 are enabled on each challenge before publishing.

Difficulty per challenge (set in the HackerRank admin UI after upload; the automator does not set this field):

| # | Title | Difficulty |
|---|-------|-----------|
| Q1 | Biweekly1: Roster Ordering | Easy |
| Q2 | Biweekly1: First Non-Repeating Character Index | Easy |
| Q3 | Biweekly1: Subarrays with Target Sum | Medium |
| Q4 | Biweekly1: Cycle Start Value | Medium |
| Q5 | Biweekly1: Longest Subarray Divisible by K | Hard |
| Q6 | Biweekly1: Minimum Window Substring | Hard |

Suggested weights: mark cases 0..1 as samples (score 0), give cases 2..9 weight so each problem sums to 50 (400/8 = 50, contest max 300 → set overall accordingly). Adjust per contest scoring policy.

---

## Biweekly1: Roster Ordering
**Difficulty**: Easy

**Problem Statement**
The university registrar needs to sort a list of student records based on their final exam scores. You are given `N` students, each with a name and a score.

Sort the students such that:
- They are ordered by score in descending order (highest score first).
- If two students have the exact same score, they must be ordered by name in lexicographical (alphabetical) ascending order.

**Input Format**
- Line 1: a single integer `N` — the number of students.
- Next `N` lines: each contains a string (the student's name, lowercase English letters only) and an integer (the score), separated by a single space.

**Output Format**
Print `N` lines. Each line contains a student's name and score separated by a single space, in the required sorted order.

**Constraints**
- `1 <= N <= 100000`
- Names consist of lowercase English letters only.
- `0 <= score <= 10^9`

**Sample Input 0**
```
4
alice 85
bob 92
charlie 85
david 92
```

**Sample Output 0**
```
bob 92
david 92
alice 85
charlie 85
```

**Sample Input 1**
```
3
zebra 50
alpha 50
beta 50
```

**Sample Output 1**
```
alpha 50
beta 50
zebra 50
```

**Sample Input 2**
```
1
mirai 100
```

**Sample Output 2**
```
mirai 100
```

**Sample Input 3**
```
5
a 10
b 20
c 30
d 40
e 50
```

**Sample Output 3**
```
e 50
d 40
c 30
b 20
a 10
```

**Sample Input 4**
```
4
xyz 0
abc 0
mno 0
pqr 0
```

**Sample Output 4**
```
abc 0
mno 0
pqr 0
xyz 0
```

**Sample Input 5**
```
2
apple 75
banana 75
```

**Sample Output 5**
```
apple 75
banana 75
```

**Sample Input 6**
```
6
tom 60
jerry 80
spike 60
tyke 80
butch 70
toodles 90
```

**Sample Output 6**
```
toodles 90
jerry 80
tyke 80
butch 70
spike 60
tom 60
```

**Sample Input 7**
```
5
gamma 100
alpha 100
delta 100
beta 100
epsilon 100
```

**Sample Output 7**
```
alpha 100
beta 100
delta 100
epsilon 100
gamma 100
```

**Sample Input 8**
```
2
aaaaa 1000
bbbbb 999
```

**Sample Output 8**
```
aaaaa 1000
bbbbb 999
```

**Sample Input 9**
```
4
rahul 88
seema 88
amit 88
deepa 88
```

**Sample Output 9**
```
amit 88
deepa 88
rahul 88
seema 88
```

**Tags**
Sorting, Comparators, Lambdas

---

## Biweekly1: First Non-Repeating Character Index
**Difficulty**: Easy

**Problem Statement**
A satellite dish receives a continuous string of lowercase characters. Identify the 1-based index of the first character in the string that does not repeat anywhere else in the string. If every character repeats at least once, print `-1`.

**Input Format**
A single line containing the string `S`.

**Output Format**
A single integer — the 1-based index of the first non-repeating character, or `-1` if none exists.

**Constraints**
- `1 <= |S| <= 100000`
- `S` consists only of lowercase English letters.

**Sample Input 0**
```
leetcode
```

**Sample Output 0**
```
1
```

**Sample Input 1**
```
loveleetcode
```

**Sample Output 1**
```
3
```

**Sample Input 2**
```
aabbccdd
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
z
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
xxyyzzw
```

**Sample Output 4**
```
7
```

**Sample Input 5**
```
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy
```

**Sample Output 5**
```
26
```

**Sample Input 6**
```
aabb
```

**Sample Output 6**
```
-1
```

**Sample Input 7**
```
abcabc
```

**Sample Output 7**
```
-1
```

**Sample Input 8**
```
swiss
```

**Sample Output 8**
```
2
```

**Sample Input 9**
```
programming
```

**Sample Output 9**
```
1
```

**Tags**
Hashmap, Frequency Counting, Strings

---

## Biweekly1: Subarrays with Target Sum
**Difficulty**: Medium

**Problem Statement**
Given an array of integers `nums` and an integer `k`, return the total number of continuous (contiguous) subarrays whose elements sum exactly to `k`.

**Input Format**
- Line 1: two space-separated integers `N` (size of the array) and `k` (target sum).
- Line 2: `N` space-separated integers — the array elements.

**Output Format**
A single integer — the total count of valid subarrays.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= nums[i] <= 10^9`
- `-10^14 <= k <= 10^14`

**Sample Input 0**
```
3 2
1 1 1
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
3 3
1 2 3
```

**Sample Output 1**
```
2
```

**Sample Input 2**
```
4 0
0 0 0 0
```

**Sample Output 2**
```
10
```

**Sample Input 3**
```
5 -2
-1 -1 1 -1 -1
```

**Sample Output 3**
```
4
```

**Sample Input 4**
```
1 5
4
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
6 5
1 -1 5 -2 3 2
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
5 5
5 5 5 5 5
```

**Sample Output 6**
```
5
```

**Sample Input 7**
```
4 3
1 2 1 2
```

**Sample Output 7**
```
3
```

**Sample Input 8**
```
6 0
1 -1 2 -2 3 -3
```

**Sample Output 8**
```
6
```

**Sample Input 9**
```
3 100
50 50 50
```

**Sample Output 9**
```
2
```

**Tags**
Prefix Sum, Hashmap

---

## Biweekly1: Cycle Start Value
**Difficulty**: Medium

**Problem Statement**
You are given a singly linked list. If the list contains a cycle, print the value of the node where the cycle begins. If there is no cycle, print `-1`.

The input describes the list using an array of values and a tail-connection index `pos`:
- If `pos` is `-1`, the list has no cycle.
- Otherwise, the tail of the list connects back to the node at 0-based index `pos`.

Build the list from the input and report the value of the node where the cycle starts (or `-1`).

**Input Format**
- Line 1: two space-separated integers `N` (number of nodes) and `pos` (0-based tail-connection index, or `-1`).
- Line 2: `N` space-separated integers — the node values in order.

**Output Format**
A single integer — the value at the cycle-start node, or `-1` if there is no cycle.

**Constraints**
- `1 <= N <= 100000`
- `pos` is `-1` or a valid index in `[0, N-1]`.
- `-10^9 <= value <= 10^9`

**Sample Input 0**
```
4 1
3 2 0 -4
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
2 -1
1 2
```

**Sample Output 1**
```
-1
```

**Sample Input 2**
```
1 -1
10
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
2 0
1 2
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
5 4
10 20 30 40 50
```

**Sample Output 4**
```
50
```

**Sample Input 5**
```
7 3
1 2 3 4 5 6 7
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
3 -1
5 10 15
```

**Sample Output 6**
```
-1
```

**Sample Input 7**
```
6 2
1 2 3 4 5 6
```

**Sample Output 7**
```
3
```

**Sample Input 8**
```
1 0
42
```

**Sample Output 8**
```
42
```

**Sample Input 9**
```
8 5
11 22 33 44 55 66 77 88
```

**Sample Output 9**
```
66
```

**Tags**
Linked List, Floyd's Algorithm, Two Pointers

**Boilerplate (C++14)** — NOT parsed by the automator. Paste into HackerRank admin **Head Code / Body / Tail Code** slots after upload.

Head Code:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

static ListNode* buildList(const vector<int>& vals, int pos) {
    if (vals.empty()) return nullptr;
    vector<ListNode*> nodes;
    nodes.reserve(vals.size());
    for (int v : vals) nodes.push_back(new ListNode(v));
    for (size_t i = 0; i + 1 < nodes.size(); ++i) nodes[i]->next = nodes[i + 1];
    if (pos >= 0 && pos < (int)nodes.size()) nodes.back()->next = nodes[pos];
    return nodes.front();
}
```

Solution Template (the user writes only this):
```cpp
int detectCycleValue(ListNode* head) {
    // Write your code here
    return -1;
}
```

Tail Code:
```cpp
int main() {
    int n, pos;
    if (!(cin >> n >> pos)) return 0;
    vector<int> vals(n);
    for (int i = 0; i < n; ++i) cin >> vals[i];
    ListNode* head = buildList(vals, pos);
    cout << detectCycleValue(head) << endl;
    return 0;
}
```

**Boilerplate (Java 8)** — same convention as the C++ version above.

Head Code:
```java
import java.util.*;
import java.io.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int v) { val = v; }
}

public class Solution {
    static ListNode buildList(int[] vals, int pos) {
        if (vals.length == 0) return null;
        ListNode[] nodes = new ListNode[vals.length];
        for (int i = 0; i < vals.length; i++) nodes[i] = new ListNode(vals[i]);
        for (int i = 0; i + 1 < nodes.length; i++) nodes[i].next = nodes[i + 1];
        if (pos >= 0 && pos < nodes.length) nodes[nodes.length - 1].next = nodes[pos];
        return nodes[0];
    }
```

Solution Template:
```java
    static int detectCycleValue(ListNode head) {
        // Write your code here
        return -1;
    }
```

Tail Code:
```java
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int pos = sc.nextInt();
        int[] vals = new int[n];
        for (int i = 0; i < n; i++) vals[i] = sc.nextInt();
        ListNode head = buildList(vals, pos);
        System.out.println(detectCycleValue(head));
    }
}
```

---

## Biweekly1: Longest Subarray Divisible by K
**Difficulty**: Hard

**Problem Statement**
Given an integer array `nums` and an integer `k`, return the maximum length of a contiguous subarray whose sum is perfectly divisible by `k`. If no such subarray exists, print `0`.

**Input Format**
- Line 1: two space-separated integers `N` (size of the array) and `k`.
- Line 2: `N` space-separated integers — the array elements.

**Output Format**
A single integer — the maximum length of a valid subarray, or `0` if none exists.

**Constraints**
- `1 <= N <= 100000`
- `1 <= k <= 10^9`
- `-10^9 <= nums[i] <= 10^9`

**Sample Input 0**
```
6 3
2 7 6 1 4 5
```

**Sample Output 0**
```
4
```

**Sample Input 1**
```
1 2
-2
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
4 5
1 2 3 4
```

**Sample Output 2**
```
4
```

**Sample Input 3**
```
5 4
-4 -8 -12 -16 -20
```

**Sample Output 3**
```
5
```

**Sample Input 4**
```
7 7
1 1 1 1 1 1 1
```

**Sample Output 4**
```
7
```

**Sample Input 5**
```
4 3
-1 -1 -1 -1
```

**Sample Output 5**
```
3
```

**Sample Input 6**
```
3 5
1 2 4
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
5 3
3 6 9 12 15
```

**Sample Output 7**
```
5
```

**Sample Input 8**
```
4 5
5 10 -15 20
```

**Sample Output 8**
```
4
```

**Sample Input 9**
```
6 4
1 2 3 4 5 6
```

**Sample Output 9**
```
5
```

**Tags**
Prefix Sum, Hashmap, Modular Arithmetic

---

## Biweekly1: Minimum Window Substring
**Difficulty**: Hard

**Problem Statement**
Given two strings `S` and `T`, return the minimum-length window (contiguous substring) of `S` such that every character of `T` (including duplicates) appears in the window. If no such window exists, print an empty line.

If multiple valid windows share the minimum length, print the one that appears first in `S`. Matching is case-sensitive.

**Input Format**
- Line 1: string `S`.
- Line 2: string `T`.

**Output Format**
A single line: the minimum window substring, or an empty line if no valid window exists.

**Constraints**
- `1 <= |S|, |T| <= 100000`
- `S` and `T` consist of uppercase and lowercase English letters.

**Sample Input 0**
```
ADOBECODEBANC
ABC
```

**Sample Output 0**
```
BANC
```

**Sample Input 1**
```
a
a
```

**Sample Output 1**
```
a
```

**Sample Input 2**
```
a
aa
```

**Sample Output 2**
```

```

**Sample Input 3**
```
aAbBcC
abc
```

**Sample Output 3**
```

```

**Sample Input 4**
```
xyzzyxxz
zzx
```

**Sample Output 4**
```
xyzz
```

**Sample Input 5**
```
aaaaaaaaaaaaab
b
```

**Sample Output 5**
```
b
```

**Sample Input 6**
```
abcdef
f
```

**Sample Output 6**
```
f
```

**Sample Input 7**
```
XYZABCXYZ
XYZ
```

**Sample Output 7**
```
XYZ
```

**Sample Input 8**
```
ABABABAB
AB
```

**Sample Output 8**
```
AB
```

**Sample Input 9**
```
abcdefghij
j
```

**Sample Output 9**
```
j
```

**Tags**
Sliding Window, Hashmap, Strings
