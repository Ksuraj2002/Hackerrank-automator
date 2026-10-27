# DSA-101 Homework - Part 3 (Days 35 to 59)

Strict rule: titles and statements describe WHAT the problem is, not HOW to
solve it. LC / GfG-tagged curriculum rows carry a source link at the top of
their statement.

After uploading:
1. `venv\Scripts\python.exe tools\hr_mark_samples.py --md homework_part3_days35_59.md --apply`
2. Enable C++14, Java 8, Python 3 on each challenge in the admin UI.
3. `venv\Scripts\python.exe tools\hr_add_to_contest.py --md homework_part3_days35_59.md --apply`

---


## Homework: First and Last Position of an Element in a Sorted Array
**Problem Statement**
> Original problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

You are given an array of `N` integers sorted in non-decreasing order, and an integer target `T`. Print two 0-indexed positions on a single line, separated by one space:

- the smallest index at which `T` appears,
- the largest index at which `T` appears.

If `T` does not appear at all, print `-1 -1`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated non-decreasing integers.
- Line 3: the integer `T`.

**Output Format**
A single line with two integers separated by one space.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i], T <= 10^9`

**Sample Input 0**
```
6
5 7 7 8 8 10
8
```

**Sample Output 0**
```
3 4
```

**Sample Input 1**
```
6
5 7 7 8 8 10
6
```

**Sample Output 1**
```
-1 -1
```

**Sample Input 2**
```
1
1
1
```

**Sample Output 2**
```
0 0
```

**Sample Input 3**
```
1
1
2
```

**Sample Output 3**
```
-1 -1
```

**Sample Input 4**
```
5
1 2 3 4 5
3
```

**Sample Output 4**
```
2 2
```

**Sample Input 5**
```
7
1 1 1 1 1 1 1
1
```

**Sample Output 5**
```
0 6
```

**Sample Input 6**
```
5
-5 -3 -3 -1 2
-3
```

**Sample Output 6**
```
1 2
```

**Sample Input 7**
```
5
1 2 3 4 5
5
```

**Sample Output 7**
```
4 4
```

**Sample Input 8**
```
8
2 2 2 4 4 6 6 6
4
```

**Sample Output 8**
```
3 4
```

**Sample Input 9**
```
5
1 3 5 7 9
4
```

**Sample Output 9**
```
-1 -1
```

**Tags**
Arrays, Searching

---

## Homework: Rearrange Positives and Negatives Alternately
**Problem Statement**
You are given an array of `N` integers. Produce a new arrangement in which positives and negatives alternate, starting with a positive number (or zero, which counts as non-negative).

Within the non-negative group and within the negative group, the relative order from the input must be preserved. If one group is exhausted while the other still has elements, append those remaining elements at the end in their original order.

Print the resulting arrangement on a single line, elements separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the rearranged array.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
6
1 2 3 -4 -1 4
```

**Sample Output 0**
```
1 -4 2 -1 3 4
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
6
-5 1 -3 2 -1 3
```

**Sample Output 3**
```
1 -5 2 -3 3 -1
```

**Sample Input 4**
```
1
0
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
6
0 -1 0 -2 0 -3
```

**Sample Output 5**
```
0 -1 0 -2 0 -3
```

**Sample Input 6**
```
8
5 -5 4 -4 3 -3 2 -2
```

**Sample Output 6**
```
5 -5 4 -4 3 -3 2 -2
```

**Sample Input 7**
```
4
-1 -2 3 4
```

**Sample Output 7**
```
3 -1 4 -2
```

**Sample Input 8**
```
5
1 -1 1 -1 1
```

**Sample Output 8**
```
1 -1 1 -1 1
```

**Sample Input 9**
```
7
10 -20 30 -40 50 -60 70
```

**Sample Output 9**
```
10 -20 30 -40 50 -60 70
```

**Tags**
Arrays, Rearrangement

---

## Homework: Apply Range Updates to an Array
**Problem Statement**
> Original problem: https://www.geeksforgeeks.org/?s=difference+array+range+update

An array `A` of length `N` is initially filled with zeros. You are given `Q` update operations. Each update is described by three integers `L R V`; it adds the value `V` to every element `A[L], A[L+1], ..., A[R]` (indices are 0-indexed and both `L` and `R` are inclusive).

