# DSA-301 Homework - LEC 1..10 (missing challenges)

Author-ready markdown for `automator.py`. Statements are strictly descriptive: no hints on approach, data structure, or language feature. LeetCode-sourced rows carry a link at the top of the statement. Each challenge has 10 sample I/O pairs; run `tools/hr_mark_samples.py --md dsa301_homework_lec1-10.md --apply` to flag the first two as samples. Ensure C++14, Java 8 and Python 3 are enabled on each challenge before publishing.

---

## Homework: Print Vector Elements
**Problem Statement**
You are given `N` integers. Print each integer on its own line, in the order they were given.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
`N` lines. The i-th line contains `a_i`.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i <= 10^9`

**Sample Input 0**
```
3
1 2 3
```

**Sample Output 0**
```
1
2
3
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
5
5 4 3 2 1
```

**Sample Output 2**
```
5
4
3
2
1
```

**Sample Input 3**
```
4
-1 0 1 -2
```

**Sample Output 3**
```
-1
0
1
-2
```

**Sample Input 4**
```
6
100 200 300 400 500 600
```

**Sample Output 4**
```
100
200
300
400
500
600
```

**Sample Input 5**
```
2
-1000000000 1000000000
```

**Sample Output 5**
```
-1000000000
1000000000
```

**Sample Input 6**
```
5
0 0 0 0 0
```

**Sample Output 6**
```
0
0
0
0
0
```

**Sample Input 7**
```
3
7 7 7
```

**Sample Output 7**
```
7
7
7
```

**Sample Input 8**
```
4
10 -10 10 -10
```

**Sample Output 8**
```
10
-10
10
-10
```

**Sample Input 9**
```
5
1 -2 3 -4 5
```

**Sample Output 9**
```
1
-2
3
-4
5
```

**Tags**
Basics, IO, Arrays

---

## Homework: Sort Strings in Reverse Alphabetical Order
**Problem Statement**
You are given `N` strings, each consisting of lowercase English letters. Print the strings in reverse alphabetical (lexicographic) order, one per line.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: one string per line.

**Output Format**
`N` lines: the input strings sorted in reverse alphabetical order.

**Constraints**
- `1 <= N <= 100000`
- Each string has length between 1 and 50; only lowercase English letters.

**Sample Input 0**
```
3
apple
banana
cherry
```

**Sample Output 0**
```
cherry
banana
apple
```

**Sample Input 1**
```
1
hello
```

**Sample Output 1**
```
hello
```

**Sample Input 2**
```
4
dog
cat
bird
ant
```

**Sample Output 2**
```
dog
cat
bird
ant
```

**Sample Input 3**
```
3
zzz
aaa
mmm
```

**Sample Output 3**
```
zzz
mmm
aaa
```

**Sample Input 4**
```
5
one
two
three
four
five
```

**Sample Output 4**
```
two
three
one
four
five
```

**Sample Input 5**
```
3
abc
ab
abcd
```

**Sample Output 5**
```
abcd
abc
ab
```

**Sample Input 6**
```
4
xyz
xy
x
xyzw
```

**Sample Output 6**
```
xyzw
xyz
xy
x
```

**Sample Input 7**
```
2
a
b
```

**Sample Output 7**
```
b
a
```

**Sample Input 8**
```
5
red
blue
green
yellow
orange
```

**Sample Output 8**
```
yellow
red
orange
green
blue
```

**Sample Input 9**
```
6
z
y
x
w
v
u
```

**Sample Output 9**
```
z
y
x
w
v
u
```

**Tags**
Sorting, Strings

---

## Homework: Sorted Key-Value Pairs
**Problem Statement**
You are given `N` key-value pairs. Each key is a lowercase word; each value is an integer. If the same key appears more than once, only its LATEST assignment (the one occurring last in the input) is retained. Print the final set of key-value pairs sorted by key in ascending alphabetical order, one pair per line as `key value`.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: a lowercase word `key`, one space, and an integer `value`.

**Output Format**
One line per distinct key in ascending alphabetical order: `key value`, where `value` is the last one assigned to that key.

**Constraints**
- `1 <= N <= 100000`
- Key length is between 1 and 30; keys use only lowercase English letters.
- `-10^9 <= value <= 10^9`

**Sample Input 0**
```
3
a 1
b 2
c 3
```

**Sample Output 0**
```
a 1
b 2
c 3
```

**Sample Input 1**
```
3
c 3
a 1
b 2
```

**Sample Output 1**
```
a 1
b 2
c 3
```

**Sample Input 2**
```
4
a 1
a 5
a 10
a 100
```

**Sample Output 2**
```
a 100
```

**Sample Input 3**
```
5
banana 2
apple 5
cherry 8
apple 10
banana 3
```

**Sample Output 3**
```
apple 10
banana 3
cherry 8
```

**Sample Input 4**
```
1
hello 42
```

**Sample Output 4**
```
hello 42
```

**Sample Input 5**
```
4
z 26
a 1
m 13
n 14
```

**Sample Output 5**
```
a 1
m 13
n 14
z 26
```

**Sample Input 6**
```
3
x 0
y -1
z 1
```

**Sample Output 6**
```
x 0
y -1
z 1
```

**Sample Input 7**
```
5
red 5
blue 5
red 5
blue 5
red 5
```

**Sample Output 7**
```
blue 5
red 5
```

**Sample Input 8**
```
3
xy 1
x 2
xyz 3
```

**Sample Output 8**
```
x 2
xy 1
xyz 3
```

**Sample Input 9**
```
6
one 1
two 2
three 3
one 11
two 22
three 33
```

**Sample Output 9**
```
one 11
three 33
two 22
```

**Tags**
Sorting, Maps

---

## Homework: Sort Records by Score
**Problem Statement**
You are given `N` records. Each record is a single-word `name` and an integer `score`. Sort the records by `score` in non-decreasing order. When two records share the same score, break the tie by `name` in ascending alphabetical order. Print each record on its own line as `name score`.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: `name score` (a single word followed by an integer, space-separated).

**Output Format**
`N` lines in the required order, each formatted as `name score`.

**Constraints**
- `1 <= N <= 100000`
- Name length is between 1 and 30; only lowercase English letters.
- `-10^9 <= score <= 10^9`

**Sample Input 0**
```
3
alice 90
bob 75
carol 80
```

**Sample Output 0**
```
bob 75
carol 80
alice 90
```

**Sample Input 1**
```
4
a 5
b 5
c 5
d 5
```

**Sample Output 1**
```
a 5
b 5
c 5
d 5
```

**Sample Input 2**
```
1
solo 100
```

**Sample Output 2**
```
solo 100
```

**Sample Input 3**
```
3
x -10
y 0
z 10
```

**Sample Output 3**
```
x -10
y 0
z 10
```

**Sample Input 4**
```
5
one 1
two 2
three 3
four 4
five 5
```

**Sample Output 4**
```
one 1
two 2
three 3
four 4
five 5
```

**Sample Input 5**
```
4
bob 10
alice 10
carol 5
dave 10
```

**Sample Output 5**
```
carol 5
alice 10
bob 10
dave 10
```

**Sample Input 6**
```
3
zack 0
adam 0
bill 0
```

**Sample Output 6**
```
adam 0
bill 0
zack 0
```

**Sample Input 7**
```
5
a 1000000000
b 999999999
c 1000000000
d 1
e -1000000000
```

**Sample Output 7**
```
e -1000000000
d 1
b 999999999
a 1000000000
c 1000000000
```

**Sample Input 8**
```
2
aa 5
a 5
```

**Sample Output 8**
```
a 5
aa 5
```

**Sample Input 9**
```
6
p 3
q 2
r 3
s 2
t 1
u 1
```

**Sample Output 9**
```
t 1
u 1
q 2
s 2
p 3
r 3
```

**Tags**
Sorting, Records

---

## Homework: Contains Value
**Problem Statement**
You are given `N` integers followed by a target integer `Q`. Determine whether `Q` occurs at least once in the sequence. Print `YES` if it does; otherwise print `NO`.

**Input Format**
- Line 1: two space-separated integers `N` and `Q`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single line: `YES` or `NO`.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i, Q <= 10^9`

