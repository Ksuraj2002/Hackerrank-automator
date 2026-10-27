# DSA-101 Classwork - Part 3 (Days 34 to 59)

Author-ready markdown for `automator.py`. Strict statements (no approach
hints). Each problem has 10 sample I/O pairs computed by reference solvers.

Skipped as duplicate content:
- Day 37 CW2 "Rotate by k using reversal" - same I/O as the kept public-HR
  "Left Rotation".

Includes replacements for the 8 public-HR challenges removed from the
contest (Remove Duplicates, Add Strings-style, Next Permutation, etc.).

After uploading:
1. `venv\Scripts\python.exe tools\hr_mark_samples.py --md classwork_part3_days34_59.md --apply`
2. Enable C++14, Java 8, Python 3 in the admin UI on each challenge.
3. `venv\Scripts\python.exe tools\hr_add_to_contest.py --md classwork_part3_days34_59.md --apply`

---


## Classwork: Linear Search - Return the Index
**Problem Statement**
You are given an array of `N` integers and an integer `X`. Print the smallest 0-indexed position at which `X` appears in the array. If `X` does not appear, print `-1`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.
- Line 3: the integer `X`.

**Output Format**
A single line containing the 0-indexed position of `X`, or `-1`.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i], X <= 10^9`

**Sample Input 0**
```
5
1 2 3 4 5
3
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
5
1 2 3 4 5
6
```

**Sample Output 1**
```
-1
```

**Sample Input 2**
```
1
7
7
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
6
5 5 5 5 5 5
5
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
4
-1 -2 -3 -4
-3
```

**Sample Output 4**
```
2
```

**Sample Input 5**
```
3
0 0 0
0
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
5
1 2 3 4 5
1
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
5
1 2 3 4 5
5
```

**Sample Output 7**
```
4
```

**Sample Input 8**
```
6
10 20 30 20 10 40
20
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
5
1000000000 -1000000000 0 500 -500
-1000000000
```

**Sample Output 9**
```
1
```

**Tags**
Arrays, Searching

---

## Classwork: Sum of a Given Range
**Problem Statement**
You are given an array of `N` integers and two 0-indexed positions `L` and `R` (with `L <= R`). Print the sum of the elements `A[L] + A[L+1] + ... + A[R]`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.
- Line 3: two space-separated integers `L R`.

**Output Format**
A single line containing the sum.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`
- `0 <= L <= R < N`

**Sample Input 0**
```
5
1 2 3 4 5
1 3
```

**Sample Output 0**
```
9
```

**Sample Input 1**
```
5
1 2 3 4 5
0 4
```

**Sample Output 1**
```
15
```

**Sample Input 2**
```
5
1 2 3 4 5
2 2
```

**Sample Output 2**
```
3
```

**Sample Input 3**
```
1
7
0 0
```

**Sample Output 3**
```
7
```

**Sample Input 4**
```
6
-1 -2 -3 -4 -5 -6
0 5
```

**Sample Output 4**
```
-21
```

**Sample Input 5**
```
5
10 20 30 40 50
0 2
```

**Sample Output 5**
```
60
```

**Sample Input 6**
```
5
100 -100 100 -100 100
0 4
```

**Sample Output 6**
```
100
```

**Sample Input 7**
```
4
1000000000 1000000000 1000000000 1000000000
0 3
```

**Sample Output 7**
```
4000000000
```

**Sample Input 8**
```
5
5 4 3 2 1
3 4
```

**Sample Output 8**
```
3
```

**Sample Input 9**
```
6
1 2 3 4 5 6
1 4
```

**Sample Output 9**
```
14
```

**Tags**
Arrays, Loops

---

## Classwork: Range Sum Query - Immutable (LC303)
**Problem Statement**
You are given an array of `N` integers and `Q` queries. Each query gives two 0-indexed positions `L` and `R` (`L <= R`). For each query, print the sum `A[L] + A[L+1] + ... + A[R]` on its own line.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.
- Line 3: an integer `Q`.
- Next `Q` lines: each contains two space-separated integers `L R`.

**Output Format**
`Q` lines, each containing the answer to one query.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`
- `1 <= Q <= 10^5`
- `0 <= L <= R < N`

**Sample Input 0**
```
5
1 2 3 4 5
3
0 4
1 3
2 2
```

**Sample Output 0**
```
15
9
3
```

**Sample Input 1**
```
1
7
1
0 0
```

**Sample Output 1**
```
7
```

**Sample Input 2**
```
5
10 20 30 40 50
2
0 2
2 4
```

**Sample Output 2**
```
60
120
```

**Sample Input 3**
```
5
-1 -2 -3 -4 -5
1
0 4
```

**Sample Output 3**
```
-15
```

**Sample Input 4**
```
6
1 1 1 1 1 1
3
0 5
0 2
3 5
```

**Sample Output 4**
```
6
3
3
```

**Sample Input 5**
```
4
100 -100 100 -100
2
0 3
1 2
```

**Sample Output 5**
```
0
0
```

**Sample Input 6**
```
5
5 4 3 2 1
5
0 0
1 1
2 2
3 3
4 4
```

**Sample Output 6**
```
5
4
3
2
1
```

**Sample Input 7**
```
8
1 2 3 4 5 6 7 8
2
0 7
2 5
```

**Sample Output 7**
```
36
18
```

**Sample Input 8**
```
3
-100 0 100
3
0 0
1 1
2 2
```

**Sample Output 8**
```
-100
0
100
```

**Sample Input 9**
```
10
1 1 1 1 1 1 1 1 1 1
1
0 9
```

**Sample Output 9**
```
10
```

**Tags**
Arrays, Prefix Sums

---

## Classwork: Maximum Subarray with Start and End Indices
**Problem Statement**
You are given an array of `N` integers. Print the maximum possible sum over all contiguous non-empty subarrays, together with the 0-indexed positions of the start and the end of one such subarray.

If several subarrays have the same maximum sum, print the one with the smallest start position; among those, the smallest end position.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing three integers: the maximum sum, the start index, and the end index, separated by single spaces.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
9
-2 1 -3 4 -1 2 1 -5 4
```

