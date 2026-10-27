# Mid-Term — Binary Search only

Subset for the one challenge the first automator run skipped.

## Midterm: Binary Search
**Difficulty**: Easy

**Problem Statement**
Given a sorted (non-decreasing) array of integers `nums` and a target value `target`, return the 0-based index of `target` in the array. If the target does not exist, return `-1`. Your algorithm must run in `O(log N)` time.

**Input Format**
- Line 1: two space-separated integers `N` (size of the array) and `target`.
- Line 2: `N` space-separated integers — the sorted array elements.

**Output Format**
A single integer — the 0-based index of `target`, or `-1` if not present.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order.

**Sample Input 0**
```
6 9
-1 0 3 5 9 12
```

**Sample Output 0**
```
4
```

**Sample Explanation 0**
The target `9` is located at index `4` of the sorted array.

**Sample Input 1**
```
6 2
-1 0 3 5 9 12
```

**Sample Output 1**
```
-1
```

**Sample Explanation 1**
The target `2` is not present anywhere in the array, so we return `-1`.

**Sample Input 2**
```
1 5
5
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
1 5
3
```

**Sample Output 3**
```
-1
```

**Sample Input 4**
```
5 1
1 2 3 4 5
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
5 5
1 2 3 4 5
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
5 3
1 2 3 4 5
```

**Sample Output 6**
```
2
```

**Sample Input 7**
```
7 -4
-10 -7 -4 -1 2 5 8
```

**Sample Output 7**
```
2
```

**Sample Input 8**
```
8 100
1 2 3 4 5 6 7 8
```

**Sample Output 8**
```
-1
```

**Sample Input 9**
```
6 7
1 3 5 7 9 11
```

**Sample Output 9**
```
3
```

**Tags**
Binary Search, Arrays

---
