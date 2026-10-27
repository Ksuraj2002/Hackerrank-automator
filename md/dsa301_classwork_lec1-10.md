# DSA-301 Classwork - LEC 1..10 (missing challenges)

Author-ready markdown for `automator.py`. Each problem is stated descriptively with no hints on approach, data structure, or language feature. LeetCode-sourced problems include a link at the top of the statement. Every challenge carries 10 sample I/O pairs; run `tools/hr_mark_samples.py --md dsa301_classwork_lec1-10.md --apply` to flag the first two as samples. Ensure C++14, Java 8 and Python 3 are enabled on each challenge before publishing.

---

## Classwork: Sum of Two Integers
**Problem Statement**
You are given two integers `a` and `b` on a single line. Print their sum.

**Input Format**
A single line containing two space-separated integers `a` and `b`.

**Output Format**
A single line containing one integer: `a + b`.

**Constraints**
- `-10^9 <= a, b <= 10^9`

**Sample Input 0**
```
3 5
```

**Sample Output 0**
```
8
```

**Sample Input 1**
```
10 -4
```

**Sample Output 1**
```
6
```

**Sample Input 2**
```
0 0
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
-7 -8
```

**Sample Output 3**
```
-15
```

**Sample Input 4**
```
100 250
```

**Sample Output 4**
```
350
```

**Sample Input 5**
```
999999999 1
```

**Sample Output 5**
```
1000000000
```

**Sample Input 6**
```
-1000000000 1000000000
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
42 42
```

**Sample Output 7**
```
84
```

**Sample Input 8**
```
-1 1
```

**Sample Output 8**
```
0
```

**Sample Input 9**
```
12345 67890
```

**Sample Output 9**
```
80235
```

**Tags**
Basics, IO, Arithmetic

---

## Classwork: Sort in Descending Order
**Problem Statement**
You are given `N` integers. Print them in non-increasing (descending) order on a single line, separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, a_2, ..., a_N`.

**Output Format**
A single line with the `N` integers sorted in non-increasing order, separated by single spaces.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i <= 10^9`

**Sample Input 0**
```
5
3 1 4 1 5
```

**Sample Output 0**
```
5 4 3 1 1
```

**Sample Input 1**
```
4
10 -1 7 2
```

**Sample Output 1**
```
10 7 2 -1
```

**Sample Input 2**
```
1
42
```

**Sample Output 2**
```
42
```

**Sample Input 3**
```
6
9 9 9 9 9 9
```

**Sample Output 3**
```
9 9 9 9 9 9
```

**Sample Input 4**
```
3
-5 -1 -100
```

**Sample Output 4**
```
-1 -5 -100
```

**Sample Input 5**
```
7
0 5 -2 8 3 -6 4
```

**Sample Output 5**
```
8 5 4 3 0 -2 -6
```

**Sample Input 6**
```
2
1000000000 -1000000000
```

**Sample Output 6**
```
1000000000 -1000000000
```

**Sample Input 7**
```
5
2 4 6 8 10
```

**Sample Output 7**
```
10 8 6 4 2
```

**Sample Input 8**
```
5
10 8 6 4 2
```

**Sample Output 8**
```
10 8 6 4 2
```

**Sample Input 9**
```
8
1 2 3 4 5 6 7 8
```

**Sample Output 9**
```
8 7 6 5 4 3 2 1
```

**Tags**
Sorting, Arrays

---

## Classwork: Count Elements Greater Than K
**Problem Statement**
You are given `N` integers and a threshold `K`. Print the number of elements that are strictly greater than `K`.

**Input Format**
- Line 1: two space-separated integers `N` and `K`.
- Line 2: `N` space-separated integers `a_1, a_2, ..., a_N`.