**Sample Output 0**
```
6 3 6
```

**Sample Input 1**
```
1
7
```

**Sample Output 1**
```
7 0 0
```

**Sample Input 2**
```
5
-1 -2 -3 -4 -5
```

**Sample Output 2**
```
-1 0 0
```

**Sample Input 3**
```
5
1 2 3 4 5
```

**Sample Output 3**
```
15 0 4
```

**Sample Input 4**
```
5
5 -1 5 -1 5
```

**Sample Output 4**
```
13 0 4
```

**Sample Input 5**
```
6
-2 -3 4 -1 -2 1
```

**Sample Output 5**
```
4 2 2
```

**Sample Input 6**
```
3
0 0 0
```

**Sample Output 6**
```
0 0 0
```

**Sample Input 7**
```
6
1 -1 1 -1 1 -1
```

**Sample Output 7**
```
1 0 0
```

**Sample Input 8**
```
8
-10 5 -2 5 -3 5 -10 5
```

**Sample Output 8**
```
10 1 5
```

**Sample Input 9**
```
4
1000000000 -1 1000000000 -1
```

**Sample Output 9**
```
1999999999 0 2
```

**Tags**
Arrays, Dynamic Programming

---

## Classwork: Frequency of Each Element
**Problem Statement**
You are given an array of `N` integers. For every distinct value in the array, print two integers on a line: the value and its frequency, separated by one space.

Distinct values must be printed in strictly increasing order.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
One line per distinct value, in increasing order of value: `<value> <frequency>`.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
6
1 2 2 3 3 3
```

**Sample Output 0**
```
1 1
2 2
3 3
```

**Sample Input 1**
```
1
7
```

**Sample Output 1**
```
7 1
```

**Sample Input 2**
```
5
5 5 5 5 5
```

**Sample Output 2**
```
5 5
```

**Sample Input 3**
```
5
1 2 3 4 5
```

**Sample Output 3**
```
1 1
2 1
3 1
4 1
5 1
```

**Sample Input 4**
```
6
-1 -2 -1 -2 -3 -3
```

**Sample Output 4**
```
-3 2
-2 2
-1 2
```

**Sample Input 5**
```
8
4 4 4 4 4 4 4 4
```

**Sample Output 5**
```
4 8
```

**Sample Input 6**
```
6
10 20 10 30 20 10
```

**Sample Output 6**
```
10 3
20 2
30 1
```

**Sample Input 7**
```
5
0 0 0 1 1
```

**Sample Output 7**
```
0 3
1 2
```

**Sample Input 8**
```
6
-100 100 0 -100 100 0
```

**Sample Output 8**
```
-100 2
0 2
100 2
```

**Sample Input 9**
```
10
5 4 3 2 1 5 4 3 2 1
```

**Sample Output 9**
```
1 2
2 2
3 2
4 2
5 2
```

**Tags**
Arrays, Hashing

---

## Classwork: Most Frequent Element
**Problem Statement**
You are given an array of `N` integers. Print the element that appears the greatest number of times. If several elements share the greatest frequency, print the smallest of them.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the most frequent element.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
7
2 3 2 4 3 5 3
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
6
1 2 2 1 3 3
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
1
7
```

**Sample Output 2**
```
7
```

**Sample Input 3**
```
5
5 5 5 5 5
```

**Sample Output 3**
```
5
```

**Sample Input 4**
```
5
10 20 30 40 50
```

**Sample Output 4**
```
10
```

**Sample Input 5**
```
6
-1 -1 -2 -2 -3 -3
```

**Sample Output 5**
```
-3
```

**Sample Input 6**
```
8
0 0 0 0 1 1 1 1
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
9
4 4 4 2 2 2 1 1 1
```

**Sample Output 7**
```
1
```

**Sample Input 8**
```
7
-5 -5 -5 3 3 7 7
```

**Sample Output 8**
```
-5
```

**Sample Input 9**
```
8
1000000000 -1000000000 1000000000 -1000000000 0 0 0 0
```

**Sample Output 9**
```
0
```

**Tags**
Arrays, Hashing

---