**Sample Input 0**
```
5 3
1 2 3 4 5
```

**Sample Output 0**
```
YES
```

**Sample Input 1**
```
5 6
1 2 3 4 5
```

**Sample Output 1**
```
NO
```

**Sample Input 2**
```
1 42
42
```

**Sample Output 2**
```
YES
```

**Sample Input 3**
```
1 42
43
```

**Sample Output 3**
```
NO
```

**Sample Input 4**
```
4 0
-1 -2 -3 -4
```

**Sample Output 4**
```
NO
```

**Sample Input 5**
```
4 0
-1 0 1 2
```

**Sample Output 5**
```
YES
```

**Sample Input 6**
```
6 -1000000000
-1000000000 0 1000000000 -1000000000 0 1
```

**Sample Output 6**
```
YES
```

**Sample Input 7**
```
3 100
99 98 97
```

**Sample Output 7**
```
NO
```

**Sample Input 8**
```
5 5
5 5 5 5 5
```

**Sample Output 8**
```
YES
```

**Sample Input 9**
```
7 -50
1 2 3 -50 4 5 6
```

**Sample Output 9**
```
YES
```

**Tags**
Search, Arrays

---

## Homework: LC136 Single Number
**Problem Statement**
> Original problem: https://leetcode.com/problems/single-number/