**Output Format**
A single integer: the count of elements `a_i` with `a_i > K`.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i, K <= 10^9`

**Sample Input 0**
```
5 3
1 2 3 4 5
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
6 0
-1 -2 0 1 2 3
```

**Sample Output 1**
```
3
```

**Sample Input 2**
```
4 10
5 6 7 8
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
4 -100
-5 -6 -7 -8
```

**Sample Output 3**
```
4
```

**Sample Input 4**
```
1 0
0
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
1 0
1
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
7 100
100 101 99 200 50 300 100
```

**Sample Output 6**
```
3
```

**Sample Input 7**
```
5 5
5 5 5 5 5
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
5 5
6 6 6 6 6
```

**Sample Output 8**
```
5
```

**Sample Input 9**
```
8 0
-3 -1 0 1 3 5 7 9
```

**Sample Output 9**
```
5
```

**Tags**
Arrays, Counting

---

## Classwork: Add Two Numbers Mixed Types
**Problem Statement**
You will process `T` queries. Each query specifies a numeric type flag on its own line, followed by two numbers of that type on the next line:

- Flag `I` — the two values are integers. Print their sum as an integer (no decimal point).
- Flag `D` — the two values are decimal numbers. Print their sum with exactly six digits after the decimal point.

Print the result of each query on its own line, in the order the queries appear.

**Input Format**
- Line 1: an integer `T`, the number of queries.
- For each query, two lines:
  - Line 1: the type flag, either `I` or `D`.
  - Line 2: two space-separated values of the declared type.

**Output Format**
`T` lines. For a query of type `I`, print the integer sum. For a query of type `D`, print the sum formatted with exactly 6 digits after the decimal point (round-half-to-even or standard `%.6f` formatting is acceptable).

**Constraints**
- `1 <= T <= 100`
- For type `I`: each value fits in a 64-bit signed integer and `|value| <= 10^9`.
- For type `D`: `|value| <= 10^6`, and inputs will have at most 6 digits after the decimal point.

**Sample Input 0**
```
2
I
3 5
D
1.5 2.5
```

**Sample Output 0**
```
8
4.000000
```

**Sample Input 1**
```
3
I
-1 1
I
100 200
D
0.1 0.2
```

**Sample Output 1**
```
0
300
0.300000
```

**Sample Input 2**
```
1
I
1000000000 999999999
```

**Sample Output 2**
```
1999999999
```

**Sample Input 3**
```
1
D
-3.14 2.14
```

**Sample Output 3**
```
-1.000000
```

**Sample Input 4**
```
2
D
0.0 0.0
I
0 0
```

**Sample Output 4**
```
0.000000
0
```

**Sample Input 5**
```
4
I
5 5
I
10 -5
D
1.25 2.75
D
-1.5 1.5
```

**Sample Output 5**
```
10
5
4.000000
0.000000
```

**Sample Input 6**
```
1
I
0 0
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
2
D
100.5 200.25
D
-50.5 -49.5
```

**Sample Output 7**
```
300.750000
-100.000000
```

**Sample Input 8**
```
3
D
0.001 0.002
I
7 8
D
5.5 4.5
```

**Sample Output 8**
```
0.003000
15
10.000000
```

**Sample Input 9**
```
2
I
-500 -500
D
3.333333 6.666667
```

**Sample Output 9**
```
-1000
10.000000
```

**Tags**
IO, Arithmetic, Formatting

---

## Classwork: Square Every Element
**Problem Statement**
You are given `N` integers. Produce a new sequence in which every element has been replaced by its square, preserving the original order.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single line with `N` space-separated integers, where the i-th value equals `a_i * a_i`, in the same order as the input.

**Constraints**
- `1 <= N <= 100000`
- `-10000 <= a_i <= 10000`

**Sample Input 0**
```
5
1 2 3 4 5
```

**Sample Output 0**
```
1 4 9 16 25
```

**Sample Input 1**
```
3
-1 -2 -3
```

**Sample Output 1**
```
1 4 9
```

**Sample Input 2**
```
1
0
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
4
10 -10 20 -20
```

**Sample Output 3**
```
100 100 400 400
```

**Sample Input 4**
```
6
0 1 2 3 4 5
```

**Sample Output 4**
```
0 1 4 9 16 25
```

**Sample Input 5**
```
2
10000 -10000
```

**Sample Output 5**
```
100000000 100000000
```

**Sample Input 6**
```
5
7 7 7 7 7
```

**Sample Output 6**
```
49 49 49 49 49
```

**Sample Input 7**
```
3
100 -50 25
```

**Sample Output 7**
```
10000 2500 625
```

**Sample Input 8**
```
4
1 -1 1 -1
```

**Sample Output 8**
```
1 1 1 1
```

**Sample Input 9**
```
8
-5 -4 -3 -2 -1 1 2 3
```

**Sample Output 9**
```
25 16 9 4 1 1 4 9
```

**Tags**
Arrays, Basics

---

## Classwork: Sort Pairs by Second Value
**Problem Statement**
You are given `N` pairs of integers `(a_i, b_i)`. Print the pairs in a specific order:
- Primary key: `b_i` in non-decreasing order.
- Tie-break: when two pairs share the same `b`, order them by `a` in non-decreasing order.

Print each pair on its own line as `a b` (space-separated), in the required order.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: each line contains two space-separated integers `a_i` and `b_i`.

**Output Format**
`N` lines, each containing `a_i b_i` of the corresponding pair, in the required order.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i, b_i <= 10^9`