After all `Q` updates are applied, print the resulting array on a single line, elements separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: an integer `Q`.
- Next `Q` lines: each contains three space-separated integers `L R V`.

**Output Format**
A single line with the final array of `N` integers.

**Constraints**
- `1 <= N <= 10^5`
- `0 <= Q <= 10^5`
- `0 <= L <= R < N`
- `-10^4 <= V <= 10^4`

**Sample Input 0**
```
5
2
0 2 3
1 3 4
```

**Sample Output 0**
```
3 7 7 4 0
```

**Sample Input 1**
```
5
0
```

**Sample Output 1**
```
0 0 0 0 0
```

**Sample Input 2**
```
3
1
0 2 5
```

**Sample Output 2**
```
5 5 5
```

**Sample Input 3**
```
4
3
0 0 1
1 1 2
2 2 3
```

**Sample Output 3**
```
1 2 3 0
```

**Sample Input 4**
```
6
2
1 4 10
0 5 -1
```

**Sample Output 4**
```
-1 9 9 9 9 -1
```

**Sample Input 5**
```
5
1
2 2 100
```

**Sample Output 5**
```
0 0 100 0 0
```

**Sample Input 6**
```
1
1
0 0 7
```

**Sample Output 6**
```
7
```

**Sample Input 7**
```
5
3
0 4 1
0 4 1
0 4 1
```

**Sample Output 7**
```
3 3 3 3 3
```

**Sample Input 8**
```
6
1
0 5 -5
```

**Sample Output 8**
```
-5 -5 -5 -5 -5 -5
```

**Sample Input 9**
```
8
4
0 3 5
2 5 -3
4 7 2
0 7 1
```

**Sample Output 9**
```
6 6 3 3 0 0 3 3
```

**Tags**
Arrays, Prefix Sums

---

## Homework: Maximum Contiguous Subarray Sum
**Problem Statement**
> Original problem: https://www.geeksforgeeks.org/?s=kadane+algorithm+maximum+contiguous+subarray

You are given an array of `N` integers (values may be negative, zero, or positive). Print the maximum possible sum over all contiguous non-empty subarrays.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the maximum sum.

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
6
```

**Sample Input 1**
```
1
7
```

**Sample Output 1**
```
7
```

**Sample Input 2**
```
5
-1 -2 -3 -4 -5
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
5
1 2 3 4 5
```

**Sample Output 3**
```
15
```

**Sample Input 4**
```
3
0 0 0
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
6
-2 -3 4 -1 -2 1
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
8
-10 5 -2 5 -3 5 -10 5
```

**Sample Output 6**
```
10
```

**Sample Input 7**
```
4
1000000000 -1 1000000000 -1
```

**Sample Output 7**
```
1999999999
```

**Sample Input 8**
```
6
1 -1 1 -1 1 -1
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
5
5 -1 5 -1 5
```

**Sample Output 9**
```
13
```

**Tags**
Arrays

---

## Homework: Element that Appears Only Once
**Problem Statement**
You are given an array of `N` integers in which every element appears exactly twice, except for one element which appears exactly once. Print that element.

**Input Format**
- Line 1: an integer `N` (`N` is odd).
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the element that appears once.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`
- Every element except one appears exactly twice.

**Sample Input 0**
```
5
2 3 2 4 4
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
1
7
```

**Sample Output 1**
```
7
```

**Sample Input 2**
```
3
1 2 1
```

**Sample Output 2**
```
2
```

**Sample Input 3**
```
7
5 5 6 7 6 8 8
```

**Sample Output 3**
```
7
```

**Sample Input 4**
```
5
-1 -2 -1 -3 -2
```

**Sample Output 4**
```
-3
```

**Sample Input 5**
```
3
0 1 1
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
9
10 20 10 30 40 30 40 50 50
```

**Sample Output 6**
```
20
```

**Sample Input 7**
```
7
100 200 300 100 200 300 999
```

**Sample Output 7**
```
999
```

**Sample Input 8**
```
5
1 2 3 2 3
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
11
1 2 3 4 5 1 2 3 4 5 100
```

**Sample Output 9**
```
100
```

**Tags**
Arrays

---