## Classwork: Count of Distinct Elements
**Problem Statement**
You are given an array of `N` integers. Print the number of distinct values that appear in the array.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the count of distinct values.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
1 2 3 4 5
```

**Sample Output 0**
```
5
```

**Sample Input 1**
```
5
1 1 1 1 1
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
1
7
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
6
1 2 2 3 3 3
```

**Sample Output 3**
```
3
```

**Sample Input 4**
```
10
1 2 3 4 5 1 2 3 4 5
```

**Sample Output 4**
```
5
```

**Sample Input 5**
```
5
-1 -1 -2 -2 -3
```

**Sample Output 5**
```
3
```

**Sample Input 6**
```
8
1000000000 -1000000000 1000000000 -1000000000 0 0 0 0
```

**Sample Output 6**
```
3
```

**Sample Input 7**
```
6
0 0 0 0 0 1
```

**Sample Output 7**
```
2
```

**Sample Input 8**
```
5
5 4 3 2 1
```

**Sample Output 8**
```
5
```

**Sample Input 9**
```
10
10 20 30 40 50 60 70 80 90 100
```

**Sample Output 9**
```
10
```

**Tags**
Arrays, Hashing

---

## Classwork: Counting Sort a Small-Range Array
**Problem Statement**
You are given an array of `N` integers where every element is in the range `[0, K]`. Print the array sorted in non-decreasing order.

**Input Format**
- Line 1: two space-separated integers `N K`.
- Line 2: `N` space-separated integers, each in `[0, K]`.

**Output Format**
A single line with the sorted array, elements separated by a single space.

**Constraints**
- `1 <= N <= 10^5`
- `0 <= K <= 10^5`
- `0 <= A[i] <= K`

**Sample Input 0**
```
5 5
4 2 2 1 5
```

**Sample Output 0**
```
1 2 2 4 5
```

**Sample Input 1**
```
5 9
9 8 7 6 5
```

**Sample Output 1**
```
5 6 7 8 9
```

**Sample Input 2**
```
1 0
0
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
6 3
3 1 2 3 1 2
```

**Sample Output 3**
```
1 1 2 2 3 3
```

**Sample Input 4**
```
8 10
0 10 0 10 0 10 0 10
```

**Sample Output 4**
```
0 0 0 0 10 10 10 10
```

**Sample Input 5**
```
10 100
50 40 30 20 10 5 15 25 35 45
```

**Sample Output 5**
```
5 10 15 20 25 30 35 40 45 50
```

**Sample Input 6**
```
5 5
5 5 5 5 5
```

**Sample Output 6**
```
5 5 5 5 5
```

**Sample Input 7**
```
4 4
0 0 0 0
```

**Sample Output 7**
```
0 0 0 0
```

**Sample Input 8**
```
7 7
7 6 5 4 3 2 1
```

**Sample Output 8**
```
1 2 3 4 5 6 7
```

**Sample Input 9**
```
10 9
9 8 7 6 5 4 3 2 1 0
```

**Sample Output 9**
```
0 1 2 3 4 5 6 7 8 9
```

**Tags**
Sorting, Arrays

---

## Classwork: Two Sum on a Sorted Array (LC167)
**Problem Statement**
You are given a 1-indexed array of `N` integers sorted in non-decreasing order, and an integer target `T`. Find two distinct positions `i` and `j` (with `1 <= i < j <= N`) such that `A[i] + A[j] == T`, and print them separated by a single space.

It is guaranteed that at most one such pair exists in every test. If no such pair exists, print `-1 -1`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated non-decreasing integers.
- Line 3: the integer `T`.

**Output Format**
A single line containing the two 1-indexed positions, or `-1 -1`.

**Constraints**
- `2 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`
- `-2*10^9 <= T <= 2*10^9`

**Sample Input 0**
```
4
2 7 11 15
9
```

**Sample Output 0**
```
1 2
```

**Sample Input 1**
```
3
1 2 3
5
```

**Sample Output 1**
```
2 3
```

**Sample Input 2**
```
2
1 1
2
```

**Sample Output 2**
```
1 2
```

**Sample Input 3**
```
5
-3 -1 0 2 4
1
```

**Sample Output 3**
```
1 5
```

**Sample Input 4**
```
6
1 2 3 4 5 6
11
```

**Sample Output 4**
```
5 6
```

**Sample Input 5**
```
5
1 2 3 4 5
100
```

**Sample Output 5**
```
-1 -1
```

**Sample Input 6**
```
5
-5 -4 -3 -2 -1
-8
```

**Sample Output 6**
```
1 3
```

**Sample Input 7**
```
4
0 0 3 4
0
```

**Sample Output 7**
```
1 2
```

**Sample Input 8**
```
6
1 1 1 1 1 2
3
```

**Sample Output 8**
```
1 6
```

**Sample Input 9**
```
5
1 5 5 5 9
10
```

**Sample Output 9**
```
1 5
```

**Tags**
Two Pointers, Arrays

---

## Classwork: Move Zeroes to the End (LC283)
**Problem Statement**
You are given an array of `N` integers. Move all `0` elements to the end of the array while keeping the relative order of the non-zero elements unchanged. Print the resulting array on a single line, elements separated by a single space.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line with the transformed array, elements separated by a single space.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
0 1 0 3 12
```

**Sample Output 0**
```
1 3 12 0 0
```

**Sample Input 1**
```
1
0
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
1
5
```

**Sample Output 2**
```
5
```

**Sample Input 3**
```
5
0 0 0 0 0
```

**Sample Output 3**
```
0 0 0 0 0
```

**Sample Input 4**
```
5
1 2 3 4 5
```

**Sample Output 4**
```
1 2 3 4 5
```