**Sample Input 0**
```
3
1 2
3 1
2 2
```

**Sample Output 0**
```
3 1
1 2
2 2
```

**Sample Input 1**
```
4
5 10
1 10
3 5
2 5
```

**Sample Output 1**
```
2 5
3 5
1 10
5 10
```

**Sample Input 2**
```
1
0 0
```

**Sample Output 2**
```
0 0
```

**Sample Input 3**
```
5
1 1
1 2
1 3
1 1
1 2
```

**Sample Output 3**
```
1 1
1 1
1 2
1 2
1 3
```

**Sample Input 4**
```
3
-1 -1
0 -2
2 0
```

**Sample Output 4**
```
0 -2
-1 -1
2 0
```

**Sample Input 5**
```
4
10 3
-5 3
0 3
7 3
```

**Sample Output 5**
```
-5 3
0 3
7 3
10 3
```

**Sample Input 6**
```
2
1000000000 1
-1000000000 1
```

**Sample Output 6**
```
-1000000000 1
1000000000 1
```

**Sample Input 7**
```
6
9 4
8 4
7 5
6 5
5 6
4 6
```

**Sample Output 7**
```
8 4
9 4
6 5
7 5
4 6
5 6
```

**Sample Input 8**
```
3
100 50
200 10
300 20
```

**Sample Output 8**
```
200 10
300 20
100 50
```

**Sample Input 9**
```
5
1 5
2 4
3 3
4 2
5 1
```

**Sample Output 9**
```
5 1
4 2
3 3
2 4
1 5
```

**Tags**
Sorting, Pairs

---