## Homework: Check if Two Arrays are Permutations of Each Other
**Problem Statement**
You are given two arrays of `N` integers each. Print `Yes` if the second array is a permutation of the first — that is, both arrays contain the same multiset of values — otherwise print `No`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers (array `A`).
- Line 3: `N` space-separated integers (array `B`).

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i], B[i] <= 10^9`

**Sample Input 0**
```
5
1 2 3 4 5
5 4 3 2 1
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
5
1 2 3 4 5
1 2 3 4 6
```

**Sample Output 1**
```
No
```

**Sample Input 2**
```
1
7
7
```

**Sample Output 2**
```
Yes
```

**Sample Input 3**
```
1
7
8
```

**Sample Output 3**
```
No
```

**Sample Input 4**
```
3
1 1 2
1 2 2
```

**Sample Output 4**
```
No
```

**Sample Input 5**
```
4
1 1 2 2
2 1 2 1
```

**Sample Output 5**
```
Yes
```

**Sample Input 6**
```
5
0 0 0 0 0
0 0 0 0 0
```

**Sample Output 6**
```
Yes
```

**Sample Input 7**
```
5
-1 -2 -3 -4 -5
-5 -4 -3 -2 -1
```

**Sample Output 7**
```
Yes
```

**Sample Input 8**
```
6
1 2 3 1 2 3
3 2 1 3 2 1
```

**Sample Output 8**
```
Yes
```

**Sample Input 9**
```
4
1 2 3 4
1 2 3 3
```

**Sample Output 9**
```
No
```

**Tags**
Arrays

---

## Homework: Remove Duplicates from a Sorted Array
**Problem Statement**
> Original problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

You are given an array of `N` integers sorted in non-decreasing order. Print two things:

- Line 1: the number of distinct values in the array.
- Line 2: those distinct values in non-decreasing order, separated by single spaces.

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
Arrays

---

## Homework: Container With Most Water
**Problem Statement**
> Original problem: https://leetcode.com/problems/container-with-most-water/

You are given an array of `N` non-negative integers `H[0], H[1], ..., H[N-1]`, where `H[i]` is the height of a vertical line drawn at position `i` on the x-axis.

Two of these lines, together with the x-axis, form a container. The amount of water a container between positions `i` and `j` (with `i < j`) can hold equals `(j - i) * min(H[i], H[j])`.

Print the maximum amount of water a container formed by any two of the given lines can hold.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated non-negative integers.

**Output Format**
A single line containing the maximum water amount.

**Constraints**
- `2 <= N <= 10^5`
- `0 <= H[i] <= 10^4`

**Sample Input 0**
```
9
1 8 6 2 5 4 8 3 7
```

**Sample Output 0**
```
49
```

**Sample Input 1**
```
2
1 1
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
5
1 2 3 4 5
```

**Sample Output 2**
```
6
```

**Sample Input 3**
```
5
5 4 3 2 1
```

**Sample Output 3**
```
6
```

**Sample Input 4**
```
3
0 0 0
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
4
4 3 2 1
```

**Sample Output 5**
```
4
```

**Sample Input 6**
```
6
1 5 4 3 2 6
```

**Sample Output 6**
```
20
```

**Sample Input 7**
```
3
10 1 10
```

**Sample Output 7**
```
20
```

**Sample Input 8**
```
5
2 3 4 5 18
```

**Sample Output 8**
```
9
```

**Sample Input 9**
```
8
1 2 4 3 8 6 7 5
```

**Sample Output 9**
```
20
```

**Tags**
Arrays

---

## Homework: 3Sum Closest
**Problem Statement**
> Original problem: https://leetcode.com/problems/3sum-closest/

You are given an array of `N` integers and a target integer `T`. From the array, choose three elements at three different positions whose sum is as close as possible to `T` — that is, whose sum minimises `|sum - T|`.

Print that sum. It is guaranteed that a valid triplet exists (so `N >= 3`).

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.
- Line 3: the integer `T`.

**Output Format**
A single line containing the closest sum.

**Constraints**
- `3 <= N <= 500`
- `-1000 <= A[i], T <= 1000`

**Sample Input 0**
```
4
-1 2 1 -4
1
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
3
0 0 0
1
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
3
1 1 1
0
```

**Sample Output 2**
```
3
```

**Sample Input 3**
```
6
1 1 1 0 0 0
100
```

**Sample Output 3**
```
3
```

**Sample Input 4**
```
5
-3 -2 -5 3 -4
-1
```

**Sample Output 4**
```
-2
```

**Sample Input 5**
```
4
0 0 0 0
1
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
5
1 2 3 4 5
10
```

**Sample Output 6**
```
10
```

**Sample Input 7**
```
5
-5 -4 -3 -2 -1
-8
```

**Sample Output 7**
```
-8
```

**Sample Input 8**
```
6
1 2 4 8 16 32
50
```

**Sample Output 8**
```
50
```

**Sample Input 9**
```
5
10 20 30 40 50
25
```

**Sample Output 9**
```
60
```

**Tags**
Arrays

---

## Homework: Two Sum in an Unsorted Array
**Problem Statement**
You are given an array of `N` integers and an integer target `T`. Find two distinct 0-indexed positions `i < j` such that `A[i] + A[j] == T`, and print `i` and `j` separated by a space.

If there are several such pairs, print the one whose second index `j` is smallest; if there is a tie on `j`, pick the one with the smallest `i`. If no such pair exists, print `-1 -1`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.
- Line 3: the integer `T`.

**Output Format**
A single line with two 0-indexed positions, or `-1 -1`.

**Constraints**
- `2 <= N <= 10^5`
- `-10^9 <= A[i], T <= 2*10^9`

**Sample Input 0**
```
4
2 7 11 15
9
```

**Sample Output 0**
```
0 1
```

**Sample Input 1**
```
3
3 2 4
6
```

**Sample Output 1**
```
1 2
```

**Sample Input 2**
```
2
3 3
6
```

**Sample Output 2**
```
0 1
```

**Sample Input 3**
```
5
1 2 3 4 5
100
```

**Sample Output 3**
```
-1 -1
```

**Sample Input 4**
```
5
-1 -2 -3 -4 -5
-5
```

**Sample Output 4**
```
1 2
```

**Sample Input 5**
```
6
0 4 3 0 -1 5
0
```

**Sample Output 5**
```
0 3
```

**Sample Input 6**
```
5
5 5 5 5 5
10
```

**Sample Output 6**
```
0 1
```

**Sample Input 7**
```
4
1 1 1 1
2
```

**Sample Output 7**
```
0 1
```

**Sample Input 8**
```
6
1 2 3 4 5 6
11
```

**Sample Output 8**
```
4 5
```

**Sample Input 9**
```
5
0 0 0 0 0
1
```

**Sample Output 9**
```
-1 -1
```

**Tags**
Arrays

---

## Homework: Smallest Window Containing All Characters
**Problem Statement**
> Original problem: https://www.geeksforgeeks.org/?s=smallest+window+containing+all+characters

Two lines of input are given.

- Line 1: a string `S`.
- Line 2: a string `T`.

Both strings consist of printable ASCII characters and contain no whitespace.

Find the shortest contiguous substring of `S` that contains every character of `T` at least as many times as it appears in `T`.

Print that substring on a single line. If two substrings tie in length, print the one that starts earliest. If no such substring exists, print `-1`.

**Input Format**
- Line 1: the string `S`.
- Line 2: the string `T`.

**Output Format**
A single line containing the shortest window, or `-1`.

**Constraints**
- `1 <= |S| <= 10^5`
- `1 <= |T| <= 100`

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
b
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
aa
aa
```