**Sample Input 5**
```
6
0 0 1 0 0 2
```

**Sample Output 5**
```
1 2 0 0 0 0
```

**Sample Input 6**
```
8
1 0 2 0 3 0 4 0
```

**Sample Output 6**
```
1 2 3 4 0 0 0 0
```

**Sample Input 7**
```
5
-1 0 -2 0 -3
```

**Sample Output 7**
```
-1 -2 -3 0 0
```

**Sample Input 8**
```
4
0 1 2 3
```

**Sample Output 8**
```
1 2 3 0
```

**Sample Input 9**
```
4
1 2 3 0
```

**Sample Output 9**
```
1 2 3 0
```

**Tags**
Two Pointers, Arrays

---

## Classwork: Partition an Array Around a Pivot
**Problem Statement**
You are given an array of `N` integers and an integer pivot value `P`. Rearrange the array so that every element less than or equal to `P` appears before every element strictly greater than `P`, and within each of these two groups the elements keep their original relative order.

Print the transformed array on a single line, elements separated by a single space.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.
- Line 3: the integer `P`.

**Output Format**
A single line with the transformed array.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i], P <= 10^9`

**Sample Input 0**
```
6
3 1 4 1 5 9
3
```

**Sample Output 0**
```
3 1 1 4 5 9
```

**Sample Input 1**
```
5
1 2 3 4 5
3
```

**Sample Output 1**
```
1 2 3 4 5
```

**Sample Input 2**
```
5
5 4 3 2 1
3
```

**Sample Output 2**
```
3 2 1 5 4
```

**Sample Input 3**
```
1
7
7
```

**Sample Output 3**
```
7
```

**Sample Input 4**
```
5
5 5 5 5 5
5
```

**Sample Output 4**
```
5 5 5 5 5
```

**Sample Input 5**
```
6
-1 -2 3 4 -3 5
0
```

**Sample Output 5**
```
-1 -2 -3 3 4 5
```

**Sample Input 6**
```
6
0 0 0 0 0 0
0
```

**Sample Output 6**
```
0 0 0 0 0 0
```

**Sample Input 7**
```
8
8 1 7 2 6 3 5 4
4
```

**Sample Output 7**
```
1 2 3 4 8 7 6 5
```

**Sample Input 8**
```
5
1000000000 -1000000000 0 500 -500
0
```

**Sample Output 8**
```
-1000000000 0 -500 1000000000 500
```

**Sample Input 9**
```
7
2 2 2 3 3 3 4
3
```

**Sample Output 9**
```
2 2 2 3 3 3 4
```

**Tags**
Two Pointers, Arrays

---

## Classwork: Move Negatives to the Left
**Problem Statement**
You are given an array of `N` integers. Rearrange the array so that every negative element appears before every non-negative element, keeping the original relative order within each group.

Print the transformed array on a single line, elements separated by a single space.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line with the transformed array.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
6
1 -2 3 -4 5 -6
```

**Sample Output 0**
```
-2 -4 -6 1 3 5
```

**Sample Input 1**
```
5
1 2 3 4 5
```

**Sample Output 1**
```
1 2 3 4 5
```

**Sample Input 2**
```
5
-1 -2 -3 -4 -5
```

**Sample Output 2**
```
-1 -2 -3 -4 -5
```

**Sample Input 3**
```
1
0
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
1
-1
```

**Sample Output 4**
```
-1
```

**Sample Input 5**
```
6
0 0 0 -1 -1 -1
```

**Sample Output 5**
```
-1 -1 -1 0 0 0
```

**Sample Input 6**
```
6
-1 1 -2 2 -3 3
```

**Sample Output 6**
```
-1 -2 -3 1 2 3
```

**Sample Input 7**
```
5
0 -1 0 -2 0
```

**Sample Output 7**
```
-1 -2 0 0 0
```

**Sample Input 8**
```
4
-5 -4 -3 -2
```

**Sample Output 8**
```
-5 -4 -3 -2
```

**Sample Input 9**
```
7
7 -1 6 -2 5 -3 4
```

**Sample Output 9**
```
-1 -2 -3 7 6 5 4
```

**Tags**
Two Pointers, Arrays

---

## Classwork: 3Sum (LC15)
**Problem Statement**
You are given an array of `N` integers. Find every unique triplet `(a, b, c)` of elements from the array (using each index at most once) such that `a + b + c == 0`.

For each triplet, print its three values in non-decreasing order. Print the triplets themselves in lexicographic order (compare the first values, then the second, then the third).

Print the total number of unique triplets on the first line, then the triplets on the following lines, one per line.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
- Line 1: the number of unique triplets.
- Next lines: one triplet per line, sorted as described.

**Constraints**
- `3 <= N <= 3000`
- `-10^5 <= A[i] <= 10^5`

**Sample Input 0**
```
6
-1 0 1 2 -1 -4
```

**Sample Output 0**
```
2
-1 -1 2
-1 0 1
```

**Sample Input 1**
```
3
0 0 0
```

**Sample Output 1**
```
1
0 0 0
```

**Sample Input 2**
```
3
1 2 -3
```

**Sample Output 2**
```
1
-3 1 2
```

**Sample Input 3**
```
5
0 0 0 0 0
```

**Sample Output 3**
```
1
0 0 0
```

**Sample Input 4**
```
6
-2 0 1 1 2 -1
```

