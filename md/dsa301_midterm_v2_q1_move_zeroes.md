# DSA-301 Mid-Term Test Batch 2 — Single challenge (Q1)

Standalone re-upload for `Midterm: Move Zeroes` after the first attempt failed to capture the challenge id. **Ensure ONLY C++14 and Java 8 are enabled on this challenge** (unselect every other language) before publishing.

---

## Midterm: Move Zeroes
**Problem Statement**
Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements. The operation must be performed in place — do not allocate a second array of the same size. Print the final array on one line, elements separated by single spaces.

**Input Format**
- Line 1: a single integer `N` — the size of the array.
- Line 2: `N` space-separated integers — the array elements.

**Output Format**
A single line of `N` space-separated integers — the array after moving every `0` to the end.

**Constraints**
- `1 <= N <= 300000`
- `-10^9 <= nums[i] <= 10^9`
- A quadratic swap-one-at-a-time approach will not fit in the time limit; the intended solution is `O(N)` with `O(1)` extra space.

**Sample Input 0**
```
5
0 1 0 3 12
```

**Sample Output 0**
```
1 3 12 0 0
```

**Sample Explanation 0**
The non-zero elements in their original order are `1, 3, 12`. The two zeroes are pushed to the end, giving `1 3 12 0 0`.

**Sample Input 1**
```
1
0
```

**Sample Output 1**
```
0
```

**Sample Explanation 1**
The array contains a single zero. Moving zeroes to the end leaves the array unchanged.

**Sample Input 2**
```
4
1 2 3 4
```

**Sample Output 2**
```
1 2 3 4
```

**Sample Input 3**
```
6
0 0 0 0 0 0
```

**Sample Output 3**
```
0 0 0 0 0 0
```

**Sample Input 4**
```
6
0 0 0 1 2 3
```

**Sample Output 4**
```
1 2 3 0 0 0
```

**Sample Input 5**
```
6
1 2 3 0 0 0
```

**Sample Output 5**
```
1 2 3 0 0 0
```

**Sample Input 6**
```
8
4 2 4 0 0 3 0 4
```

**Sample Output 6**
```
4 2 4 3 4 0 0 0
```

**Sample Input 7**
```
5
-1 0 -2 0 3
```

**Sample Output 7**
```
-1 -2 3 0 0
```

**Sample Input 8**
```
3
0 1 0
```

**Sample Output 8**
```
1 0 0
```

**Sample Input 9**
```
7
5 0 5 0 5 0 5
```

**Sample Output 9**
```
5 5 5 5 0 0 0
```

**Tags**
Two Pointers, Arrays, In-place