**Sample Output 3**
```
aa
```

**Sample Input 4**
```
this is a test string
tist
```

**Sample Output 4**
```
t stri
```

**Sample Input 5**
```
abcdef
fa
```

**Sample Output 5**
```
abcdef
```

**Sample Input 6**
```
geeksforgeeks
for
```

**Sample Output 6**
```
for
```

**Sample Input 7**
```
aabbcc
abc
```

**Sample Output 7**
```
abbc
```

**Sample Input 8**
```
hello
ol
```

**Sample Output 8**
```
lo
```

**Sample Input 9**
```
xyzxyz
yxz
```

**Sample Output 9**
```
xyz
```

**Tags**
Strings

---

## Homework: Longest Word in a Sentence
**Problem Statement**
A single line of input contains a sentence — one or more words separated by single spaces. Each word consists of letters and digits (no punctuation).

Print the longest word in the sentence. If several words share the maximum length, print the one that appears first.

**Input Format**
A single line containing the sentence.

**Output Format**
A single line containing the longest word.

**Constraints**
- The sentence has between `1` and `1000` characters.
- Each word has between `1` and `50` characters.

**Sample Input 0**
```
the quick brown fox
```

**Sample Output 0**
```
quick
```

**Sample Input 1**
```
hello
```

**Sample Output 1**
```
hello
```