**Sample Output 4**
```
3
-2 0 2
-2 1 1
-1 0 1
```

**Sample Input 5**
```
5
1 2 3 4 5
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
4
-1 -1 2 0
```

**Sample Output 6**
```
1
-1 -1 2
```

**Sample Input 7**
```
6
3 0 -2 -1 1 2
```

**Sample Output 7**
```
3
-2 -1 3
-2 0 2
-1 0 1
```

**Sample Input 8**
```
7
-4 -1 -1 0 1 2 3
```

**Sample Output 8**
```
3
-4 1 3
-1 -1 2
-1 0 1
```

**Sample Input 9**
```
5
-5 -5 -5 -5 10
```

**Sample Output 9**
```
1
-5 -5 10
```

**Tags**
Two Pointers, Arrays

---

## Classwork: Count Pairs with Difference K
**Problem Statement**
You are given an array of `N` integers and a non-negative integer `K`. Print the number of index pairs `(i, j)` with `i < j` such that `|A[i] - A[j]| == K`.

**Input Format**
- Line 1: two space-separated integers `N K`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the count.

**Constraints**
- `1 <= N <= 3000`
- `0 <= K <= 10^9`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5 2
1 3 5 7 9
```

**Sample Output 0**
```
4
```

**Sample Input 1**
```
5 0
1 1 1 1 1
```

**Sample Output 1**
```
10
```

**Sample Input 2**
```
1 5
7
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
6 3
1 4 7 10 2 5
```

**Sample Output 3**
```
4
```

**Sample Input 4**
```
5 100
1 2 3 4 5
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
5 5
-3 2 7 12 17
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
4 0
1 2 3 4
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
6 1
1 2 3 4 5 6
```

**Sample Output 7**
```
5
```

**Sample Input 8**
```
4 10
5 -5 15 -15
```

**Sample Output 8**
```
3
```

**Sample Input 9**
```
8 2
1 3 3 5 5 7 7 9
```

**Sample Output 9**
```
12
```

**Tags**
Two Pointers, Arrays

---

## Classwork: Remove Duplicates from a Sorted Array (LC26)
**Problem Statement**
You are given an array of `N` integers sorted in non-decreasing order. Print two things:

- Line 1: the number of distinct values in the array.
- Line 2: those distinct values, in non-decreasing order, separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated non-decreasing integers.

**Output Format**
Two lines: the count on line 1, the deduplicated values on line 2.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
1 1 2 2 3
```

**Sample Output 0**
```
3
1 2 3
```

**Sample Input 1**
```
1
7
```

**Sample Output 1**
```
1
7
```

**Sample Input 2**
```
5
1 2 3 4 5
```

**Sample Output 2**
```
5
1 2 3 4 5
```

**Sample Input 3**
```
5
1 1 1 1 1
```

**Sample Output 3**
```
1
1
```

**Sample Input 4**
```
6
-1 -1 0 0 1 1
```

**Sample Output 4**
```
3
-1 0 1
```

**Sample Input 5**
```
3
5 5 5
```

**Sample Output 5**
```
1
5
```

**Sample Input 6**
```
6
1 2 3 3 4 5
```

**Sample Output 6**
```
5
1 2 3 4 5
```

**Sample Input 7**
```
8
1 1 2 2 3 3 4 4
```

**Sample Output 7**
```
4
1 2 3 4
```

**Sample Input 8**
```
5
-3 -2 -1 0 1
```

**Sample Output 8**
```
5
-3 -2 -1 0 1
```

**Sample Input 9**
```
10
0 0 0 0 0 0 0 0 0 0
```

**Sample Output 9**
```
1
0
```

**Tags**
Two Pointers, Arrays

---

## Classwork: Read and Print a Matrix
**Problem Statement**
You are given a matrix with `R` rows and `C` columns of integers. Print the same matrix, one row per line, with elements separated by a single space.

**Input Format**
- Line 1: two space-separated integers `R C`.
- Next `R` lines: each contains `C` space-separated integers.

**Output Format**
`R` lines, each printing the corresponding row of the matrix.

**Constraints**
- `1 <= R, C <= 500`
- `-10^9 <= A[i][j] <= 10^9`

**Sample Input 0**
```
2 3
1 2 3
4 5 6
```

**Sample Output 0**
```
1 2 3
4 5 6
```

**Sample Input 1**
```
1 1
42
```

**Sample Output 1**
```
42
```

**Sample Input 2**
```
3 3
1 0 0
0 1 0
0 0 1
```

**Sample Output 2**
```
1 0 0
0 1 0
0 0 1
```

**Sample Input 3**
```
1 5
1 2 3 4 5
```

**Sample Output 3**
```
1 2 3 4 5
```

**Sample Input 4**
```
5 1
1
2
3
4
5
```

**Sample Output 4**
```
1
2
3
4
5
```

**Sample Input 5**
```
2 2
-1 -2
-3 -4
```

**Sample Output 5**
```
-1 -2
-3 -4
```

**Sample Input 6**
```
3 4
1 2 3 4
5 6 7 8
9 10 11 12
```

**Sample Output 6**
```
1 2 3 4
5 6 7 8
9 10 11 12
```

**Sample Input 7**
```
2 2
1000000000 -1000000000
-1000000000 1000000000
```