## Classwork: Print Distinct Values in Sorted Order
**Problem Statement**
You are given `N` integers, possibly containing duplicates. Print every distinct value exactly once, in ascending (non-decreasing) order, on a single line separated by single spaces.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single line with the distinct values in ascending order, space-separated.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i <= 10^9`

**Sample Input 0**
```
5
3 1 4 1 5
```

**Sample Output 0**
```
1 3 4 5
```

**Sample Input 1**
```
6
2 2 2 2 2 2
```

**Sample Output 1**
```
2
```

**Sample Input 2**
```
4
10 20 30 40
```

**Sample Output 2**
```
10 20 30 40
```

**Sample Input 3**
```
1
7
```

**Sample Output 3**
```
7
```

**Sample Input 4**
```
5
-1 -2 -3 -2 -1
```

**Sample Output 4**
```
-3 -2 -1
```

**Sample Input 5**
```
8
5 3 5 3 8 1 2 8
```

**Sample Output 5**
```
1 2 3 5 8
```

**Sample Input 6**
```
3
0 0 0
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
5
1000000000 -1000000000 0 1000000000 -1000000000
```

**Sample Output 7**
```
-1000000000 0 1000000000
```

**Sample Input 8**
```
7
7 6 5 4 3 2 1
```

**Sample Output 8**
```
1 2 3 4 5 6 7
```

**Sample Input 9**
```
6
1 2 3 4 5 6
```

**Sample Output 9**
```
1 2 3 4 5 6
```

**Tags**
Sorting, Arrays

---

## Classwork: Sum and Maximum
**Problem Statement**
You are given `N` integers. Compute the sum of all elements and the maximum element. Print both on a single line, separated by a single space: the sum first, then the maximum.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single line: `SUM MAX` (two integers separated by one space).

**Constraints**
- `1 <= N <= 100000`
- `-10000 <= a_i <= 10000`

**Sample Input 0**
```
5
1 2 3 4 5
```

**Sample Output 0**
```
15 5
```

**Sample Input 1**
```
4
-1 -2 -3 -4
```

**Sample Output 1**
```
-10 -1
```

**Sample Input 2**
```
1
42
```

**Sample Output 2**
```
42 42
```

**Sample Input 3**
```
6
10 20 30 40 50 60
```

**Sample Output 3**
```
210 60
```

**Sample Input 4**
```
3
-5 0 5
```

**Sample Output 4**
```
0 5
```

**Sample Input 5**
```
5
100 -100 100 -100 100
```

**Sample Output 5**
```
100 100
```

**Sample Input 6**
```
2
10000 -10000
```

**Sample Output 6**
```
0 10000
```

**Sample Input 7**
```
4
7 7 7 7
```

**Sample Output 7**
```
28 7
```

**Sample Input 8**
```
7
3 1 4 1 5 9 2
```

**Sample Output 8**
```
25 9
```

**Sample Input 9**
```
8
0 0 0 0 0 0 0 0
```

**Sample Output 9**
```
0 0
```

**Tags**
Arrays, Basics

---

## Classwork: Sum of First N Natural Numbers
**Problem Statement**
You are given a positive integer `N`. Print the value of `1 + 2 + 3 + ... + N`.

**Input Format**
A single line containing the integer `N`.

**Output Format**
A single line containing the sum.

**Constraints**
- `1 <= N <= 100000`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
1
```

**Sample Input 1**
```
5
```

**Sample Output 1**
```
15
```

**Sample Input 2**
```
10
```

**Sample Output 2**
```
55
```

**Sample Input 3**
```
100
```

**Sample Output 3**
```
5050
```

**Sample Input 4**
```
2
```

**Sample Output 4**
```
3
```

**Sample Input 5**
```
50
```

**Sample Output 5**
```
1275
```

**Sample Input 6**
```
1000
```

**Sample Output 6**
```
500500
```

**Sample Input 7**
```
7
```

**Sample Output 7**
```
28
```

**Sample Input 8**
```
99
```

**Sample Output 8**
```
4950
```

**Sample Input 9**
```
100000
```

**Sample Output 9**
```
5000050000
```

**Tags**
Math, Basics

---

## Classwork: Character Frequency
**Problem Statement**
You are given a string `s` consisting only of lowercase English letters. For each distinct character that appears in `s`, print one line containing the character, one space, and the number of times it appears in `s`. Print the lines in ascending alphabetical order of the character.

**Input Format**
A single line containing the string `s`.

**Output Format**
For every distinct character present in `s`, in ascending alphabetical order, print one line of the form `<char> <count>`.

**Constraints**
- `1 <= |s| <= 100000`
- `s` contains only lowercase English letters `'a'..'z'`.

**Sample Input 0**
```
banana
```

**Sample Output 0**
```
a 3
b 1
n 2
```

**Sample Input 1**
```
hello
```

**Sample Output 1**
```
e 1
h 1
l 2
o 1
```

**Sample Input 2**
```
aaa
```

**Sample Output 2**
```
a 3
```

**Sample Input 3**
```
abcabc
```

**Sample Output 3**
```
a 2
b 2
c 2
```

**Sample Input 4**
```
z
```

**Sample Output 4**
```
z 1
```

**Sample Input 5**
```
programming
```

**Sample Output 5**
```
a 1
g 2
i 1
m 2
n 1
o 1
p 1
r 2
```

**Sample Input 6**
```
aabb
```

**Sample Output 6**
```
a 2
b 2
```

**Sample Input 7**
```
mississippi
```

**Sample Output 7**
```
i 4
m 1
p 2
s 4
```