**Sample Input 2**
```
a bb ccc
```

**Sample Output 2**
```
ccc
```

**Sample Input 3**
```
one two six ten
```

**Sample Output 3**
```
one
```

**Sample Input 4**
```
abc def ghi jklmn
```

**Sample Output 4**
```
jklmn
```

**Sample Input 5**
```
sky is the limit
```

**Sample Output 5**
```
limit
```

**Sample Input 6**
```
programming is fun
```

**Sample Output 6**
```
programming
```

**Sample Input 7**
```
coding contests are great
```

**Sample Output 7**
```
contests
```

**Sample Input 8**
```
no matter what happens
```

**Sample Output 8**
```
happens
```

**Sample Input 9**
```
elephants love bananas
```

**Sample Output 9**
```
elephants
```

**Tags**
Strings

---

## Homework: Row with the Maximum Sum
**Problem Statement**
You are given a matrix with `R` rows and `C` columns of integers. Print the 0-indexed row number whose elements sum to the largest value. If several rows tie for the largest sum, print the smallest such row number.

**Input Format**
- Line 1: two space-separated integers `R C`.
- Next `R` lines: each contains `C` space-separated integers.

**Output Format**
A single line containing the 0-indexed row number.

**Constraints**
- `1 <= R, C <= 500`
- `-10^6 <= A[i][j] <= 10^6`

**Sample Input 0**
```
3 3
1 2 3
4 5 6
7 8 9
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
1 1
42
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
2 3
0 0 0
0 0 0
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
3 2
1 1
2 2
3 3
```

**Sample Output 3**
```
2
```

**Sample Input 4**
```
4 3
-1 -1 -1
1 1 1
0 0 0
-2 -2 -2
```

**Sample Output 4**
```
1
```

**Sample Input 5**
```
2 2
5 5
5 5
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
3 3
-1 -2 -3
-4 -5 -6
-7 -8 -9
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
3 4
10 20 30 40
5 5 5 5
1 2 3 4
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
3 3
100 -100 0
50 50 0
30 30 40
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
5 1
10
20
30
40
50
```

**Sample Output 9**
```
4
```

**Tags**
Matrices

---

## Homework: Check if a Matrix is the Identity Matrix
**Problem Statement**
You are given a square matrix of size `N x N` of integers. Print `Yes` if it is the identity matrix (`1` on the main diagonal, `0` everywhere else), otherwise print `No`.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: each contains `N` space-separated integers.

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `1 <= N <= 500`
- `-10^9 <= A[i][j] <= 10^9`

**Sample Input 0**
```
3
1 0 0
0 1 0
0 0 1
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
1
1
```

**Sample Output 1**
```
Yes
```

**Sample Input 2**
```
1
0
```

**Sample Output 2**
```
No
```

**Sample Input 3**
```
2
1 0
0 1
```

**Sample Output 3**
```
Yes
```

**Sample Input 4**
```
3
1 0 0
0 1 0
0 0 0
```

**Sample Output 4**
```
No
```

**Sample Input 5**
```
3
1 1 0
0 1 0
0 0 1
```

**Sample Output 5**
```
No
```

**Sample Input 6**
```
4
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
```

**Sample Output 6**
```
Yes
```

**Sample Input 7**
```
2
1 0
1 1
```

**Sample Output 7**
```
No
```

**Sample Input 8**
```
3
0 0 0
0 0 0
0 0 0
```

**Sample Output 8**
```
No
```

**Sample Input 9**
```
3
2 0 0
0 2 0
0 0 2
```

**Sample Output 9**
```
No
```

**Tags**
Matrices

---

## Homework: Double and Halve a Number
**Problem Statement**
Two integers `N` and `K` are given on a single line. Print two lines:

- Line 1: the value of `N` doubled `K` times (that is, `N * 2^K`).
- Line 2: the value of `N` halved `K` times, using integer division that truncates toward zero (that is, `trunc(N / 2^K)`).

**Input Format**
A single line with two space-separated integers `N K`.

**Output Format**
Two lines: the doubled value, then the halved value.

**Constraints**
- `-10^9 <= N <= 10^9`
- `0 <= K <= 30`

**Sample Input 0**
```
8 1
```

**Sample Output 0**
```
16
4
```