**Sample Output 7**
```
1000000000 -1000000000
-1000000000 1000000000
```

**Sample Input 8**
```
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

**Sample Output 8**
```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

**Sample Input 9**
```
2 3
0 0 0
0 0 0
```

**Sample Output 9**
```
0 0 0
0 0 0
```

**Tags**
2D Arrays, Matrices

---

## Classwork: Sum of Each Row and Column
**Problem Statement**
You are given a matrix with `R` rows and `C` columns of integers. Print two lines:

- Line 1: the `R` row sums, top to bottom, separated by single spaces.
- Line 2: the `C` column sums, left to right, separated by single spaces.

**Input Format**
- Line 1: two space-separated integers `R C`.
- Next `R` lines: each contains `C` space-separated integers.

**Output Format**
Two lines: row sums on line 1, column sums on line 2.

**Constraints**
- `1 <= R, C <= 500`
- `-10^6 <= A[i][j] <= 10^6`

**Sample Input 0**
```
2 3
1 2 3
4 5 6
```

**Sample Output 0**
```
6 15
5 7 9
```

**Sample Input 1**
```
1 1
42
```

**Sample Output 1**
```
42
42
```

**Sample Input 2**
```
3 3
1 2 3
4 5 6
7 8 9
```

**Sample Output 2**
```
6 15 24
12 15 18
```

**Sample Input 3**
```
1 4
10 20 30 40
```

**Sample Output 3**
```
100
10 20 30 40
```

**Sample Input 4**
```
4 1
1
2
3
4
```

**Sample Output 4**
```
1 2 3 4
10
```

**Sample Input 5**
```
3 3
0 0 0
0 0 0
0 0 0
```

**Sample Output 5**
```
0 0 0
0 0 0
```

**Sample Input 6**
```
2 2
-1 -2
-3 -4
```

**Sample Output 6**
```
-3 -7
-4 -6
```

**Sample Input 7**
```
3 3
1 -1 1
-1 1 -1
1 -1 1
```

**Sample Output 7**
```
1 -1 1
1 -1 1
```

**Sample Input 8**
```
2 3
100 200 300
400 500 600
```

**Sample Output 8**
```
600 1500
500 700 900
```

**Sample Input 9**
```
4 4
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

**Sample Output 9**
```
4 8 12 16
10 10 10 10
```

**Tags**
2D Arrays, Matrices

---

## Classwork: Sum of Both Diagonals of a Square Matrix
**Problem Statement**
You are given a square matrix of size `N x N`. Compute the sum of the main diagonal (elements `A[i][i]`) and the sum of the anti-diagonal (elements `A[i][N - 1 - i]`).

Print both sums on a single line, separated by a single space: main-diagonal sum first, then anti-diagonal sum.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: each contains `N` space-separated integers.

**Output Format**
A single line with two integers: main diagonal sum and anti-diagonal sum.

**Constraints**
- `1 <= N <= 500`
- `-10^6 <= A[i][j] <= 10^6`

**Sample Input 0**
```
3
1 2 3
4 5 6
7 8 9
```

**Sample Output 0**
```
15 15
```

**Sample Input 1**
```
1
7
```

**Sample Output 1**
```
7 7
```

**Sample Input 2**
```
2
1 2
3 4
```

**Sample Output 2**
```
5 5
```

**Sample Input 3**
```
4
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
```

**Sample Output 3**
```
4 0
```

**Sample Input 4**
```
3
0 0 0
0 0 0
0 0 0
```

**Sample Output 4**
```
0 0
```

**Sample Input 5**
```
3
5 5 5
5 5 5
5 5 5
```

**Sample Output 5**
```
15 15
```

**Sample Input 6**
```
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

**Sample Output 6**
```
34 34
```

**Sample Input 7**
```
3
-1 -2 -3
-4 -5 -6
-7 -8 -9
```

**Sample Output 7**
```
-15 -15
```

**Sample Input 8**
```
5
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
```

**Sample Output 8**
```
5 5
```

**Sample Input 9**
```
2
1000000 1
1 1000000
```

**Sample Output 9**
```
2000000 2
```

**Tags**
2D Arrays, Matrices

---

## Classwork: Swap Two Numbers using XOR
**Problem Statement**
Two integers `A` and `B` are given on a single line, separated by one space. Print them swapped: `B` first, then `A`, separated by one space.

**Input Format**
A single line with two space-separated integers `A B`.

**Output Format**
A single line with two integers: `B A`.

**Constraints**
- `-10^9 <= A, B <= 10^9`

**Sample Input 0**
```
3 5
```

**Sample Output 0**
```
5 3
```

**Sample Input 1**
```
0 0
```

**Sample Output 1**
```
0 0
```

**Sample Input 2**
```
1 -1
```

**Sample Output 2**
```
-1 1
```

**Sample Input 3**
```
1000000000 -1000000000
```

**Sample Output 3**
```
-1000000000 1000000000
```

**Sample Input 4**
```
42 42
```

**Sample Output 4**
```
42 42
```

**Sample Input 5**
```
7 0
```

**Sample Output 5**
```
0 7
```

**Sample Input 6**
```
0 7
```

**Sample Output 6**
```
7 0
```

**Sample Input 7**
```
-5 5
```

**Sample Output 7**
```
5 -5
```

**Sample Input 8**
```
100 200
```