You are given a non-empty array of `N` integers. Every value appears exactly twice, except for one value which appears exactly once. Print the value that appears only once.

**Input Format**
- Line 1: an integer `N` (`N` is odd).
- Line 2: `N` space-separated integers.

**Output Format**
A single integer: the value that appears only once.

**Constraints**
- `1 <= N <= 30000` and `N` is odd.
- `-30000 <= a_i <= 30000`
- Exactly one value occurs once; every other value occurs exactly twice.

**Sample Input 0**
```
3
2 2 1
```

**Sample Output 0**
```
1
```

**Sample Input 1**
```
5
4 1 2 1 2
```

**Sample Output 1**
```
4
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
5
5 5 6 6 7
```

**Sample Output 3**
```
7
```

**Sample Input 4**
```
7
-1 -1 -2 -2 -3 -3 100
```

**Sample Output 4**
```
100
```

**Sample Input 5**
```
3
0 0 42
```

**Sample Output 5**
```
42
```

**Sample Input 6**
```
5
30000 30000 -30000 -30000 12345
```

**Sample Output 6**
```
12345
```

**Sample Input 7**
```
3
99 -99 99
```

**Sample Output 7**
```
-99
```

**Sample Input 8**
```
7
1 2 3 4 3 2 1
```

**Sample Output 8**
```
4
```

**Sample Input 9**
```
5
-5 5 -5 5 100
```

**Sample Output 9**
```
100
```

**Tags**
Arrays, Counting

---

## Homework: LC1512 Number of Good Pairs
**Problem Statement**
> Original problem: https://leetcode.com/problems/number-of-good-pairs/

You are given an array of `N` integers. A pair of indices `(i, j)` is called a "good pair" when `i < j` and `a_i == a_j`. Print the total number of good pairs in the array.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
A single integer: the number of good pairs.

**Constraints**
- `1 <= N <= 100`
- `1 <= a_i <= 100`

**Sample Input 0**
```
4
1 2 3 1
```

**Sample Output 0**
```
1
```

**Sample Input 1**
```
4
1 1 1 1
```

**Sample Output 1**
```
6
```

**Sample Input 2**
```
6
1 2 3 1 1 3
```

**Sample Output 2**
```
4
```

**Sample Input 3**
```
5
1 2 3 4 5
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
1
7
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
5
5 5 5 5 5
```

**Sample Output 5**
```
10
```

**Sample Input 6**
```
6
1 2 3 1 2 3
```

**Sample Output 6**
```
3
```

**Sample Input 7**
```
7
10 20 10 30 10 20 40
```

**Sample Output 7**
```
4
```

**Sample Input 8**
```
4
1 1 2 2
```

**Sample Output 8**
```
2
```

**Sample Input 9**
```
3
100 100 100
```

**Sample Output 9**
```
3
```

**Tags**
Arrays, Counting

---

## Homework: LC1464 Maximum Product of Two Elements in an Array
**Problem Statement**
> Original problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

You are given an array of `N` positive integers (`N >= 2`). Consider every pair of distinct indices `(i, j)` with `i != j` and compute the value `(a_i - 1) * (a_j - 1)`. Print the maximum such value.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated positive integers `a_1, ..., a_N`.

**Output Format**
A single integer: the maximum value of `(a_i - 1) * (a_j - 1)` over all `i != j`.

**Constraints**
- `2 <= N <= 500`
- `1 <= a_i <= 1000`

**Sample Input 0**
```
4
3 4 5 2
```

**Sample Output 0**
```
12
```

**Sample Input 1**
```
3
1 5 4
```

**Sample Output 1**
```
12
```

**Sample Input 2**
```
5
3 7 3 4 2
```

**Sample Output 2**
```
18
```