**Sample Input 1**
```
8 3
```

**Sample Output 1**
```
64
1
```

**Sample Input 2**
```
100 0
```

**Sample Output 2**
```
100
100
```

**Sample Input 3**
```
1 10
```

**Sample Output 3**
```
1024
0
```

**Sample Input 4**
```
1024 5
```

**Sample Output 4**
```
32768
32
```

**Sample Input 5**
```
-16 2
```

**Sample Output 5**
```
-64
-4
```

**Sample Input 6**
```
0 5
```

**Sample Output 6**
```
0
0
```

**Sample Input 7**
```
7 3
```

**Sample Output 7**
```
56
0
```

**Sample Input 8**
```
1000000000 3
```

**Sample Output 8**
```
8000000000
125000000
```

**Sample Input 9**
```
-1 4
```

**Sample Output 9**
```
-16
0
```

**Tags**
Numbers, Basics

---

## Homework: Two Elements that Appear Only Once
**Problem Statement**
> Original problem: https://www.geeksforgeeks.org/?s=find+two+non+repeating+elements

You are given an array of `N` integers in which exactly two elements appear only once each; every other element appears exactly twice.

Print those two elements on a single line, separated by a space, in non-decreasing order.

**Input Format**
- Line 1: an integer `N` (`N` is even).
- Line 2: `N` space-separated integers.

**Output Format**
A single line with the two values, smaller first.

**Constraints**
- `2 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`, `A[i] != 0`
- Exactly two elements appear once; all others appear twice.

**Sample Input 0**
```
6
1 2 3 2 1 4
```

**Sample Output 0**
```
3 4
```

**Sample Input 1**
```
2
5 7
```

**Sample Output 1**
```
5 7
```

**Sample Input 2**
```
4
1 1 3 5
```

**Sample Output 2**
```
3 5
```

**Sample Input 3**
```
6
7 8 7 9 8 10
```

**Sample Output 3**
```
9 10
```

**Sample Input 4**
```
8
1 2 3 4 1 2 5 6
```

**Sample Output 4**
```
3 7
```

**Sample Input 5**
```
4
-1 -2 -1 3
```

**Sample Output 5**
```
-2 3
```

**Sample Input 6**
```
6
100 200 100 300 200 400
```

**Sample Output 6**
```
300 400
```

**Sample Input 7**
```
8
10 20 30 40 10 20 30 50
```

**Sample Output 7**
```
40 50
```

**Sample Input 8**
```
4
99999 1 99999 88888
```

**Sample Output 8**
```
1 88888
```

**Sample Input 9**
```
6
5 4 3 4 5 2
```

**Sample Output 9**
```
2 3
```

**Tags**
Arrays

---

## Homework: Sort an Array of Colors
**Problem Statement**
> Original problem: https://leetcode.com/problems/sort-colors/

You are given an array of `N` integers, each of which is `0`, `1`, or `2`. Print the array sorted in non-decreasing order — that is, all `0`s first, followed by all `1`s, followed by all `2`s — on a single line, elements separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers, each `0`, `1` or `2`.

**Output Format**
A single line containing the sorted array.

**Constraints**
- `1 <= N <= 10^5`
- Each element is `0`, `1`, or `2`.

**Sample Input 0**
```
6
2 0 2 1 1 0
```

**Sample Output 0**
```
0 0 1 1 2 2
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
1
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
1
2
```

**Sample Output 3**
```
2
```

**Sample Input 4**
```
5
2 2 2 2 2
```

**Sample Output 4**
```
2 2 2 2 2
```

**Sample Input 5**
```
6
0 0 0 1 1 1
```

**Sample Output 5**
```
0 0 0 1 1 1
```

**Sample Input 6**
```
9
2 1 0 2 1 0 2 1 0
```

**Sample Output 6**
```
0 0 0 1 1 1 2 2 2
```

**Sample Input 7**
```
5
1 0 2 0 1
```

**Sample Output 7**
```
0 0 1 1 2
```

**Sample Input 8**
```
10
0 0 0 0 0 1 1 1 2 2
```

**Sample Output 8**
```
0 0 0 0 0 1 1 1 2 2
```

**Sample Input 9**
```
7
2 2 1 1 0 0 0
```

**Sample Output 9**
```
0 0 0 1 1 2 2
```

**Tags**
Arrays, Sorting

---