**Sample Output 8**
```
200 100
```

**Sample Input 9**
```
999999999 1
```

**Sample Output 9**
```
1 999999999
```

**Tags**
Bit Manipulation, Basics

---

## Classwork: Check if the K-th Bit is Set
**Problem Statement**
Two non-negative integers `N` and `K` are given on a single line, separated by one space. Bits of `N` are 1-indexed from the least significant bit (so `K = 1` is the lowest bit).

Print `Yes` if bit `K` of `N` is `1`, otherwise print `No`.

**Input Format**
A single line with two space-separated integers `N K`.

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `0 <= N <= 10^18`
- `1 <= K <= 60`

**Sample Input 0**
```
5 1
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
5 2
```

**Sample Output 1**
```
No
```

**Sample Input 2**
```
5 3
```

**Sample Output 2**
```
Yes
```

**Sample Input 3**
```
1 1
```

**Sample Output 3**
```
Yes
```

**Sample Input 4**
```
0 1
```

**Sample Output 4**
```
No
```

**Sample Input 5**
```
1024 11
```

**Sample Output 5**
```
Yes
```

**Sample Input 6**
```
1024 10
```

**Sample Output 6**
```
No
```

**Sample Input 7**
```
1073741824 31
```

**Sample Output 7**
```
Yes
```

**Sample Input 8**
```
7 3
```

**Sample Output 8**
```
Yes
```

**Sample Input 9**
```
8 4
```

**Sample Output 9**
```
Yes
```

**Tags**
Bit Manipulation, Basics

---

## Classwork: Generate All Non-Empty Subsets using Bit Manipulation
**Problem Statement**
You are given an array of `N` distinct integers. Print every non-empty subset of the array, one per line.

For every mask `k = 1, 2, ..., 2^N - 1`, print the subset formed by taking `A[i]` for exactly those positions `i` (0-indexed from the left) where bit `i` of `k` is set. Elements inside one subset are printed in the same order as they appear in the input array, separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated distinct integers.

**Output Format**
`2^N - 1` lines. Each line is one non-empty subset, printed in the order defined by the bitmask above.

**Constraints**
- `1 <= N <= 12`
- All `A[i]` are distinct integers with `-10^9 <= A[i] <= 10^9`.

**Sample Input 0**
```
1
7
```

**Sample Output 0**
```
7
```

**Sample Input 1**
```
2
1 2
```

**Sample Output 1**
```
1
2
1 2
```

**Sample Input 2**
```
3
1 2 3
```

**Sample Output 2**
```
1
2
1 2
3
1 3
2 3
1 2 3
```

**Sample Input 3**
```
3
-1 -2 -3
```

**Sample Output 3**
```
-1
-2
-1 -2
-3
-1 -3
-2 -3
-1 -2 -3
```

**Sample Input 4**
```
4
1 2 3 4
```

**Sample Output 4**
```
1
2
1 2
3
1 3
2 3
1 2 3
4
1 4
2 4
1 2 4
3 4
1 3 4
2 3 4
1 2 3 4
```

**Sample Input 5**
```
3
10 20 30
```

**Sample Output 5**
```
10
20
10 20
30
10 30
20 30
10 20 30
```

**Sample Input 6**
```
2
0 5
```

**Sample Output 6**
```
0
5
0 5
```

**Sample Input 7**
```
4
-1 2 -3 4
```

**Sample Output 7**
```
-1
2
-1 2
-3
-1 -3
2 -3
-1 2 -3
4
-1 4
2 4
-1 2 4
-3 4
-1 -3 4
2 -3 4
-1 2 -3 4
```

**Sample Input 8**
```
5
1 2 3 4 5
```

**Sample Output 8**
```
1
2
1 2
3
1 3
2 3
1 2 3
4
1 4
2 4
1 2 4
3 4
1 3 4
2 3 4
1 2 3 4
5
1 5
2 5
1 2 5
3 5
1 3 5
2 3 5
1 2 3 5
4 5
1 4 5
2 4 5
1 2 4 5
3 4 5
1 3 4 5
2 3 4 5
1 2 3 4 5
```

**Sample Input 9**
```
3
100 200 300
```

**Sample Output 9**
```
100
200
100 200
300
100 300
200 300
100 200 300
```

**Tags**
Bit Manipulation, Subsets

---

## Classwork: Find the Index of the First Occurrence (LC28)
**Problem Statement**
Two lines of input are given. The first line is a string `haystack` and the second line is a string `needle`. Print the smallest 0-indexed position at which `needle` occurs as a contiguous substring of `haystack`. If `needle` does not occur, print `-1`.

If `needle` is empty, print `0`.

**Input Format**
- Line 1: the string `haystack`.
- Line 2: the string `needle`.

**Output Format**
A single line containing the position, or `-1`.

**Constraints**
- `1 <= |haystack| <= 10^4`
- `0 <= |needle| <= |haystack|`
- Both strings consist of printable ASCII characters and contain no whitespace.

**Sample Input 0**
```
sadbutsad
sad
```

**Sample Output 0**
```
0
```

**Sample Input 1**
```
leetcode
leeto
```

**Sample Output 1**
```
-1
```

**Sample Input 2**
```
hello
ll
```

**Sample Output 2**
```
2
```

**Sample Input 3**
```
abcde
abc
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
abcde
de
```