**Sample Input 8**
```
abcdefghij
```

**Sample Output 8**
```
a 1
b 1
c 1
d 1
e 1
f 1
g 1
h 1
i 1
j 1
```

**Sample Input 9**
```
zzzyyxxww
```

**Sample Output 9**
```
w 2
x 2
y 2
z 3
```

**Tags**
Strings, Counting

---

## Classwork: LC1207 Unique Number of Occurrences
**Problem Statement**
> Original problem: https://leetcode.com/problems/unique-number-of-occurrences/

You are given an array of `N` integers. Determine whether the number of occurrences of each distinct value in the array is unique — that is, no two distinct values appear the same number of times. Print `YES` if all occurrence counts are distinct, otherwise print `NO`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single line containing `YES` or `NO`.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i <= 10^9`

**Sample Input 0**
```
6
1 2 2 1 1 3
```

**Sample Output 0**
```
YES
```

**Sample Input 1**
```
2
1 2
```

**Sample Output 1**
```
NO
```

**Sample Input 2**
```
10
-3 0 1 -3 1 1 1 -3 10 0
```

**Sample Output 2**
```
YES
```

**Sample Input 3**
```
1
1
```

**Sample Output 3**
```
YES
```

**Sample Input 4**
```
4
1 1 2 2
```

**Sample Output 4**
```
NO
```

**Sample Input 5**
```
5
5 5 5 4 4
```

**Sample Output 5**
```
YES
```

**Sample Input 6**
```
8
1 2 3 4 5 6 7 8
```

**Sample Output 6**
```
NO
```

**Sample Input 7**
```
6
7 7 7 7 7 7
```

**Sample Output 7**
```
YES
```

**Sample Input 8**
```
9
1 1 1 2 2 3 3 3 3
```

**Sample Output 8**
```
YES
```

**Sample Input 9**
```
6
1 1 2 2 3 3
```

**Sample Output 9**
```
NO
```

**Tags**
Arrays, Counting

---

## Classwork: Three Smallest Elements
**Problem Statement**
You are given `N` integers with `N >= 3`. Print the three smallest values in the input, in non-decreasing order, on a single line separated by single spaces. If a value repeats among the three smallest, include the repetitions.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single line with three space-separated integers: the three smallest values of the input in non-decreasing order.

**Constraints**
- `3 <= N <= 100000`
- `-10^9 <= a_i <= 10^9`

**Sample Input 0**
```
5
5 1 4 2 3
```

**Sample Output 0**
```
1 2 3
```

**Sample Input 1**
```
3
10 20 30
```

**Sample Output 1**
```
10 20 30
```

**Sample Input 2**
```
6
-1 -5 -3 0 2 -4
```

**Sample Output 2**
```
-5 -4 -3
```

**Sample Input 3**
```
4
7 7 7 7
```

**Sample Output 3**
```
7 7 7
```

**Sample Input 4**
```
8
1 1 1 2 2 3 4 5
```

**Sample Output 4**
```
1 1 1
```

**Sample Input 5**
```
5
100 50 75 25 60
```

**Sample Output 5**
```
25 50 60
```

**Sample Input 6**
```
7
-1000000000 0 1000000000 -1000000000 5 -1000000000 100
```

**Sample Output 6**
```
-1000000000 -1000000000 -1000000000
```

**Sample Input 7**
```
3
3 2 1
```

**Sample Output 7**
```
1 2 3
```

**Sample Input 8**
```
6
9 8 7 6 5 4
```

**Sample Output 8**
```
4 5 6
```

**Sample Input 9**
```
10
0 -1 -2 -3 -4 -5 -6 -7 -8 -9
```

**Sample Output 9**
```
-9 -8 -7
```

**Tags**
Arrays, Sorting

---

## Classwork: LC506 Relative Ranks
**Problem Statement**
> Original problem: https://leetcode.com/problems/relative-ranks/

You are given `N` athletes' scores; all scores are distinct. Determine each athlete's rank when the scores are compared from highest to lowest:
- The athlete with the highest score receives the label `Gold Medal`.
- The athlete with the second-highest score receives the label `Silver Medal`.
- The athlete with the third-highest score receives the label `Bronze Medal`.
- All other athletes receive their integer rank as a string (`"4"`, `"5"`, ...).

Print the label for each athlete on its own line in the same order as the athletes appear in the input.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated distinct integers `score_1, ..., score_N`.

**Output Format**
`N` lines. The i-th line contains the label of athlete `i` (the one whose score is `score_i`).

**Constraints**
- `1 <= N <= 100000`
- `0 <= score_i <= 10^9`
- All scores are distinct.

**Sample Input 0**
```
5
5 4 3 2 1
```

**Sample Output 0**
```
Gold Medal
Silver Medal
Bronze Medal
4
5
```

**Sample Input 1**
```
5
10 3 8 9 4
```

**Sample Output 1**
```
Gold Medal
5
Bronze Medal
Silver Medal
4
```

**Sample Input 2**
```
1
42
```

**Sample Output 2**
```
Gold Medal
```

**Sample Input 3**
```
2
1 2
```

**Sample Output 3**
```
Silver Medal
Gold Medal
```

**Sample Input 4**
```
3
100 50 75
```

**Sample Output 4**
```
Gold Medal
Bronze Medal
Silver Medal
```

**Sample Input 5**
```
4
1 2 3 4
```

**Sample Output 5**
```
4
Bronze Medal
Silver Medal
Gold Medal
```

**Sample Input 6**
```
5
5 10 15 20 25
```

**Sample Output 6**
```
5
4
Bronze Medal
Silver Medal
Gold Medal
```

**Sample Input 7**
```
6
1 3 5 7 9 11
```

**Sample Output 7**
```
6
5
4
Bronze Medal
Silver Medal
Gold Medal
```

**Sample Input 8**
```
4
100 200 300 400
```

**Sample Output 8**
```
4
Bronze Medal
Silver Medal
Gold Medal
```

**Sample Input 9**
```
5
50 40 30 20 10
```

**Sample Output 9**
```
Gold Medal
Silver Medal
Bronze Medal
4
5
```

**Tags**
Sorting, Arrays

---

## Classwork: LC1636 Sort Array by Increasing Frequency
**Problem Statement**
> Original problem: https://leetcode.com/problems/sort-array-by-increasing-frequency/

You are given an array of `N` integers. Reorder the array so that values with a lower frequency of occurrence come first. When two values occur the same number of times, the value with the larger numeric value comes first (i.e. ties are broken in decreasing order of value). Each value must be repeated in the output the same number of times as it appears in the input. Print the reordered array on a single line, space-separated.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single line with `N` space-separated integers representing the reordered array.

**Constraints**
- `1 <= N <= 100`
- `-100 <= a_i <= 100`

**Sample Input 0**
```
6
1 1 2 2 2 3
```

**Sample Output 0**
```
3 1 1 2 2 2
```

**Sample Input 1**
```
5
2 3 1 3 2
```

**Sample Output 1**
```
1 3 3 2 2
```

**Sample Input 2**
```
9
-1 1 -6 4 5 -6 1 4 1
```

**Sample Output 2**
```
5 -1 4 4 -6 -6 1 1 1
```

**Sample Input 3**
```
1
7
```

**Sample Output 3**
```
7
```

**Sample Input 4**
```
4
1 2 3 4
```

**Sample Output 4**
```
4 3 2 1
```

**Sample Input 5**
```
5
5 5 5 5 5
```

**Sample Output 5**
```
5 5 5 5 5
```

**Sample Input 6**
```
6
1 2 2 3 3 3
```

**Sample Output 6**
```
1 2 2 3 3 3
```

**Sample Input 7**
```
8
4 4 4 1 1 2 2 3
```

**Sample Output 7**
```
3 2 2 1 1 4 4 4
```

**Sample Input 8**
```
5
-1 -2 -3 -4 -5
```

**Sample Output 8**
```
-1 -2 -3 -4 -5
```

**Sample Input 9**
```
6
10 10 20 20 30 30
```

**Sample Output 9**
```
30 30 20 20 10 10
```

**Tags**
Sorting, Counting