**Sample Input 3**
```
2
1 1
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
4
10 20 30 40
```

**Sample Output 4**
```
1131
```

**Sample Input 5**
```
3
1000 1000 1
```

**Sample Output 5**
```
998001
```

**Sample Input 6**
```
5
5 5 5 5 5
```

**Sample Output 6**
```
16
```

**Sample Input 7**
```
6
1 2 3 4 5 6
```

**Sample Output 7**
```
20
```

**Sample Input 8**
```
3
2 3 5
```

**Sample Output 8**
```
8
```

**Sample Input 9**
```
4
100 1 100 50
```

**Sample Output 9**
```
9801
```

**Tags**
Arrays, Arithmetic

---

## Homework: LC1337 The K Weakest Rows in a Matrix
**Problem Statement**
> Original problem: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

You are given a binary matrix with `M` rows and `N` columns; each entry is `0` or `1`. In every row the `1`s appear before the `0`s (soldiers stand at the front, civilians behind). Row `i` is defined to be "weaker" than row `j` when either:
- row `i` contains fewer `1`s than row `j`, or
- both rows contain the same number of `1`s and `i < j`.

Given an integer `K` (`1 <= K <= M`), print the 0-based indices of the `K` weakest rows in ascending order of weakness (weakest first), separated by single spaces on one line.

**Input Format**
- Line 1: three space-separated integers `M`, `N`, `K`.
- Next `M` lines: each contains `N` space-separated integers (each `0` or `1`) — the matrix row.

**Output Format**
A single line with `K` space-separated 0-based row indices, from weakest to strongest.

**Constraints**
- `1 <= M, N <= 100`
- `1 <= K <= M`
- Every row consists of some number of `1`s followed by some number of `0`s.

**Sample Input 0**
```
5 5 3
1 1 0 0 0
1 1 1 1 0
1 0 0 0 0
1 1 0 0 0
1 1 1 1 1
```

**Sample Output 0**
```
2 0 3
```

**Sample Input 1**
```
3 4 2
1 1 1 1
1 0 0 0
1 1 1 0
```

**Sample Output 1**
```
1 2
```

**Sample Input 2**
```
1 1 1
1
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
2 3 2
0 0 0
1 1 1
```

**Sample Output 3**
```
0 1
```

**Sample Input 4**
```
4 4 4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
```

**Sample Output 4**
```
0 1 2 3
```

**Sample Input 5**
```
3 3 1
1 1 0
1 0 0
1 1 1
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
5 3 2
1 1 1
1 1 0
1 0 0
1 1 0
0 0 0
```

**Sample Output 6**
```
4 2
```

**Sample Input 7**
```
2 2 1
1 1
1 0
```

**Sample Output 7**
```
1
```

**Sample Input 8**
```
4 2 3
0 0
1 0
0 0
1 1
```

**Sample Output 8**
```
0 2 1
```

**Sample Input 9**
```
3 5 3
1 1 1 1 1
1 1 1 0 0
1 1 1 1 0
```

**Sample Output 9**
```
1 2 0
```

**Tags**
Matrix, Sorting

---

## Homework: LC1394 Find Lucky Integer in an Array
**Problem Statement**
> Original problem: https://leetcode.com/problems/find-lucky-integer-in-an-array/

You are given an array of `N` positive integers. A value `v` in the array is called "lucky" when its frequency in the array is exactly equal to `v` itself. Print the LARGEST lucky value. If no lucky value exists in the array, print `-1`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated positive integers `a_1, ..., a_N`.

**Output Format**
A single integer: the largest lucky value, or `-1` if none exists.

**Constraints**
- `1 <= N <= 500`
- `1 <= a_i <= 500`

**Sample Input 0**
```
3
2 2 3
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
6
1 2 2 3 3 3
```

**Sample Output 1**
```
3
```

**Sample Input 2**
```
2
2 2
```

**Sample Output 2**
```
2
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
3
7 7 7
```

**Sample Output 4**
```
-1
```

**Sample Input 5**
```
1
1
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
4
4 4 4 4
```

**Sample Output 6**
```
4
```

**Sample Input 7**
```
5
1 2 2 3 3
```

**Sample Output 7**
```
2
```

**Sample Input 8**
```
4
2 2 4 4
```

**Sample Output 8**
```
2
```

**Sample Input 9**
```
5
5 6 7 8 9
```

**Sample Output 9**
```
-1
```

**Tags**
Arrays, Counting