**Sample Output 4**
```
3
```

**Sample Input 5**
```
aaaaa
aaa
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
mississippi
issi
```

**Sample Output 6**
```
1
```

**Sample Input 7**
```
abc
d
```

**Sample Output 7**
```
-1
```

**Sample Input 8**
```
abcd

```

**Sample Output 8**
```
0
```

**Sample Input 9**
```
abcabcabc
cab
```

**Sample Output 9**
```
2
```

**Tags**
Strings, Searching

---

## Classwork: Add Two Numbers Given as Strings (LC415)
**Problem Statement**
Two non-negative integers `A` and `B` are given as strings on two separate lines. Neither has a leading zero unless it is the digit `0` itself. Print their sum as a string.

You may assume that using arbitrary-precision arithmetic is not the intended approach; behaviour with typical language big-integer libraries is nonetheless correct.

**Input Format**
- Line 1: the string `A`.
- Line 2: the string `B`.

**Output Format**
A single line containing the sum `A + B` as a string with no leading zeros (except the value `0` itself).

**Constraints**
- `1 <= |A|, |B| <= 10^4`
- `A` and `B` consist only of digit characters `0-9`.

**Sample Input 0**
```
11
123
```

**Sample Output 0**
```
134
```

**Sample Input 1**
```
456
77
```

**Sample Output 1**
```
533
```

**Sample Input 2**
```
0
0
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
1
9
```

**Sample Output 3**
```
10
```

**Sample Input 4**
```
99
1
```

**Sample Output 4**
```
100
```

**Sample Input 5**
```
12345
67890
```

**Sample Output 5**
```
80235
```

**Sample Input 6**
```
100000000000000000000
1
```

**Sample Output 6**
```
100000000000000000001
```

**Sample Input 7**
```
0
1000000000
```

**Sample Output 7**
```
1000000000
```

**Sample Input 8**
```
999999999999999
1
```

**Sample Output 8**
```
1000000000000000
```

**Sample Input 9**
```
5
5
```

**Sample Output 9**
```
10
```

**Tags**
Strings, Math

---

## Classwork: Find the Row with the Maximum 1s
**Problem Statement**
You are given a binary matrix of `R` rows and `C` columns (every entry is `0` or `1`). Print the 0-indexed row number that contains the greatest number of `1`s. If several rows are tied, print the smallest such row number.

**Input Format**
- Line 1: two space-separated integers `R C`.
- Next `R` lines: each contains `C` space-separated integers that are either `0` or `1`.

**Output Format**
A single line containing the 0-indexed row number.

**Constraints**
- `1 <= R, C <= 500`

**Sample Input 0**
```
3 4
0 1 1 0
1 1 1 1
0 0 1 0
```

**Sample Output 0**
```
1
```

**Sample Input 1**
```
1 1
1
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
1 1
0
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
2 3
0 0 0
0 0 0
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
3 3
1 0 0
0 1 0
0 0 1
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
4 4
0 0 0 0
1 1 0 0
1 1 1 0
1 1 1 1
```

**Sample Output 5**
```
3
```

**Sample Input 6**
```
3 4
1 1 1 1
1 1 1 1
1 1 1 1
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
5 3
1 0 0
1 1 0
0 1 1
1 1 1
1 1 0
```

**Sample Output 7**
```
3
```

**Sample Input 8**
```
2 5
1 0 1 0 1
0 1 0 1 0
```

**Sample Output 8**
```
0
```

**Sample Input 9**
```
3 3
0 0 0
1 1 1
1 1 1
```

**Sample Output 9**
```
1
```

**Tags**
2D Arrays, Matrices

---

## Classwork: Next Permutation (LC31)
**Problem Statement**
You are given an array of `N` non-negative integers. Print the array rearranged into the next lexicographically greater permutation of its elements. If the array is already the greatest permutation, print the smallest permutation (that is, the array sorted in non-decreasing order).

The output is one line with the resulting `N` elements separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated non-negative integers.

**Output Format**
A single line with the next permutation.

**Constraints**
- `1 <= N <= 10^4`
- `0 <= A[i] <= 10^9`

**Sample Input 0**
```
3
1 2 3
```

**Sample Output 0**
```
1 3 2
```

**Sample Input 1**
```
3
3 2 1
```

**Sample Output 1**
```
1 2 3
```

**Sample Input 2**
```
3
1 1 5
```

**Sample Output 2**
```
1 5 1
```

**Sample Input 3**
```
4
1 3 2 4
```

**Sample Output 3**
```
1 3 4 2
```

**Sample Input 4**
```
1
7
```

**Sample Output 4**
```
7
```

**Sample Input 5**
```
5
1 2 3 4 5
```

**Sample Output 5**
```
1 2 3 5 4
```

**Sample Input 6**
```
5
5 4 3 2 1
```

**Sample Output 6**
```
1 2 3 4 5
```

**Sample Input 7**
```
4
1 2 2 1
```

**Sample Output 7**
```
2 1 1 2
```

**Sample Input 8**
```
6
1 5 1 5 1 5
```

**Sample Output 8**
```
1 5 1 5 5 1
```

**Sample Input 9**
```
5
2 3 1 3 3
```

**Sample Output 9**
```
2 3 3 1 3
```

**Tags**
Arrays, Permutations

---
